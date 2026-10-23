"""What the sync and async clients share: configuration, headers, retry policy and error decoding."""

from __future__ import annotations

import email.utils
import json
import random
import time
import uuid
from typing import Any, Dict, Mapping, Optional

from ._errors import ERROR_CLASSES, ApiError
from ._version import API_VERSION, VERSION

DEFAULT_BASE_URL = "https://referalli.com"
DEFAULT_TIMEOUT = 30.0
DEFAULT_MAX_RETRIES = 3
RETRY_STATUSES = frozenset({429, 500, 502, 503, 504})
#: Methods that are safe to retry without an idempotency key.
IDEMPOTENT_METHODS = frozenset({"GET", "HEAD", "PUT", "DELETE", "OPTIONS"})
#: Writes that get a generated ``Idempotency-Key`` when you don't pass one.
KEYED_METHODS = frozenset({"POST", "PATCH"})
MAX_RETRY_DELAY = 30.0


class _Config:
    """Settings shared by both clients. ``with_options`` copies and overrides them."""

    def __init__(self, api_key: Optional[str], base_url: Optional[str], timeout: float, max_retries: int,
                 retry_base_delay: float, api_version: str, mode: Optional[str],
                 default_headers: Optional[Mapping[str, str]]) -> None:
        if mode not in (None, "test", "live"):
            raise ValueError('mode must be "test", "live" or None')
        self.api_key = api_key
        self.base_url = (base_url or DEFAULT_BASE_URL).rstrip("/")
        self.timeout = timeout
        self.max_retries = max_retries
        self.retry_base_delay = retry_base_delay
        self.api_version = api_version
        self.mode = mode
        self.default_headers = dict(default_headers or {})

    def _replace(self, **changes: Any) -> "_Config":
        c = _Config.__new__(_Config)
        c.__dict__.update(self.__dict__)
        for k, v in changes.items():
            if v is not None:
                setattr(c, k, v)
        c.base_url = c.base_url.rstrip("/")
        return c

    def headers(self, method: str, body: Any, idempotency_key: Optional[str], lang: str) -> Dict[str, str]:
        h = {
            "accept": "application/json",
            # Wire protocol: the API reads these header names.
            "referalli-version": self.api_version,
            "user-agent": f"referalli-{lang}/{VERSION}",
            **self.default_headers,
        }
        if self.mode:
            h["referalli-mode"] = self.mode
        if self.api_key:
            h["authorization"] = f"Bearer {self.api_key}"
        if body is not None:
            h["content-type"] = "application/json"
        if idempotency_key:
            h["idempotency-key"] = idempotency_key
        elif method in KEYED_METHODS:
            h["idempotency-key"] = str(uuid.uuid4())
        return h

    def can_retry(self, method: str, headers: Mapping[str, str], attempt: int) -> bool:
        """Only idempotent requests are retried: safe methods, or writes that carry an idempotency key."""
        return attempt < self.max_retries and (method in IDEMPOTENT_METHODS or "idempotency-key" in headers)

    def delay(self, attempt: int, retry_after: Optional[float]) -> float:
        """Exponential backoff with jitter; ``Retry-After`` wins when the server sends it."""
        if retry_after is not None:
            return min(max(0.0, retry_after), MAX_RETRY_DELAY)
        base = min(self.retry_base_delay * (2 ** attempt), MAX_RETRY_DELAY)
        return base * (0.5 + random.random() * 0.5)


def encode_body(body: Any) -> Optional[bytes]:
    return None if body is None else json.dumps(body).encode()


def query_value(v: Any) -> str:
    if isinstance(v, bool):
        return "true" if v else "false"
    return str(v)


def clean_query(query: Optional[Mapping[str, Any]]) -> Dict[str, str]:
    return {k: query_value(v) for k, v in (query or {}).items() if v is not None}


def parse_retry_after(value: Optional[str]) -> Optional[float]:
    if not value:
        return None
    try:
        return float(value)
    except ValueError:
        try:
            parsed = email.utils.parsedate_to_datetime(value)
        except (TypeError, ValueError):
            return None
        return max(0.0, parsed.timestamp() - time.time()) if parsed else None


def decode_success(raw: str, kind: str) -> Any:
    if kind == "text":
        return raw
    if kind == "empty" or not raw:
        return None
    return json.loads(raw)


def api_error(status: int, raw: str, headers: Dict[str, str], retry_after: Optional[float]) -> ApiError:
    try:
        err = json.loads(raw)["error"]
        if not isinstance(err, dict):
            raise TypeError
    except Exception:
        err = {"code": "http_error", "message": raw or f"HTTP {status}"}
    code = str(err.get("code") or "http_error")
    cls = ERROR_CLASSES.get(code, ApiError)
    return cls(status, code, str(err.get("message", "")), request_id=err.get("requestId") or headers.get("x-request-id"),
               docs_url=err.get("docs_url"), details=err.get("details"), retry_after=retry_after, headers=headers)


def call_args(operations: Mapping[str, tuple], operation_id: str, path: Optional[Mapping[str, str]],
              query: Optional[Mapping[str, Any]], body: Any) -> tuple:
    """Positional and keyword arguments for an operation's typed method, from wire names."""
    _, _, path_params, query_params, has_body, _, name = operations[operation_id]
    args = [(path or {})[p] for p in path_params]
    if has_body:
        args.append(body)
    wire_to_py = {wire: py for wire, py in query_params}
    kwargs = {wire_to_py[k]: v for k, v in (query or {}).items()}
    return name, args, kwargs


__all__ = ["API_VERSION", "DEFAULT_BASE_URL", "DEFAULT_MAX_RETRIES", "DEFAULT_TIMEOUT", "VERSION"]
