"""The synchronous Referalli client (standard library only)."""

from __future__ import annotations

import time
import urllib.error
import urllib.parse
import urllib.request
from typing import Any, Callable, Iterator, Mapping, Optional

from ._base import (
    DEFAULT_MAX_RETRIES,
    DEFAULT_TIMEOUT,
    RETRY_STATUSES,
    _Config,
    api_error,
    call_args,
    clean_query,
    decode_success,
    encode_body,
    parse_retry_after,
)
from ._errors import ApiConnectionError
from ._operations import OPERATIONS, Operations
from ._version import API_VERSION


class Referalli(Operations):
    """Server-side client. Keep the ``rk_`` key on your server.

    Every operation has a typed method named after its operationId
    (``post_links``, ``get_partners``, ...). Writes carry an ``Idempotency-Key``
    (generated unless you pass ``idempotency_key=``) that is reused across
    retries. Idempotent requests are retried on 429, 5xx and network errors with
    exponential backoff and jitter, honoring ``Retry-After``.

    ``mode="test"`` (or ``"live"``) asserts the key's mode on every request: the
    API refuses a request whose key is in the other mode.
    """

    def __init__(self, api_key: Optional[str] = None, base_url: Optional[str] = None, *, timeout: float = DEFAULT_TIMEOUT,
                 max_retries: int = DEFAULT_MAX_RETRIES, retry_base_delay: float = 0.5, api_version: str = API_VERSION,
                 mode: Optional[str] = None, default_headers: Optional[Mapping[str, str]] = None) -> None:
        self._config = _Config(api_key, base_url, timeout, max_retries, retry_base_delay, api_version, mode, default_headers)

    # --- configuration ------------------------------------------------------
    @property
    def base_url(self) -> str:
        return self._config.base_url

    @property
    def api_version(self) -> str:
        return self._config.api_version

    @property
    def mode(self) -> Optional[str]:
        return self._config.mode

    def with_options(self, *, timeout: Optional[float] = None, max_retries: Optional[int] = None,
                     retry_base_delay: Optional[float] = None, api_version: Optional[str] = None,
                     mode: Optional[str] = None, base_url: Optional[str] = None) -> "Referalli":
        """A copy of this client with some settings changed: ``client.with_options(timeout=5).get_partners()``."""
        copy = Referalli.__new__(Referalli)
        copy._config = self._config._replace(timeout=timeout, max_retries=max_retries, retry_base_delay=retry_base_delay,
                                             api_version=api_version, mode=mode, base_url=base_url)
        return copy

    # --- transport ----------------------------------------------------------
    def _request(self, method: str, path: str, *, query: Optional[Mapping[str, Any]] = None, body: Any = None,
                 idempotency_key: Optional[str] = None, kind: str = "json") -> Any:
        cfg = self._config
        url = cfg.base_url + path
        params = clean_query(query)
        if params:
            url += "?" + urllib.parse.urlencode(params)
        headers = cfg.headers(method, body, idempotency_key, "python")
        data = encode_body(body)

        attempt = 0
        while True:
            req = urllib.request.Request(url, data=data, method=method, headers=headers)
            try:
                with urllib.request.urlopen(req, timeout=cfg.timeout) as res:
                    return decode_success(res.read().decode(), kind)
            except urllib.error.HTTPError as e:
                raw = e.read().decode(errors="replace")
                res_headers = {k.lower(): v for k, v in e.headers.items()}
                retry_after = parse_retry_after(res_headers.get("retry-after"))
                if e.code in RETRY_STATUSES and cfg.can_retry(method, headers, attempt):
                    time.sleep(cfg.delay(attempt, retry_after))
                    attempt += 1
                    continue
                raise api_error(e.code, raw, res_headers, retry_after) from None
            except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
                if cfg.can_retry(method, headers, attempt):
                    time.sleep(cfg.delay(attempt, None))
                    attempt += 1
                    continue
                raise ApiConnectionError(str(e)) from None

    def _paginate(self, fetch: Callable[[Optional[str]], Any]) -> Iterator[Any]:
        cursor: Optional[str] = None
        while True:
            page = fetch(cursor)
            yield from page["data"]
            if not page.get("has_more") or not page.get("next_cursor"):
                return
            cursor = page["next_cursor"]

    # --- generic access -----------------------------------------------------
    def call(self, operation_id: str, *, path: Optional[Mapping[str, str]] = None, query: Optional[Mapping[str, Any]] = None,
             body: Any = None, idempotency_key: Optional[str] = None) -> Any:
        """Call any operation by its id (see ``OPERATIONS``) through its typed method, with wire-named params."""
        name, args, kwargs = call_args(OPERATIONS, operation_id, path, query, body)
        return getattr(self, name)(*args, idempotency_key=idempotency_key, **kwargs)

    def list_all(self, operation_id: str, *, path: Optional[Mapping[str, str]] = None,
                 query: Optional[Mapping[str, Any]] = None) -> Iterator[Any]:
        """Every item of a list operation, following ``next_cursor``."""
        q = dict(query or {})
        return self._paginate(lambda cursor: self.call(operation_id, path=path, query={**q, "starting_after": cursor}))
