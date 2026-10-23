# Changelog

All notable changes to this SDK are documented here. It follows [Semantic Versioning](https://semver.org).

## 0.1.0 (unreleased)

First release as `referalli`.

- One typed method per Referalli API operation (API version 2026-11-01), generated from the OpenAPI document, with doc comments.
- Sync client (`Referalli`, standard library only) and async client (`AsyncReferalli`, httpx; `pip install "referalli[async]"`).
- Retries with exponential backoff and jitter on 429, 5xx and network errors, honoring `Retry-After`, for idempotent requests only (safe methods, or writes carrying an `Idempotency-Key`; POST and PATCH always carry one).
- Per-attempt timeouts, configurable per client and per call.
- One error class per API error code.
- Auto-paging iterators for every list operation.
- Webhook verification (Standard Webhooks, constant-time, 5-minute tolerance) and typed webhook events.
- Test-mode assertion (`Referalli-Mode` header) and a `referalli-<lang>/<version>` User-Agent.
