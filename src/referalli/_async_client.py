"""The asynchronous Referalli client, on ``httpx.AsyncClient`` (``pip install "referalli[async]"``)."""

from __future__ import annotations

import asyncio
from typing import Any, AsyncIterator, Awaitable, Callable, Mapping, Optional

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
from ._operations import OPERATIONS, AsyncOperations
from ._version import API_VERSION


def _httpx() -> Any:
    try:
        import httpx
    except ImportError as e:  # pragma: no cover - exercised only without the extra
        raise ImportError('AsyncReferalli needs httpx: pip install "referalli[async]"') from e
    return httpx


class AsyncReferalli(AsyncOperations):
    """Async server-side client: the same methods as ``Referalli``, awaited.

        async with AsyncReferalli(api_key="rk_live_...") as client:
            link = await client.post_links({...})
            async for partner in client.get_partners_iter(status="active"):
                ...

    Pass ``http_client=`` to share your own ``httpx.AsyncClient`` (it is then
    yours to close).
    """

    def __init__(self, api_key: Optional[str] = None, base_url: Optional[str] = None, *, timeout: float = DEFAULT_TIMEOUT,
                 max_retries: int = DEFAULT_MAX_RETRIES, retry_base_delay: float = 0.5, api_version: str = API_VERSION,
                 mode: Optional[str] = None, default_headers: Optional[Mapping[str, str]] = None,
                 http_client: Any = None) -> None:
        self._config = _Config(api_key, base_url, timeout, max_retries, retry_base_delay, api_version, mode, default_headers)
        self._owns_http = http_client is None
        self._http = http_client if http_client is not None else _httpx().AsyncClient()

    @property
    def base_url(self) -> str:
        return self._config.base_url

    @property
    def mode(self) -> Optional[str]:
        return self._config.mode

    def with_options(self, *, timeout: Optional[float] = None, max_retries: Optional[int] = None,
                     retry_base_delay: Optional[float] = None, api_version: Optional[str] = None,
                     mode: Optional[str] = None, base_url: Optional[str] = None) -> "AsyncReferalli":
        """A copy of this client (sharing its connection pool) with some settings changed."""
        copy = AsyncReferalli.__new__(AsyncReferalli)
        copy._config = self._config._replace(timeout=timeout, max_retries=max_retries, retry_base_delay=retry_base_delay,
                                             api_version=api_version, mode=mode, base_url=base_url)
        copy._http = self._http
        copy._owns_http = False
        return copy

    async def aclose(self) -> None:
        if self._owns_http:
            await self._http.aclose()

    async def __aenter__(self) -> "AsyncReferalli":
        return self

    async def __aexit__(self, *exc: Any) -> None:
        await self.aclose()

    # --- transport ----------------------------------------------------------
    async def _request(self, method: str, path: str, *, query: Optional[Mapping[str, Any]] = None, body: Any = None,
                       idempotency_key: Optional[str] = None, kind: str = "json") -> Any:
        httpx = _httpx()
        cfg = self._config
        headers = cfg.headers(method, body, idempotency_key, "python")
        data = encode_body(body)
        params = clean_query(query)
        attempt = 0
        while True:
            try:
                res = await self._http.request(method, cfg.base_url + path, params=params or None, content=data,
                                               headers=headers, timeout=cfg.timeout)
            except (httpx.TransportError, asyncio.TimeoutError) as e:
                if cfg.can_retry(method, headers, attempt):
                    await asyncio.sleep(cfg.delay(attempt, None))
                    attempt += 1
                    continue
                raise ApiConnectionError(str(e) or type(e).__name__) from None
            if 200 <= res.status_code < 300:
                return decode_success(res.text, kind)
            res_headers = {k.lower(): v for k, v in res.headers.items()}
            retry_after = parse_retry_after(res_headers.get("retry-after"))
            if res.status_code in RETRY_STATUSES and cfg.can_retry(method, headers, attempt):
                await asyncio.sleep(cfg.delay(attempt, retry_after))
                attempt += 1
                continue
            raise api_error(res.status_code, res.text, res_headers, retry_after)

    async def _paginate(self, fetch: Callable[[Optional[str]], Awaitable[Any]]) -> AsyncIterator[Any]:
        cursor: Optional[str] = None
        while True:
            page = await fetch(cursor)
            for item in page["data"]:
                yield item
            if not page.get("has_more") or not page.get("next_cursor"):
                return
            cursor = page["next_cursor"]

    # --- generic access -----------------------------------------------------
    async def call(self, operation_id: str, *, path: Optional[Mapping[str, str]] = None,
                   query: Optional[Mapping[str, Any]] = None, body: Any = None,
                   idempotency_key: Optional[str] = None) -> Any:
        """Call any operation by its id (see ``OPERATIONS``) through its typed method, with wire-named params."""
        name, args, kwargs = call_args(OPERATIONS, operation_id, path, query, body)
        return await getattr(self, name)(*args, idempotency_key=idempotency_key, **kwargs)

    def list_all(self, operation_id: str, *, path: Optional[Mapping[str, str]] = None,
                 query: Optional[Mapping[str, Any]] = None) -> AsyncIterator[Any]:
        """Every item of a list operation, following ``next_cursor`` (use ``async for``)."""
        q = dict(query or {})
        return self._paginate(lambda cursor: self.call(operation_id, path=path, query={**q, "starting_after": cursor}))
