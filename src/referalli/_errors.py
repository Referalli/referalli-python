# Code generated from the Referalli OpenAPI document. DO NOT EDIT.
# Changes belong in the generator, which overwrites this file.
"""Typed API errors: one class per error code the API emits."""

from __future__ import annotations

from typing import Any, Dict, Mapping, Optional, Type


class ReferalliError(Exception):
    """Base class for every error this SDK raises."""


class ApiConnectionError(ReferalliError):
    """The API could not be reached (network error or timeout), after retries."""


class WebhookVerificationError(ReferalliError):
    """A webhook delivery failed signature or timestamp verification, or isn't a JSON event."""


class ApiError(ReferalliError):
    """The API answered with an error. ``code`` is stable; ``docs_url`` explains it."""

    def __init__(self, status: int, code: str, message: str, *, request_id: Optional[str] = None,
                 docs_url: Optional[str] = None, details: Any = None, retry_after: Optional[float] = None,
                 headers: Optional[Mapping[str, str]] = None) -> None:
        super().__init__(f"{code} ({status}): {message}")
        self.status = status
        self.code = code
        self.message = message
        self.request_id = request_id
        self.docs_url = docs_url
        self.details = details
        self.retry_after = retry_after
        self.headers = dict(headers or {})


class ValidationError(ApiError):
    """``validation_error`` (HTTP 400)."""


class ModeMismatchError(ApiError):
    """``mode_mismatch`` (HTTP 400)."""


class BadRequestError(ApiError):
    """``bad_request`` (HTTP 400)."""


class AuthenticationError(ApiError):
    """``unauthorized`` (HTTP 401)."""


class StepUpRequiredError(ApiError):
    """``step_up_required`` (HTTP 401)."""


class PaymentRequiredError(ApiError):
    """``payment_required`` (HTTP 402)."""


class PermissionDeniedError(ApiError):
    """``forbidden`` (HTTP 403)."""


class WebhooksDisabledError(ApiError):
    """``webhooks_disabled`` (HTTP 403)."""


class SsoRequiredError(ApiError):
    """``sso_required`` (HTTP 403)."""


class AccessSuspendedError(ApiError):
    """``access_suspended`` (HTTP 403)."""


class NotFoundError(ApiError):
    """``not_found`` (HTTP 404)."""


class ConflictError(ApiError):
    """``conflict`` (HTTP 409)."""


class IdempotencyInProgressError(ApiError):
    """``idempotency_in_progress`` (HTTP 409)."""


class ReplayError(ApiError):
    """``replay`` (HTTP 409)."""


class LiveModeOnlyError(ApiError):
    """``live_mode_only`` (HTTP 409)."""


class TestModeOnlyError(ApiError):
    """``test_mode_only`` (HTTP 409)."""


class TestModeUnsupportedError(ApiError):
    """``test_mode_unsupported`` (HTTP 409)."""


class GoneError(ApiError):
    """``gone`` (HTTP 410)."""


class IdempotencyKeyReusedError(ApiError):
    """``idempotency_key_reused`` (HTTP 422)."""


class PayloadTooLargeError(ApiError):
    """``payload_too_large`` (HTTP 413)."""


class ConnectionPausedError(ApiError):
    """``connection_paused`` (HTTP 423)."""


class RateLimitedError(ApiError):
    """``rate_limited`` (HTTP 429)."""


class InternalServerError(ApiError):
    """``internal_error`` (HTTP 500)."""


class AtlasError(ApiError):
    """``atlas_error`` (HTTP 502)."""


class SsoProviderError(ApiError):
    """``sso_provider_error`` (HTTP 502)."""


class SsoNotConfiguredError(ApiError):
    """``sso_not_configured`` (HTTP 503)."""


ERROR_CLASSES: Dict[str, Type[ApiError]] = {
    "validation_error": ValidationError,
    "mode_mismatch": ModeMismatchError,
    "bad_request": BadRequestError,
    "unauthorized": AuthenticationError,
    "step_up_required": StepUpRequiredError,
    "payment_required": PaymentRequiredError,
    "forbidden": PermissionDeniedError,
    "webhooks_disabled": WebhooksDisabledError,
    "sso_required": SsoRequiredError,
    "access_suspended": AccessSuspendedError,
    "not_found": NotFoundError,
    "conflict": ConflictError,
    "idempotency_in_progress": IdempotencyInProgressError,
    "replay": ReplayError,
    "live_mode_only": LiveModeOnlyError,
    "test_mode_only": TestModeOnlyError,
    "test_mode_unsupported": TestModeUnsupportedError,
    "gone": GoneError,
    "idempotency_key_reused": IdempotencyKeyReusedError,
    "payload_too_large": PayloadTooLargeError,
    "connection_paused": ConnectionPausedError,
    "rate_limited": RateLimitedError,
    "internal_error": InternalServerError,
    "atlas_error": AtlasError,
    "sso_provider_error": SsoProviderError,
    "sso_not_configured": SsoNotConfiguredError,
}
