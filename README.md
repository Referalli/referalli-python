# Referalli Python SDK

The official Python client for the [Referalli](https://referalli.com) API: attribution-first affiliate and referral programs.

- One typed method per API operation, with `TypedDict` models for every request and response.
- Sync (`Referalli`, standard library only) and async (`AsyncReferalli`, on httpx) clients with the same methods.
- Retries with backoff, idempotency keys, timeouts, auto-paging iterators and one exception class per error code.
- Webhook signature verification and typed webhook events.

Python 3.11+. Docs: <https://referalli.com/docs>.

## Install

```bash
pip install referalli            # sync client, no dependencies
pip install "referalli[async]"   # adds httpx for AsyncReferalli
```

## Quickstart

Keep the `rk_` API key on your server.

```python
import os

from referalli import Referalli

client = Referalli(api_key=os.environ["REFERALLI_API_KEY"])

# 1. Create a referral link for a partner
link = client.post_links({
    "programId": "prg_123",
    "partnerId": "ptr_123",
    "destinationUrl": "https://example.com/pricing",
})
print(link.get("shortUrl"))

# 2. Attribute a signup to the partner who referred it
client.post_referrals_associate({"programId": "prg_123", "customerRef": "user_42", "anonId": "anon_from_cookie"})

# 3. Track a conversion: a purchase your server has validated
client.post_mobile_purchases({"eventId": "order_1001", "customerRef": "user_42", "amountMinor": 4900, "currency": "usd"})
```

Verify a webhook delivery (Flask shown; any framework works, as long as you pass the raw body):

```python
import os

from flask import Flask, request

from referalli import WebhookVerificationError, webhooks

app = Flask(__name__)


@app.post("/webhooks/referalli")
def referalli_webhook():
    try:
        event = webhooks.construct_event(request.get_data(), request.headers, os.environ["REFERALLI_WEBHOOK_SECRET"])
    except WebhookVerificationError:
        return "", 400
    if event["topic"] == "commission.earned":
        print("commission", event["data"])
    return "", 204
```

## Configuration

```python
from referalli import Referalli

client = Referalli(
    api_key="rk_live_...",
    base_url="https://referalli.com",  # the default
    timeout=30.0,                      # seconds per attempt
    max_retries=3,                     # retries for idempotent requests
    mode="live",                       # optional: assert the key's mode ("test" or "live")
)

fast = client.with_options(timeout=5, max_retries=0)  # a copy with some settings changed
```

Every request is pinned to the API version this SDK was generated against (`referalli.API_VERSION`); pass `api_version=` to pin another.

### Async

```python
import asyncio

from referalli import AsyncReferalli


async def main() -> None:
    async with AsyncReferalli(api_key="rk_live_...") as client:
        programs = await client.get_programs()
        async for partner in client.get_partners_iter(status="active"):
            print(partner["email"])


asyncio.run(main())
```

### Test mode

Use a test-mode key (`rk_test_...`) to work against your organization's test data. Pass `mode="test"` to make every request assert it: the API rejects a request whose key is in the other mode with `ModeMismatchError`, so test code can never write live data. Webhook events carry `livemode`.

## Errors

Every API error raises a subclass of `ApiError` named after its code, with `status`, `code`, `message`, `request_id`, `docs_url`, `details` and `retry_after`. Network failures and timeouts raise `ApiConnectionError` after the retries run out. All of them derive from `ReferalliError`.

```python
from referalli import ApiError, NotFoundError, RateLimitedError, Referalli

client = Referalli(api_key="rk_live_...")
try:
    client.get_partners_id("ptr_missing")
except NotFoundError as e:
    print(e.code, e.status, e.request_id, e.docs_url)
except RateLimitedError as e:
    print("retry after", e.retry_after)
except ApiError as e:
    print(e.code, e.message)
```

Retries: GET, PUT and DELETE requests, and writes carrying an `Idempotency-Key`, are retried on 429, 5xx and network errors with exponential backoff and jitter, honoring `Retry-After`. POST and PATCH requests always carry a key (generated unless you pass `idempotency_key=`), and the same key is reused across retries, so a retried write is applied once.

## Pagination

List methods return one page (`{"object": "list", "data": [...], "has_more": ..., "next_cursor": ...}`); their `_iter` twin follows the cursor for you.

```python
from referalli import Referalli

client = Referalli(api_key="rk_live_...")
page = client.get_partners(status="active", limit=50)
next_page = client.get_partners(status="active", limit=50, starting_after=page["next_cursor"])

for referral in client.get_referrals_iter():
    print(referral["id"])
```

## Webhooks

`webhooks.construct_event(raw_body, headers, secrets)` checks the Standard Webhooks signature (`webhook-id`, `webhook-timestamp`, `webhook-signature`) in constant time, rejects deliveries more than 5 minutes old or ahead (`tolerance_sec=`), and returns the event typed by topic (`referalli.WebhookEvent`, one `TypedDict` per topic in `referalli.TOPICS`). Pass a list of secrets while you rotate one. `webhooks.verify(...)` returns a bool instead of raising.

```python
from referalli import webhooks

secrets = ["whsec_current", "whsec_previous"]


def handle(raw_body: bytes, headers: dict) -> None:
    if not webhooks.verify(raw_body, headers, secrets):
        raise PermissionError("bad signature")
```

## Any operation by id

```python
from referalli import Referalli

client = Referalli(api_key="rk_live_...")
partner = client.call("getPartnersId", path={"id": "ptr_123"})
for item in client.list_all("getPartners", query={"status": "active"}):
    print(item["id"])
```

## Versioning

This SDK follows semantic versioning; see [CHANGELOG.md](./CHANGELOG.md). The API version it pins is `referalli.API_VERSION`.

## License

MIT. See [LICENSE](./LICENSE).
