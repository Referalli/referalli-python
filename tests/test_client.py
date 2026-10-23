"""Unit tests: async client transport, retry policy, webhooks and the README samples. Run with pytest."""

import ast
import asyncio
import base64
import hashlib
import hmac
import json
import os
import re
import time

import pytest

import referalli
from referalli import AsyncReferalli, NotFoundError, Referalli, WebhookVerificationError, webhooks

httpx = pytest.importorskip("httpx")

HERE = os.path.dirname(os.path.abspath(__file__))
PARTNER = {"id": "ptr_1", "email": "a@example.com", "displayName": "A", "externalRef": None, "status": "active",
           "tags": [], "notes": None, "createdAt": "2026-10-21T12:00:00.000Z"}


def run(coro):
    return asyncio.run(coro)


def client_with(handler, **kw):
    http = httpx.AsyncClient(transport=httpx.MockTransport(handler))
    return AsyncReferalli(api_key="rk_test_1", base_url="http://mock", http_client=http, retry_base_delay=0.001, **kw)


def test_async_post_sends_headers_and_reuses_idempotency_key_on_retry():
    seen = []

    def handler(req):
        seen.append(req)
        if len(seen) == 1:
            return httpx.Response(429, headers={"retry-after": "0"}, json={"error": {"code": "rate_limited", "message": "slow"}})
        return httpx.Response(200, json=PARTNER)

    client = client_with(handler, mode="test")
    out = run(client.post_partners({"email": "a@example.com"}))
    assert out["id"] == "ptr_1"
    assert len(seen) == 2
    first = seen[0].headers
    assert first["authorization"] == "Bearer rk_test_1"
    assert first["referalli-version"] == referalli.API_VERSION
    assert first["referalli-mode"] == "test"
    assert first["user-agent"] == f"referalli-python/{referalli.VERSION}"
    assert first["idempotency-key"] and first["idempotency-key"] == seen[1].headers["idempotency-key"]
    assert json.loads(seen[0].content) == {"email": "a@example.com"}


def test_async_typed_error_and_no_retry_on_4xx():
    calls = []

    def handler(req):
        calls.append(req)
        return httpx.Response(404, json={"error": {"code": "not_found", "message": "nope", "requestId": "req_1",
                                                   "docs_url": "https://referalli.com/docs/errors-and-limits#not_found"}})

    with pytest.raises(NotFoundError) as info:
        run(client_with(handler).get_partners_id("ptr x/y"))
    assert info.value.request_id == "req_1" and info.value.status == 404
    assert len(calls) == 1
    assert calls[0].url.raw_path == b"/v1/partners/ptr%20x%2Fy"


def test_async_iterator_follows_cursor():
    pages = [
        {"object": "list", "data": [PARTNER], "has_more": True, "next_cursor": "ptr_1"},
        {"object": "list", "data": [{**PARTNER, "id": "ptr_2"}], "has_more": False, "next_cursor": None},
    ]
    seen = []

    def handler(req):
        seen.append(dict(req.url.params))
        return httpx.Response(200, json=pages[len(seen) - 1])

    async def collect():
        return [p["id"] async for p in client_with(handler).get_partners_iter(status="active", limit=1)]

    assert run(collect()) == ["ptr_1", "ptr_2"]
    assert seen == [{"status": "active", "limit": "1"}, {"status": "active", "limit": "1", "starting_after": "ptr_1"}]


def test_unkeyed_writes_are_not_retried():
    cfg = Referalli(api_key="k")._config
    assert cfg.can_retry("GET", {}, 0)
    assert cfg.can_retry("POST", {"idempotency-key": "k"}, 0)
    assert not cfg.can_retry("POST", {}, 0)
    assert not cfg.can_retry("GET", {}, cfg.max_retries)
    assert "idempotency-key" in cfg.headers("PATCH", {}, None, "python")
    assert "idempotency-key" not in cfg.headers("GET", None, None, "python")


def test_with_options_copies():
    client = Referalli(api_key="k")
    fast = client.with_options(timeout=1, mode="test")
    assert fast._config.timeout == 1 and fast.mode == "test"
    assert client._config.timeout == 30.0 and client.mode is None


def sign(body, secret, msg_id="msg_1", ts=None):
    ts = str(int(time.time()) if ts is None else ts)
    key = base64.b64decode(secret[len("whsec_"):])
    sig = base64.b64encode(hmac.new(key, f"{msg_id}.{ts}.{body}".encode(), hashlib.sha256).digest()).decode()
    return {"webhook-id": msg_id, "webhook-timestamp": ts, "webhook-signature": f"v1,{sig}"}


SECRET = "whsec_" + base64.b64encode(b"0123456789abcdef0123456789abcdef").decode()


def test_construct_event_returns_the_typed_event():
    body = json.dumps({"id": "evt_1", "topic": "referral.created", "orgId": "org_1", "livemode": False,
                       "createdAt": "2026-10-21T12:00:00Z", "data": {"partnerId": "ptr_1"}})
    event = webhooks.construct_event(body.encode(), sign(body, SECRET), [SECRET])
    assert event["topic"] == "referral.created" and event["data"]["partnerId"] == "ptr_1"
    assert "referral.created" in referalli.TOPICS


def test_construct_event_rejects_bad_signatures_and_stale_timestamps():
    body = '{"id":"evt_1","topic":"referral.created","data":{}}'
    with pytest.raises(WebhookVerificationError):
        webhooks.construct_event(body, sign(body, SECRET), "whsec_" + base64.b64encode(b"other").decode())
    with pytest.raises(WebhookVerificationError):
        webhooks.construct_event(body, sign(body, SECRET, ts=int(time.time()) - 301), SECRET)
    assert webhooks.verify(body, sign(body, SECRET, ts=1_000), SECRET, now=1_200)
    assert not webhooks.verify(body + " ", sign(body, SECRET), SECRET)


def readme_blocks():
    text = open(os.path.join(HERE, "..", "README.md")).read()
    return re.findall(r"```python\n(.*?)```", text, re.S)


def test_readme_samples_compile_and_use_real_methods():
    blocks = readme_blocks()
    assert len(blocks) >= 5
    for block in blocks:
        tree = ast.parse(block)
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == "referalli":
                for alias in node.names:
                    assert hasattr(referalli, alias.name), alias.name
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
                owner = node.func.value
                if isinstance(owner, ast.Name) and owner.id in ("client", "fast"):
                    name = node.func.attr
                    assert hasattr(Referalli, name) and hasattr(AsyncReferalli, name), name
                if isinstance(owner, ast.Name) and owner.id == "webhooks":
                    assert hasattr(webhooks, node.func.attr), node.func.attr
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == "call":
                op = node.args[0].value
                assert op in referalli.OPERATIONS, op
