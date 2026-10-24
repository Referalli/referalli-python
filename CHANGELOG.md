# Changelog

All notable changes to this SDK are documented here. It follows [Semantic Versioning](https://semver.org).

## 0.2.0 - 2026-10-24

- API 2026-11-01 additions: 56 new operations (inbound signup connectors, billing product filters, per-org SSO and partner-portal sign-in, support-tool context cards, data-rights executors, account closure, rewards, integration health, plans, the event feed and bulk webhook replay) and 2 webhook topics (`webhook_endpoint.failing`, `webhook_endpoint.recovered`).
- New error code `reauth_required` (401): sign in again before changing payout details.

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
