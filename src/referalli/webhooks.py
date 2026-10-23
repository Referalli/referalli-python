"""Verify and parse Referalli webhook deliveries (Standard Webhooks signatures).

    from referalli import webhooks

    event = webhooks.construct_event(request.body, request.headers, "whsec_...")
    if event["topic"] == "referral.created":
        ...

The signature is ``v1,`` + base64 HMAC-SHA256 of ``{webhook-id}.{webhook-timestamp}.{raw body}``,
keyed with the base64 after ``whsec_``. Compare it in constant time and reject deliveries more
than ``tolerance_sec`` (default 300) from now, in either direction.
"""

from __future__ import annotations

import base64
import binascii
import hashlib
import hmac
import json
import time
from typing import Any, Iterable, Mapping, Optional, Union

from ._errors import WebhookVerificationError
from ._webhook_events import TOPICS, WebhookEvent

WEBHOOK_TOLERANCE_SEC = 300

Secrets = Union[str, Iterable[str]]


def _key(secret: str) -> bytes:
    if secret.startswith("whsec_"):
        try:
            return base64.b64decode(secret[len("whsec_"):])
        except (binascii.Error, ValueError):
            return secret.encode()
    return secret.encode()


def _check(raw_body: Union[bytes, str], headers: Mapping[str, Any], secrets: Secrets, now: Optional[float],
           tolerance_sec: int) -> Optional[str]:
    """None when the delivery verifies, else why it doesn't."""
    lower = {str(k).lower(): (v[0] if isinstance(v, (list, tuple)) and v else v) for k, v in headers.items()}
    msg_id = lower.get("webhook-id")
    ts = lower.get("webhook-timestamp")
    sig = lower.get("webhook-signature")
    if not msg_id or not ts or not sig:
        return "missing webhook-id, webhook-timestamp or webhook-signature header"
    ts = str(ts)
    if not ts.isdigit():
        return "webhook-timestamp is not a unix timestamp"
    current = time.time() if now is None else now
    if abs(current - int(ts)) > tolerance_sec:
        return "webhook-timestamp is outside the tolerance (replayed or clock skew)"
    body = raw_body if isinstance(raw_body, bytes) else raw_body.encode()
    provided = [p for p in str(sig).split(" ") if p.startswith("v1,")]
    for secret in [secrets] if isinstance(secrets, str) else list(secrets):
        digest = hmac.new(_key(secret), msg_id.encode() + b"." + ts.encode() + b"." + body, hashlib.sha256).digest()
        expected = "v1," + base64.b64encode(digest).decode()
        if any(hmac.compare_digest(p.encode(), expected.encode()) for p in provided):
            return None
    return "no signature matches the secret"


def verify(raw_body: Union[bytes, str], headers: Mapping[str, Any], secrets: Secrets, *, now: Optional[float] = None,
           tolerance_sec: int = WEBHOOK_TOLERANCE_SEC) -> bool:
    """True when ``raw_body`` (exactly as received) was signed with one of ``secrets`` within the tolerance.

    ``headers`` is any mapping of header names (any case) to values. Pass two secrets while you rotate one.
    """
    return _check(raw_body, headers, secrets, now, tolerance_sec) is None


def construct_event(raw_body: Union[bytes, str], headers: Mapping[str, Any], secrets: Secrets, *,
                    now: Optional[float] = None, tolerance_sec: int = WEBHOOK_TOLERANCE_SEC) -> WebhookEvent:
    """Verify a delivery and return its event, typed by topic. Raises ``WebhookVerificationError``."""
    problem = _check(raw_body, headers, secrets, now, tolerance_sec)
    if problem:
        raise WebhookVerificationError(problem)
    try:
        event = json.loads(raw_body)
    except ValueError as e:
        raise WebhookVerificationError(f"the body is not JSON: {e}") from None
    if not isinstance(event, dict) or not isinstance(event.get("topic"), str):
        raise WebhookVerificationError("the body is not a webhook event")
    return event  # type: ignore[return-value]


#: The verifier under its earlier name.
verify_webhook = verify

__all__ = ["TOPICS", "WEBHOOK_TOLERANCE_SEC", "WebhookEvent", "WebhookVerificationError", "construct_event", "verify",
           "verify_webhook"]
