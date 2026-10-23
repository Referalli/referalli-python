"""Official Referalli SDK for Python.

    from referalli import Referalli

    client = Referalli(api_key="rk_live_...")
    link = client.post_links({"programId": "prg_...", "partnerId": "ptr_...", "destinationUrl": "https://example.com"})
    for partner in client.get_partners_iter(status="active"):
        ...

``AsyncReferalli`` has the same methods, awaited (``pip install "referalli[async]"``).
"""

from . import webhooks
from ._async_client import AsyncReferalli
from ._base import DEFAULT_BASE_URL
from ._client import Referalli
from ._errors import *  # noqa: F401,F403
from ._errors import ERROR_CLASSES, ApiConnectionError, ApiError, ReferalliError, WebhookVerificationError
from ._operations import OPERATIONS
from ._page import Page
from ._version import API_VERSION, VERSION
from ._webhook_events import TOPICS, WebhookEvent
from .webhooks import WEBHOOK_TOLERANCE_SEC, construct_event, verify_webhook

__version__ = VERSION
__all__ = [
    "API_VERSION",
    "ApiConnectionError",
    "ApiError",
    "AsyncReferalli",
    "DEFAULT_BASE_URL",
    "ERROR_CLASSES",
    "OPERATIONS",
    "Page",
    "Referalli",
    "ReferalliError",
    "TOPICS",
    "VERSION",
    "WEBHOOK_TOLERANCE_SEC",
    "WebhookEvent",
    "WebhookVerificationError",
    "construct_event",
    "verify_webhook",
    "webhooks",
]
