# Code generated from the Referalli OpenAPI document. DO NOT EDIT.
# Changes belong in the generator, which overwrites this file.
"""One method per Referalli API operation: ``Operations`` (sync) and ``AsyncOperations``."""

from __future__ import annotations

from typing import Any, AsyncIterator, Callable, Dict, Iterator, List, Literal, Optional, Union
from urllib.parse import quote

from .models import *  # noqa: F401,F403
from .models import Page


def _seg(value: str) -> str:
    return quote(str(value), safe="")


class Operations:
    _request: Callable[..., Any]
    _paginate: Callable[..., Any]

    def delete_api_keys_id(self, id: str, *, cascade: Optional[Literal["true", "false"]] = None, pair: Optional[Literal["true", "false"]] = None, idempotency_key: Optional[str] = None) -> DeleteApiKeysIdResponse:
        """Revoke an API key. DELETE /v1/api-keys/{id}

        Revokes a key at once. `cascade=true` also revokes every key it minted (and theirs); `pair=true` also revokes its live/test twin. Returns the revoked ids. Needs an owner or admin session, or an API key with the `admin` scope. Audited.

        **Auth:** an API key with `team:write` (or `full`), or a session of any role.

        cascade: true: also revoke every key this key minted, and theirs.
        pair: true: also revoke its live/test twin.
        """
        return self._request("DELETE", f"/v1/api-keys/{_seg(id)}", query={"cascade": cascade, "pair": pair}, body=None, idempotency_key=idempotency_key, kind="json")

    def delete_assets_id(self, id: str, *, idempotency_key: Optional[str] = None) -> Ok:
        """Delete a marketing asset. DELETE /v1/assets/{id}

        Removes a marketing asset.

        **Auth:** an API key with `partners:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("DELETE", f"/v1/assets/{_seg(id)}", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def delete_auth_connections_id(self, id: str, *, idempotency_key: Optional[str] = None) -> Ok:
        """Delete an auth connection. DELETE /v1/auth/connections/{id}

        Removes the connection; its webhook URL and signed endpoints stop accepting calls. Referrals it filed stay.

        **Auth:** an API key with `integrations:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("DELETE", f"/v1/auth/connections/{_seg(id)}", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def delete_billing_connections_id(self, id: str, *, idempotency_key: Optional[str] = None) -> Ok:
        """Delete a billing connection. DELETE /v1/billing/connections/{id}

        Deletes the connection: its secrets and credentials are wiped and its webhook URL stops accepting events. Recorded billing events stay. Audited.

        **Auth:** an API key with `billing:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("DELETE", f"/v1/billing/connections/{_seg(id)}", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def delete_branding_domain(self, *, idempotency_key: Optional[str] = None) -> Ok:
        """Remove the portal domain. DELETE /v1/branding/domain

        Stops serving the partner portal on the custom domain.

        **Auth:** an API key with `org:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("DELETE", f"/v1/branding/domain", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def delete_branding_link_domain(self, *, idempotency_key: Optional[str] = None) -> Ok:
        """Remove the link domain. DELETE /v1/branding/link-domain

        Stops using the custom link domain; links go back to the default host.

        **Auth:** an API key with `org:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("DELETE", f"/v1/branding/link-domain", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def delete_cli_listeners_id(self, id: str, *, idempotency_key: Optional[str] = None) -> Ok:
        """Close a CLI listener. DELETE /v1/cli/listeners/{id}

        Closes the listener; queued events are dropped.

        **Auth:** an API key with `webhooks:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("DELETE", f"/v1/cli/listeners/{_seg(id)}", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def delete_email_templates_event_locale(self, event: str, locale: str, *, idempotency_key: Optional[str] = None) -> DeleteEmailTemplatesEventLocaleResponse:
        """Reset an email template. DELETE /v1/email/templates/{event}/{locale}

        Removes the override; the default template is used again.

        **Auth:** an API key with `org:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("DELETE", f"/v1/email/templates/{_seg(event)}/{_seg(locale)}", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def delete_integrations_kind(self, kind: str, *, idempotency_key: Optional[str] = None) -> Ok:
        """Disconnect an integration. DELETE /v1/integrations/{kind}

        Removes the HubSpot or Segment connection and its stored credential.

        **Auth:** an API key with `integrations:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("DELETE", f"/v1/integrations/{_seg(kind)}", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def delete_org_members_user_id(self, user_id: str, *, idempotency_key: Optional[str] = None) -> Ok:
        """Remove a team member. DELETE /v1/org/members/{userId}

        Removes a member. Members can remove themselves; otherwise owner or admin. The last owner stays (409). Audited. Live mode only.

        **Auth:** an API key with `team:write` (or `full`), or a session of any role.
        """
        return self._request("DELETE", f"/v1/org/members/{_seg(user_id)}", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def delete_partners_id(self, id: str, *, idempotency_key: Optional[str] = None) -> Ok:
        """Delete a partner. DELETE /v1/partners/{id}

        Deletes a partner that never did anything, with its enrollments, links, coupons and payout profile. A partner with any clicks, referrals, commissions, payouts or other history is `409`: archive it instead (`status: "archived"`). Audited.

        **Auth:** an API key with `partners:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("DELETE", f"/v1/partners/{_seg(id)}", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def delete_payout_connections_provider(self, provider: str, *, idempotency_key: Optional[str] = None) -> DeletePayoutConnectionsProviderResponse:
        """Disconnect a payout provider. DELETE /v1/payout-connections/{provider}

        Removes the stored credentials for a provider. Payouts by that method are then simulated until you reconnect. Audited.

        **Auth:** an API key with `payouts:write` (or `full`), or a session with role `owner`, `admin`, `finance`.
        """
        return self._request("DELETE", f"/v1/payout-connections/{_seg(provider)}", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def delete_profitability_products_product_ref(self, product_ref: str, *, idempotency_key: Optional[str] = None) -> OkStatus:
        """Delete a product margin. DELETE /v1/profitability/products/{productRef}

        Removes a product from the margin catalog; its payments fall back to the program or org margin. Audited.

        **Auth:** an API key with `analytics:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("DELETE", f"/v1/profitability/products/{_seg(product_ref)}", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def delete_webhook_endpoints_id(self, id: str, *, idempotency_key: Optional[str] = None) -> Ok:
        """Delete a webhook endpoint. DELETE /v1/webhook-endpoints/{id}

        Removes the endpoint and its delivery history. Audited.

        **Auth:** an API key with `webhooks:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("DELETE", f"/v1/webhook-endpoints/{_seg(id)}", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def delete_zapier_hooks_id(self, id: str, *, idempotency_key: Optional[str] = None) -> Ok:
        """Unsubscribe a Zapier hook. DELETE /v1/zapier/hooks/{id}

        REST hook unsubscribe, called by Zapier when a Zap turns off.

        **Auth:** an API key with `integrations:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("DELETE", f"/v1/zapier/hooks/{_seg(id)}", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_admin_metrics(self, *, idempotency_key: Optional[str] = None) -> GetAdminMetricsResponse:
        """Get platform metrics. GET /v1/admin/metrics

        Platform admins only. Live orgs (and suspended ones), partner accounts (and banned ones), programs, commission earned, payouts sent and open fraud cases across the platform.

        **Auth:** a platform admin session.
        """
        return self._request("GET", f"/v1/admin/metrics", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_admin_orgs(self, *, q: Optional[str] = None, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetAdminOrgsResponseDataItem]:
        """List organizations. GET /v1/admin/orgs

        Platform admins only. Organizations, searchable by name with `q`.

        **Auth:** a platform admin session.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/admin/orgs", query={"q": q, "limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_admin_orgs_iter(self, *, q: Optional[str] = None, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[GetAdminOrgsResponseDataItem]:
        """Every item of ``get_admin_orgs``, following the pages."""
        return self._paginate(lambda cursor: self.get_admin_orgs(q=q, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_admin_partner_accounts(self, *, flagged: Optional[bool] = None, q: Optional[str] = None, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetAdminPartnerAccountsResponseDataItem]:
        """List partner accounts. GET /v1/admin/partner-accounts

        Platform admins only. Partner accounts with KYC and sanctions status, filtered by `flagged` (banned) and text `q`.

        **Auth:** a platform admin session.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/admin/partner-accounts", query={"flagged": flagged, "q": q, "limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_admin_partner_accounts_iter(self, *, flagged: Optional[bool] = None, q: Optional[str] = None, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[GetAdminPartnerAccountsResponseDataItem]:
        """Every item of ``get_admin_partner_accounts``, following the pages."""
        return self._paginate(lambda cursor: self.get_admin_partner_accounts(flagged=flagged, q=q, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_agents(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetAgentsResponseDataItem]:
        """List partnered AI agents. GET /v1/agents

        The AI agents partnered with this org, with their wallet, metadata and how many recommendations each has attributed, most active first.

        **Auth:** an API key with `growth:read` (or `full`), or a session with role `owner`, `admin`, `analyst`.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/agents", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_agents_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[GetAgentsResponseDataItem]:
        """Every item of ``get_agents``, following the pages."""
        return self._paginate(lambda cursor: self.get_agents(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_agents_recommendations(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetAgentsRecommendationsResponseDataItem]:
        """List agent recommendations. GET /v1/agents/recommendations

        Signed recommendations AI agents have attributed in this org, newest first.

        **Auth:** an API key with `growth:read` (or `full`), or a session with role `owner`, `admin`, `analyst`.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/agents/recommendations", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_agents_recommendations_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[GetAgentsRecommendationsResponseDataItem]:
        """Every item of ``get_agents_recommendations``, following the pages."""
        return self._paginate(lambda cursor: self.get_agents_recommendations(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_analytics_by_channel(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetAnalyticsByChannelResponseDataItem]:
        """Get revenue by channel. GET /v1/analytics/by-channel

        Referrals and referred revenue by how they were matched (`coupon`, `deterministic` click, `email_hash`, `probabilistic`, `manual`…).

        **Auth:** an API key with `analytics:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/analytics/by-channel", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_analytics_by_channel_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[GetAnalyticsByChannelResponseDataItem]:
        """Every item of ``get_analytics_by_channel``, following the pages."""
        return self._paginate(lambda cursor: self.get_analytics_by_channel(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_analytics_by_geo(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetAnalyticsByGeoResponseDataItem]:
        """Get revenue by country. GET /v1/analytics/by-geo

        Referrals and referred revenue by the country of the winning click, highest revenue first.

        **Auth:** an API key with `analytics:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/analytics/by-geo", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_analytics_by_geo_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[GetAnalyticsByGeoResponseDataItem]:
        """Every item of ``get_analytics_by_geo``, following the pages."""
        return self._paginate(lambda cursor: self.get_analytics_by_geo(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_analytics_cohort_ltv(self, *, months: Optional[int] = None, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetAnalyticsCohortLtvResponseDataItem]:
        """Get cohort LTV. GET /v1/analytics/cohort-ltv

        Referred customers grouped by sign-up month over the last `months` (default 6), with net revenue (payments minus refunds) and revenue per customer.

        **Auth:** an API key with `analytics:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/analytics/cohort-ltv", query={"months": months, "limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_analytics_cohort_ltv_iter(self, *, months: Optional[int] = None, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[GetAnalyticsCohortLtvResponseDataItem]:
        """Every item of ``get_analytics_cohort_ltv``, following the pages."""
        return self._paginate(lambda cursor: self.get_analytics_cohort_ltv(months=months, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_analytics_coupon_performance(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetAnalyticsCouponPerformanceResponseDataItem]:
        """Get coupon performance. GET /v1/analytics/coupon-performance

        Referrals and revenue per coupon code, highest revenue first.

        **Auth:** an API key with `analytics:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/analytics/coupon-performance", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_analytics_coupon_performance_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[GetAnalyticsCouponPerformanceResponseDataItem]:
        """Every item of ``get_analytics_coupon_performance``, following the pages."""
        return self._paginate(lambda cursor: self.get_analytics_coupon_performance(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_analytics_overview(self, *, program_id: Optional[str] = None, days: Optional[int] = None, idempotency_key: Optional[str] = None) -> GetAnalyticsOverviewResponse:
        """Get the funnel overview. GET /v1/analytics/overview

        Over the last `days` (default 30), optionally for one program: clicks (and how many were filtered), visitors, sign-ups, payments, referred revenue, commission earned and reversed, active partners and the click-to-sign-up and sign-up-to-paid rates.

        **Auth:** an API key with `analytics:read` (or `full`), or a session of any role.
        """
        return self._request("GET", f"/v1/analytics/overview", query={"programId": program_id, "days": days}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_analytics_timeseries(self, *, metric: Literal["clicks", "signups", "revenue"], days: Optional[int] = None, program_id: Optional[str] = None, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetAnalyticsTimeseriesResponseDataItem]:
        """Get a daily time series. GET /v1/analytics/timeseries

        One `metric` (`clicks`, `signups` or `revenue` in minor units) per day over the last `days`, optionally for one program.

        **Auth:** an API key with `analytics:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/analytics/timeseries", query={"metric": metric, "days": days, "programId": program_id, "limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_analytics_timeseries_iter(self, *, metric: Literal["clicks", "signups", "revenue"], days: Optional[int] = None, program_id: Optional[str] = None, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[GetAnalyticsTimeseriesResponseDataItem]:
        """Every item of ``get_analytics_timeseries``, following the pages."""
        return self._paginate(lambda cursor: self.get_analytics_timeseries(metric=metric, days=days, program_id=program_id, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_api_keys(self, *, mode: Optional[Literal["live", "test"]] = None, owner: Optional[str] = None, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[ApiKey]:
        """List API keys. GET /v1/api-keys

        Every key of the org, live and test (a test-mode caller sees test keys only), oldest first, with scopes, pinned version, owner, expiry and last use. Never returns the secret. Filter by `mode` or `owner`.

        **Auth:** an API key with `team:read` (or `full`), or a session of any role.

        mode: Only live or only test keys; default both.
        owner: Only keys with this owner.
        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/api-keys", query={"mode": mode, "owner": owner, "limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_api_keys_iter(self, *, mode: Optional[Literal["live", "test"]] = None, owner: Optional[str] = None, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[ApiKey]:
        """Every item of ``get_api_keys``, following the pages."""
        return self._paginate(lambda cursor: self.get_api_keys(mode=mode, owner=owner, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_api_keys_id(self, id: str, *, idempotency_key: Optional[str] = None) -> ApiKey:
        """Get an API key. GET /v1/api-keys/{id}

        One key of the org, without its secret.

        **Auth:** an API key with `team:read` (or `full`), or a session of any role.
        """
        return self._request("GET", f"/v1/api-keys/{_seg(id)}", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_assets(self, *, program_id: Optional[str] = None, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetAssetsResponseDataItem]:
        """List marketing assets. GET /v1/assets

        Marketing assets, filtered by `programId`.

        **Auth:** an API key with `partners:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/assets", query={"programId": program_id, "limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_assets_iter(self, *, program_id: Optional[str] = None, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[GetAssetsResponseDataItem]:
        """Every item of ``get_assets``, following the pages."""
        return self._paginate(lambda cursor: self.get_assets(program_id=program_id, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_assistant_suggestions(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetAssistantSuggestionsResponseDataItem]:
        """Get program suggestions. GET /v1/assistant/suggestions

        Draft-only suggestions for running the program, each with a suggested action for a person to take: partners who never drove a click, links with clicks but no referrals, programs without a commission rule, the review queue, and credit ROI findings. It never changes anything.

        **Auth:** an API key with `analytics:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/assistant/suggestions", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_assistant_suggestions_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[GetAssistantSuggestionsResponseDataItem]:
        """Every item of ``get_assistant_suggestions``, following the pages."""
        return self._paginate(lambda cursor: self.get_assistant_suggestions(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_audit_logs(self, *, actor: Optional[str] = None, actor_type: Optional[str] = None, action: Optional[str] = None, subject_type: Optional[str] = None, subject_id: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[AuditLogEntry]:
        """List audit log entries. GET /v1/audit-logs

        Every change recorded in the org, newest first: who did it (`actor`, `actorType`), what (`action`; a trailing `*` matches a prefix such as `payout.*`) and to what (`subjectType`, `subjectId`). Filter by any of those and by `created[gte]`/`created[lte]`.

        **Auth:** an API key with `audit:read` (or `full`), or a session with role `owner`, `admin`.

        actor: Actor id: a user, API key or connection id.
        action: Exact action, or a prefix ending in * (e.g. payout.*).
        starting_after: An entry id: return the entries after it.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/audit-logs", query={"actor": actor, "actorType": actor_type, "action": action, "subjectType": subject_type, "subjectId": subject_id, "created[gte]": created_gte, "created[lte]": created_lte, "limit": limit, "starting_after": starting_after, "ending_before": ending_before}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_audit_logs_iter(self, *, actor: Optional[str] = None, actor_type: Optional[str] = None, action: Optional[str] = None, subject_type: Optional[str] = None, subject_id: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, limit: Optional[int] = None, ending_before: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[AuditLogEntry]:
        """Every item of ``get_audit_logs``, following the pages."""
        return self._paginate(lambda cursor: self.get_audit_logs(actor=actor, actor_type=actor_type, action=action, subject_type=subject_type, subject_id=subject_id, created_gte=created_gte, created_lte=created_lte, limit=limit, ending_before=ending_before, starting_after=cursor, idempotency_key=idempotency_key))

    def get_auth_connections(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[AuthConnection]:
        """List auth connections. GET /v1/auth/connections

        Auth-platform connections with provider, program, status, signature version and rotation state. Secrets are never returned.

        **Auth:** an API key with `integrations:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/auth/connections", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_auth_connections_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[AuthConnection]:
        """Every item of ``get_auth_connections``, following the pages."""
        return self._paginate(lambda cursor: self.get_auth_connections(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_auth_connections_id_export(self, id: str, *, customer_ref: str, idempotency_key: Optional[str] = None) -> GetAuthConnectionsIdExportResponse:
        """Export a user (signed protocol). GET /v1/auth/connections/{id}/export

        An access request the platform forwards: everything filed under the customer and their partner record. Signed with the connection secret in `x-referalli-signature: t=<unix>,v1=…,v2=…` (v2 also signs the request line; once a connection has seen v2 it requires it), with a unique `x-referalli-id` per call. Calls older than 5 minutes, reused ids (`409 replay`), paused connections (`423 connection_paused`) and unknown fields (`422`) are refused.

        **Auth:** a signature (see above); no API key.
        """
        return self._request("GET", f"/v1/auth/connections/{_seg(id)}/export", query={"customerRef": customer_ref}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_auth_providers(self, *, idempotency_key: Optional[str] = None) -> GetAuthProvidersResponse:
        """List sign-in providers. GET /v1/auth/providers

        The identity providers configured on this deployment, for rendering sign-in buttons.

        **Auth:** none.
        """
        return self._request("GET", f"/v1/auth/providers", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_billing_connections(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[BillingConnection]:
        """List billing connections. GET /v1/billing/connections

        Billing connections (deleted ones excluded), with status, whether credentials are needed and set, the value mapping and secret-rotation state.

        **Auth:** an API key with `billing:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/billing/connections", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_billing_connections_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[BillingConnection]:
        """Every item of ``get_billing_connections``, following the pages."""
        return self._paginate(lambda cursor: self.get_billing_connections(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_billing_connections_id(self, id: str, *, idempotency_key: Optional[str] = None) -> BillingConnection:
        """Get a billing connection. GET /v1/billing/connections/{id}

        One billing connection, without its secrets.

        **Auth:** an API key with `billing:read` (or `full`), or a session of any role.
        """
        return self._request("GET", f"/v1/billing/connections/{_seg(id)}", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_billing_events(self, *, customer_ref: Optional[str] = None, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[BillingEvent]:
        """List billing events. GET /v1/billing/events

        Payments, refunds and other billing events received from every connection, newest first. Filter with `customerRef`.

        **Auth:** an API key with `billing:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/billing/events", query={"customerRef": customer_ref, "limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_billing_events_iter(self, *, customer_ref: Optional[str] = None, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[BillingEvent]:
        """Every item of ``get_billing_events``, following the pages."""
        return self._paginate(lambda cursor: self.get_billing_events(customer_ref=customer_ref, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_billing_plan(self, *, idempotency_key: Optional[str] = None) -> GetBillingPlanResponse:
        """Get the plan. GET /v1/billing/plan

        The org's Referalli plan and status, its limits and current usage (programs, partners), the plan catalog, whether there is a subscription to manage and whether this caller may activate a plan without checkout.

        **Auth:** an API key with `billing:read` (or `full`), or a session of any role.
        """
        return self._request("GET", f"/v1/billing/plan", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_branding(self, *, idempotency_key: Optional[str] = None) -> GetBrandingResponse:
        """Get branding. GET /v1/branding

        The org's logo, theme tokens, sender address, and its custom portal and link domains with their status (`none`, `pending` DNS, `provisioning` a certificate, `active`).

        **Auth:** an API key with `org:read` (or `full`), or a session of any role.
        """
        return self._request("GET", f"/v1/branding", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_cleanroom_consent(self, *, customer_ref: str, idempotency_key: Optional[str] = None) -> GetCleanroomConsentResponse:
        """Get a customer's consent. GET /v1/cleanroom/consent

        A customer's recorded consent: whether granted, its purposes, the attributes they declared and when it changed. `consent: null` when none is recorded.

        **Auth:** an API key with `growth:read` (or `full`), or a session of any role.
        """
        return self._request("GET", f"/v1/cleanroom/consent", query={"customerRef": customer_ref}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_cleanroom_query(self, *, dimension: str, idempotency_key: Optional[str] = None) -> GetCleanroomQueryResponse:
        """Query the clean room. GET /v1/cleanroom/query

        Aggregates over consenting customers only, grouped by a zero-party attribute they declared (`dimension`): customers, converted customers and referred revenue per value. Cohorts smaller than 5 are suppressed (k-anonymity); individual rows never leave.

        **Auth:** an API key with `growth:read` (or `full`), or a session of any role.
        """
        return self._request("GET", f"/v1/cleanroom/query", query={"dimension": dimension}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_cli_device_codes_user_code(self, user_code: str, *, idempotency_key: Optional[str] = None) -> GetCliDeviceCodesUserCodeResponse:
        """Get a pending CLI sign-in. GET /v1/cli/device-codes/{userCode}

        For the approval page: the pending code, which CLI asked and when it expires. Needs a signed-in person (owner or admin). 404 when expired or used.

        **Auth:** an API key with `team:read` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("GET", f"/v1/cli/device-codes/{_seg(user_code)}", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_cli_listeners_id_events(self, id: str, *, wait: Optional[int] = None, idempotency_key: Optional[str] = None) -> GetCliListenersIdEventsResponse:
        """Receive listener events. GET /v1/cli/listeners/{id}/events

        Up to 50 queued events for the listener, oldest first, each with its body and signed headers. `wait` long-polls up to 25 seconds for the first event. Polling keeps the listener alive.

        **Auth:** an API key with `webhooks:read` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("GET", f"/v1/cli/listeners/{_seg(id)}/events", query={"wait": wait}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_cli_logs(self, *, after: Optional[int] = None, wait: Optional[int] = None, limit: Optional[int] = None, idempotency_key: Optional[str] = None) -> GetCliLogsResponse:
        """Tail the request log. GET /v1/cli/logs

        The CLI's `logs tail` command: the org's recent API requests (method, path without query string, status, latency, actor). The first call returns the latest 20 and a `cursor`; pass it as `after` (with `wait` to long-poll up to 25 seconds) for newer entries. Kept for a day.

        **Auth:** an API key with `audit:read` (or `full`), or a session with role `owner`, `admin`.

        after: Return entries after this cursor.
        """
        return self._request("GET", f"/v1/cli/logs", query={"after": after, "wait": wait, "limit": limit}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_cli_topics(self, *, idempotency_key: Optional[str] = None) -> GetCliTopicsResponse:
        """List triggerable topics. GET /v1/cli/topics

        The event topics `POST /v1/cli/trigger` can send.

        **Auth:** an API key with `webhooks:read` (or `full`), or a session of any role.
        """
        return self._request("GET", f"/v1/cli/topics", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_commission_rules(self, *, program_id: Optional[str] = None, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[CommissionRule]:
        """List commission rules. GET /v1/commission-rules

        Every rule version, by program and newest version first. Filter with `programId`.

        **Auth:** an API key with `commissions:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/commission-rules", query={"programId": program_id, "limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_commission_rules_iter(self, *, program_id: Optional[str] = None, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[CommissionRule]:
        """Every item of ``get_commission_rules``, following the pages."""
        return self._paginate(lambda cursor: self.get_commission_rules(program_id=program_id, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_commissions(self, *, partner_id: Optional[str] = None, program_id: Optional[str] = None, type_: Optional[Literal["earned", "adjusted", "reversed", "approved", "paid"]] = None, referral_id: Optional[str] = None, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[CommissionEvent]:
        """List commission ledger events. GET /v1/commissions

        The append-only commission ledger, newest first: `earned` lines and the `approved`, `paid`, `reversed` and `adjusted` events recorded against them (`relatedCommissionId`). Filter by `partnerId`, `programId`, `type` or `referralId`.

        **Auth:** an API key with `commissions:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/commissions", query={"partnerId": partner_id, "programId": program_id, "type": type_, "referralId": referral_id, "limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_commissions_iter(self, *, partner_id: Optional[str] = None, program_id: Optional[str] = None, type_: Optional[Literal["earned", "adjusted", "reversed", "approved", "paid"]] = None, referral_id: Optional[str] = None, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[CommissionEvent]:
        """Every item of ``get_commissions``, following the pages."""
        return self._paginate(lambda cursor: self.get_commissions(partner_id=partner_id, program_id=program_id, type_=type_, referral_id=referral_id, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_commissions_id(self, id: str, *, idempotency_key: Optional[str] = None) -> CommissionLine:
        """Get a commission. GET /v1/commissions/{id}

        One ledger event. An `earned` line also carries its billing event, its net after reversals and adjustments, its state (`pending`, `approved` or `paid`) and every event recorded against it.

        **Auth:** an API key with `commissions:read` (or `full`), or a session of any role.
        """
        return self._request("GET", f"/v1/commissions/{_seg(id)}", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_contracts(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetContractsResponseDataItem]:
        """List partner contracts. GET /v1/contracts

        The org's contracts and their status (`draft`, `sent`, `accepted`, `declined`, `void`).

        **Auth:** an API key with `partners:read` (or `full`), or a session with role `owner`, `admin`.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/contracts", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_contracts_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[GetContractsResponseDataItem]:
        """Every item of ``get_contracts``, following the pages."""
        return self._paginate(lambda cursor: self.get_contracts(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_coupons(self, *, program_id: Optional[str] = None, partner_id: Optional[str] = None, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[Coupon]:
        """List coupon codes. GET /v1/coupons

        Coupon codes, filtered by `programId` and/or `partnerId`.

        **Auth:** an API key with `links:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/coupons", query={"programId": program_id, "partnerId": partner_id, "limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_coupons_iter(self, *, program_id: Optional[str] = None, partner_id: Optional[str] = None, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[Coupon]:
        """Every item of ``get_coupons``, following the pages."""
        return self._paginate(lambda cursor: self.get_coupons(program_id=program_id, partner_id=partner_id, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_creators(self, *, q: Optional[str] = None, category: Optional[str] = None, channel: Optional[str] = None, min_audience: Optional[int] = None, min_engagement_bps: Optional[int] = None, audience_country: Optional[str] = None, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[CreatorProfile]:
        """Search creators. GET /v1/creators

        Published creator profiles, most engaged first, filtered by text (`q`), `category`, `channel`, minimum audience, minimum engagement and audience country. Each carries verified stats and whether this org already invited them. Emails are never returned.

        **Auth:** an API key with `growth:read` (or `full`), or a session with role `owner`, `admin`.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/creators", query={"q": q, "category": category, "channel": channel, "minAudience": min_audience, "minEngagementBps": min_engagement_bps, "audienceCountry": audience_country, "limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_creators_iter(self, *, q: Optional[str] = None, category: Optional[str] = None, channel: Optional[str] = None, min_audience: Optional[int] = None, min_engagement_bps: Optional[int] = None, audience_country: Optional[str] = None, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[CreatorProfile]:
        """Every item of ``get_creators``, following the pages."""
        return self._paginate(lambda cursor: self.get_creators(q=q, category=category, channel=channel, min_audience=min_audience, min_engagement_bps=min_engagement_bps, audience_country=audience_country, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_creators_account_id(self, account_id: str, *, idempotency_key: Optional[str] = None) -> CreatorProfile:
        """Get a creator. GET /v1/creators/{accountId}

        One published creator profile with verified stats. 404 when not listed.

        **Auth:** an API key with `growth:read` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("GET", f"/v1/creators/{_seg(account_id)}", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_deals(self, *, status: Optional[Literal["submitted", "approved", "rejected", "won", "lost"]] = None, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetDealsResponseDataItem]:
        """List registered deals. GET /v1/deals

        Deals partners registered, newest first. Filter with `status` (`submitted`, `approved`, `rejected`, `won`, `lost`).

        **Auth:** an API key with `growth:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/deals", query={"status": status, "limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_deals_iter(self, *, status: Optional[Literal["submitted", "approved", "rejected", "won", "lost"]] = None, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[GetDealsResponseDataItem]:
        """Every item of ``get_deals``, following the pages."""
        return self._paginate(lambda cursor: self.get_deals(status=status, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_disputes(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetDisputesResponseDataItem]:
        """List partner disputes. GET /v1/disputes

        Disputes partners filed with this org, newest first.

        **Auth:** an API key with `commissions:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/disputes", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_disputes_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[GetDisputesResponseDataItem]:
        """Every item of ``get_disputes``, following the pages."""
        return self._paginate(lambda cursor: self.get_disputes(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_email_settings(self, *, idempotency_key: Optional[str] = None) -> EmailSettings:
        """Get email settings. GET /v1/email/settings

        The org's own email provider (`resend`, `brevo` or `postmark`), sender identity, branding and sending-domain status. The API key is never returned.

        **Auth:** an API key with `org:read` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("GET", f"/v1/email/settings", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_email_templates(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[EmailTemplateEvent]:
        """List email templates. GET /v1/email/templates

        Every email event with its placeholders and, per locale, the default template and the org's override if any.

        **Auth:** an API key with `org:read` (or `full`), or a session with role `owner`, `admin`.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/email/templates", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_email_templates_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[EmailTemplateEvent]:
        """Every item of ``get_email_templates``, following the pages."""
        return self._paginate(lambda cursor: self.get_email_templates(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_embed_summary(self, *, idempotency_key: Optional[str] = None) -> GetEmbedSummaryResponse:
        """Read embedded partner stats. GET /v1/embed/summary

        Called by the embed component with `Authorization: Bearer <embed token>`: the partner's name, eligible clicks, active referrals, balances and link codes. 401 for a missing, invalid or expired token.

        **Auth:** none.
        """
        return self._request("GET", f"/v1/embed/summary", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_export_accounting(self, *, format_: Optional[Literal["quickbooks", "xero"]] = None, year: int, idempotency_key: Optional[str] = None) -> str:
        """Export payouts for accounting. GET /v1/export/accounting

        A year's sent payouts as a CSV that QuickBooks (`format=quickbooks`, the default) or Xero imports.

        **Auth:** an API key with `payouts:read` (or `full`), or a session with role `owner`, `admin`, `finance`.
        """
        return self._request("GET", f"/v1/export/accounting", query={"format": format_, "year": year}, body=None, idempotency_key=idempotency_key, kind="text")

    def get_export_full(self, *, idempotency_key: Optional[str] = None) -> str:
        """Export all org data. GET /v1/export/full

        Every tenant table of the org as NDJSON (one JSON object per line, tagged with its table), streamed so any size works. Owner or admin.

        **Auth:** an API key with `analytics:read` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("GET", f"/v1/export/full", query={}, body=None, idempotency_key=idempotency_key, kind="text")

    def get_fraud_cases(self, *, status: Optional[Literal["open", "dismissed", "actioned"]] = None, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[FraudCase]:
        """List fraud cases. GET /v1/fraud/cases

        The fraud case queue (self-referrals, quality, rings, value patterns, identity risk), newest first, with the evidence. Filter with `status`.

        **Auth:** an API key with `fraud:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/fraud/cases", query={"status": status, "limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_fraud_cases_iter(self, *, status: Optional[Literal["open", "dismissed", "actioned"]] = None, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[FraudCase]:
        """Every item of ``get_fraud_cases``, following the pages."""
        return self._paginate(lambda cursor: self.get_fraud_cases(status=status, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_fx_rates(self, *, base: Optional[str] = None, quote: Optional[str] = None, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[FxRate]:
        """List FX rates. GET /v1/fx-rates

        The org's rates first, then the platform fallback, newest per pair first. A payout uses the org's latest rate at or before the run, else the platform's. Filter by `base` and `quote`.

        **Auth:** an API key with `payouts:read` (or `full`), or a session with role `owner`, `admin`, `finance`.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/fx-rates", query={"base": base, "quote": quote, "limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_fx_rates_iter(self, *, base: Optional[str] = None, quote: Optional[str] = None, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[FxRate]:
        """Every item of ``get_fx_rates``, following the pages."""
        return self._paginate(lambda cursor: self.get_fx_rates(base=base, quote=quote, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_graphql(self, *, idempotency_key: Optional[str] = None) -> GetGraphqlResponse:
        """Query the GraphQL read layer. GET /v1/graphql

        A read-only GraphQL endpoint over the same org-scoped data as REST (programs, partners, referrals, analytics), with the same authentication. Mutations stay in REST.

        **Auth:** an API key with `analytics:read` (or `full`), or a session of any role.
        """
        return self._request("GET", f"/v1/graphql", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_health(self, *, idempotency_key: Optional[str] = None) -> Ok:
        """Check API health. GET /v1/health

        `200 { "ok": true }` when this instance can serve requests: both database pools answer and it is not shutting down. Otherwise `503` with `reason` (`shutting_down`, with `Retry-After`, or `database_unreachable`).

        **Auth:** none.
        """
        return self._request("GET", f"/v1/health", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_hosts_current(self, *, idempotency_key: Optional[str] = None) -> GetHostsCurrentResponse:
        """Describe the current host. GET /v1/hosts/current

        What the request's host is: a merchant's verified portal domain (with the org's name, branding and public programs), a merchant link domain, or Referalli's own app. Used by the web app before anyone signs in.

        **Auth:** none.
        """
        return self._request("GET", f"/v1/hosts/current", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_hosts_current_theme_css(self, *, idempotency_key: Optional[str] = None) -> str:
        """Get the current host's theme stylesheet. GET /v1/hosts/current/theme.css

        On a merchant's portal domain, the org's theme tokens as a `:root` stylesheet; empty elsewhere.

        **Auth:** none.
        """
        return self._request("GET", f"/v1/hosts/current/theme.css", query={}, body=None, idempotency_key=idempotency_key, kind="text")

    def get_incrementality(self, *, program_id: str, idempotency_key: Optional[str] = None) -> GetIncrementalityResponse:
        """Get incrementality results. GET /v1/incrementality

        For a program's active referrals: treatment and control counts, conversion rates and lift, overall and per partner.

        **Auth:** an API key with `analytics:read` (or `full`), or a session of any role.
        """
        return self._request("GET", f"/v1/incrementality", query={"programId": program_id}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_integrations(self, *, idempotency_key: Optional[str] = None) -> GetIntegrationsResponse:
        """List integrations. GET /v1/integrations

        The HubSpot and Segment connections with status, settings and the last test result. Credentials are never returned.

        **Auth:** an API key with `integrations:read` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("GET", f"/v1/integrations", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_integrations_deliveries(self, *, kind: Optional[Literal["zapier", "hubspot", "segment"]] = None, status: Optional[Literal["pending", "sent", "failed", "skipped"]] = None, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[IntegrationDelivery]:
        """List integration deliveries. GET /v1/integrations/deliveries

        What was sent to Zapier, HubSpot and Segment, newest first, filtered by `kind` and `status`.

        **Auth:** an API key with `integrations:read` (or `full`), or a session with role `owner`, `admin`.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/integrations/deliveries", query={"kind": kind, "status": status, "limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_integrations_deliveries_iter(self, *, kind: Optional[Literal["zapier", "hubspot", "segment"]] = None, status: Optional[Literal["pending", "sent", "failed", "skipped"]] = None, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[IntegrationDelivery]:
        """Every item of ``get_integrations_deliveries``, following the pages."""
        return self._paginate(lambda cursor: self.get_integrations_deliveries(kind=kind, status=status, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_invitations(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetInvitationsResponseDataItem]:
        """List creator invitations. GET /v1/invitations

        The org's creator invitations and their status (`pending`, `accepted`, `declined`, `withdrawn`).

        **Auth:** an API key with `partners:read` (or `full`), or a session with role `owner`, `admin`.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/invitations", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_invitations_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[GetInvitationsResponseDataItem]:
        """Every item of ``get_invitations``, following the pages."""
        return self._paginate(lambda cursor: self.get_invitations(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_links(self, *, program_id: Optional[str] = None, partner_id: Optional[str] = None, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[Link]:
        """List links. GET /v1/links

        Tracked links with their short URL and click count, filtered by `programId` and/or `partnerId`.

        **Auth:** an API key with `links:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/links", query={"programId": program_id, "partnerId": partner_id, "limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_links_iter(self, *, program_id: Optional[str] = None, partner_id: Optional[str] = None, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[Link]:
        """Every item of ``get_links``, following the pages."""
        return self._paginate(lambda cursor: self.get_links(program_id=program_id, partner_id=partner_id, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_links_id_qr(self, id: str, *, idempotency_key: Optional[str] = None) -> str:
        """Get a link's QR code. GET /v1/links/{id}/qr

        An SVG QR code for the link's short URL.

        **Auth:** an API key with `links:read` (or `full`), or a session of any role.
        """
        return self._request("GET", f"/v1/links/{_seg(id)}/qr", query={}, body=None, idempotency_key=idempotency_key, kind="text")

    def get_marketplace_listing(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetMarketplaceListingResponseDataItem]:
        """List the org's marketplace listings. GET /v1/marketplace/listing

        The org's listings with their platform-computed stats: eligible clicks, active referrals, earnings per click, conversion rate, payout reliability and approval latency.

        **Auth:** an API key with `growth:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/marketplace/listing", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_marketplace_listing_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[GetMarketplaceListingResponseDataItem]:
        """Every item of ``get_marketplace_listing``, following the pages."""
        return self._paginate(lambda cursor: self.get_marketplace_listing(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_me(self, *, idempotency_key: Optional[str] = None) -> GetMeResponse:
        """Get the current caller. GET /v1/me

        Who is calling. With a user session: the user and their org memberships (no `x-org-id` needed). With an API key: the key (name, prefix, scopes, pinned version, mode, owner, expiry) and its org.

        **Auth:** an API key with `team:read` (or `full`), or a session of any role.
        """
        return self._request("GET", f"/v1/me", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_negotiations(self, *, program_id: Optional[str] = None, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetNegotiationsResponseDataItem]:
        """List negotiation rounds. GET /v1/negotiations

        Agent negotiation rounds and their decisions, newest first, optionally for one program.

        **Auth:** an API key with `growth:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/negotiations", query={"programId": program_id, "limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_negotiations_iter(self, *, program_id: Optional[str] = None, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[GetNegotiationsResponseDataItem]:
        """Every item of ``get_negotiations``, following the pages."""
        return self._paginate(lambda cursor: self.get_negotiations(program_id=program_id, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_network_journey(self, *, email_hash: str, model: Optional[Literal["linear", "first", "last", "time_decay"]] = None, idempotency_key: Optional[str] = None) -> GetNetworkJourneyResponse:
        """Get a customer's network journey. GET /v1/network/journey

        For a hashed customer email, the partner accounts that touched them at any opted-in merchant (never which merchant) and each one's credit under `model`. 403 unless the org has joined the network.

        **Auth:** an API key with `growth:read` (or `full`), or a session of any role.
        """
        return self._request("GET", f"/v1/network/journey", query={"emailHash": email_hash, "model": model}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_network_settings(self, *, idempotency_key: Optional[str] = None) -> GetNetworkSettingsResponse:
        """Get network membership. GET /v1/network/settings

        Whether the org contributes to (and can read) the attribution network.

        **Auth:** an API key with `growth:read` (or `full`), or a session of any role.
        """
        return self._request("GET", f"/v1/network/settings", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_notifications(self, *, unread: Optional[Literal["true", "false"]] = None, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[Notification]:
        """List notifications. GET /v1/notifications

        The org's in-app notifications (failing webhooks, anomalies, answered invitations…), newest first. `unread=true` for unread only.

        **Auth:** an API key with `org:read` (or `full`), or a session of any role.

        unread: true: unread notifications only.
        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/notifications", query={"unread": unread, "limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_notifications_iter(self, *, unread: Optional[Literal["true", "false"]] = None, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[Notification]:
        """Every item of ``get_notifications``, following the pages."""
        return self._paginate(lambda cursor: self.get_notifications(unread=unread, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_onchain_connections(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetOnchainConnectionsResponseDataItem]:
        """List on-chain connections. GET /v1/onchain/connections

        The org's on-chain conversion connections.

        **Auth:** an API key with `billing:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/onchain/connections", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_onchain_connections_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[GetOnchainConnectionsResponseDataItem]:
        """Every item of ``get_onchain_connections``, following the pages."""
        return self._paginate(lambda cursor: self.get_onchain_connections(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_openapi_json(self, *, idempotency_key: Optional[str] = None) -> GetOpenapiJsonResponse:
        """Get the OpenAPI document. GET /v1/openapi.json

        This reference as an OpenAPI 3.1 document (JSON).

        **Auth:** none.
        """
        return self._request("GET", f"/v1/openapi.json", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_openapi_yaml(self, *, idempotency_key: Optional[str] = None) -> str:
        """Get the OpenAPI document as YAML. GET /v1/openapi.yaml

        The same OpenAPI 3.1 document as `GET /v1/openapi.json`, serialized as YAML.

        **Auth:** none.
        """
        return self._request("GET", f"/v1/openapi.yaml", query={}, body=None, idempotency_key=idempotency_key, kind="text")

    def get_org(self, *, idempotency_key: Optional[str] = None) -> Org:
        """Get the organization. GET /v1/org

        The current org: name, plan, settings, public `trackingToken`, payout KYC requirement and mode (`livemode`; test orgs also carry `liveOrgId`).

        **Auth:** an API key with `org:read` (or `full`), or a session of any role.
        """
        return self._request("GET", f"/v1/org", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_org_fx_feed(self, *, idempotency_key: Optional[str] = None) -> GetOrgFxFeedResponse:
        """Get the FX feed setting. GET /v1/org/fx-feed

        Whether the daily ECB reference-rate feed is on for this org, and the date of its latest rate.

        **Auth:** an API key with `org:read` (or `full`), or a session with role `owner`, `admin`, `finance`.
        """
        return self._request("GET", f"/v1/org/fx-feed", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_org_members(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[Member]:
        """List team members. GET /v1/org/members

        Members of the org with their role and email, oldest first.

        **Auth:** an API key with `team:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/org/members", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_org_members_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[Member]:
        """Every item of ``get_org_members``, following the pages."""
        return self._paginate(lambda cursor: self.get_org_members(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_org_payout_schedule(self, *, idempotency_key: Optional[str] = None) -> GetOrgPayoutScheduleResponse:
        """Get payout schedules. GET /v1/org/payout-schedule

        The org schedule and its next run date, plus each program's override (`{ kind: 'off' }`, its own schedule, or `null` to follow the org) and next run date.

        **Auth:** an API key with `payouts:read` (or `full`), or a session of any role.
        """
        return self._request("GET", f"/v1/org/payout-schedule", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_org_referral_params(self, *, idempotency_key: Optional[str] = None) -> GetOrgReferralParamsResponse:
        """Get referral query parameters. GET /v1/org/referral-params

        The query parameters aff.js reads a referral code from: the built-in ones (`via`, `ref`, `aff`) and the org's extra ones.

        **Auth:** an API key with `org:read` (or `full`), or a session of any role.
        """
        return self._request("GET", f"/v1/org/referral-params", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_org_retention(self, *, idempotency_key: Optional[str] = None) -> Retention:
        """Get the data retention policy. GET /v1/org/retention

        How many days each kind of raw data is kept before the nightly purge, the allowed minimum and default per kind, and the last purge run.

        **Auth:** an API key with `org:read` (or `full`), or a session of any role.
        """
        return self._request("GET", f"/v1/org/retention", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_org_sso(self, *, idempotency_key: Optional[str] = None) -> GetOrgSsoResponse:
        """Get SSO settings. GET /v1/org/sso

        Single sign-on for the org: whether SSO is configured on this deployment and linked to a directory tenant, its connections and domains, whether SSO is required, the role mapping, recent setup tickets and any provider error.

        **Auth:** an API key with `org:read` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("GET", f"/v1/org/sso", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_org_sso_connections_id_saml_metadata(self, id: str, *, idempotency_key: Optional[str] = None) -> GetOrgSsoConnectionsIdSamlMetadataResponse:
        """Get SAML metadata. GET /v1/org/sso/connections/{id}/saml-metadata

        The SAML service-provider metadata for one of the org's SSO connections, to give the identity provider.

        **Auth:** an API key with `org:read` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("GET", f"/v1/org/sso/connections/{_seg(id)}/saml-metadata", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_org_tax_profile(self, *, idempotency_key: Optional[str] = None) -> TaxProfile:
        """Get the tax profile. GET /v1/org/tax-profile

        The org's legal name, address, country, VAT id, EIN, domestic VAT rate, whether partner VAT ids are checked against EU VIES, and the 1099 filing provider.

        **Auth:** an API key with `org:read` (or `full`), or a session with role `owner`, `admin`, `finance`.
        """
        return self._request("GET", f"/v1/org/tax-profile", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_outreach(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetOutreachResponseDataItem]:
        """List outreach messages. GET /v1/outreach

        Drafted, approved and sent outreach messages, newest first.

        **Auth:** an API key with `growth:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/outreach", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_outreach_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[GetOutreachResponseDataItem]:
        """Every item of ``get_outreach``, following the pages."""
        return self._paginate(lambda cursor: self.get_outreach(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_partner_achievements(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetPartnerAchievementsResponseDataItem]:
        """List my achievements. GET /v1/partner/achievements

        Badges computed from the ledger (first click, referral milestones, first payout, $1,000 earned), each with progress toward its target.

        **Auth:** a partner session.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/partner/achievements", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_partner_achievements_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[GetPartnerAchievementsResponseDataItem]:
        """Every item of ``get_partner_achievements``, following the pages."""
        return self._paginate(lambda cursor: self.get_partner_achievements(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_partner_advance(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetPartnerAdvanceResponseDataItem]:
        """List my advances. GET /v1/partner/advance

        The partner's advances with what remains to repay.

        **Auth:** a partner session.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/partner/advance", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_partner_advance_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[GetPartnerAdvanceResponseDataItem]:
        """Every item of ``get_partner_advance``, following the pages."""
        return self._paginate(lambda cursor: self.get_partner_advance(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_partner_advance_offer(self, *, idempotency_key: Optional[str] = None) -> GetPartnerAdvanceOfferResponse:
        """Get my advance offer. GET /v1/partner/advance/offer

        How much the partner could receive now against future commissions (`maxAdvanceMinor`), from their recent run rate and quality score, and the fee.

        **Auth:** a partner session.
        """
        return self._request("GET", f"/v1/partner/advance/offer", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_partner_assets(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetPartnerAssetsResponseDataItem]:
        """List marketing assets. GET /v1/partner/assets

        Marketing assets (copy, images, banners) of the programs the partner is approved in; group-only assets show only to that group's members.

        **Auth:** a partner session.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/partner/assets", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_partner_assets_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[GetPartnerAssetsResponseDataItem]:
        """Every item of ``get_partner_assets``, following the pages."""
        return self._paginate(lambda cursor: self.get_partner_assets(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_partner_contracts(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetPartnerContractsResponseDataItem]:
        """List my contracts. GET /v1/partner/contracts

        Contracts merchants sent the partner.

        **Auth:** a partner session.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/partner/contracts", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_partner_contracts_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[GetPartnerContractsResponseDataItem]:
        """Every item of ``get_partner_contracts``, following the pages."""
        return self._paginate(lambda cursor: self.get_partner_contracts(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_partner_deals(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetPartnerDealsResponseDataItem]:
        """List my deals. GET /v1/partner/deals

        The partner's registered deals across merchants, newest first.

        **Auth:** a partner session.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/partner/deals", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_partner_deals_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[GetPartnerDealsResponseDataItem]:
        """Every item of ``get_partner_deals``, following the pages."""
        return self._paginate(lambda cursor: self.get_partner_deals(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_partner_disputes(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetPartnerDisputesResponseDataItem]:
        """List my disputes. GET /v1/partner/disputes

        Disputes the partner filed about missing or wrong credit, newest first, with the merchant's resolution.

        **Auth:** a partner session.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/partner/disputes", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_partner_disputes_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[GetPartnerDisputesResponseDataItem]:
        """Every item of ``get_partner_disputes``, following the pages."""
        return self._paginate(lambda cursor: self.get_partner_disputes(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_partner_groups(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetPartnerGroupsResponseDataItem]:
        """List my groups. GET /v1/partner/groups

        The partner's groups across programs, with their onboarding and payout terms.

        **Auth:** a partner session.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/partner/groups", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_partner_groups_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[GetPartnerGroupsResponseDataItem]:
        """Every item of ``get_partner_groups``, following the pages."""
        return self._paginate(lambda cursor: self.get_partner_groups(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_partner_invitations(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetPartnerInvitationsResponseDataItem]:
        """List my invitations. GET /v1/partner/invitations

        Program invitations merchants sent the partner.

        **Auth:** a partner session.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/partner/invitations", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_partner_invitations_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[GetPartnerInvitationsResponseDataItem]:
        """Every item of ``get_partner_invitations``, following the pages."""
        return self._paginate(lambda cursor: self.get_partner_invitations(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_partner_kyc_status(self, *, idempotency_key: Optional[str] = None) -> GetPartnerKycStatusResponse:
        """Get my identity verification status. GET /v1/partner/kyc/status

        The partner account's KYC status (`unverified`, `pending`, `verified`, `rejected`), sanctions screening status and when it was verified.

        **Auth:** a partner session.
        """
        return self._request("GET", f"/v1/partner/kyc/status", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_partner_links(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetPartnerLinksResponseDataItem]:
        """List my links. GET /v1/partner/links

        The partner's tracked links across merchants, newest first, with the short URL, the `?via=` parameter for direct links and eligible clicks.

        **Auth:** a partner session.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/partner/links", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_partner_links_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[GetPartnerLinksResponseDataItem]:
        """Every item of ``get_partner_links``, following the pages."""
        return self._paginate(lambda cursor: self.get_partner_links(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_partner_links_id_qr(self, id: str, *, idempotency_key: Optional[str] = None) -> str:
        """Get my link's QR code. GET /v1/partner/links/{id}/qr

        An SVG QR code for one of the partner's links.

        **Auth:** a partner session.
        """
        return self._request("GET", f"/v1/partner/links/{_seg(id)}/qr", query={}, body=None, idempotency_key=idempotency_key, kind="text")

    def get_partner_marketplace(self, *, category: Optional[str] = None, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetPartnerMarketplaceResponseDataItem]:
        """Browse the marketplace. GET /v1/partner/marketplace

        Public listings of active live programs across every merchant, sponsored first, with commission terms and platform-computed stats. Filter with `category`. Partner session only.

        **Auth:** a partner session.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/partner/marketplace", query={"category": category, "limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_partner_marketplace_iter(self, *, category: Optional[str] = None, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[GetPartnerMarketplaceResponseDataItem]:
        """Every item of ``get_partner_marketplace``, following the pages."""
        return self._paginate(lambda cursor: self.get_partner_marketplace(category=category, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_partner_me(self, *, idempotency_key: Optional[str] = None) -> GetPartnerMeResponse:
        """Get my account and memberships. GET /v1/partner/me

        The partner account and every merchant it partners with, each with its programs and enrollment status.

        **Auth:** a partner session.
        """
        return self._request("GET", f"/v1/partner/me", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_partner_notifications(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[Notification]:
        """List my notifications. GET /v1/partner/notifications

        The partner account's notifications, newest first.

        **Auth:** a partner session.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/partner/notifications", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_partner_notifications_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[Notification]:
        """Every item of ``get_partner_notifications``, following the pages."""
        return self._paginate(lambda cursor: self.get_partner_notifications(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_partner_orgs_org_id_self_billing(self, org_id: str, *, idempotency_key: Optional[str] = None) -> GetPartnerOrgsOrgIdSelfBillingResponse:
        """Get self-billing status. GET /v1/partner/orgs/{orgId}/self-billing

        The partner's VAT details with this merchant and whether they accepted the current self-billing agreement (`currentVersion`).

        **Auth:** a partner session.
        """
        return self._request("GET", f"/v1/partner/orgs/{_seg(org_id)}/self-billing", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_partner_passport(self, *, idempotency_key: Optional[str] = None) -> Passport:
        """Get my reputation passport. GET /v1/partner/passport

        A signed, portable passport of the partner's verified performance across every program (programs, eligible clicks, referrals, repeat-payer rate, average quality), valid for 90 days.

        **Auth:** a partner session.
        """
        return self._request("GET", f"/v1/partner/passport", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_partner_payouts(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetPartnerPayoutsResponseDataItem]:
        """List my payouts. GET /v1/partner/payouts

        The partner's payouts across merchants, newest first.

        **Auth:** a partner session.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/partner/payouts", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_partner_payouts_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[GetPartnerPayoutsResponseDataItem]:
        """Every item of ``get_partner_payouts``, following the pages."""
        return self._paginate(lambda cursor: self.get_partner_payouts(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_partner_payouts_id_invoice(self, id: str, *, format_: Optional[Literal["json", "html"]] = None, idempotency_key: Optional[str] = None) -> Invoice:
        """Get my payout invoice. GET /v1/partner/payouts/{id}/invoice

        The invoice for one of the partner's payouts, as JSON or (`format=html`) a printable page.

        **Auth:** a partner session.
        """
        return self._request("GET", f"/v1/partner/payouts/{_seg(id)}/invoice", query={"format": format_}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_partner_postback_logs(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetPartnerPostbackLogsResponseDataItem]:
        """List my postback calls. GET /v1/partner/postback-logs

        Recent postback calls with the topic, URL and the status code the partner's server answered.

        **Auth:** a partner session.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/partner/postback-logs", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_partner_postback_logs_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[GetPartnerPostbackLogsResponseDataItem]:
        """Every item of ``get_partner_postback_logs``, following the pages."""
        return self._paginate(lambda cursor: self.get_partner_postback_logs(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_partner_profile(self, *, idempotency_key: Optional[str] = None) -> CreatorProfile:
        """Get my creator profile. GET /v1/partner/profile

        The partner's creator profile (headline, bio, channels, audience, engagement) and verified stats.

        **Auth:** a partner session.
        """
        return self._request("GET", f"/v1/partner/profile", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_partner_profile_verified(self, *, idempotency_key: Optional[str] = None) -> GetPartnerProfileVerifiedResponse:
        """Get my verified performance. GET /v1/partner/profile/verified

        The partner's performance across all programs, computed by the platform from the ledger rather than self-reported: programs, eligible clicks, active referrals and repeat-payer rate.

        **Auth:** a partner session.
        """
        return self._request("GET", f"/v1/partner/profile/verified", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_partner_programs_program_id_leaderboard(self, program_id: str, *, idempotency_key: Optional[str] = None) -> GetPartnerProgramsProgramIdLeaderboardResponse:
        """Get a program leaderboard. GET /v1/partner/programs/{programId}/leaderboard

        Top 25 partners by approved commission in the program (during the active contest, if any). Other partners' names are masked; the partner's own row is marked `you`. 403 when the program has no leaderboard.

        **Auth:** a partner session.
        """
        return self._request("GET", f"/v1/partner/programs/{_seg(program_id)}/leaderboard", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_partner_recruit(self, *, idempotency_key: Optional[str] = None) -> GetPartnerRecruitResponse:
        """Get my recruiting link. GET /v1/partner/recruit

        The partner's recruit code and sign-up URL. Partners who sign up through it become their sub-affiliates where both partner the same merchant.

        **Auth:** a partner session.
        """
        return self._request("GET", f"/v1/partner/recruit", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_partner_referrals(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetPartnerReferralsResponseDataItem]:
        """List my referrals. GET /v1/partner/referrals

        The partner's referrals across merchants, newest first. Customer ids are redacted to their last 4 characters.

        **Auth:** a partner session.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/partner/referrals", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_partner_referrals_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[GetPartnerReferralsResponseDataItem]:
        """Every item of ``get_partner_referrals``, following the pages."""
        return self._paginate(lambda cursor: self.get_partner_referrals(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_partner_referrals_id_transparency(self, id: str, *, idempotency_key: Optional[str] = None) -> GetPartnerReferralsIdTransparencyResponse:
        """Explain a referral. GET /v1/partner/referrals/{id}/transparency

        Why a referral credited the partner (or did not fully): the model, window, touchpoints considered, the partner's share of the credit and the reasoning notes. No customer data.

        **Auth:** a partner session.
        """
        return self._request("GET", f"/v1/partner/referrals/{_seg(id)}/transparency", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_partners(self, *, email: Optional[str] = None, external_ref: Optional[str] = None, status: Optional[Literal["active", "suspended", "banned", "archived"]] = None, include_archived: Optional[Literal["true", "false"]] = None, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[Partner]:
        """List partners. GET /v1/partners

        Partners, newest first. Filter by `email`, `externalRef` or `status`. Archived partners are hidden unless you ask for them with `status=archived` or `includeArchived=true`.

        **Auth:** an API key with `partners:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/partners", query={"email": email, "externalRef": external_ref, "status": status, "includeArchived": include_archived, "limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_partners_iter(self, *, email: Optional[str] = None, external_ref: Optional[str] = None, status: Optional[Literal["active", "suspended", "banned", "archived"]] = None, include_archived: Optional[Literal["true", "false"]] = None, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[Partner]:
        """Every item of ``get_partners``, following the pages."""
        return self._paginate(lambda cursor: self.get_partners(email=email, external_ref=external_ref, status=status, include_archived=include_archived, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_partner_security(self, *, idempotency_key: Optional[str] = None) -> GetPartnerSecurityResponse:
        """Get my security settings. GET /v1/partner/security

        Whether two-factor sign-in is on for the partner account.

        **Auth:** a partner session.
        """
        return self._request("GET", f"/v1/partner/security", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_partners_id(self, id: str, *, idempotency_key: Optional[str] = None) -> GetPartnersIdResponse:
        """Get a partner. GET /v1/partners/{id}

        One partner, with a cross-network warning when the same account is flagged or banned by other merchants (it never says which).

        **Auth:** an API key with `partners:read` (or `full`), or a session of any role.
        """
        return self._request("GET", f"/v1/partners/{_seg(id)}", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_partners_id_balances(self, id: str, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[Balance]:
        """Get a partner's balances. GET /v1/partners/{id}/balances

        The partner's commission balances per currency: pending (in hold), approved (payable), paid and reversed.

        **Auth:** an API key with `commissions:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/partners/{_seg(id)}/balances", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_partners_id_balances_iter(self, id: str, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[Balance]:
        """Every item of ``get_partners_id_balances``, following the pages."""
        return self._paginate(lambda cursor: self.get_partners_id_balances(id, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_partners_id_enrollments(self, id: str, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetPartnersIdEnrollmentsResponseDataItem]:
        """List a partner's enrollments. GET /v1/partners/{id}/enrollments

        The programs a partner is enrolled in or applied to, with status and group.

        **Auth:** an API key with `partners:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/partners/{_seg(id)}/enrollments", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_partners_id_enrollments_iter(self, id: str, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[GetPartnersIdEnrollmentsResponseDataItem]:
        """Every item of ``get_partners_id_enrollments``, following the pages."""
        return self._paginate(lambda cursor: self.get_partners_id_enrollments(id, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_partners_id_payout_profile(self, id: str, *, idempotency_key: Optional[str] = None) -> PayoutProfile:
        """Get a partner's payout profile. GET /v1/partners/{id}/payout-profile

        The partner's payout method, currency, threshold and tax form status. Method details are not returned. 404 when none is set.

        **Auth:** an API key with `payouts:read` (or `full`), or a session of any role.
        """
        return self._request("GET", f"/v1/partners/{_seg(id)}/payout-profile", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_partners_id_quality(self, id: str, *, idempotency_key: Optional[str] = None) -> GetPartnersIdQualityResponse:
        """Get a partner's quality score. GET /v1/partners/{id}/quality

        The partner's quality score computed now (with its metrics) and the last stored snapshot.

        **Auth:** an API key with `partners:read` (or `full`), or a session of any role.
        """
        return self._request("GET", f"/v1/partners/{_seg(id)}/quality", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_partner_stats(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetPartnerStatsResponseDataItem]:
        """Get my stats. GET /v1/partner/stats

        Per merchant: eligible clicks, active referrals, payments and commission balances.

        **Auth:** a partner session.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/partner/stats", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_partner_stats_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[GetPartnerStatsResponseDataItem]:
        """Every item of ``get_partner_stats``, following the pages."""
        return self._paginate(lambda cursor: self.get_partner_stats(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_partner_tax_documents(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetPartnerTaxDocumentsResponseDataItem]:
        """List my tax documents. GET /v1/partner/tax-documents

        Tax forms delivered to the partner by every merchant they work with, newest year first.

        **Auth:** a partner session.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/partner/tax-documents", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_partner_tax_documents_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[GetPartnerTaxDocumentsResponseDataItem]:
        """Every item of ``get_partner_tax_documents``, following the pages."""
        return self._paginate(lambda cursor: self.get_partner_tax_documents(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_partner_tax_documents_id(self, id: str, *, idempotency_key: Optional[str] = None) -> str:
        """Get my tax document. GET /v1/partner/tax-documents/{id}

        The recipient copy of a delivered tax form, as an HTML page.

        **Auth:** a partner session.
        """
        return self._request("GET", f"/v1/partner/tax-documents/{_seg(id)}", query={}, body=None, idempotency_key=idempotency_key, kind="text")

    def get_partner_terms(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetPartnerTermsResponseDataItem]:
        """List program terms. GET /v1/partner/terms

        The latest terms version of each program the partner is approved in, and whether they accepted it.

        **Auth:** a partner session.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/partner/terms", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_partner_terms_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[GetPartnerTermsResponseDataItem]:
        """Every item of ``get_partner_terms``, following the pages."""
        return self._paginate(lambda cursor: self.get_partner_terms(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_passport_public_key(self, *, idempotency_key: Optional[str] = None) -> GetPassportPublicKeyResponse:
        """Get the passport signing key. GET /v1/passport/public-key

        The ed25519 public key partner passports are signed with, so anyone can verify one offline.

        **Auth:** none.
        """
        return self._request("GET", f"/v1/passport/public-key", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_payout_connections(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetPayoutConnectionsResponseDataItem]:
        """List payout provider connections. GET /v1/payout-connections

        The payout providers the org connected with its own credentials (PayPal, Stripe, Circle, Wise, Payoneer, Tremendous), with environment and status. Secrets are never returned.

        **Auth:** an API key with `payouts:read` (or `full`), or a session with role `owner`, `admin`, `finance`.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/payout-connections", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_payout_connections_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[GetPayoutConnectionsResponseDataItem]:
        """Every item of ``get_payout_connections``, following the pages."""
        return self._paginate(lambda cursor: self.get_payout_connections(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_payout_runs(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[PayoutRun]:
        """List payout runs. GET /v1/payout-runs

        Payout runs, newest first, with their status and summary.

        **Auth:** an API key with `payouts:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/payout-runs", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_payout_runs_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[PayoutRun]:
        """Every item of ``get_payout_runs``, following the pages."""
        return self._paginate(lambda cursor: self.get_payout_runs(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_payouts(self, *, partner_id: Optional[str] = None, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[Payout]:
        """List payouts. GET /v1/payouts

        Individual payouts, newest first, with rail, provider reference and failure reason. Filter with `partnerId`.

        **Auth:** an API key with `payouts:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/payouts", query={"partnerId": partner_id, "limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_payouts_iter(self, *, partner_id: Optional[str] = None, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[Payout]:
        """Every item of ``get_payouts``, following the pages."""
        return self._paginate(lambda cursor: self.get_payouts(partner_id=partner_id, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_payouts_id_invoice(self, id: str, *, format_: Optional[Literal["json", "html"]] = None, idempotency_key: Optional[str] = None) -> Invoice:
        """Get a payout's invoice. GET /v1/payouts/{id}/invoice

        The self-billing invoice issued for a payout, as JSON or (`format=html`) a printable page. 404 when the payout has no invoice.

        **Auth:** an API key with `payouts:read` (or `full`), or a session of any role.
        """
        return self._request("GET", f"/v1/payouts/{_seg(id)}/invoice", query={"format": format_}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_privacy_export(self, *, customer_ref: str, idempotency_key: Optional[str] = None) -> CustomerExport:
        """Export a customer's data. GET /v1/privacy/export

        Every stored row that references the customer, for a data-subject access request.

        **Auth:** an API key with `privacy:read` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("GET", f"/v1/privacy/export", query={"customerRef": customer_ref}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_privacy_requests(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[PrivacyRequest]:
        """List data-subject requests. GET /v1/privacy/requests

        Access and erasure requests, newest first, with their status.

        **Auth:** an API key with `privacy:read` (or `full`), or a session with role `owner`, `admin`.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/privacy/requests", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_privacy_requests_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[PrivacyRequest]:
        """Every item of ``get_privacy_requests``, following the pages."""
        return self._paginate(lambda cursor: self.get_privacy_requests(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_privacy_requests_id(self, id: str, *, idempotency_key: Optional[str] = None) -> PrivacyRequest:
        """Get a data-subject request. GET /v1/privacy/requests/{id}

        Poll one request: `pending`, `completed` or `failed`, and whether data was found.

        **Auth:** an API key with `privacy:read` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("GET", f"/v1/privacy/requests/{_seg(id)}", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_privacy_requests_id_result(self, id: str, *, idempotency_key: Optional[str] = None) -> GetPrivacyRequestsIdResultResponse:
        """Get a data-subject request result. GET /v1/privacy/requests/{id}/result

        The full result of a completed request; for access requests, the exported data. 400 until it is completed.

        **Auth:** an API key with `privacy:read` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("GET", f"/v1/privacy/requests/{_seg(id)}/result", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_profitability_products(self, *, idempotency_key: Optional[str] = None) -> GetProfitabilityProductsResponse:
        """List product margins. GET /v1/profitability/products

        The margin catalog: per product, a margin (bps) or a unit cost, used to turn revenue into profit.

        **Auth:** an API key with `analytics:read` (or `full`), or a session of any role.
        """
        return self._request("GET", f"/v1/profitability/products", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_profitability_products_product_ref(self, product_ref: str, *, idempotency_key: Optional[str] = None) -> GetProfitabilityProductsProductRefResponse:
        """Get a product margin. GET /v1/profitability/products/{productRef}

        One product of the margin catalog.

        **Auth:** an API key with `analytics:read` (or `full`), or a session of any role.
        """
        return self._request("GET", f"/v1/profitability/products/{_seg(product_ref)}", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_profitability_rebuild_job_id(self, job_id: str, *, idempotency_key: Optional[str] = None) -> GetProfitabilityRebuildJobIdResponse:
        """Get a rebuild job. GET /v1/profitability/rebuild/{jobId}

        Progress of a rebuild: `queued`, `running`, `done` or `failed` (a job untouched for an hour reports `failed` with `error: "stale"`), with processed and total counts.

        **Auth:** an API key with `analytics:read` (or `full`), or a session of any role.
        """
        return self._request("GET", f"/v1/profitability/rebuild/{_seg(job_id)}", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_profitability_settings(self, *, program_id: Optional[str] = None, idempotency_key: Optional[str] = None) -> GetProfitabilitySettingsResponse:
        """Get profitability settings. GET /v1/profitability/settings

        The economics credit ROI is computed with: reporting currency, default margin, how a credit's cost is modelled, how credit use is inferred, attribution and churn windows, target ROI and more. With `programId`, the program's overrides merged over the org's.

        **Auth:** an API key with `analytics:read` (or `full`), or a session of any role.
        """
        return self._request("GET", f"/v1/profitability/settings", query={"programId": program_id}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_programs(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[Program]:
        """List programs. GET /v1/programs

        The org's programs, oldest first, with their settings.

        **Auth:** an API key with `programs:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/programs", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_programs_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[Program]:
        """Every item of ``get_programs``, following the pages."""
        return self._paginate(lambda cursor: self.get_programs(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_programs_id(self, id: str, *, idempotency_key: Optional[str] = None) -> Program:
        """Get a program. GET /v1/programs/{id}

        One program with its settings (defaults filled in) and public page.

        **Auth:** an API key with `programs:read` (or `full`), or a session of any role.
        """
        return self._request("GET", f"/v1/programs/{_seg(id)}", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_programs_id_autopricing(self, id: str, *, idempotency_key: Optional[str] = None) -> GetProgramsIdAutopricingResponse:
        """Get autopricing settings. GET /v1/programs/{id}/autopricing

        The program's autopricing configuration, or `null` when it's off.

        **Auth:** an API key with `programs:read` (or `full`), or a session of any role.
        """
        return self._request("GET", f"/v1/programs/{_seg(id)}/autopricing", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_programs_id_enrollments(self, id: str, *, status: Optional[Literal["applied", "approved", "rejected", "removed"]] = None, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetProgramsIdEnrollmentsResponseDataItem]:
        """List program enrollments. GET /v1/programs/{id}/enrollments

        The program's enrollments and applications, newest first, each with the partner and a cross-network warning when other merchants banned the same account. Filter with `status`.

        **Auth:** an API key with `programs:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/programs/{_seg(id)}/enrollments", query={"status": status, "limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_programs_id_enrollments_iter(self, id: str, *, status: Optional[Literal["applied", "approved", "rejected", "removed"]] = None, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[GetProgramsIdEnrollmentsResponseDataItem]:
        """Every item of ``get_programs_id_enrollments``, following the pages."""
        return self._paginate(lambda cursor: self.get_programs_id_enrollments(id, status=status, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_programs_id_graph(self, id: str, *, root: str, depth: Optional[int] = None, idempotency_key: Optional[str] = None) -> GetProgramsIdGraphResponse:
        """Get the referral tree. GET /v1/programs/{id}/graph

        Who referred whom from one partner (`root`) down, with revenue and net commission per node. Where customers are partners too (customerRef equals a partner's externalRef), the tree continues up to `depth` partner levels. Stops at 5,000 referrals and says so.

        **Auth:** an API key with `programs:read` (or `full`), or a session of any role.
        """
        return self._request("GET", f"/v1/programs/{_seg(id)}/graph", query={"root": root, "depth": depth}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_programs_id_groups(self, id: str, *, include_archived: Optional[Literal["true", "false"]] = None, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[PartnerGroup]:
        """List partner groups. GET /v1/programs/{id}/groups

        The program's partner groups with member counts. Archived groups are hidden unless `includeArchived=true`.

        **Auth:** an API key with `programs:read` (or `full`), or a session of any role.

        includeArchived: true: include archived groups.
        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/programs/{_seg(id)}/groups", query={"includeArchived": include_archived, "limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_programs_id_groups_iter(self, id: str, *, include_archived: Optional[Literal["true", "false"]] = None, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[PartnerGroup]:
        """Every item of ``get_programs_id_groups``, following the pages."""
        return self._paginate(lambda cursor: self.get_programs_id_groups(id, include_archived=include_archived, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_programs_id_negotiation_policy(self, id: str, *, idempotency_key: Optional[str] = None) -> GetProgramsIdNegotiationPolicyResponse:
        """Get the agent negotiation policy. GET /v1/programs/{id}/negotiation-policy

        The program's negotiation policy, or `null` when it isn't open to negotiation.

        **Auth:** an API key with `programs:read` (or `full`), or a session of any role.
        """
        return self._request("GET", f"/v1/programs/{_seg(id)}/negotiation-policy", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_programs_id_promotions(self, id: str, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[Promotion]:
        """List promotions. GET /v1/programs/{id}/promotions

        The program's promotions, latest start first.

        **Auth:** an API key with `programs:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/programs/{_seg(id)}/promotions", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_programs_id_promotions_iter(self, id: str, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[Promotion]:
        """Every item of ``get_programs_id_promotions``, following the pages."""
        return self._paginate(lambda cursor: self.get_programs_id_promotions(id, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_programs_id_referee_reward(self, id: str, *, idempotency_key: Optional[str] = None) -> GetProgramsIdRefereeRewardResponse:
        """Get the referee reward. GET /v1/programs/{id}/referee-reward

        The program's reward for referred customers (the friend's side of a double-sided program), or `null` when it has none.

        **Auth:** an API key with `programs:read` (or `full`), or a session of any role.
        """
        return self._request("GET", f"/v1/programs/{_seg(id)}/referee-reward", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_programs_id_terms_acceptances(self, id: str, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetProgramsIdTermsAcceptancesResponseDataItem]:
        """List terms acceptances. GET /v1/programs/{id}/terms-acceptances

        Which partner accepted which version of the program's terms, newest first.

        **Auth:** an API key with `programs:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/programs/{_seg(id)}/terms-acceptances", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_programs_id_terms_acceptances_iter(self, id: str, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[GetProgramsIdTermsAcceptancesResponseDataItem]:
        """Every item of ``get_programs_id_terms_acceptances``, following the pages."""
        return self._paginate(lambda cursor: self.get_programs_id_terms_acceptances(id, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_prospects(self, *, status: Optional[Literal["identified", "queued", "contacted", "replied", "interested", "declined", "converted"]] = None, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetProspectsResponseDataItem]:
        """List prospects. GET /v1/prospects

        Prospects, best fit first, with channel, audience, evidence and outreach status. Filter with `status`.

        **Auth:** an API key with `growth:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/prospects", query={"status": status, "limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_prospects_iter(self, *, status: Optional[Literal["identified", "queued", "contacted", "replied", "interested", "declined", "converted"]] = None, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[GetProspectsResponseDataItem]:
        """Every item of ``get_prospects``, following the pages."""
        return self._paginate(lambda cursor: self.get_prospects(status=status, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_public_programs_handle(self, handle: str, *, idempotency_key: Optional[str] = None) -> GetPublicProgramsHandleResponse:
        """Get a program's public page. GET /v1/public/programs/{handle}

        What a program's public join page shows: the program and merchant names, pitch, cookie window, terms, base commission, branding and whether joining is approved at once. No authentication; only active live programs with a `publicHandle` are found.

        **Auth:** none.
        """
        return self._request("GET", f"/v1/public/programs/{_seg(handle)}", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_referrals(self, *, program_id: Optional[str] = None, partner_id: Optional[str] = None, status: Optional[Literal["active", "pending_review", "paused", "void"]] = None, customer_ref: Optional[str] = None, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[Referral]:
        """List referrals. GET /v1/referrals

        Referrals, newest first, filtered by `programId`, `partnerId`, `status` or `customerRef`.

        **Auth:** an API key with `referrals:read` (or `full`), or a session of any role.

        customerRef: Your id for the referred customer.
        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/referrals", query={"programId": program_id, "partnerId": partner_id, "status": status, "customerRef": customer_ref, "limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_referrals_iter(self, *, program_id: Optional[str] = None, partner_id: Optional[str] = None, status: Optional[Literal["active", "pending_review", "paused", "void"]] = None, customer_ref: Optional[str] = None, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[Referral]:
        """Every item of ``get_referrals``, following the pages."""
        return self._paginate(lambda cursor: self.get_referrals(program_id=program_id, partner_id=partner_id, status=status, customer_ref=customer_ref, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_referrals_id(self, id: str, *, idempotency_key: Optional[str] = None) -> Referral:
        """Get a referral. GET /v1/referrals/{id}

        One referral with its touch credits and attribution reasoning.

        **Auth:** an API key with `referrals:read` (or `full`), or a session of any role.
        """
        return self._request("GET", f"/v1/referrals/{_seg(id)}", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_referrals_id_journey(self, id: str, *, idempotency_key: Optional[str] = None) -> GetReferralsIdJourneyResponse:
        """Get the attribution journey. GET /v1/referrals/{id}/journey

        The referral with every touchpoint considered: each click's time, URL, fraud score, eligibility, credit weight and which one won.

        **Auth:** an API key with `referrals:read` (or `full`), or a session of any role.
        """
        return self._request("GET", f"/v1/referrals/{_seg(id)}/journey", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_reports_filtered_clicks(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetReportsFilteredClicksResponseDataItem]:
        """Report filtered clicks. GET /v1/reports/filtered-clicks

        Per day, newest first: total clicks, clicks excluded from attribution (bots, rate limits, invalid traffic) and the average fraud score.

        **Auth:** an API key with `analytics:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/reports/filtered-clicks", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_reports_filtered_clicks_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[GetReportsFilteredClicksResponseDataItem]:
        """Every item of ``get_reports_filtered_clicks``, following the pages."""
        return self._paginate(lambda cursor: self.get_reports_filtered_clicks(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_reports_partner_performance(self, *, format_: Optional[Literal["json", "csv"]] = None, idempotency_key: Optional[str] = None) -> GetReportsPartnerPerformanceResponse:
        """Get partner performance. GET /v1/reports/partner-performance

        Per partner, highest revenue first: clicks, referrals, payments, referred revenue, commission earned and reversed. `format=csv` returns the same as a CSV file.

        **Auth:** an API key with `analytics:read` (or `full`), or a session of any role.

        format: csv: the same rows as a CSV file.
        """
        return self._request("GET", f"/v1/reports/partner-performance", query={"format": format_}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_rewards(self, *, status: Optional[Literal["issued", "redeemed", "void"]] = None, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetRewardsResponseDataItem]:
        """List issued referee rewards. GET /v1/rewards

        Rewards issued to referred customers, newest first, with code and status (`issued`, `redeemed`, `void`). Filter with `status`.

        **Auth:** an API key with `commissions:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/rewards", query={"status": status, "limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_rewards_iter(self, *, status: Optional[Literal["issued", "redeemed", "void"]] = None, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[GetRewardsResponseDataItem]:
        """Every item of ``get_rewards``, following the pages."""
        return self._paginate(lambda cursor: self.get_rewards(status=status, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_rewards_lookup_code(self, code: str, *, idempotency_key: Optional[str] = None) -> GetRewardsLookupCodeResponse:
        """Look up a reward code. GET /v1/rewards/lookup/{code}

        Whether a reward code is valid (issued and unredeemed), with its kind and amount, so your checkout can apply it. Unknown codes answer `{ "valid": false }`.

        **Auth:** an API key with `commissions:read` (or `full`), or a session of any role.
        """
        return self._request("GET", f"/v1/rewards/lookup/{_seg(code)}", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_roi_breakdown(self, *, from_: Optional[str] = None, to: Optional[str] = None, program_id: Optional[str] = None, partner_id: Optional[str] = None, window_days: Optional[int] = None, currency: Optional[str] = None, format_: Optional[Literal["json", "csv"]] = None, by: Literal["program", "partner", "cohort", "source", "role"], limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetRoiBreakdownResponseDataItem]:
        """Get the ROI breakdown. GET /v1/roi/breakdown

        The summary figures grouped `by` program, partner, cohort (grant month), source or role, best ROI first (cohorts in date order). Partner and program rows also carry their referrals' combined figures. `from`/`to` select grants by grant date (a date covers its whole UTC day), `programId` and `partnerId` narrow them, `windowDays` overrides each program's attribution window (30, 90, 180, 365, or 0 for lifetime), and `currency` views one native currency instead of the reporting currency. `format=csv` returns the same as a CSV file.

        **Auth:** an API key with `analytics:read` (or `full`), or a session of any role.

        from: Grants (or referrals) from this instant or date, inclusive.
        to: Up to this instant, or through the end of this date (UTC), inclusive.
        partnerId: The grant's partner: the referrer, or the partner of the referee's referral.
        windowDays: Attribution window; default each program's setting. 0 = lifetime.
        currency: Default the reporting currency (converted); another code gives that currency only.
        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/roi/breakdown", query={"from": from_, "to": to, "programId": program_id, "partnerId": partner_id, "windowDays": window_days, "currency": currency, "format": format_, "by": by, "limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_roi_breakdown_iter(self, *, from_: Optional[str] = None, to: Optional[str] = None, program_id: Optional[str] = None, partner_id: Optional[str] = None, window_days: Optional[int] = None, currency: Optional[str] = None, format_: Optional[Literal["json", "csv"]] = None, by: Literal["program", "partner", "cohort", "source", "role"], limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[GetRoiBreakdownResponseDataItem]:
        """Every item of ``get_roi_breakdown``, following the pages."""
        return self._paginate(lambda cursor: self.get_roi_breakdown(from_=from_, to=to, program_id=program_id, partner_id=partner_id, window_days=window_days, currency=currency, format_=format_, by=by, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_roi_data_quality(self, *, from_: Optional[str] = None, to: Optional[str] = None, format_: Optional[Literal["json", "csv"]] = None, idempotency_key: Optional[str] = None) -> GetRoiDataQualityResponse:
        """Get ROI data quality. GET /v1/roi/data-quality

        How complete the inputs to ROI are over `from`/`to`: payments with credit-applied info, products with a margin, partners linked to their own customer id, events excluded for a missing FX rate, and a list of gaps with how to fix each.

        **Auth:** an API key with `analytics:read` (or `full`), or a session of any role.

        from: Grants (or referrals) from this instant or date, inclusive.
        to: Up to this instant, or through the end of this date (UTC), inclusive.
        """
        return self._request("GET", f"/v1/roi/data-quality", query={"from": from_, "to": to, "format": format_}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_roi_grants(self, *, from_: Optional[str] = None, to: Optional[str] = None, program_id: Optional[str] = None, partner_id: Optional[str] = None, window_days: Optional[int] = None, currency: Optional[str] = None, format_: Optional[Literal["json", "csv"]] = None, status: Optional[Literal["open", "used", "expired", "revoked"]] = None, role: Optional[Literal["referee", "referrer"]] = None, paid_back: Optional[Literal["true", "false"]] = None, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[RoiGrant]:
        """List credit grants. GET /v1/roi/grants

        Each credit grant in view with its status (`open`, `used`, `expired`, `revoked`) and figures, newest first. Filter by `status`, `role` (`referee` or `referrer`) and `paidBack`. `from`/`to` select grants by grant date (a date covers its whole UTC day), `programId` and `partnerId` narrow them, `windowDays` overrides each program's attribution window (30, 90, 180, 365, or 0 for lifetime), and `currency` views one native currency instead of the reporting currency. `format=csv` returns the same as a CSV file. CSV returns every grant, unpaged.

        **Auth:** an API key with `analytics:read` (or `full`), or a session of any role.

        from: Grants (or referrals) from this instant or date, inclusive.
        to: Up to this instant, or through the end of this date (UTC), inclusive.
        partnerId: The grant's partner: the referrer, or the partner of the referee's referral.
        windowDays: Attribution window; default each program's setting. 0 = lifetime.
        currency: Default the reporting currency (converted); another code gives that currency only.
        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/roi/grants", query={"from": from_, "to": to, "programId": program_id, "partnerId": partner_id, "windowDays": window_days, "currency": currency, "format": format_, "status": status, "role": role, "paidBack": paid_back, "limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_roi_grants_iter(self, *, from_: Optional[str] = None, to: Optional[str] = None, program_id: Optional[str] = None, partner_id: Optional[str] = None, window_days: Optional[int] = None, currency: Optional[str] = None, format_: Optional[Literal["json", "csv"]] = None, status: Optional[Literal["open", "used", "expired", "revoked"]] = None, role: Optional[Literal["referee", "referrer"]] = None, paid_back: Optional[Literal["true", "false"]] = None, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[RoiGrant]:
        """Every item of ``get_roi_grants``, following the pages."""
        return self._paginate(lambda cursor: self.get_roi_grants(from_=from_, to=to, program_id=program_id, partner_id=partner_id, window_days=window_days, currency=currency, format_=format_, status=status, role=role, paid_back=paid_back, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_roi_partners_id_trace(self, id: str, *, window_days: Optional[int] = None, format_: Optional[Literal["json", "csv"]] = None, idempotency_key: Optional[str] = None) -> RoiTrace:
        """Trace a partner's value. GET /v1/roi/partners/{id}/trace

        The same trace for a partner's own customer identity (through their externalRef).

        **Auth:** an API key with `analytics:read` (or `full`), or a session of any role.

        windowDays: Attribution window; default each program's setting. 0 = lifetime.
        """
        return self._request("GET", f"/v1/roi/partners/{_seg(id)}/trace", query={"windowDays": window_days, "format": format_}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_roi_patterns(self, *, idempotency_key: Optional[str] = None) -> GetRoiPatternsResponse:
        """List value patterns. GET /v1/roi/patterns

        Every value pattern from one detection run, with the matching subjects: `credit_only` (a referee used their credit and paid no cash after within the window), `churn_at_exhaustion` (used it up, paid, then stopped), `bonus_collector` (a partner holding commission credit who never spends their own cash) and `negative_partner` (a partner whose referrals net below zero). Matches wait until the evidence is in, so young customers are never flagged.

        **Auth:** an API key with `analytics:read` (or `full`), or a session of any role.
        """
        return self._request("GET", f"/v1/roi/patterns", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_roi_patterns_pattern(self, pattern: str, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[RoiPatternEntry]:
        """Get a value pattern. GET /v1/roi/patterns/{pattern}

        The subjects currently matching one pattern, with the detail of each match.

        **Auth:** an API key with `analytics:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/roi/patterns/{_seg(pattern)}", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_roi_patterns_pattern_iter(self, pattern: str, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[RoiPatternEntry]:
        """Every item of ``get_roi_patterns_pattern``, following the pages."""
        return self._paginate(lambda cursor: self.get_roi_patterns_pattern(pattern, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_roi_summary(self, *, from_: Optional[str] = None, to: Optional[str] = None, program_id: Optional[str] = None, partner_id: Optional[str] = None, window_days: Optional[int] = None, currency: Optional[str] = None, format_: Optional[Literal["json", "csv"]] = None, model: Optional[Literal["naive", "incremental"]] = None, include_projection: Optional[Literal["true", "false"]] = None, idempotency_key: Optional[str] = None) -> RoiSummary:
        """Get the ROI summary. GET /v1/roi/summary

        Credit ROI for the grants in view: credit cost, cash and profit from the recipients after each grant, net, ROI, payback share and median days, outstanding credit and how much of it is measured rather than inferred. With `programId`, also status against the program's target ROI. `model=incremental` adds the lift against the program's holdout group; `includeProjection=true` adds the expected payback of open grants. `from`/`to` select grants by grant date (a date covers its whole UTC day), `programId` and `partnerId` narrow them, `windowDays` overrides each program's attribution window (30, 90, 180, 365, or 0 for lifetime), and `currency` views one native currency instead of the reporting currency. `format=csv` returns the same as a CSV file.

        **Auth:** an API key with `analytics:read` (or `full`), or a session of any role.

        from: Grants (or referrals) from this instant or date, inclusive.
        to: Up to this instant, or through the end of this date (UTC), inclusive.
        partnerId: The grant's partner: the referrer, or the partner of the referee's referral.
        windowDays: Attribution window; default each program's setting. 0 = lifetime.
        currency: Default the reporting currency (converted); another code gives that currency only.
        model: naive (default): ROI of every grant. incremental: also `incremental`, the program's credit-caused lift against its recorded holdout (requires programId; reporting currency; from/to select referrals by first qualifying payment).
        includeProjection: true: also `projection`, the expected payback of the open grants in view from their program-and-role cohort's median curve (labelled 'projection'; needs 50 closed grants per cohort).
        """
        return self._request("GET", f"/v1/roi/summary", query={"from": from_, "to": to, "programId": program_id, "partnerId": partner_id, "windowDays": window_days, "currency": currency, "format": format_, "model": model, "includeProjection": include_projection}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_roi_trace_customer_ref(self, customer_ref: str, *, window_days: Optional[int] = None, format_: Optional[Literal["json", "csv"]] = None, idempotency_key: Optional[str] = None) -> RoiTrace:
        """Trace a customer's value. GET /v1/roi/trace/{customerRef}

        Every value event of a customer (and the identities linked to them) in order, with the running net, to see exactly how their ROI was computed. `format=csv` for a file.

        **Auth:** an API key with `analytics:read` (or `full`), or a session of any role.

        windowDays: Attribution window; default each program's setting. 0 = lifetime.
        """
        return self._request("GET", f"/v1/roi/trace/{_seg(customer_ref)}", query={"windowDays": window_days, "format": format_}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_setup_status(self, *, idempotency_key: Optional[str] = None) -> GetSetupStatusResponse:
        """Get setup progress. GET /v1/setup/status

        The install checker: which integration steps are done (auth or associate, program and rule, partner, snippet or click, billing, a payable partner, webhooks) and the next steps as hints.

        **Auth:** an API key with `analytics:read` (or `full`), or a session of any role.
        """
        return self._request("GET", f"/v1/setup/status", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_status(self, *, idempotency_key: Optional[str] = None) -> GetStatusResponse:
        """Get platform status. GET /v1/status

        Overall state (`operational`, `degraded` or `major_outage`), each component's health and the open incidents. Cached 30 seconds.

        **Auth:** none.
        """
        return self._request("GET", f"/v1/status", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_status_incidents(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[Incident]:
        """List status incidents. GET /v1/status/incidents

        Recent incidents, newest first, with their updates.

        **Auth:** none.

        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/status/incidents", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_status_incidents_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[Incident]:
        """Every item of ``get_status_incidents``, following the pages."""
        return self._paginate(lambda cursor: self.get_status_incidents(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_status_incidents_atom(self, *, idempotency_key: Optional[str] = None) -> str:
        """Get the incidents feed. GET /v1/status/incidents.atom

        The 50 most recent incidents as an Atom feed.

        **Auth:** none.
        """
        return self._request("GET", f"/v1/status/incidents.atom", query={}, body=None, idempotency_key=idempotency_key, kind="text")

    def get_status_incidents_id(self, id: str, *, idempotency_key: Optional[str] = None) -> Incident:
        """Get a status incident. GET /v1/status/incidents/{id}

        One incident with its updates.

        **Auth:** none.
        """
        return self._request("GET", f"/v1/status/incidents/{_seg(id)}", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_tax1099(self, *, year: int, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetTax1099ResponseDataItem]:
        """Export 1099-NEC data. GET /v1/tax/1099

        For each partner with a W-9 on file: the total actually paid in the tax year, in USD at recorded FX rates, and whether a form is required (US$600 or more, or a currency that couldn't be converted, listed in `fxMissingCurrencies` for review).

        **Auth:** an API key with `payouts:read` (or `full`), or a session with role `owner`, `admin`, `finance`.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/tax/1099", query={"year": year, "limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_tax1099_iter(self, *, year: int, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[GetTax1099ResponseDataItem]:
        """Every item of ``get_tax1099``, following the pages."""
        return self._paginate(lambda cursor: self.get_tax1099(year=year, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_tax1099_filings(self, *, year: int, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetTax1099FilingsResponseDataItem]:
        """List 1099 filings. GET /v1/tax/1099/filings

        A tax year's filings with their provider status and the documents in each.

        **Auth:** an API key with `payouts:read` (or `full`), or a session with role `owner`, `admin`, `finance`.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/tax/1099/filings", query={"year": year, "limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_tax1099_filings_iter(self, *, year: int, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[GetTax1099FilingsResponseDataItem]:
        """Every item of ``get_tax1099_filings``, following the pages."""
        return self._paginate(lambda cursor: self.get_tax1099_filings(year=year, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_tax1099_preview(self, *, year: int, idempotency_key: Optional[str] = None) -> NecPreview:
        """Preview 1099-NEC filings. GET /v1/tax/1099/preview

        Which partners would get a 1099-NEC for a tax year, with amounts and anything missing (W-9s, TINs), without filing.

        **Auth:** an API key with `payouts:read` (or `full`), or a session with role `owner`, `admin`, `finance`.
        """
        return self._request("GET", f"/v1/tax/1099/preview", query={"year": year}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_test_clock(self, *, idempotency_key: Optional[str] = None) -> GetTestClockResponse:
        """Get the test clock. GET /v1/test_clock

        Test mode only (`409 test_mode_only` otherwise). The test org's current time and how far it has been advanced.

        **Auth:** an API key with `org:read` (or `full`), or a session of any role.
        """
        return self._request("GET", f"/v1/test_clock", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_test_emails(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetTestEmailsResponseDataItem]:
        """List captured test emails. GET /v1/test/emails

        Test mode only. Emails the test org would have sent, captured instead of delivered, newest first.

        **Auth:** an API key with `org:read` (or `full`), or a session of any role.

        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/test/emails", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_test_emails_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[GetTestEmailsResponseDataItem]:
        """Every item of ``get_test_emails``, following the pages."""
        return self._paginate(lambda cursor: self.get_test_emails(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_value_import_job_id(self, job_id: str, *, idempotency_key: Optional[str] = None) -> GetValueImportJobIdResponse:
        """Get a value import job. GET /v1/value/import/{jobId}

        Progress and result of a background import: status, processed and total rows, recorded and duplicate counts and row errors.

        **Auth:** an API key with `analytics:read` (or `full`), or a session of any role.
        """
        return self._request("GET", f"/v1/value/import/{_seg(job_id)}", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_versions(self, *, idempotency_key: Optional[str] = None) -> GetVersionsResponse:
        """List API versions. GET /v1/versions

        Every API version, newest first, with what changed in it, the latest version and the deprecation policy. Pin a version with the `Referalli-Version` header or on the API key.

        **Auth:** none.
        """
        return self._request("GET", f"/v1/versions", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_webhook_deliveries(self, *, endpoint_id: Optional[str] = None, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[WebhookDelivery]:
        """List webhook deliveries. GET /v1/webhook-deliveries

        Deliveries to every endpoint, newest first: topic, status (`pending`, `delivered`, `failed`), attempts, the last response code and, while pending, when the next attempt is. Filter with `endpointId`.

        **Auth:** an API key with `webhooks:read` (or `full`), or a session of any role.

        endpointId: Only deliveries to this endpoint.
        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/webhook-deliveries", query={"endpointId": endpoint_id, "limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_webhook_deliveries_iter(self, *, endpoint_id: Optional[str] = None, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[WebhookDelivery]:
        """Every item of ``get_webhook_deliveries``, following the pages."""
        return self._paginate(lambda cursor: self.get_webhook_deliveries(endpoint_id=endpoint_id, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_webhook_deliveries_id(self, id: str, *, idempotency_key: Optional[str] = None) -> GetWebhookDeliveriesIdResponse:
        """Get a webhook delivery. GET /v1/webhook-deliveries/{id}

        One delivery in full: the exact `payload` sent, its `eventId`, and what the endpoint answered last (`lastStatusCode`, the first 2,000 characters of `lastResponseBody`, or `lastError` when there was no response).

        **Auth:** an API key with `webhooks:read` (or `full`), or a session of any role.
        """
        return self._request("GET", f"/v1/webhook-deliveries/{_seg(id)}", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_webhook_endpoints(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[WebhookEndpoint]:
        """List webhook endpoints. GET /v1/webhook-endpoints

        Endpoints with their topics, programs, status (`active`, `paused`, `disabled`), secret-rotation state and failure state. Secrets are never returned.

        **Auth:** an API key with `webhooks:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/webhook-endpoints", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_webhook_endpoints_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[WebhookEndpoint]:
        """Every item of ``get_webhook_endpoints``, following the pages."""
        return self._paginate(lambda cursor: self.get_webhook_endpoints(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_webhook_endpoints_id(self, id: str, *, idempotency_key: Optional[str] = None) -> WebhookEndpoint:
        """Get a webhook endpoint. GET /v1/webhook-endpoints/{id}

        One endpoint with its status, rotation and failure state.

        **Auth:** an API key with `webhooks:read` (or `full`), or a session of any role.
        """
        return self._request("GET", f"/v1/webhook-endpoints/{_seg(id)}", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_webhook_endpoints_id_deliveries(self, id: str, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[WebhookDelivery]:
        """List an endpoint's deliveries. GET /v1/webhook-endpoints/{id}/deliveries

        What one endpoint was sent, newest first.

        **Auth:** an API key with `webhooks:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/webhook-endpoints/{_seg(id)}/deliveries", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_webhook_endpoints_id_deliveries_iter(self, id: str, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[WebhookDelivery]:
        """Every item of ``get_webhook_endpoints_id_deliveries``, following the pages."""
        return self._paginate(lambda cursor: self.get_webhook_endpoints_id_deliveries(id, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_zapier_events(self, *, idempotency_key: Optional[str] = None) -> GetZapierEventsResponse:
        """List Zapier trigger events. GET /v1/zapier/events

        The event keys Zapier triggers can subscribe to.

        **Auth:** an API key with `integrations:read` (or `full`), or a session of any role.
        """
        return self._request("GET", f"/v1/zapier/events", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def get_zapier_hooks(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[ZapierHook]:
        """List Zapier hooks. GET /v1/zapier/hooks

        Active Zapier REST hook subscriptions, newest first.

        **Auth:** an API key with `integrations:read` (or `full`), or a session with role `owner`, `admin`.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return self._request("GET", f"/v1/zapier/hooks", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_zapier_hooks_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Iterator[ZapierHook]:
        """Every item of ``get_zapier_hooks``, following the pages."""
        return self._paginate(lambda cursor: self.get_zapier_hooks(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    def get_zapier_triggers_event(self, event: str, *, limit: Optional[int] = None, idempotency_key: Optional[str] = None) -> GetZapierTriggersEventResponse:
        """Poll a Zapier trigger. GET /v1/zapier/triggers/{event}

        Zapier polling and sample data: the latest `limit` events of that kind, newest first, in the shape the hook delivers. Always a plain array (Zapier's contract), whatever the API version.

        **Auth:** an API key with `integrations:read` (or `full`), or a session of any role.
        """
        return self._request("GET", f"/v1/zapier/triggers/{_seg(event)}", query={"limit": limit}, body=None, idempotency_key=idempotency_key, kind="json")

    def patch_admin_status_incidents_id(self, id: str, body: PatchAdminStatusIncidentsIdBody, *, idempotency_key: Optional[str] = None) -> Incident:
        """Edit a status incident. PATCH /v1/admin/status/incidents/{id}

        Platform admins only. Changes an incident's title, severity, state, body or affected components. Setting `state: "resolved"` stamps `resolvedAt`.

        **Auth:** a platform admin session.
        """
        return self._request("PATCH", f"/v1/admin/status/incidents/{_seg(id)}", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def patch_api_keys_id(self, id: str, body: PatchApiKeysIdBody, *, idempotency_key: Optional[str] = None) -> PatchApiKeysIdResponse:
        """Update an API key. PATCH /v1/api-keys/{id}

        Changes a key's pinned `apiVersion`, `owner` or expiry (`expiresInDays` from now; `null` removes it). Revoked keys are 404. Needs an owner or admin session, or an API key with the `admin` scope. Audited.

        **Auth:** an API key with `team:write` (or `full`), or a session of any role.
        """
        return self._request("PATCH", f"/v1/api-keys/{_seg(id)}", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def patch_auth_connections_id(self, id: str, body: PatchAuthConnectionsIdBody, *, idempotency_key: Optional[str] = None) -> PatchAuthConnectionsIdResponse:
        """Update an auth connection. PATCH /v1/auth/connections/{id}

        Pauses or resumes a connection, renames it, changes `autoEnrollUsers` or the destination of auto-created links, or (signed-protocol connections) sets `signatureVersion`: `v2` to require request-line signatures, `v1+v2` to accept both again.

        **Auth:** an API key with `integrations:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("PATCH", f"/v1/auth/connections/{_seg(id)}", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def patch_billing_connections_id(self, id: str, body: PatchBillingConnectionsIdBody, *, idempotency_key: Optional[str] = None) -> BillingConnection:
        """Update a billing connection. PATCH /v1/billing/connections/{id}

        Renames a connection or sets `status`: `paused` makes its webhook URL refuse events until set back to `active`. Audited.

        **Auth:** an API key with `billing:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("PATCH", f"/v1/billing/connections/{_seg(id)}", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def patch_org(self, body: PatchOrgBody, *, idempotency_key: Optional[str] = None) -> PatchOrgResponse:
        """Update the organization. PATCH /v1/org

        Changes the org name, merges keys into `settings` (a free-form map) and turns `payoutKycRequired` on or off. Audited.

        **Auth:** an API key with `org:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("PATCH", f"/v1/org", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def patch_org_members_user_id(self, user_id: str, body: PatchOrgMembersUserIdBody, *, idempotency_key: Optional[str] = None) -> PatchOrgMembersUserIdResponse:
        """Change a member's role. PATCH /v1/org/members/{userId}

        Changes a member's role. Only owners change owner roles, and the last owner can't be demoted (409). Audited. Live mode only.

        **Auth:** an API key with `team:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("PATCH", f"/v1/org/members/{_seg(user_id)}", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def patch_org_sso(self, body: PatchOrgSsoBody, *, idempotency_key: Optional[str] = None) -> PatchOrgSsoResponse:
        """Update SSO settings. PATCH /v1/org/sso

        Requires SSO for members on the org's SSO domains (`requireSso`; needs an active connection and the owner signed in through SSO, so nobody is locked out) and maps identity-provider roles to Referalli roles. Owner only. Live mode only.

        **Auth:** an API key with `org:write` (or `full`), or a session with role `owner`.
        """
        return self._request("PATCH", f"/v1/org/sso", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def patch_partner_groups_id(self, id: str, body: PatchPartnerGroupsIdBody, *, idempotency_key: Optional[str] = None) -> PartnerGroup:
        """Update a partner group. PATCH /v1/partner-groups/{id}

        Changes a group's terms, or archives it (`archived: true`); archived groups take no new members.

        **Auth:** an API key with `programs:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("PATCH", f"/v1/partner-groups/{_seg(id)}", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def patch_partners_id(self, id: str, body: PatchPartnersIdBody, *, idempotency_key: Optional[str] = None) -> Partner:
        """Update a partner. PATCH /v1/partners/{id}

        Changes the display name, status (`active`, `suspended`, `banned`, `archived`), tags, notes or externalRef (`null` clears it). Suspended partners keep earning but are not paid; banned ones stop attributing. 409 when another partner has the externalRef. Audited.

        **Auth:** an API key with `partners:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("PATCH", f"/v1/partners/{_seg(id)}", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def patch_partners_id_payout_profile(self, id: str, body: PatchPartnersIdPayoutProfileBody, *, idempotency_key: Optional[str] = None) -> PatchPartnersIdPayoutProfileResponse:
        """Change a partner's payout threshold. PATCH /v1/partners/{id}/payout-profile

        Changes only the minimum balance before a payout (`minThresholdMinor`). 404 when the partner has no profile. Audited.

        **Auth:** an API key with `payouts:write` (or `full`), or a session with role `owner`, `admin`, `finance`.
        """
        return self._request("PATCH", f"/v1/partners/{_seg(id)}/payout-profile", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def patch_programs_id(self, id: str, body: PatchProgramsIdBody, *, idempotency_key: Optional[str] = None) -> Program:
        """Update a program. PATCH /v1/programs/{id}

        Changes any program field or setting; omitted fields keep their value, and `publicPage` is merged. Changing `termsMd` records a new terms version. Setting `status` to `paused` or `archived` stops new attribution. `mobileApp` (iOS Team ID and bundle id, Android package and signing-certificate fingerprints) publishes the program's apps in the universal-links and App Links files on the org's link hosts. Audited.

        **Auth:** an API key with `programs:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("PATCH", f"/v1/programs/{_seg(id)}", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def patch_referrals_id(self, id: str, body: PatchReferralsIdBody, *, idempotency_key: Optional[str] = None) -> Referral:
        """Pause or resume a referral. PATCH /v1/referrals/{id}

        Sets `status` to `paused` (no new commissions) or back to `active`. Only active referrals can be paused and only paused ones resumed (409 otherwise); setting the current status is a no-op. Publishes `referral.paused` or `referral.resumed`. Audited.

        **Auth:** an API key with `referrals:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("PATCH", f"/v1/referrals/{_seg(id)}", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def patch_webhook_endpoints_id(self, id: str, body: PatchWebhookEndpointsIdBody, *, idempotency_key: Optional[str] = None) -> WebhookEndpoint:
        """Update a webhook endpoint. PATCH /v1/webhook-endpoints/{id}

        Changes the URL, topics, programs (`null` or `[]` for every program) or legacy signature, or pauses it (`status: "paused"`, deliveries held). Setting `active` re-enables a paused or auto-disabled endpoint: held deliveries resume and the failure clock starts over. Audited.

        **Auth:** an API key with `webhooks:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("PATCH", f"/v1/webhook-endpoints/{_seg(id)}", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_admin_orgs_id_plan(self, id: str, body: PostAdminOrgsIdPlanBody, *, idempotency_key: Optional[str] = None) -> PostAdminOrgsIdPlanResponse:
        """Set an organization's plan. POST /v1/admin/orgs/{id}/plan

        Platform admins only. Moves an org to a plan without checkout.

        **Auth:** a platform admin session.
        """
        return self._request("POST", f"/v1/admin/orgs/{_seg(id)}/plan", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_admin_orgs_id_suspend(self, id: str, body: PostAdminOrgsIdSuspendBody, *, idempotency_key: Optional[str] = None) -> PostAdminOrgsIdSuspendResponse:
        """Suspend an organization. POST /v1/admin/orgs/{id}/suspend

        Platform admins only. Suspends an org with a reason; its members and keys get 403 until it's unsuspended.

        **Auth:** a platform admin session.
        """
        return self._request("POST", f"/v1/admin/orgs/{_seg(id)}/suspend", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_admin_orgs_id_unsuspend(self, id: str, *, idempotency_key: Optional[str] = None) -> PostAdminOrgsIdUnsuspendResponse:
        """Unsuspend an organization. POST /v1/admin/orgs/{id}/unsuspend

        Platform admins only. Lifts a suspension.

        **Auth:** a platform admin session.
        """
        return self._request("POST", f"/v1/admin/orgs/{_seg(id)}/unsuspend", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def post_admin_partner_accounts_id_ban(self, id: str, *, idempotency_key: Optional[str] = None) -> PostAdminPartnerAccountsIdBanResponse:
        """Ban a partner account. POST /v1/admin/partner-accounts/{id}/ban

        Platform admins only. Bans a partner account across the platform and signs it out everywhere.

        **Auth:** a platform admin session.
        """
        return self._request("POST", f"/v1/admin/partner-accounts/{_seg(id)}/ban", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def post_admin_partner_accounts_id_unban(self, id: str, *, idempotency_key: Optional[str] = None) -> PostAdminPartnerAccountsIdUnbanResponse:
        """Unban a partner account. POST /v1/admin/partner-accounts/{id}/unban

        Platform admins only. Lifts a platform ban.

        **Auth:** a platform admin session.
        """
        return self._request("POST", f"/v1/admin/partner-accounts/{_seg(id)}/unban", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def post_admin_status_incidents(self, body: PostAdminStatusIncidentsBody, *, idempotency_key: Optional[str] = None) -> Incident:
        """Open a status incident. POST /v1/admin/status/incidents

        Platform admins only. Opens an incident on the status page (and mirrors it to the hosted status space when configured).

        **Auth:** a platform admin session.
        """
        return self._request("POST", f"/v1/admin/status/incidents", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_admin_status_incidents_id_updates(self, id: str, body: PostAdminStatusIncidentsIdUpdatesBody, *, idempotency_key: Optional[str] = None) -> Incident:
        """Post an incident update. POST /v1/admin/status/incidents/{id}/updates

        Platform admins only. Adds a timestamped update to an incident and moves it to the given state.

        **Auth:** a platform admin session.
        """
        return self._request("POST", f"/v1/admin/status/incidents/{_seg(id)}/updates", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_agents_register(self, body: PostAgentsRegisterBody, *, idempotency_key: Optional[str] = None) -> PostAgentsRegisterResponse:
        """Register an AI agent. POST /v1/agents/register

        Registers (or updates) an AI agent identity, proven by a wallet signature over a nonce from `POST /v1/partner/auth/wallet/nonce`. The nonce is single use and valid for 10 minutes. `instantPayout` pays the agent per outcome on the crypto rail. No API key: the signature is the credential.

        **Auth:** none.
        """
        return self._request("POST", f"/v1/agents/register", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_anomalies_scan(self, *, idempotency_key: Optional[str] = None) -> PostAnomaliesScanResponse:
        """Scan for anomalies. POST /v1/anomalies/scan

        Compares the last 24 hours of clicks, sign-ups and revenue with the trailing 7-day average and returns this org's spikes (3x or more) and drops (under 20%). Findings also become notifications; nothing is changed automatically. Also runs hourly.

        **Auth:** an API key with `analytics:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/anomalies/scan", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def post_api_keys(self, body: PostApiKeysBody, *, idempotency_key: Optional[str] = None) -> PostApiKeysResponse:
        """Create an API key. POST /v1/api-keys

        Mints a secret key (`rk_live_…` / `rk_test_…`), shown only in this response. `scopes` defaults to `full`; a key can't grant scopes it doesn't hold. `mode` picks live, test or a matching pair of both (`both` returns `{ pairId, live, test }`); a test-mode caller can mint test keys only. `publishable: true` mints a browser-safe `rk_pub_` key limited to `programs:read` and `events:write` from `allowedOrigins`. `apiVersion` pins the key (default: latest). Needs an owner or admin session, or an API key with the `admin` scope. Audited.

        **Auth:** an API key with `team:write` (or `full`), or a session of any role.
        """
        return self._request("POST", f"/v1/api-keys", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_assets(self, body: PostAssetsBody, *, idempotency_key: Optional[str] = None) -> PostAssetsResponse:
        """Create a marketing asset. POST /v1/assets

        Adds a marketing asset (`banner`, `copy`, `video` or `logo`) to a program for its approved partners, or only for one group's members with `groupId`.

        **Auth:** an API key with `partners:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/assets", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_attribution_replay(self, body: PostAttributionReplayBody, *, idempotency_key: Optional[str] = None) -> PostAttributionReplayResponse:
        """Replay attribution. POST /v1/attribution/replay

        Deterministically recomputes attribution for a program's referrals from the recorded clicks and identity links, under its current model. Returns what changed. Audited.

        **Auth:** an API key with `referrals:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/attribution/replay", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_auth_connections(self, body: PostAuthConnectionsBody, *, idempotency_key: Optional[str] = None) -> CreatedAuthConnection:
        """Connect an auth platform. POST /v1/auth/connections

        Connects your sign-up system so new users are attributed server-side without calling associate: `clerk`, `supabase`, `workos` or `generic` receive the platform's user webhooks at the returned URL; `atlas` and `custom` call the signed protocol endpoints under `/v1/auth/connections/{id}/`. `autoEnrollUsers` makes every new user a partner too. Returns the signing secret once. 409 when an Atlas instance already has a connection.

        **Auth:** an API key with `integrations:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/auth/connections", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_auth_connections_id_aliases(self, id: str, body: PostAuthConnectionsIdAliasesBody, *, idempotency_key: Optional[str] = None) -> PostAuthConnectionsIdAliasesResponse:
        """Change a user's id (signed protocol). POST /v1/auth/connections/{id}/aliases

        The app stamped or changed a user's id after the sign-up was filed: referrals and identity move from `fromCustomerRef` to `toCustomerRef`. Publishes `customer.aliased`. Signed with the connection secret in `x-referalli-signature: t=<unix>,v1=…,v2=…` (v2 also signs the request line; once a connection has seen v2 it requires it), with a unique `x-referalli-id` per call. Calls older than 5 minutes, reused ids (`409 replay`), paused connections (`423 connection_paused`) and unknown fields (`422`) are refused.

        **Auth:** a signature (see above); no API key.
        """
        return self._request("POST", f"/v1/auth/connections/{_seg(id)}/aliases", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_auth_connections_id_erase(self, id: str, body: PostAuthConnectionsIdEraseBody, *, idempotency_key: Optional[str] = None) -> PostAuthConnectionsIdEraseResponse:
        """Erase a user (signed protocol). POST /v1/auth/connections/{id}/erase

        The platform deleted a user or fulfilled an erasure request: the customer's referral data and their partner record are erased. An unknown user succeeds with nothing erased. Signed with the connection secret in `x-referalli-signature: t=<unix>,v1=…,v2=…` (v2 also signs the request line; once a connection has seen v2 it requires it), with a unique `x-referalli-id` per call. Calls older than 5 minutes, reused ids (`409 replay`), paused connections (`423 connection_paused`) and unknown fields (`422`) are refused.

        **Auth:** a signature (see above); no API key.
        """
        return self._request("POST", f"/v1/auth/connections/{_seg(id)}/erase", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_auth_connections_id_ping(self, id: str, body: Dict[str, Any], *, idempotency_key: Optional[str] = None) -> PostAuthConnectionsIdPingResponse:
        """Test an auth connection (signed protocol). POST /v1/auth/connections/{id}/ping

        Proves the secret works: returns the connection, its program and org and the server time, to check clock skew. Signed with the connection secret in `x-referalli-signature: t=<unix>,v1=…,v2=…` (v2 also signs the request line; once a connection has seen v2 it requires it), with a unique `x-referalli-id` per call. Calls older than 5 minutes, reused ids (`409 replay`), paused connections (`423 connection_paused`) and unknown fields (`422`) are refused.

        **Auth:** a signature (see above); no API key.
        """
        return self._request("POST", f"/v1/auth/connections/{_seg(id)}/ping", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_auth_connections_id_revoke_previous_secret(self, id: str, *, idempotency_key: Optional[str] = None) -> PostAuthConnectionsIdRevokePreviousSecretResponse:
        """Revoke the previous auth secret. POST /v1/auth/connections/{id}/revoke-previous-secret

        Ends the rotation overlap at once: only the newest secret verifies from now on.

        **Auth:** an API key with `integrations:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/auth/connections/{_seg(id)}/revoke-previous-secret", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def post_auth_connections_id_rotate_secret(self, id: str, *, idempotency_key: Optional[str] = None) -> PostAuthConnectionsIdRotateSecretResponse:
        """Rotate an auth connection secret. POST /v1/auth/connections/{id}/rotate-secret

        Issues a new signing secret, returned once. The previous one keeps verifying for 24 hours, or until revoked.

        **Auth:** an API key with `integrations:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/auth/connections/{_seg(id)}/rotate-secret", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def post_auth_connections_id_signals(self, id: str, body: PostAuthConnectionsIdSignalsBody, *, idempotency_key: Optional[str] = None) -> PostAuthConnectionsIdSignalsResponse:
        """Report a user signal (signed protocol). POST /v1/auth/connections/{id}/signals

        A later verdict about a user: `email_verified` releases a hold for an unverified email, `fraud_confirmed` or `self_referral` voids their referral, `banned`/`unbanned` follow on their partner record. `details` is kept as evidence. Signed with the connection secret in `x-referalli-signature: t=<unix>,v1=…,v2=…` (v2 also signs the request line; once a connection has seen v2 it requires it), with a unique `x-referalli-id` per call. Calls older than 5 minutes, reused ids (`409 replay`), paused connections (`423 connection_paused`) and unknown fields (`422`) are refused.

        **Auth:** a signature (see above); no API key.
        """
        return self._request("POST", f"/v1/auth/connections/{_seg(id)}/signals", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_auth_connections_id_signups(self, id: str, body: PostAuthConnectionsIdSignupsBody, *, idempotency_key: Optional[str] = None) -> PostAuthConnectionsIdSignupsResponse:
        """Attribute a new user (signed protocol). POST /v1/auth/connections/{id}/signups

        The auth platform reports a new user with the referral context captured at sign-up (`referral.code`, or with cookie consent `clickId`/`anonId`) and optional risk signals. The user is attributed (risky sign-ups are held for review), optionally made a partner with their own link, and the answer says why with reason codes. `test: true` or `atlas-test: 1` simulates without storing. Repeating the same user is idempotent. Signed with the connection secret in `x-referalli-signature: t=<unix>,v1=…,v2=…` (v2 also signs the request line; once a connection has seen v2 it requires it), with a unique `x-referalli-id` per call. Calls older than 5 minutes, reused ids (`409 replay`), paused connections (`423 connection_paused`) and unknown fields (`422`) are refused.

        **Auth:** a signature (see above); no API key.
        """
        return self._request("POST", f"/v1/auth/connections/{_seg(id)}/signups", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_auth_connections_id_users(self, id: str, body: PostAuthConnectionsIdUsersBody, *, idempotency_key: Optional[str] = None) -> PostAuthConnectionsIdUsersResponse:
        """Update a user (signed protocol). POST /v1/auth/connections/{id}/users

        The user changed: email and name follow to their partner record, `suspended` suspends it, `deleted` erases. Signed with the connection secret in `x-referalli-signature: t=<unix>,v1=…,v2=…` (v2 also signs the request line; once a connection has seen v2 it requires it), with a unique `x-referalli-id` per call. Calls older than 5 minutes, reused ids (`409 replay`), paused connections (`423 connection_paused`) and unknown fields (`422`) are refused.

        **Auth:** a signature (see above); no API key.
        """
        return self._request("POST", f"/v1/auth/connections/{_seg(id)}/users", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_auth_logout(self, *, idempotency_key: Optional[str] = None) -> PostAuthLogoutResponse:
        """Sign out. POST /v1/auth/logout

        Ends the browser session (and any portal-domain sessions handed off from it) and clears the cookies. Returns the identity provider's `logoutUrl` to end the provider session too, or `null`.

        **Auth:** none.
        """
        return self._request("POST", f"/v1/auth/logout", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def post_billing_activate(self, body: PostBillingActivateBody, *, idempotency_key: Optional[str] = None) -> PostBillingActivateResponse:
        """Activate a plan directly. POST /v1/billing/activate

        Moves the org to a plan without checkout: anyone may move to Free (after cancelling a subscription); paid plans only for platform admins or self-hosted deployments (403 otherwise). Owner only. Audited.

        **Auth:** an API key with `billing:write` (or `full`), or a session with role `owner`.
        """
        return self._request("POST", f"/v1/billing/activate", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_billing_checkout(self, body: PostBillingCheckoutBody, *, idempotency_key: Optional[str] = None) -> PostBillingCheckoutResponse:
        """Start a plan checkout. POST /v1/billing/checkout

        Creates a checkout session for a paid plan and returns its `url` to redirect to. 400 when billing is not configured on this deployment.

        **Auth:** an API key with `billing:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/billing/checkout", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_billing_connections(self, body: PostBillingConnectionsBody, *, idempotency_key: Optional[str] = None) -> CreatedBillingConnection:
        """Create a billing connection. POST /v1/billing/connections

        Connects a billing provider (`stripe`, `paddle`, `lemonsqueezy`, `polar`, `chargebee`, `shopify`, `recurly`, `braintree`, `woocommerce`, `bigcommerce` or `generic`) so its payment webhooks become commissions. Returns the `webhookUrl` path to register with the provider and its signing secret (generated unless you pass the provider's own `webhookSecret`); the secret is returned only here. Audited.

        **Auth:** an API key with `billing:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/billing/connections", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_billing_connections_id_rotate_secret(self, id: str, *, idempotency_key: Optional[str] = None) -> PostBillingConnectionsIdRotateSecretResponse:
        """Rotate the webhook signing secret. POST /v1/billing/connections/{id}/rotate-secret

        Generates a new signing secret, returned once. The previous one keeps verifying until `previousSecretExpiresAt` (24 hours). Audited.

        **Auth:** an API key with `billing:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/billing/connections/{_seg(id)}/rotate-secret", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def post_billing_connections_id_value_mapping_preview(self, id: str, body: PostBillingConnectionsIdValueMappingPreviewBody, *, idempotency_key: Optional[str] = None) -> ValueMappingPreview:
        """Preview the value mapping. POST /v1/billing/connections/{id}/value-mapping/preview

        Applies the saved mapping (or a draft `mapping`) to a sample `payload` and returns what would be recorded. Writes nothing. A generic-connector body with `events` gets one result per event.

        **Auth:** an API key with `billing:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/billing/connections/{_seg(id)}/value-mapping/preview", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_billing_portal(self, *, idempotency_key: Optional[str] = None) -> PostBillingPortalResponse:
        """Open the subscription portal. POST /v1/billing/portal

        Returns the `url` of the billing portal where the owner manages or cancels the subscription. 400 before there is a subscription.

        **Auth:** an API key with `billing:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/billing/portal", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def post_branding_domain(self, body: PostBrandingDomainBody, *, idempotency_key: Optional[str] = None) -> PostBrandingDomainResponse:
        """Set a custom portal domain. POST /v1/branding/domain

        Starts serving the partner portal on your own domain (such as `partners.example.com`), in your branding: returns the CNAME and TXT records to add. Needs a plan with custom domains (402 otherwise).

        **Auth:** an API key with `org:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/branding/domain", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_branding_domain_verify(self, *, idempotency_key: Optional[str] = None) -> PostBrandingLinkDomainVerifyResponse:
        """Verify the portal domain. POST /v1/branding/domain/verify

        Checks the portal domain's TXT record and CNAME, routes it and reports `provisioning` or `active` as for the link domain.

        **Auth:** an API key with `org:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/branding/domain/verify", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def post_branding_link_domain(self, body: PostBrandingLinkDomainBody, *, idempotency_key: Optional[str] = None) -> PostBrandingLinkDomainResponse:
        """Set a custom link domain. POST /v1/branding/link-domain

        Starts using your own domain (such as `go.example.com`) for partner links: returns the CNAME target and the TXT record that proves you control it. Links move onto it once verified. Needs a plan with custom domains (402 otherwise); 409 when the domain is in use.

        **Auth:** an API key with `org:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/branding/link-domain", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_branding_link_domain_verify(self, *, idempotency_key: Optional[str] = None) -> PostBrandingLinkDomainVerifyResponse:
        """Verify the link domain. POST /v1/branding/link-domain/verify

        Checks the TXT record and the CNAME. When both are right the domain is routed here; it is `active` once HTTPS answers on it (`provisioning` while the certificate is issued, which finishes on its own). 400 with what is missing otherwise.

        **Auth:** an API key with `org:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/branding/link-domain/verify", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def post_cli_device_codes(self, body: PostCliDeviceCodesBody, *, idempotency_key: Optional[str] = None) -> PostCliDeviceCodesResponse:
        """Start a CLI sign-in. POST /v1/cli/device-codes

        The CLI `login` command calls this to start a device sign-in: returns a `deviceCode` for polling and a `userCode` for the person to approve at `verificationUri`. Codes expire after 10 minutes. No authentication; limited per IP.

        **Auth:** none.
        """
        return self._request("POST", f"/v1/cli/device-codes", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_cli_device_codes_token(self, body: PostCliDeviceCodesTokenBody, *, idempotency_key: Optional[str] = None) -> PostCliDeviceCodesTokenResponse:
        """Poll a CLI sign-in. POST /v1/cli/device-codes/token

        Polled by the CLI every `interval` seconds with its `deviceCode`. Answers `pending`, `expired`, `denied` or `consumed`, or once approved, `approved` with the new API key (returned once). Polling faster than allowed is `429`.

        **Auth:** none.
        """
        return self._request("POST", f"/v1/cli/device-codes/token", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_cli_device_codes_user_code_approve(self, user_code: str, body: PostCliDeviceCodesUserCodeApproveBody, *, idempotency_key: Optional[str] = None) -> PostCliDeviceCodesUserCodeApproveResponse:
        """Approve a CLI sign-in. POST /v1/cli/device-codes/{userCode}/approve

        Approves the sign-in and mints its API key in this org. `access` picks the scopes: `cli` (webhooks write and read access to the rest, the default), `read` or `full`. Needs a signed-in owner or admin. Audited.

        **Auth:** an API key with `team:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/cli/device-codes/{_seg(user_code)}/approve", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_cli_device_codes_user_code_deny(self, user_code: str, *, idempotency_key: Optional[str] = None) -> Ok:
        """Deny a CLI sign-in. POST /v1/cli/device-codes/{userCode}/deny

        Refuses a pending sign-in; the CLI then sees `denied`.

        **Auth:** an API key with `team:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/cli/device-codes/{_seg(user_code)}/deny", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def post_cli_listeners(self, body: PostCliListenersBody, *, idempotency_key: Optional[str] = None) -> PostCliListenersResponse:
        """Open a CLI event listener. POST /v1/cli/listeners

        The CLI `listen` command opens a listener for some `topics` (default every topic). Events are queued for it while it polls at least every 2 minutes, and each comes with Standard Webhooks headers signed with the returned `secret`, so the CLI can forward them to a local server.

        **Auth:** an API key with `webhooks:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/cli/listeners", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_cli_trigger(self, body: PostCliTriggerBody, *, idempotency_key: Optional[str] = None) -> PostCliTriggerResponse:
        """Send a test event. POST /v1/cli/trigger

        The CLI `trigger` command sends a realistic sample event (ids `*_test_…`, `test: true`) to the org's listeners and webhook endpoints. `data` overrides fields of the sample. 400 for a topic with no sample; `GET /v1/cli/topics` lists them.

        **Auth:** an API key with `webhooks:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/cli/trigger", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_commission_rules(self, body: PostCommissionRulesBody, *, idempotency_key: Optional[str] = None) -> PostCommissionRulesResponse:
        """Publish a commission rule. POST /v1/commission-rules

        Publishes a new version of a program's commission rule; the latest version applies to new payments, and past lines keep the version that earned them. A rule has a `base` (percent in basis points, or a fixed amount), what it applies to (gross or net of tax or fees), how long it recurs, a hold before lines can be paid (`holdDays`, default 30), and optional conditions, per-partner/link/product overrides, volume tiers, event bounties, sub-affiliate levels and new-vs-expansion rates. Unknown fields at any depth are rejected. Audited.

        **Auth:** an API key with `commissions:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/commission-rules", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_commissions_approve_due(self, *, idempotency_key: Optional[str] = None) -> PostCommissionsApproveDueResponse:
        """Approve due commissions. POST /v1/commissions/approve-due

        Approves every pending line whose hold has elapsed (this also runs on a schedule). Returns how many were approved. Audited.

        **Auth:** an API key with `commissions:write` (or `full`), or a session with role `owner`, `admin`, `finance`.
        """
        return self._request("POST", f"/v1/commissions/approve-due", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def post_commissions_id_adjust(self, id: str, body: PostCommissionsIdAdjustBody, *, idempotency_key: Optional[str] = None) -> PostCommissionsIdAdjustResponse:
        """Adjust a commission. POST /v1/commissions/{id}/adjust

        Records an `adjusted` event against an earned line (a correction; the ledger is append-only). `amountMinor` is signed. An adjustment that would take the line below zero is refused unless `allowNegative`. Audited.

        **Auth:** an API key with `commissions:write` (or `full`), or a session with role `owner`, `admin`, `finance`.
        """
        return self._request("POST", f"/v1/commissions/{_seg(id)}/adjust", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_commissions_id_settle(self, id: str, body: PostCommissionsIdSettleBody, *, idempotency_key: Optional[str] = None) -> Settlement:
        """Settle a commission yourself. POST /v1/commissions/{id}/settle

        Marks an earned line paid because you credited the partner yourself (for example as store credit), with your `reference`: records `approved` (if it isn't yet) and `paid`, and publishes `commission.settled`. The line never reaches a payout run or the 1099 export. Repeating the same reference returns the original settlement; a line already paid otherwise is 409. Audited.

        **Auth:** an API key with `commissions:write` (or `full`), or a session with role `owner`, `admin`, `finance`.
        """
        return self._request("POST", f"/v1/commissions/{_seg(id)}/settle", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_contracts(self, body: PostContractsBody, *, idempotency_key: Optional[str] = None) -> PostContractsResponse:
        """Create a partner contract. POST /v1/contracts

        A contract offering one partner custom terms (`termsMd`) and `compensation` (percent or fixed) in a program, as a draft or sent at once (`send: true`). When accepted, the compensation becomes a partner override on a new rule version. Audited.

        **Auth:** an API key with `partners:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/contracts", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_contracts_id_send(self, id: str, *, idempotency_key: Optional[str] = None) -> OkStatus:
        """Send a contract. POST /v1/contracts/{id}/send

        Sends a draft contract to the partner. 400 when it is not a draft.

        **Auth:** an API key with `partners:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/contracts/{_seg(id)}/send", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def post_coupons(self, body: PostCouponsBody, *, idempotency_key: Optional[str] = None) -> PostCouponsResponse:
        """Create a coupon code. POST /v1/coupons

        Registers a coupon code for a partner in a program, so checkouts that use it attribute to them (coupon codes win over clicks). Codes match case-insensitively and are unique per org (409).

        **Auth:** an API key with `links:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/coupons", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_creators_account_id_invite(self, account_id: str, body: PostCreatorsAccountIdInviteBody, *, idempotency_key: Optional[str] = None) -> PostCreatorsAccountIdInviteResponse:
        """Invite a creator. POST /v1/creators/{accountId}/invite

        Invites a listed creator to a program with an optional message. 400 when they do not accept invitations or were already invited to that program.

        **Auth:** an API key with `growth:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/creators/{_seg(account_id)}/invite", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_deals_id_approve(self, id: str, body: PostDealsIdApproveBody, *, idempotency_key: Optional[str] = None) -> PostDealsIdApproveResponse:
        """Approve a deal. POST /v1/deals/{id}/approve

        Approves a submitted deal and protects it for the partner for `protectionDays` (default 90). 404 when there's no submitted deal with that id.

        **Auth:** an API key with `growth:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/deals/{_seg(id)}/approve", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_deals_id_reject(self, id: str, *, idempotency_key: Optional[str] = None) -> PostDealsIdRejectResponse:
        """Reject a deal. POST /v1/deals/{id}/reject

        Rejects a submitted deal.

        **Auth:** an API key with `growth:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/deals/{_seg(id)}/reject", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def post_deals_id_won(self, id: str, body: PostDealsIdWonBody, *, idempotency_key: Optional[str] = None) -> PostDealsIdWonResponse:
        """Mark a deal won. POST /v1/deals/{id}/won

        Marks an approved deal won, within its protection window: creates the referral for `customerRef` so the customer's payments earn the partner commission. Publishes `referral.created`.

        **Auth:** an API key with `growth:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/deals/{_seg(id)}/won", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_discovery_corpus(self, body: PostDiscoveryCorpusBody, *, idempotency_key: Optional[str] = None) -> PostDiscoveryCorpusResponse:
        """Ingest prospects. POST /v1/discovery/corpus

        Adds up to 500 prospects from your own crawl or data source. Raw page `html` is scanned for affiliate footprints (the competitor programs it recognizes) to enrich the evidence; `keywords` scores fit. Duplicate URLs are skipped. Needs a plan with discovery (402 otherwise).

        **Auth:** an API key with `growth:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/discovery/corpus", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_discovery_search(self, body: PostDiscoverySearchBody, *, idempotency_key: Optional[str] = None) -> PostDiscoverySearchResponse:
        """Search for prospective partners. POST /v1/discovery/search

        Searches the configured corpus for creators and sites matching `keywords` (and `category`), scores their fit and saves them as prospects. Needs a plan with discovery (402 otherwise).

        **Auth:** an API key with `growth:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/discovery/search", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_disputes_id_resolve(self, id: str, body: PostDisputesIdResolveBody, *, idempotency_key: Optional[str] = None) -> Ok:
        """Resolve a dispute. POST /v1/disputes/{id}/resolve

        Resolves an open dispute with a `resolution` note, which the partner sees. Publishes `dispute.resolved`. 404 when not open. Audited.

        **Auth:** an API key with `commissions:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/disputes/{_seg(id)}/resolve", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_email_preview(self, body: PostEmailPreviewBody, *, idempotency_key: Optional[str] = None) -> EmailRendered:
        """Preview an email. POST /v1/email/preview

        Renders an event's email with sample values, from the stored template or an unsaved draft.

        **Auth:** an API key with `org:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/email/preview", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_email_settings_verify_domain(self, *, idempotency_key: Optional[str] = None) -> PostEmailSettingsVerifyDomainResponse:
        """Check the sending domain. POST /v1/email/settings/verify-domain

        Asks the email provider whether the from address's domain is verified for sending, and stores the result. 400 until a provider, key and from address are set.

        **Auth:** an API key with `org:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/email/settings/verify-domain", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def post_email_test(self, body: PostEmailTestBody, *, idempotency_key: Optional[str] = None) -> PostEmailTestResponse:
        """Send a test email. POST /v1/email/test

        Sends one email with sample values to `to` through the org's provider. 400 without a provider or when the provider refuses it.

        **Auth:** an API key with `org:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/email/test", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_embed_tokens(self, body: PostEmbedTokensBody, *, idempotency_key: Optional[str] = None) -> PostEmbedTokensResponse:
        """Mint a partner embed token. POST /v1/embed/tokens

        A 15-minute token for the partner with this email, for the partner stats web component (`/embed.js`) in your app.

        **Auth:** an API key with `links:write` (or `full`), or a session of any role.
        """
        return self._request("POST", f"/v1/embed/tokens", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_fraud_cases_id_resolve(self, id: str, body: PostFraudCasesIdResolveBody, *, idempotency_key: Optional[str] = None) -> Ok:
        """Resolve a fraud case. POST /v1/fraud/cases/{id}/resolve

        Closes a case with an `action`: `dismiss` (a held referral is approved), `void_referral`, `suspend_partner` or `ban_partner`. The matching `referral.*` events are published. Audited.

        **Auth:** an API key with `fraud:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/fraud/cases/{_seg(id)}/resolve", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_fraud_detect_rings(self, *, idempotency_key: Optional[str] = None) -> PostFraudDetectRingsResponse:
        """Detect referral rings. POST /v1/fraud/detect-rings

        Looks for partners who are likely one operator with many accounts (a shared payout destination or a shared non-freemail sign-up domain) and opens a `ring` case for each group.

        **Auth:** an API key with `fraud:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/fraud/detect-rings", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def post_fraud_invalid_traffic_scan(self, body: PostFraudInvalidTrafficScanBody, *, idempotency_key: Optional[str] = None) -> PostFraudInvalidTrafficScanResponse:
        """Scan for invalid traffic. POST /v1/fraud/invalid-traffic/scan

        Scores each partner's clicks over the last `windowHours` (1 to 168, default 24) for invalid traffic and returns the probability, label and contributing signals per partner, plus how many were flagged.

        **Auth:** an API key with `fraud:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/fraud/invalid-traffic/scan", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_fx_rates(self, body: PostFxRatesBody, *, idempotency_key: Optional[str] = None) -> FxRate:
        """Record an FX rate. POST /v1/fx-rates

        Records the rate cross-currency payouts convert at, for a currency pair, as a decimal string (`"1.0825"`), effective now or at `effectiveAt`. A manual rate pins its pair over the daily feed until cleared. Audited.

        **Auth:** an API key with `payouts:write` (or `full`), or a session with role `owner`, `admin`, `finance`.
        """
        return self._request("POST", f"/v1/fx-rates", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_fx_rates_clear_override(self, body: PostFxRatesClearOverrideBody, *, idempotency_key: Optional[str] = None) -> PostFxRatesClearOverrideResponse:
        """Clear a manual FX rate. POST /v1/fx-rates/clear-override

        Retires the manual rates for a pair, handing it back to the feed. Returns how many were cleared. Audited.

        **Auth:** an API key with `payouts:write` (or `full`), or a session with role `owner`, `admin`, `finance`.
        """
        return self._request("POST", f"/v1/fx-rates/clear-override", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_fx_rates_sync(self, *, idempotency_key: Optional[str] = None) -> PostFxRatesSyncResponse:
        """Sync the FX feed now. POST /v1/fx-rates/sync

        Fetches the latest ECB reference rates for this org now, instead of waiting for the daily sync.

        **Auth:** an API key with `payouts:write` (or `full`), or a session with role `owner`, `admin`, `finance`.
        """
        return self._request("POST", f"/v1/fx-rates/sync", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def post_graphql(self, body: PostGraphqlBody, *, idempotency_key: Optional[str] = None) -> PostGraphqlResponse:
        """Query the GraphQL read layer (POST). POST /v1/graphql

        The GraphQL endpoint with the query in a JSON body. Read-only, so a read-scoped API key may call it.

        **Auth:** an API key with `analytics:read` (or `full`), or a session of any role.
        """
        return self._request("POST", f"/v1/graphql", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_import_provider(self, provider: str, body: PostImportProviderBody, *, program_id: str, dry_run: Optional[bool] = None, destination_url: Optional[str] = None, idempotency_key: Optional[str] = None) -> PostImportProviderResponse:
        """Import partners from another tool. POST /v1/import/{provider}

        Imports partners, links and codes from a Rewardful, FirstPromoter, Tolt or PartnerStack CSV export (as a `text/csv` body or `{ "csv": "…" }`) into a program. `dryRun=true` reports what would happen; `destinationUrl` is used when the export has no link column. The tool's referral parameter is added to aff.js so shared links keep crediting. Audited.

        **Auth:** an API key with `integrations:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/import/{_seg(provider)}", query={"programId": program_id, "dryRun": dry_run, "destinationUrl": destination_url}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_integrations_deliveries_id_retry(self, id: str, *, idempotency_key: Optional[str] = None) -> IntegrationDelivery:
        """Retry an integration delivery. POST /v1/integrations/deliveries/{id}/retry

        Queues a failed or skipped delivery again. 404 when there is no failed or skipped delivery with that id.

        **Auth:** an API key with `integrations:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/integrations/deliveries/{_seg(id)}/retry", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def post_integrations_hubspot_test(self, body: PostIntegrationsHubspotTestBody, *, idempotency_key: Optional[str] = None) -> PostIntegrationsHubspotTestResponse:
        """Test the HubSpot connection. POST /v1/integrations/hubspot/test

        Checks the token against HubSpot and (unless `setupProperties: false`) creates the custom properties the sync uses. Returns `ok` and the error, if any, rather than failing.

        **Auth:** an API key with `integrations:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/integrations/hubspot/test", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_integrations_segment_test(self, *, idempotency_key: Optional[str] = None) -> PostIntegrationsSegmentTestResponse:
        """Test the Segment connection. POST /v1/integrations/segment/test

        Sends one test track event with the write key and reports whether Segment accepted it.

        **Auth:** an API key with `integrations:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/integrations/segment/test", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def post_invitations_id_withdraw(self, id: str, *, idempotency_key: Optional[str] = None) -> OkStatus:
        """Withdraw an invitation. POST /v1/invitations/{id}/withdraw

        Withdraws a pending creator invitation. 400 when it was already answered or withdrawn.

        **Auth:** an API key with `partners:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/invitations/{_seg(id)}/withdraw", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def post_links(self, body: PostLinksBody, *, idempotency_key: Optional[str] = None) -> CreatedLink:
        """Create a tracked link. POST /v1/links

        Creates a partner's tracked link in a program. `code` (letters, digits, `-`; stored lowercase) is unique per org and generated when omitted. Returns the `shortUrl` to share, on the org's verified link domain when it has one. 409 when the code is taken. Audited.

        **Auth:** an API key with `links:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/links", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_mobile_purchases(self, body: PostMobilePurchasesBody, *, idempotency_key: Optional[str] = None) -> PostMobilePurchasesResponse:
        """Report an in-app purchase. POST /v1/mobile/purchases

        Your backend reports a validated App Store or Play purchase (or refund), after checking the receipt; it flows through the same commission engine as web billing. Idempotent per `eventId`. Never call this from the app itself.

        **Auth:** an API key with `billing:write` (or `full`), or a session with role `owner`, `admin`, `finance`.
        """
        return self._request("POST", f"/v1/mobile/purchases", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_notifications_id_read(self, id: str, *, idempotency_key: Optional[str] = None) -> Ok:
        """Mark a notification read. POST /v1/notifications/{id}/read

        Marks one notification read. Unknown or already-read ids are a no-op.

        **Auth:** an API key with `org:write` (or `full`), or a session of any role.
        """
        return self._request("POST", f"/v1/notifications/{_seg(id)}/read", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def post_onchain_connections(self, body: PostOnchainConnectionsBody, *, idempotency_key: Optional[str] = None) -> PostOnchainConnectionsResponse:
        """Create an on-chain connection. POST /v1/onchain/connections

        Connects an on-chain indexer: on-chain conversions posted to its webhook URL become billing events. Returns the webhook URL and signing secret.

        **Auth:** an API key with `billing:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/onchain/connections", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_org_members(self, body: PostOrgMembersBody, *, idempotency_key: Optional[str] = None) -> PostOrgMembersResponse:
        """Add a team member. POST /v1/org/members

        Adds an existing Referalli user (by email) with a role: `owner`, `admin`, `finance`, `analyst` or `support`. Only an owner can add an owner. 404 when no user has that email; 409 when already a member. Live mode only.

        **Auth:** an API key with `team:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/org/members", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_orgs(self, body: PostOrgsBody, *, idempotency_key: Optional[str] = None) -> PostOrgsResponse:
        """Create an organization. POST /v1/orgs

        Creates an organization with the signed-in user as its owner. Needs a user session (not an API key) but no `x-org-id`. Limited to 20 per hour per user. Live mode only.

        **Auth:** an API key with `team:write` (or `full`), or a session of any role.
        """
        return self._request("POST", f"/v1/orgs", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_org_sso_link(self, *, idempotency_key: Optional[str] = None) -> PostOrgSsoLinkResponse:
        """Link the org to SSO. POST /v1/org/sso/link

        Creates the org's directory tenant at the SSO provider, with the calling owner (who must have signed in with the provider) as its first admin. Owner session only. 409 when already linked elsewhere. Live mode only.

        **Auth:** an API key with `org:write` (or `full`), or a session with role `owner`.
        """
        return self._request("POST", f"/v1/org/sso/link", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def post_org_sso_tickets(self, body: PostOrgSsoTicketsBody, *, idempotency_key: Optional[str] = None) -> PostOrgSsoTicketsResponse:
        """Create an SSO setup link. POST /v1/org/sso/tickets

        A one-time link (valid `expiresInDays`, default 3) for the customer's IT admin to configure SAML or OIDC (and SCIM) on the provider's hosted page. The URL is returned once and never stored. Live mode only.

        **Auth:** an API key with `org:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/org/sso/tickets", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_org_sso_tickets_id_revoke(self, id: str, *, idempotency_key: Optional[str] = None) -> PostOrgSsoTicketsIdRevokeResponse:
        """Revoke an SSO setup link. POST /v1/org/sso/tickets/{id}/revoke

        Revokes a pending setup link. Live mode only.

        **Auth:** an API key with `org:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/org/sso/tickets/{_seg(id)}/revoke", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def post_outreach_draft(self, body: PostOutreachDraftBody, *, idempotency_key: Optional[str] = None) -> PostOutreachDraftResponse:
        """Draft an outreach sequence. POST /v1/outreach/draft

        Drafts a recruiting email sequence for a prospect. Drafts are only sent after you approve them.

        **Auth:** an API key with `growth:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/outreach/draft", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_outreach_id_approve(self, id: str, *, idempotency_key: Optional[str] = None) -> Ok:
        """Approve an outreach message. POST /v1/outreach/{id}/approve

        Approves a drafted message so `POST /v1/outreach/send-due` sends it when due. Audited.

        **Auth:** an API key with `growth:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/outreach/{_seg(id)}/approve", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def post_outreach_send_due(self, *, idempotency_key: Optional[str] = None) -> PostOutreachSendDueResponse:
        """Send due outreach. POST /v1/outreach/send-due

        Sends approved outreach messages that are due, skipping prospects without an email and addresses on the do-not-contact list (unsubscribed).

        **Auth:** an API key with `growth:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/outreach/send-due", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def post_partner_advance_accept(self, body: PostPartnerAdvanceAcceptBody, *, idempotency_key: Optional[str] = None) -> PostPartnerAdvanceAcceptResponse:
        """Take a commission advance. POST /v1/partner/advance/accept

        Takes an advance of `amountMinor` (up to the offer). The principal plus fee is repaid by withholding future commissions from payouts.

        **Auth:** a partner session.
        """
        return self._request("POST", f"/v1/partner/advance/accept", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_partner_auth_wallet_nonce(self, body: PostPartnerAuthWalletNonceBody, *, idempotency_key: Optional[str] = None) -> PostPartnerAuthWalletNonceResponse:
        """Get a wallet sign-in nonce. POST /v1/partner/auth/wallet/nonce

        Starts wallet sign-in (and AI agent registration): returns a single-use nonce, valid 10 minutes, and the message to sign with the wallet.

        **Auth:** none.
        """
        return self._request("POST", f"/v1/partner/auth/wallet/nonce", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_partner_auth_wallet_verify(self, body: PostPartnerAuthWalletVerifyBody, *, idempotency_key: Optional[str] = None) -> PostPartnerAuthWalletVerifyResponse:
        """Sign in with a wallet. POST /v1/partner/auth/wallet/verify

        Verifies the wallet's signature over the nonce message and signs the partner in (creating the account on first use), setting the session cookie. 401 for an expired nonce or a signature that does not match.

        **Auth:** none.
        """
        return self._request("POST", f"/v1/partner/auth/wallet/verify", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_partner_contracts_id_accept(self, id: str, *, idempotency_key: Optional[str] = None) -> OkStatus:
        """Accept a contract. POST /v1/partner/contracts/{id}/accept

        Accepts a sent contract; its compensation then applies to the partner's commissions in that program.

        **Auth:** a partner session.
        """
        return self._request("POST", f"/v1/partner/contracts/{_seg(id)}/accept", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def post_partner_contracts_id_decline(self, id: str, *, idempotency_key: Optional[str] = None) -> OkStatus:
        """Decline a contract. POST /v1/partner/contracts/{id}/decline

        Declines a sent contract.

        **Auth:** a partner session.
        """
        return self._request("POST", f"/v1/partner/contracts/{_seg(id)}/decline", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def post_partner_deals(self, body: PostPartnerDealsBody, *, idempotency_key: Optional[str] = None) -> PostPartnerDealsResponse:
        """Register a deal. POST /v1/partner/deals

        A partner registers a B2B deal (company, contact, expected value) in a program they are approved in, for the merchant to approve. Publishes `deal.submitted`.

        **Auth:** a partner session.
        """
        return self._request("POST", f"/v1/partner/deals", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_partner_disputes(self, body: PostPartnerDisputesBody, *, idempotency_key: Optional[str] = None) -> PostPartnerDisputesResponse:
        """File a dispute. POST /v1/partner/disputes

        Files a dispute with a merchant about a missing attribution or an unpaid commission, optionally for a referral. The merchant resolves it.

        **Auth:** a partner session.
        """
        return self._request("POST", f"/v1/partner/disputes", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_partner_invitations_id_accept(self, id: str, *, idempotency_key: Optional[str] = None) -> OkStatus:
        """Accept an invitation. POST /v1/partner/invitations/{id}/accept

        Accepts a pending invitation: the partner is created in the merchant's org if needed and enrolled, approved. The merchant is notified.

        **Auth:** a partner session.
        """
        return self._request("POST", f"/v1/partner/invitations/{_seg(id)}/accept", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def post_partner_invitations_id_decline(self, id: str, *, idempotency_key: Optional[str] = None) -> OkStatus:
        """Decline an invitation. POST /v1/partner/invitations/{id}/decline

        Declines a pending invitation. The merchant is notified.

        **Auth:** a partner session.
        """
        return self._request("POST", f"/v1/partner/invitations/{_seg(id)}/decline", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def post_partner_kyc_submit(self, body: PostPartnerKycSubmitBody, *, idempotency_key: Optional[str] = None) -> PostPartnerKycSubmitResponse:
        """Submit identity verification. POST /v1/partner/kyc/submit

        Submits the partner's legal name, country and optional date of birth and document reference for identity verification and sanctions screening. Merchants that require KYC pay only verified partners. Limited to 5 per hour per IP.

        **Auth:** a partner session.
        """
        return self._request("POST", f"/v1/partner/kyc/submit", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_partner_links(self, body: PostPartnerLinksBody, *, idempotency_key: Optional[str] = None) -> CreatedLink:
        """Create a link. POST /v1/partner/links

        Creates a tracked link in a program the partner is approved in (403 otherwise), optionally for one of the program's marketing assets. `code` is generated when omitted; 409 when taken.

        **Auth:** a partner session.
        """
        return self._request("POST", f"/v1/partner/links", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_partner_notifications_id_read(self, id: str, *, idempotency_key: Optional[str] = None) -> Ok:
        """Mark my notification read. POST /v1/partner/notifications/{id}/read

        Marks one of the partner's notifications read.

        **Auth:** a partner session.
        """
        return self._request("POST", f"/v1/partner/notifications/{_seg(id)}/read", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def post_partner_orgs_org_id_self_billing(self, org_id: str, body: PostPartnerOrgsOrgIdSelfBillingBody, *, idempotency_key: Optional[str] = None) -> PostPartnerOrgsOrgIdSelfBillingResponse:
        """Accept self-billing. POST /v1/partner/orgs/{orgId}/self-billing

        Accepts the current self-billing agreement with this merchant (`{ "accept": true }`), so the merchant issues the invoices for the partner's payouts. 404 until payout details exist.

        **Auth:** a partner session.
        """
        return self._request("POST", f"/v1/partner/orgs/{_seg(org_id)}/self-billing", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_partner_orgs_org_id_tax_form(self, org_id: str, body: PostPartnerOrgsOrgIdTaxFormBody, *, idempotency_key: Optional[str] = None) -> Ok:
        """Submit my tax form. POST /v1/partner/orgs/{orgId}/tax-form

        Submits a W-9, W-8BEN or W-8BEN-E to this merchant. A tax form is required before the partner is included in payouts.

        **Auth:** a partner session.
        """
        return self._request("POST", f"/v1/partner/orgs/{_seg(org_id)}/tax-form", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_partner_programs_program_id_apply(self, program_id: str, *, idempotency_key: Optional[str] = None) -> PostPartnerProgramsProgramIdApplyResponse:
        """Apply to a program. POST /v1/partner/programs/{programId}/apply

        Applies to an active program (for example from the marketplace), creating the partner in that merchant's org if needed. The merchant approves or rejects it. Publishes `partner.applied`. 403 for blocked accounts.

        **Auth:** a partner session.
        """
        return self._request("POST", f"/v1/partner/programs/{_seg(program_id)}/apply", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def post_partners(self, body: PostPartnersBody, *, idempotency_key: Optional[str] = None) -> Partner:
        """Create a partner. POST /v1/partners

        Creates a partner. `email` is unique per org, and so is `externalRef` (your own id for them, such as a user id). With `upsert: true` an existing partner matching the email or externalRef is returned instead of a 409 (and gets the externalRef if it had none). Over the plan's partner limit this is `402 payment_required`. Audited.

        **Auth:** an API key with `partners:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/partners", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_partner_security_totp_disable(self, body: PostPartnerSecurityTotpDisableBody, *, idempotency_key: Optional[str] = None) -> PostPartnerSecurityTotpDisableResponse:
        """Turn off two-factor. POST /v1/partner/security/totp/disable

        Turns two-factor off; needs a valid current `code`. 401 for a wrong code.

        **Auth:** a partner session.
        """
        return self._request("POST", f"/v1/partner/security/totp/disable", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_partner_security_totp_enable(self, body: PostPartnerSecurityTotpEnableBody, *, idempotency_key: Optional[str] = None) -> PostPartnerSecurityTotpEnableResponse:
        """Turn on two-factor. POST /v1/partner/security/totp/enable

        Confirms setup with a current 6-digit `code`. From then on, changing payout details needs a code in `x-totp-code`. 401 for a wrong code.

        **Auth:** a partner session.
        """
        return self._request("POST", f"/v1/partner/security/totp/enable", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_partner_security_totp_setup(self, *, idempotency_key: Optional[str] = None) -> PostPartnerSecurityTotpSetupResponse:
        """Start two-factor setup. POST /v1/partner/security/totp/setup

        Generates a TOTP secret and its `otpauth://` URI for an authenticator app. 400 when two-factor is already on.

        **Auth:** a partner session.
        """
        return self._request("POST", f"/v1/partner/security/totp/setup", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def post_partners_id_tax_form(self, id: str, body: PostPartnersIdTaxFormBody, *, idempotency_key: Optional[str] = None) -> Ok:
        """Record a partner's tax form. POST /v1/partners/{id}/tax-form

        Records a W-9, W-8BEN or W-8BEN-E for the partner (`data` is the form's fields). A tax form on file is required before a partner is included in a payout run.

        **Auth:** an API key with `payouts:write` (or `full`), or a session with role `owner`, `admin`, `finance`.
        """
        return self._request("POST", f"/v1/partners/{_seg(id)}/tax-form", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_partner_terms_version_id_accept(self, version_id: str, *, idempotency_key: Optional[str] = None) -> Ok:
        """Accept program terms. POST /v1/partner/terms/{versionId}/accept

        Records the partner's acceptance of a terms version. Repeating it is a no-op.

        **Auth:** a partner session.
        """
        return self._request("POST", f"/v1/partner/terms/{_seg(version_id)}/accept", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def post_passport_verify(self, body: PostPassportVerifyBody, *, idempotency_key: Optional[str] = None) -> PostPassportVerifyResponse:
        """Verify a partner passport. POST /v1/passport/verify

        Checks a partner's signed reputation passport: `valid: true` with its claims, or `valid: false` with the reason (bad signature, expired). No authentication.

        **Auth:** none.
        """
        return self._request("POST", f"/v1/passport/verify", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_payout_runs(self, *, idempotency_key: Optional[str] = None) -> PayoutRunCreated:
        """Create a payout run. POST /v1/payout-runs

        Builds a draft run: one payout per partner who has a payout profile, a tax form and an approved, unpaid balance over their threshold, converted into their payout currency at recorded FX, each with a self-billing invoice. Partners left out are listed in `skipped` with the reason. Nothing is paid until you execute it. Audited.

        **Auth:** an API key with `payouts:write` (or `full`), or a session with role `owner`, `admin`, `finance`.
        """
        return self._request("POST", f"/v1/payout-runs", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def post_payout_runs_id_cancel(self, id: str, *, idempotency_key: Optional[str] = None) -> PostPayoutRunsIdCancelResponse:
        """Cancel a payout run. POST /v1/payout-runs/{id}/cancel

        Cancels a run that hasn't paid out and releases its lines back to the partners' approved balances. A run with money in flight is 409. Publishes `payout.cancelled` per payout. Audited.

        **Auth:** an API key with `payouts:write` (or `full`), or a session with role `owner`, `admin`, `finance`.
        """
        return self._request("POST", f"/v1/payout-runs/{_seg(id)}/cancel", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def post_payout_runs_id_execute(self, id: str, *, idempotency_key: Optional[str] = None) -> PostPayoutRunsIdExecuteResponse:
        """Execute a payout run. POST /v1/payout-runs/{id}/execute

        Pays a draft run through the org's own connected payout providers (methods with no connection are simulated and logged; test mode uses the test rail). Returns how many were sent, submitted (settling asynchronously) and failed; each outcome publishes `payout.sent`, `payout.submitted` or `payout.failed`. Audited.

        **Auth:** an API key with `payouts:write` (or `full`), or a session with role `owner`, `admin`, `finance`.
        """
        return self._request("POST", f"/v1/payout-runs/{_seg(id)}/execute", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def post_payout_runs_run_scheduled(self, *, idempotency_key: Optional[str] = None) -> PostPayoutRunsRunScheduledResponse:
        """Run due payout schedules. POST /v1/payout-runs/run-scheduled

        Creates and executes payout runs for every schedule (org or program) that is due now. This also runs hourly on its own.

        **Auth:** an API key with `payouts:write` (or `full`), or a session with role `owner`, `admin`, `finance`.
        """
        return self._request("POST", f"/v1/payout-runs/run-scheduled", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def post_privacy_forget(self, body: PostPrivacyForgetBody, *, idempotency_key: Optional[str] = None) -> PostPrivacyForgetResponse:
        """Erase a data subject. POST /v1/privacy/forget

        Erases (pseudonymizes, keeping the ledger balanced) a customer by `customerRef`, a partner by `partnerId`, or by `email` both the partner with that email and every customer stored under its hash. Send exactly one. 400 when nothing is found. Audited.

        **Auth:** an API key with `privacy:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/privacy/forget", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_privacy_lookup(self, body: PostPrivacyLookupBody, *, idempotency_key: Optional[str] = None) -> PostPrivacyLookupResponse:
        """Find a data subject by email. POST /v1/privacy/lookup

        Which customers and partners an email refers to. The email is hashed on the server and never stored.

        **Auth:** an API key with `privacy:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/privacy/lookup", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_privacy_requests(self, body: PostPrivacyRequestsBody, *, idempotency_key: Optional[str] = None) -> PostPrivacyRequestsResponse:
        """Open a data-subject request. POST /v1/privacy/requests

        Opens an `access` or `erasure` request for one subject (`email`, `customerRef` or `partnerId`) and answers `202` with the request to poll. Publishes `privacy.request_completed` when done.

        **Auth:** an API key with `privacy:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/privacy/requests", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_profitability_rebuild(self, *, idempotency_key: Optional[str] = None) -> PostProfitabilityRebuildResponse:
        """Rebuild ROI figures. POST /v1/profitability/rebuild

        Recomputes every stored ROI figure from the value events with the current settings and mappings, in the background. Returns a `jobId` to poll; while one rebuild is running, the same job is returned. Audited.

        **Auth:** an API key with `analytics:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/profitability/rebuild", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def post_programs(self, body: PostProgramsBody, *, idempotency_key: Optional[str] = None) -> Program:
        """Create a program. POST /v1/programs

        Creates an affiliate program: its attribution model, cookie window, how long after sign-up a conversion still counts, terms, public page and settings. `slug` is unique per org. Terms are versioned so partners can be asked to accept new ones. Over the plan's program limit this is `402 payment_required`.

        **Auth:** an API key with `programs:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/programs", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_programs_id_apply_leveling(self, id: str, *, idempotency_key: Optional[str] = None) -> PostProgramsIdApplyLevelingResponse:
        """Apply partner levels. POST /v1/programs/{id}/apply-leveling

        Promotes the program's partners to the highest level their referral count qualifies for (never demotes). Publishes `partner.level_up` per promotion.

        **Auth:** an API key with `programs:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/programs/{_seg(id)}/apply-leveling", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def post_programs_id_autoprice_run(self, id: str, body: PostProgramsIdAutopriceRunBody, *, idempotency_key: Optional[str] = None) -> PostProgramsIdAutopriceRunResponse:
        """Run autopricing. POST /v1/programs/{id}/autoprice/run

        Moves each partner's rate toward the target and publishes the new rates as partner overrides on a new rule version. Objective `roas` compares attributed revenue to commission; `roi` uses each partner's matured referral ROI, holding partners with too few matured referrals or an unknown ROI (listed in `held`). 400 when autopricing is off, the program has no percent-based rule, or no partner has a known ROI under `roi`.

        **Auth:** an API key with `programs:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/programs/{_seg(id)}/autoprice/run", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_programs_id_enrollments(self, id: str, body: PostProgramsIdEnrollmentsBody, *, idempotency_key: Optional[str] = None) -> Enrollment:
        """Enroll a partner. POST /v1/programs/{id}/enrollments

        Enrolls an existing partner in the program, approved at once. Publishes `partner.enrolled`. 409 when already enrolled.

        **Auth:** an API key with `programs:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/programs/{_seg(id)}/enrollments", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_programs_id_enrollments_enrollment_id_approve(self, id: str, enrollment_id: str, *, idempotency_key: Optional[str] = None) -> PostProgramsIdEnrollmentsEnrollmentIdApproveResponse:
        """Approve an application. POST /v1/programs/{id}/enrollments/{enrollmentId}/approve

        Approves a pending application (`status: "applied"`). Publishes `partner.approved`. 404 when there is no pending application with that id. Audited.

        **Auth:** an API key with `programs:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/programs/{_seg(id)}/enrollments/{_seg(enrollment_id)}/approve", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def post_programs_id_enrollments_enrollment_id_reject(self, id: str, enrollment_id: str, *, idempotency_key: Optional[str] = None) -> PostProgramsIdEnrollmentsEnrollmentIdRejectResponse:
        """Reject an application. POST /v1/programs/{id}/enrollments/{enrollmentId}/reject

        Rejects a pending application. 404 when there is no pending application with that id. Audited.

        **Auth:** an API key with `programs:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/programs/{_seg(id)}/enrollments/{_seg(enrollment_id)}/reject", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def post_programs_id_groups(self, id: str, body: PostProgramsIdGroupsBody, *, idempotency_key: Optional[str] = None) -> PartnerGroup:
        """Create a partner group. POST /v1/programs/{id}/groups

        A group of partners in a program with its own commission base (or `null` to keep the program rule's), hold days, payout threshold, payout currency, onboarding message and checklist. Names are unique per program (409).

        **Auth:** an API key with `programs:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/programs/{_seg(id)}/groups", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_programs_id_promotions(self, id: str, body: PostProgramsIdPromotionsBody, *, idempotency_key: Optional[str] = None) -> Promotion:
        """Create a promotion. POST /v1/programs/{id}/promotions

        A time-boxed commission change for the whole program or one group: `replace` the base rate, or `boost` it by `bps`, between `startsAt` and `endsAt`. Payments in that window get it.

        **Auth:** an API key with `programs:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/programs/{_seg(id)}/promotions", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_promotions_id_end(self, id: str, *, idempotency_key: Optional[str] = None) -> Promotion:
        """End a promotion. POST /v1/promotions/{id}/end

        Ends a promotion now: payments from this moment on no longer get it.

        **Auth:** an API key with `programs:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/promotions/{_seg(id)}/end", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def post_public_programs_handle_join(self, handle: str, body: PostPublicProgramsHandleJoinBody, *, idempotency_key: Optional[str] = None) -> PostPublicProgramsHandleJoinResponse:
        """Join a program. POST /v1/public/programs/{handle}/join

        One-step join from the public page for a signed-in partner: creates (or claims, with a verified email) the partner in the merchant's org and enrolls them, approved with a first link when the program auto-approves, otherwise as an application. Publishes `partner.approved` or `partner.applied`. 409 when the merchant's partner with that email belongs to another account.

        **Auth:** a partner session.
        """
        return self._request("POST", f"/v1/public/programs/{_seg(handle)}/join", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_quality_recompute(self, *, idempotency_key: Optional[str] = None) -> PostQualityRecomputeResponse:
        """Recompute quality scores. POST /v1/quality/recompute

        Snapshots every partner's quality score now; per the org's policy, low scores open a `quality` case or suspend the partner. Audited.

        **Auth:** an API key with `partners:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/quality/recompute", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def post_referrals_associate(self, body: PostReferralsAssociateBody, *, idempotency_key: Optional[str] = None) -> AssociateResponse:
        """Attribute a new customer. POST /v1/referrals/associate

        The key server-side call: tell Referalli a customer signed up, with whatever you know about where they came from (`referralToken`/`ref_click_id`, `anonId`, `couponCode`, `emailHash`, IP and user agent). The attribution engine picks the partner under the program's model and windows. `referral` is `null` when no partner matched (not an error); `reasoning.notes` says why. Repeating `idempotencyKey` returns the existing referral. `occurredAt` records a late call at the real sign-up time (up to 5 minutes of clock skew is tolerated) and backfills payments since. `emailDomain` lets burner-email sign-ups be held for review. Publishes `referral.created` (or `referral.held`).

        **Auth:** an API key with `referrals:write` (or `full`), or a session of any role.
        """
        return self._request("POST", f"/v1/referrals/associate", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_referrals_id_approve(self, id: str, *, idempotency_key: Optional[str] = None) -> Referral:
        """Approve a held referral. POST /v1/referrals/{id}/approve

        Releases a referral held for review (`pending_review`) back to `active`. 404 when it isn't pending review. Publishes `referral.approved`. Audited.

        **Auth:** an API key with `referrals:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/referrals/{_seg(id)}/approve", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def post_referrals_id_reassign(self, id: str, body: PostReferralsIdReassignBody, *, idempotency_key: Optional[str] = None) -> Referral:
        """Reassign a referral. POST /v1/referrals/{id}/reassign

        Moves the referral to another partner (recorded as a manual match). Publishes `referral.reassigned` with the previous partner. Audited.

        **Auth:** an API key with `referrals:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/referrals/{_seg(id)}/reassign", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_referrals_id_void(self, id: str, *, idempotency_key: Optional[str] = None) -> Referral:
        """Void a referral. POST /v1/referrals/{id}/void

        Voids the referral so it earns nothing more. Publishes `referral.voided`. Audited.

        **Auth:** an API key with `referrals:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/referrals/{_seg(id)}/void", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def post_rewards_id_redeem(self, id: str, body: PostRewardsIdRedeemBody, *, idempotency_key: Optional[str] = None) -> PostRewardsRedeemByCodeResponse:
        """Redeem a reward. POST /v1/rewards/{id}/redeem

        Records a (possibly partial) redemption: `amountMinor` (default the remaining balance) is capped at what's left, and the reward becomes `redeemed` once it is used up. `externalId` makes it idempotent (409 if reused for another reward). Publishes `credit.redeemed`.

        **Auth:** an API key with `commissions:write` (or `full`), or a session with role `owner`, `admin`, `finance`.
        """
        return self._request("POST", f"/v1/rewards/{_seg(id)}/redeem", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_rewards_redeem_by_code(self, body: PostRewardsRedeemByCodeBody, *, idempotency_key: Optional[str] = None) -> PostRewardsRedeemByCodeResponse:
        """Redeem a reward by code. POST /v1/rewards/redeem-by-code

        Records a redemption of the reward with this code; see `POST /v1/rewards/{id}/redeem`. 404 for an unknown code.

        **Auth:** an API key with `commissions:write` (or `full`), or a session with role `owner`, `admin`, `finance`.
        """
        return self._request("POST", f"/v1/rewards/redeem-by-code", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_roi_patterns_pattern_review(self, pattern: str, body: PostRoiPatternsPatternReviewBody, *, idempotency_key: Optional[str] = None) -> FraudCase:
        """Open a review for a pattern match. POST /v1/roi/patterns/{pattern}/review

        Turns one live pattern match (by `customerRef` and/or `partnerId`, optionally `programId`) into a `value_pattern` fraud case against its partner, or returns the open case for the same match. Publishes `fraud.case_opened`. 404 when no such match exists. Audited.

        **Auth:** an API key with `analytics:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/roi/patterns/{_seg(pattern)}/review", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_sandbox_simulate(self, body: PostSandboxSimulateBody, *, idempotency_key: Optional[str] = None) -> PostSandboxSimulateResponse:
        """Simulate billing history. POST /v1/sandbox/simulate

        Generates deterministic billing history through the real commission pipeline, so you can see commissions flow without a provider: a new sandbox customer referred to the partner, `months` (default 3) of subscription payments at `priceMinor`, then for `scenario: "refund"` a half refund of the first invoice or for `churn` a cancellation. Returns the customer and what was created. Audited.

        **Auth:** an API key with `billing:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/sandbox/simulate", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_tax1099_documents_id_correct(self, id: str, *, idempotency_key: Optional[str] = None) -> TaxFiling:
        """File a corrected 1099. POST /v1/tax/1099/documents/{id}/correct

        Files a corrected form for one document with the partner's current amount. Audited.

        **Auth:** an API key with `payouts:write` (or `full`), or a session with role `owner`, `admin`, `finance`.
        """
        return self._request("POST", f"/v1/tax/1099/documents/{_seg(id)}/correct", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def post_tax1099_filings(self, body: PostTax1099FilingsBody, *, idempotency_key: Optional[str] = None) -> TaxFiling:
        """File 1099-NEC forms. POST /v1/tax/1099/filings

        E-files the year's 1099-NEC forms through the connected provider and records one document per partner. Audited.

        **Auth:** an API key with `payouts:write` (or `full`), or a session with role `owner`, `admin`, `finance`.
        """
        return self._request("POST", f"/v1/tax/1099/filings", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_tax1099_filings_id_refresh(self, id: str, *, idempotency_key: Optional[str] = None) -> PostTax1099FilingsIdRefreshResponse:
        """Refresh a filing status. POST /v1/tax/1099/filings/{id}/refresh

        Asks the filing provider for the latest status of a filing and its documents; accepted forms are then delivered to partners (`tax.form_delivered`).

        **Auth:** an API key with `payouts:write` (or `full`), or a session with role `owner`, `admin`, `finance`.
        """
        return self._request("POST", f"/v1/tax/1099/filings/{_seg(id)}/refresh", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def post_test_clock_advance(self, body: PostTestClockAdvanceBody, *, idempotency_key: Optional[str] = None) -> PostTestClockAdvanceResponse:
        """Advance the test clock. POST /v1/test_clock/advance

        Test mode only. Moves the test org's clock forward by `seconds` (never back), then runs what came due: held commissions are approved, payout schedules fire and retention purges run. Returns the new time and what ran. Audited.

        **Auth:** an API key with `org:write` (or `full`), or a session with role `owner`, `admin`, `finance`.
        """
        return self._request("POST", f"/v1/test_clock/advance", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_track_events(self, body: Union[PostTrackEventsBodyOption1, PostTrackEventsBodyOption2, PostTrackEventsBodyOption3], *, idempotency_key: Optional[str] = None) -> PostTrackEventsResponse:
        """Track an event. POST /v1/track/events

        Records one event. `type: "event"` is a product event for a known customer (`event`, such as `trial_started`) that can pay a bounty under the program's commission rule; it returns whether it was recorded and the commission. `idempotencyKey` deduplicates. `type: "click"` records a server-side click for a partner; `type: "custom"` records an audited custom event. Publishable keys may send only custom events.

        **Auth:** an API key with `events:write` (or `full`), or a session of any role.
        """
        return self._request("POST", f"/v1/track/events", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_unsubscribe_token(self, token: str, *, idempotency_key: Optional[str] = None) -> PostUnsubscribeTokenResponse:
        """Unsubscribe from outreach. POST /v1/unsubscribe/{token}

        The one-click unsubscribe link in outreach emails. No authentication; the token identifies the recipient.

        **Auth:** none.
        """
        return self._request("POST", f"/v1/unsubscribe/{_seg(token)}", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def post_value_events(self, body: PostValueEventsBody, *, idempotency_key: Optional[str] = None) -> PostValueEventsResponse:
        """Record value events. POST /v1/value/events

        Reports up to 500 value facts from your platform: `payment`, `refund`, `credit_granted`, `credit_redeemed`, `credit_expired`, `credit_revoked`, `cost` or `adjustment`. Each needs `kind`, `currency`, `externalId` (your stable id, which makes it idempotent) and `occurredAt`, plus the customer, partner (`partnerId` or `partnerExternalRef`), grant, program, product and amount fields (`cashMinor`, `creditAppliedMinor`, `discountMinor`, `taxMinor`, `feesMinor`, `costMinor`, `faceMinor`) that apply. Each event is validated and recorded on its own: `results` and `errors` are by index. A repeat of an `externalId` with new figures supersedes the earlier one.

        **Auth:** an API key with `analytics:write` (or `full`), or a session of any role.
        """
        return self._request("POST", f"/v1/value/events", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_value_import(self, body: PostValueImportBody, *, idempotency_key: Optional[str] = None) -> PostValueImportResponse:
        """Import value events from CSV. POST /v1/value/import

        Imports value events from CSV text (up to 10,000 rows and 5 MB, else `413 payload_too_large`) with a `mapping` from column names to event fields (money as `<field>Minor` or `<field>Major`). `kind` applies to every row unless a column maps to it. Up to 500 rows are recorded before the response; a larger file answers `202` with a `jobId` to poll. `dryRun` returns the first 20 parsed rows and every row error without recording.

        **Auth:** an API key with `analytics:write` (or `full`), or a session of any role.
        """
        return self._request("POST", f"/v1/value/import", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_webhook_deliveries_id_replay(self, id: str, *, idempotency_key: Optional[str] = None) -> Ok:
        """Replay a webhook delivery. POST /v1/webhook-deliveries/{id}/replay

        Queues the delivery again at once with its attempt count reset. It keeps its `webhook-id`, so receivers can deduplicate.

        **Auth:** an API key with `webhooks:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/webhook-deliveries/{_seg(id)}/replay", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def post_webhook_endpoints(self, body: PostWebhookEndpointsBody, *, idempotency_key: Optional[str] = None) -> PostWebhookEndpointsResponse:
        """Create a webhook endpoint. POST /v1/webhook-endpoints

        Subscribes an HTTPS URL to event topics (default `["*"]`, every event; see the `webhooks` section of this document for each topic's payload). `programIds` limits it to events about those programs (org-wide events such as payouts are then not sent). Deliveries are signed the Standard Webhooks way with the returned `secret` (`whsec_…`), shown only here. `legacySignature: true` also sends the deprecated body-only signature.

        **Auth:** an API key with `webhooks:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/webhook-endpoints", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_webhook_endpoints_id_rotate_secret(self, id: str, *, idempotency_key: Optional[str] = None) -> PostWebhookEndpointsIdRotateSecretResponse:
        """Rotate an endpoint secret. POST /v1/webhook-endpoints/{id}/rotate-secret

        Issues a new signing secret, returned once. For 24 hours (`previousSecretExpiresAt`) every delivery carries a signature from each secret, so receivers can switch without dropping any. Audited.

        **Auth:** an API key with `webhooks:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/webhook-endpoints/{_seg(id)}/rotate-secret", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    def post_widget_tokens(self, body: PostWidgetTokensBody, *, idempotency_key: Optional[str] = None) -> PostWidgetTokensResponse:
        """Mint a referral widget token. POST /v1/widget/tokens

        Your backend mints a short-lived token (60 to 3600 seconds, default 900) for a signed-in customer, identified by `customerRef` or `partnerExternalRef`, for the in-app referral widget. When the program has `settings.widget.autoEnroll`, a customer who isn't a partner yet is created on demand (send `email`). The token only reads that partner's own data.

        **Auth:** an API key with `partners:write` (or `full`), or a session of any role.
        """
        return self._request("POST", f"/v1/widget/tokens", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_zapier_conversions(self, body: PostZapierConversionsBody, *, idempotency_key: Optional[str] = None) -> PostZapierConversionsResponse:
        """Record a conversion from Zapier. POST /v1/zapier/conversions

        Zapier's "Record conversion" action: a payment (or refund) for a customer through a generic billing connection (the org's first active one unless `connectionId`), with no signature needed. Idempotent by `providerEventId`. 400 without a generic billing connection.

        **Auth:** an API key with `billing:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/zapier/conversions", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def post_zapier_hooks(self, body: PostZapierHooksBody, *, idempotency_key: Optional[str] = None) -> ZapierHook:
        """Subscribe a Zapier hook. POST /v1/zapier/hooks

        REST hook subscribe, called by Zapier when a Zap turns on: events of `event` are posted to the HTTPS `target_url`.

        **Auth:** an API key with `integrations:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("POST", f"/v1/zapier/hooks", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def put_billing_connections_id_credentials(self, id: str, body: PutBillingConnectionsIdCredentialsBody, *, idempotency_key: Optional[str] = None) -> PutBillingConnectionsIdCredentialsResponse:
        """Set provider API credentials. PUT /v1/billing/connections/{id}/credentials

        For providers that send thin webhooks (Recurly, BigCommerce), the API credentials used to fetch the full event: `apiKey`, or `apiToken` plus `storeHash`, and `region`. Stored encrypted. 400 for providers that take no credentials or when a required field is missing. Audited.

        **Auth:** an API key with `billing:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("PUT", f"/v1/billing/connections/{_seg(id)}/credentials", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def put_billing_connections_id_secret(self, id: str, body: PutBillingConnectionsIdSecretBody, *, idempotency_key: Optional[str] = None) -> PutBillingConnectionsIdSecretResponse:
        """Set the webhook signing secret. PUT /v1/billing/connections/{id}/secret

        Replaces the connection's signing secret with the provider's own (at least 8 characters). The previous secret keeps verifying for 24 hours. Audited.

        **Auth:** an API key with `billing:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("PUT", f"/v1/billing/connections/{_seg(id)}/secret", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def put_billing_connections_id_value_mapping(self, id: str, body: PutBillingConnectionsIdValueMappingBody, *, idempotency_key: Optional[str] = None) -> PutBillingConnectionsIdValueMappingResponse:
        """Set the value mapping. PUT /v1/billing/connections/{id}/value-mapping

        Where cash, credit applied, discount, cost and product live in this connection's payloads, as dot paths (`[]` sums an array, for example `data.discounts[].amount`), and whether amounts are in minor or major units. Each save bumps the mapping version; a rebuild re-applies it to stored events. Audited.

        **Auth:** an API key with `billing:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("PUT", f"/v1/billing/connections/{_seg(id)}/value-mapping", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def put_branding(self, body: PutBrandingBody, *, idempotency_key: Optional[str] = None) -> Ok:
        """Update branding. PUT /v1/branding

        Sets the logo URL, theme (only the documented `--r-*` tokens, with plain CSS values) and email sender. Omitted fields keep their value.

        **Auth:** an API key with `org:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("PUT", f"/v1/branding", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def put_email_settings(self, body: PutEmailSettingsBody, *, idempotency_key: Optional[str] = None) -> EmailSettings:
        """Update email settings. PUT /v1/email/settings

        Sets the email provider and its API key (write-only: omit to keep it, `null` to remove), the from address and name, reply-to, logo and primary color for partner emails. Without a provider, no email is sent.

        **Auth:** an API key with `org:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("PUT", f"/v1/email/settings", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def put_email_templates_event_locale(self, event: str, locale: str, body: PutEmailTemplatesEventLocaleBody, *, idempotency_key: Optional[str] = None) -> PutEmailTemplatesEventLocaleResponse:
        """Override an email template. PUT /v1/email/templates/{event}/{locale}

        Replaces the subject, text and optional HTML of one event in one locale. 404 for an unknown event or locale.

        **Auth:** an API key with `org:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("PUT", f"/v1/email/templates/{_seg(event)}/{_seg(locale)}", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def put_integrations_hubspot(self, body: PutIntegrationsHubspotBody, *, idempotency_key: Optional[str] = None) -> IntegrationConnection:
        """Connect HubSpot. PUT /v1/integrations/hubspot

        Connects HubSpot with your private-app `token` (required the first time; omit to keep it) to sync partners as contacts and referrals as deals in `pipeline`, moving them to `paidDealStage` when they pay. `status: "paused"` stops syncing.

        **Auth:** an API key with `integrations:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("PUT", f"/v1/integrations/hubspot", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def put_integrations_segment(self, body: PutIntegrationsSegmentBody, *, idempotency_key: Optional[str] = None) -> IntegrationConnection:
        """Connect Segment. PUT /v1/integrations/segment

        Connects a Segment source with its `writeKey` (required the first time) and sends referral, commission, payout and partner events as track calls; `events` limits which topics (`null` for all).

        **Auth:** an API key with `integrations:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("PUT", f"/v1/integrations/segment", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def put_marketplace_listing(self, body: PutMarketplaceListingBody, *, idempotency_key: Optional[str] = None) -> Ok:
        """List a program in the marketplace. PUT /v1/marketplace/listing

        Creates or updates the marketplace listing of a program: visibility (`public` or `unlisted`), category, headline, description and sponsored placement. Audited.

        **Auth:** an API key with `growth:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("PUT", f"/v1/marketplace/listing", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def put_me_locale(self, body: PutMeLocaleBody, *, idempotency_key: Optional[str] = None) -> PutMeLocaleResponse:
        """Set my email language. PUT /v1/me/locale

        The signed-in user's preferred locale for emails. User session only.

        **Auth:** an API key with `team:write` (or `full`), or a session of any role.
        """
        return self._request("PUT", f"/v1/me/locale", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def put_me_roi_digest(self, body: PutMeRoiDigestBody, *, idempotency_key: Optional[str] = None) -> PutMeRoiDigestResponse:
        """Turn my ROI digest on or off. PUT /v1/me/roi-digest

        Whether the signed-in member receives this org's periodic credit ROI digest email. User session only.

        **Auth:** an API key with `team:write` (or `full`), or a session of any role.
        """
        return self._request("PUT", f"/v1/me/roi-digest", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def put_network_settings(self, body: PutNetworkSettingsBody, *, idempotency_key: Optional[str] = None) -> PutNetworkSettingsResponse:
        """Join or leave the attribution network. PUT /v1/network/settings

        Opts the org in or out of the cross-merchant attribution network: contributing its referral touchpoints (as hashed customer identities and partner accounts, never merchant identity or PII) and, in return, reading the network journey.

        **Auth:** an API key with `growth:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("PUT", f"/v1/network/settings", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def put_org_fx_feed(self, body: PutOrgFxFeedBody, *, idempotency_key: Optional[str] = None) -> PutOrgFxFeedResponse:
        """Turn the FX feed on or off. PUT /v1/org/fx-feed

        Turns the daily ECB reference-rate feed on or off. Turning it on syncs once at once and returns how many rates were inserted. Audited.

        **Auth:** an API key with `org:write` (or `full`), or a session with role `owner`, `admin`, `finance`.
        """
        return self._request("PUT", f"/v1/org/fx-feed", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def put_org_payout_schedule(self, body: PutOrgPayoutScheduleBody, *, idempotency_key: Optional[str] = None) -> PutOrgPayoutScheduleResponse:
        """Set the org payout schedule. PUT /v1/org/payout-schedule

        When payouts run automatically for every program without its own schedule: a `schedule` (`monthly`, `weekly`, `twice_monthly` or `custom` dates), the older `dayOfMonth` form, or `null` to turn automatic payouts off. Send exactly one of `schedule` and `dayOfMonth`. Audited.

        **Auth:** an API key with `payouts:write` (or `full`), or a session with role `owner`, `admin`, `finance`.
        """
        return self._request("PUT", f"/v1/org/payout-schedule", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def put_org_referral_params(self, body: PutOrgReferralParamsBody, *, idempotency_key: Optional[str] = None) -> GetOrgReferralParamsResponse:
        """Set referral query parameters. PUT /v1/org/referral-params

        Replaces the extra query parameters aff.js reads a referral code from (up to 10; lowercase letters, digits and `_`). Built-in names are dropped. Imports add the previous tool's parameter here so already-shared links keep crediting. Audited.

        **Auth:** an API key with `org:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("PUT", f"/v1/org/referral-params", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def put_org_retention(self, body: PutOrgRetentionBody, *, idempotency_key: Optional[str] = None) -> Retention:
        """Set the data retention policy. PUT /v1/org/retention

        Changes retention days for one or more kinds of raw data (others keep their value). Values below a kind's minimum are rejected. Audited.

        **Auth:** an API key with `org:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("PUT", f"/v1/org/retention", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def put_org_tax_filing(self, body: PutOrgTaxFilingBody, *, idempotency_key: Optional[str] = None) -> PutOrgTaxFilingResponse:
        """Connect a 1099 filing provider. PUT /v1/org/tax-filing

        Chooses who e-files 1099-NEC forms: `test` (simulated) or `tax1099` with your own API key (stored encrypted). Audited.

        **Auth:** an API key with `org:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("PUT", f"/v1/org/tax-filing", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def put_org_tax_profile(self, body: PutOrgTaxProfileBody, *, idempotency_key: Optional[str] = None) -> TaxProfile:
        """Update the tax profile. PUT /v1/org/tax-profile

        Sets any of the tax profile fields; `null` clears one. A VAT id must be a valid EU VAT number; an EIN looks like `12-3456789`. Audited.

        **Auth:** an API key with `org:write` (or `full`), or a session with role `owner`, `admin`, `finance`.
        """
        return self._request("PUT", f"/v1/org/tax-profile", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def put_partner_locale(self, body: PutPartnerLocaleBody, *, idempotency_key: Optional[str] = None) -> PutPartnerLocaleResponse:
        """Set my email language (partner). PUT /v1/partner/locale

        The partner account's preferred locale for emails.

        **Auth:** a partner session.
        """
        return self._request("PUT", f"/v1/partner/locale", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def put_partner_orgs_org_id_payout_profile(self, org_id: str, body: PutPartnerOrgsOrgIdPayoutProfileBody, *, idempotency_key: Optional[str] = None) -> PutPartnerOrgsOrgIdPayoutProfileResponse:
        """Set my payout details. PUT /v1/partner/orgs/{orgId}/payout-profile

        How this merchant pays the partner: the method, its details (checked for what the rail needs, such as a PayPal email or wallet address) and currency. When two-factor sign-in is on, send the current code in `x-totp-code` (`401 step_up_required` otherwise).

        **Auth:** a partner session.
        """
        return self._request("PUT", f"/v1/partner/orgs/{_seg(org_id)}/payout-profile", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def put_partner_orgs_org_id_postback(self, org_id: str, body: PutPartnerOrgsOrgIdPostbackBody, *, idempotency_key: Optional[str] = None) -> PutPartnerOrgsOrgIdPostbackResponse:
        """Set my conversion postback. PUT /v1/partner/orgs/{orgId}/postback

        Registers a server-to-server postback URL the merchant calls on the partner's events, with macros `{topic}`, `{partner_id}`, `{referral_id}`, `{customer}`, `{amount}`, `{currency}`. Returns a new signing secret.

        **Auth:** a partner session.
        """
        return self._request("PUT", f"/v1/partner/orgs/{_seg(org_id)}/postback", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def put_partner_orgs_org_id_vat(self, org_id: str, body: PutPartnerOrgsOrgIdVatBody, *, idempotency_key: Optional[str] = None) -> PutPartnersIdVatResponse:
        """Set my VAT number. PUT /v1/partner/orgs/{orgId}/vat

        Sets the partner's own EU VAT number with this merchant, checked against VIES when the merchant requires it.

        **Auth:** a partner session.
        """
        return self._request("PUT", f"/v1/partner/orgs/{_seg(org_id)}/vat", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def put_partner_profile(self, body: PutPartnerProfileBody, *, idempotency_key: Optional[str] = None) -> Ok:
        """Update my creator profile. PUT /v1/partner/profile

        Updates the creator profile merchants search. `published: true` lists it in creator search; `acceptsInvites` controls whether merchants can invite the partner.

        **Auth:** a partner session.
        """
        return self._request("PUT", f"/v1/partner/profile", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def put_partners_id_payout_profile(self, id: str, body: PutPartnersIdPayoutProfileBody, *, idempotency_key: Optional[str] = None) -> PutPartnersIdPayoutProfileResponse:
        """Set a partner's payout profile. PUT /v1/partners/{id}/payout-profile

        How the partner is paid: `method` (`paypal`, `wise`, `stripe_connect`, `ach`, `crypto`, `payoneer`, `tremendous` or `csv`), method `details` (a free-form map such as `{ "paypalEmail": … }`), the currency to pay in and the minimum balance before a payout. Partners can also set this themselves in the portal.

        **Auth:** an API key with `payouts:write` (or `full`), or a session with role `owner`, `admin`, `finance`.
        """
        return self._request("PUT", f"/v1/partners/{_seg(id)}/payout-profile", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def put_partners_id_vat(self, id: str, body: PutPartnersIdVatBody, *, idempotency_key: Optional[str] = None) -> PutPartnersIdVatResponse:
        """Set a partner's VAT number. PUT /v1/partners/{id}/vat

        Sets (or clears with `null`) the partner's EU VAT number on their payout profile. With `viesCheck` on, VIES must list it as registered. 404 until the partner has payout details. Audited.

        **Auth:** an API key with `partners:write` (or `full`), or a session with role `owner`, `admin`, `finance`.
        """
        return self._request("PUT", f"/v1/partners/{_seg(id)}/vat", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def put_payout_connections_provider(self, provider: str, body: Union[PutPayoutConnectionsProviderBodyOption1, PutPayoutConnectionsProviderBodyOption2, PutPayoutConnectionsProviderBodyOption3, PutPayoutConnectionsProviderBodyOption4, PutPayoutConnectionsProviderBodyOption5, PutPayoutConnectionsProviderBodyOption6], *, idempotency_key: Optional[str] = None) -> PutPayoutConnectionsProviderResponse:
        """Connect a payout provider. PUT /v1/payout-connections/{provider}

        Connects (or replaces) your own account with a payout provider, so payouts move money from your account: `paypal` (`clientId`, `secret`), `stripe` (`secretKey`), `circle` (`apiKey`, `walletId`), `wise` (`apiToken`, `profileId`), `payoneer` (`clientId`, `secret`, `programId`) or `tremendous` (`apiKey`, `fundingSourceId`), each with `env`. Stored encrypted and never echoed. Live mode only (`409 test_mode_unsupported` in test mode). Audited.

        **Auth:** an API key with `payouts:write` (or `full`), or a session with role `owner`, `admin`, `finance`.
        """
        return self._request("PUT", f"/v1/payout-connections/{_seg(provider)}", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def put_profitability_products_product_ref(self, product_ref: str, body: PutProfitabilityProductsProductRefBody, *, idempotency_key: Optional[str] = None) -> GetProfitabilityProductsProductRefResponse:
        """Set a product margin. PUT /v1/profitability/products/{productRef}

        Sets a product's margin (`marginBps`) or unit cost (`unitCostMinor`, in `currency`, default the reporting currency); exactly one of the two. Audited.

        **Auth:** an API key with `analytics:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("PUT", f"/v1/profitability/products/{_seg(product_ref)}", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def put_profitability_settings(self, body: PutProfitabilitySettingsBody, *, idempotency_key: Optional[str] = None) -> GetProfitabilitySettingsResponse:
        """Update profitability settings. PUT /v1/profitability/settings

        Changes the org's economics settings, or with `programId` that program's overrides (a program can't override org-only fields such as the reporting currency). Returns the resolved settings. Re-run `POST /v1/profitability/rebuild` to apply changes to past figures. Audited.

        **Auth:** an API key with `analytics:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("PUT", f"/v1/profitability/settings", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def put_programs_id_autopricing(self, id: str, body: PutProgramsIdAutopricingBody, *, idempotency_key: Optional[str] = None) -> PutProgramsIdAutopricingResponse:
        """Configure autopricing. PUT /v1/programs/{id}/autopricing

        Self-pricing commissions: a target (`targetRoas`, or with `objective: "roi"` a `targetRoi`) and the `minBps`/`maxBps` band partner rates may move within. `enabled: false` turns it off.

        **Auth:** an API key with `programs:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("PUT", f"/v1/programs/{_seg(id)}/autopricing", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def put_programs_id_incrementality(self, id: str, body: PutProgramsIdIncrementalityBody, *, idempotency_key: Optional[str] = None) -> PutProgramsIdIncrementalityResponse:
        """Set the incrementality holdout. PUT /v1/programs/{id}/incrementality

        Holds out a random control share of referrals (`holdoutBps`, up to 5000 = 50%) from being commissioned, so comparing control and treatment conversion measures the true lift partners cause. 0 turns it off.

        **Auth:** an API key with `programs:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("PUT", f"/v1/programs/{_seg(id)}/incrementality", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def put_programs_id_negotiation_policy(self, id: str, body: PutProgramsIdNegotiationPolicyBody, *, idempotency_key: Optional[str] = None) -> PutProgramsIdNegotiationPolicyResponse:
        """Set the agent negotiation policy. PUT /v1/programs/{id}/negotiation-policy

        What an agent may negotiate to in this program: rates between `minBps` and `maxBps`, accepted automatically up to `autoAcceptMaxBps`. Requires `minBps <= autoAcceptMaxBps <= maxBps`. `enabled: false` closes the program to negotiation.

        **Auth:** an API key with `programs:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("PUT", f"/v1/programs/{_seg(id)}/negotiation-policy", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def put_programs_id_partners_partner_id_group(self, id: str, partner_id: str, body: PutProgramsIdPartnersPartnerIdGroupBody, *, idempotency_key: Optional[str] = None) -> PutProgramsIdPartnersPartnerIdGroupResponse:
        """Set a partner's group. PUT /v1/programs/{id}/partners/{partnerId}/group

        Puts an enrolled partner in one of the program's groups, or none (`groupId: null`). A partner is in at most one group per program.

        **Auth:** an API key with `programs:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("PUT", f"/v1/programs/{_seg(id)}/partners/{_seg(partner_id)}/group", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def put_programs_id_payout_schedule(self, id: str, body: PutProgramsIdPayoutScheduleBody, *, idempotency_key: Optional[str] = None) -> PutProgramsIdPayoutScheduleResponse:
        """Set a program's payout schedule. PUT /v1/programs/{id}/payout-schedule

        Overrides the org payout schedule for this program: a schedule, `{ "kind": "off" }` to never pay it automatically, or `null` to follow the org schedule again. Returns the next run date. Audited.

        **Auth:** an API key with `programs:write` (or `full`), or a session with role `owner`, `admin`, `finance`.
        """
        return self._request("PUT", f"/v1/programs/{_seg(id)}/payout-schedule", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    def put_programs_id_referee_reward(self, id: str, body: PutProgramsIdRefereeRewardBody, *, idempotency_key: Optional[str] = None) -> PutProgramsIdRefereeRewardResponse:
        """Set the referee reward. PUT /v1/programs/{id}/referee-reward

        What a referred customer gets: `store_credit`, a `coupon` or a `gift_card`, either a flat `amountMinor` or a percent (`bps`, optionally capped with `capMinor`) of their first payment, issued on their first commission or first payment. A percent reward needs `on: "first_payment"`. `enabled: false` removes it. Each reward issued publishes `referee_reward.earned`.

        **Auth:** an API key with `programs:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return self._request("PUT", f"/v1/programs/{_seg(id)}/referee-reward", query={}, body=body, idempotency_key=idempotency_key, kind="json")


class AsyncOperations:
    _request: Callable[..., Any]
    _paginate: Callable[..., Any]

    async def delete_api_keys_id(self, id: str, *, cascade: Optional[Literal["true", "false"]] = None, pair: Optional[Literal["true", "false"]] = None, idempotency_key: Optional[str] = None) -> DeleteApiKeysIdResponse:
        """Revoke an API key. DELETE /v1/api-keys/{id}

        Revokes a key at once. `cascade=true` also revokes every key it minted (and theirs); `pair=true` also revokes its live/test twin. Returns the revoked ids. Needs an owner or admin session, or an API key with the `admin` scope. Audited.

        **Auth:** an API key with `team:write` (or `full`), or a session of any role.

        cascade: true: also revoke every key this key minted, and theirs.
        pair: true: also revoke its live/test twin.
        """
        return await self._request("DELETE", f"/v1/api-keys/{_seg(id)}", query={"cascade": cascade, "pair": pair}, body=None, idempotency_key=idempotency_key, kind="json")

    async def delete_assets_id(self, id: str, *, idempotency_key: Optional[str] = None) -> Ok:
        """Delete a marketing asset. DELETE /v1/assets/{id}

        Removes a marketing asset.

        **Auth:** an API key with `partners:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("DELETE", f"/v1/assets/{_seg(id)}", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def delete_auth_connections_id(self, id: str, *, idempotency_key: Optional[str] = None) -> Ok:
        """Delete an auth connection. DELETE /v1/auth/connections/{id}

        Removes the connection; its webhook URL and signed endpoints stop accepting calls. Referrals it filed stay.

        **Auth:** an API key with `integrations:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("DELETE", f"/v1/auth/connections/{_seg(id)}", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def delete_billing_connections_id(self, id: str, *, idempotency_key: Optional[str] = None) -> Ok:
        """Delete a billing connection. DELETE /v1/billing/connections/{id}

        Deletes the connection: its secrets and credentials are wiped and its webhook URL stops accepting events. Recorded billing events stay. Audited.

        **Auth:** an API key with `billing:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("DELETE", f"/v1/billing/connections/{_seg(id)}", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def delete_branding_domain(self, *, idempotency_key: Optional[str] = None) -> Ok:
        """Remove the portal domain. DELETE /v1/branding/domain

        Stops serving the partner portal on the custom domain.

        **Auth:** an API key with `org:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("DELETE", f"/v1/branding/domain", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def delete_branding_link_domain(self, *, idempotency_key: Optional[str] = None) -> Ok:
        """Remove the link domain. DELETE /v1/branding/link-domain

        Stops using the custom link domain; links go back to the default host.

        **Auth:** an API key with `org:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("DELETE", f"/v1/branding/link-domain", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def delete_cli_listeners_id(self, id: str, *, idempotency_key: Optional[str] = None) -> Ok:
        """Close a CLI listener. DELETE /v1/cli/listeners/{id}

        Closes the listener; queued events are dropped.

        **Auth:** an API key with `webhooks:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("DELETE", f"/v1/cli/listeners/{_seg(id)}", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def delete_email_templates_event_locale(self, event: str, locale: str, *, idempotency_key: Optional[str] = None) -> DeleteEmailTemplatesEventLocaleResponse:
        """Reset an email template. DELETE /v1/email/templates/{event}/{locale}

        Removes the override; the default template is used again.

        **Auth:** an API key with `org:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("DELETE", f"/v1/email/templates/{_seg(event)}/{_seg(locale)}", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def delete_integrations_kind(self, kind: str, *, idempotency_key: Optional[str] = None) -> Ok:
        """Disconnect an integration. DELETE /v1/integrations/{kind}

        Removes the HubSpot or Segment connection and its stored credential.

        **Auth:** an API key with `integrations:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("DELETE", f"/v1/integrations/{_seg(kind)}", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def delete_org_members_user_id(self, user_id: str, *, idempotency_key: Optional[str] = None) -> Ok:
        """Remove a team member. DELETE /v1/org/members/{userId}

        Removes a member. Members can remove themselves; otherwise owner or admin. The last owner stays (409). Audited. Live mode only.

        **Auth:** an API key with `team:write` (or `full`), or a session of any role.
        """
        return await self._request("DELETE", f"/v1/org/members/{_seg(user_id)}", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def delete_partners_id(self, id: str, *, idempotency_key: Optional[str] = None) -> Ok:
        """Delete a partner. DELETE /v1/partners/{id}

        Deletes a partner that never did anything, with its enrollments, links, coupons and payout profile. A partner with any clicks, referrals, commissions, payouts or other history is `409`: archive it instead (`status: "archived"`). Audited.

        **Auth:** an API key with `partners:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("DELETE", f"/v1/partners/{_seg(id)}", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def delete_payout_connections_provider(self, provider: str, *, idempotency_key: Optional[str] = None) -> DeletePayoutConnectionsProviderResponse:
        """Disconnect a payout provider. DELETE /v1/payout-connections/{provider}

        Removes the stored credentials for a provider. Payouts by that method are then simulated until you reconnect. Audited.

        **Auth:** an API key with `payouts:write` (or `full`), or a session with role `owner`, `admin`, `finance`.
        """
        return await self._request("DELETE", f"/v1/payout-connections/{_seg(provider)}", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def delete_profitability_products_product_ref(self, product_ref: str, *, idempotency_key: Optional[str] = None) -> OkStatus:
        """Delete a product margin. DELETE /v1/profitability/products/{productRef}

        Removes a product from the margin catalog; its payments fall back to the program or org margin. Audited.

        **Auth:** an API key with `analytics:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("DELETE", f"/v1/profitability/products/{_seg(product_ref)}", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def delete_webhook_endpoints_id(self, id: str, *, idempotency_key: Optional[str] = None) -> Ok:
        """Delete a webhook endpoint. DELETE /v1/webhook-endpoints/{id}

        Removes the endpoint and its delivery history. Audited.

        **Auth:** an API key with `webhooks:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("DELETE", f"/v1/webhook-endpoints/{_seg(id)}", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def delete_zapier_hooks_id(self, id: str, *, idempotency_key: Optional[str] = None) -> Ok:
        """Unsubscribe a Zapier hook. DELETE /v1/zapier/hooks/{id}

        REST hook unsubscribe, called by Zapier when a Zap turns off.

        **Auth:** an API key with `integrations:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("DELETE", f"/v1/zapier/hooks/{_seg(id)}", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_admin_metrics(self, *, idempotency_key: Optional[str] = None) -> GetAdminMetricsResponse:
        """Get platform metrics. GET /v1/admin/metrics

        Platform admins only. Live orgs (and suspended ones), partner accounts (and banned ones), programs, commission earned, payouts sent and open fraud cases across the platform.

        **Auth:** a platform admin session.
        """
        return await self._request("GET", f"/v1/admin/metrics", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_admin_orgs(self, *, q: Optional[str] = None, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetAdminOrgsResponseDataItem]:
        """List organizations. GET /v1/admin/orgs

        Platform admins only. Organizations, searchable by name with `q`.

        **Auth:** a platform admin session.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/admin/orgs", query={"q": q, "limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_admin_orgs_iter(self, *, q: Optional[str] = None, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[GetAdminOrgsResponseDataItem]:
        """Every item of ``get_admin_orgs``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_admin_orgs(q=q, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_admin_partner_accounts(self, *, flagged: Optional[bool] = None, q: Optional[str] = None, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetAdminPartnerAccountsResponseDataItem]:
        """List partner accounts. GET /v1/admin/partner-accounts

        Platform admins only. Partner accounts with KYC and sanctions status, filtered by `flagged` (banned) and text `q`.

        **Auth:** a platform admin session.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/admin/partner-accounts", query={"flagged": flagged, "q": q, "limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_admin_partner_accounts_iter(self, *, flagged: Optional[bool] = None, q: Optional[str] = None, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[GetAdminPartnerAccountsResponseDataItem]:
        """Every item of ``get_admin_partner_accounts``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_admin_partner_accounts(flagged=flagged, q=q, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_agents(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetAgentsResponseDataItem]:
        """List partnered AI agents. GET /v1/agents

        The AI agents partnered with this org, with their wallet, metadata and how many recommendations each has attributed, most active first.

        **Auth:** an API key with `growth:read` (or `full`), or a session with role `owner`, `admin`, `analyst`.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/agents", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_agents_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[GetAgentsResponseDataItem]:
        """Every item of ``get_agents``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_agents(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_agents_recommendations(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetAgentsRecommendationsResponseDataItem]:
        """List agent recommendations. GET /v1/agents/recommendations

        Signed recommendations AI agents have attributed in this org, newest first.

        **Auth:** an API key with `growth:read` (or `full`), or a session with role `owner`, `admin`, `analyst`.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/agents/recommendations", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_agents_recommendations_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[GetAgentsRecommendationsResponseDataItem]:
        """Every item of ``get_agents_recommendations``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_agents_recommendations(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_analytics_by_channel(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetAnalyticsByChannelResponseDataItem]:
        """Get revenue by channel. GET /v1/analytics/by-channel

        Referrals and referred revenue by how they were matched (`coupon`, `deterministic` click, `email_hash`, `probabilistic`, `manual`…).

        **Auth:** an API key with `analytics:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/analytics/by-channel", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_analytics_by_channel_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[GetAnalyticsByChannelResponseDataItem]:
        """Every item of ``get_analytics_by_channel``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_analytics_by_channel(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_analytics_by_geo(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetAnalyticsByGeoResponseDataItem]:
        """Get revenue by country. GET /v1/analytics/by-geo

        Referrals and referred revenue by the country of the winning click, highest revenue first.

        **Auth:** an API key with `analytics:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/analytics/by-geo", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_analytics_by_geo_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[GetAnalyticsByGeoResponseDataItem]:
        """Every item of ``get_analytics_by_geo``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_analytics_by_geo(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_analytics_cohort_ltv(self, *, months: Optional[int] = None, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetAnalyticsCohortLtvResponseDataItem]:
        """Get cohort LTV. GET /v1/analytics/cohort-ltv

        Referred customers grouped by sign-up month over the last `months` (default 6), with net revenue (payments minus refunds) and revenue per customer.

        **Auth:** an API key with `analytics:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/analytics/cohort-ltv", query={"months": months, "limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_analytics_cohort_ltv_iter(self, *, months: Optional[int] = None, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[GetAnalyticsCohortLtvResponseDataItem]:
        """Every item of ``get_analytics_cohort_ltv``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_analytics_cohort_ltv(months=months, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_analytics_coupon_performance(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetAnalyticsCouponPerformanceResponseDataItem]:
        """Get coupon performance. GET /v1/analytics/coupon-performance

        Referrals and revenue per coupon code, highest revenue first.

        **Auth:** an API key with `analytics:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/analytics/coupon-performance", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_analytics_coupon_performance_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[GetAnalyticsCouponPerformanceResponseDataItem]:
        """Every item of ``get_analytics_coupon_performance``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_analytics_coupon_performance(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_analytics_overview(self, *, program_id: Optional[str] = None, days: Optional[int] = None, idempotency_key: Optional[str] = None) -> GetAnalyticsOverviewResponse:
        """Get the funnel overview. GET /v1/analytics/overview

        Over the last `days` (default 30), optionally for one program: clicks (and how many were filtered), visitors, sign-ups, payments, referred revenue, commission earned and reversed, active partners and the click-to-sign-up and sign-up-to-paid rates.

        **Auth:** an API key with `analytics:read` (or `full`), or a session of any role.
        """
        return await self._request("GET", f"/v1/analytics/overview", query={"programId": program_id, "days": days}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_analytics_timeseries(self, *, metric: Literal["clicks", "signups", "revenue"], days: Optional[int] = None, program_id: Optional[str] = None, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetAnalyticsTimeseriesResponseDataItem]:
        """Get a daily time series. GET /v1/analytics/timeseries

        One `metric` (`clicks`, `signups` or `revenue` in minor units) per day over the last `days`, optionally for one program.

        **Auth:** an API key with `analytics:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/analytics/timeseries", query={"metric": metric, "days": days, "programId": program_id, "limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_analytics_timeseries_iter(self, *, metric: Literal["clicks", "signups", "revenue"], days: Optional[int] = None, program_id: Optional[str] = None, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[GetAnalyticsTimeseriesResponseDataItem]:
        """Every item of ``get_analytics_timeseries``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_analytics_timeseries(metric=metric, days=days, program_id=program_id, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_api_keys(self, *, mode: Optional[Literal["live", "test"]] = None, owner: Optional[str] = None, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[ApiKey]:
        """List API keys. GET /v1/api-keys

        Every key of the org, live and test (a test-mode caller sees test keys only), oldest first, with scopes, pinned version, owner, expiry and last use. Never returns the secret. Filter by `mode` or `owner`.

        **Auth:** an API key with `team:read` (or `full`), or a session of any role.

        mode: Only live or only test keys; default both.
        owner: Only keys with this owner.
        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/api-keys", query={"mode": mode, "owner": owner, "limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_api_keys_iter(self, *, mode: Optional[Literal["live", "test"]] = None, owner: Optional[str] = None, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[ApiKey]:
        """Every item of ``get_api_keys``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_api_keys(mode=mode, owner=owner, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_api_keys_id(self, id: str, *, idempotency_key: Optional[str] = None) -> ApiKey:
        """Get an API key. GET /v1/api-keys/{id}

        One key of the org, without its secret.

        **Auth:** an API key with `team:read` (or `full`), or a session of any role.
        """
        return await self._request("GET", f"/v1/api-keys/{_seg(id)}", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_assets(self, *, program_id: Optional[str] = None, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetAssetsResponseDataItem]:
        """List marketing assets. GET /v1/assets

        Marketing assets, filtered by `programId`.

        **Auth:** an API key with `partners:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/assets", query={"programId": program_id, "limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_assets_iter(self, *, program_id: Optional[str] = None, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[GetAssetsResponseDataItem]:
        """Every item of ``get_assets``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_assets(program_id=program_id, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_assistant_suggestions(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetAssistantSuggestionsResponseDataItem]:
        """Get program suggestions. GET /v1/assistant/suggestions

        Draft-only suggestions for running the program, each with a suggested action for a person to take: partners who never drove a click, links with clicks but no referrals, programs without a commission rule, the review queue, and credit ROI findings. It never changes anything.

        **Auth:** an API key with `analytics:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/assistant/suggestions", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_assistant_suggestions_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[GetAssistantSuggestionsResponseDataItem]:
        """Every item of ``get_assistant_suggestions``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_assistant_suggestions(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_audit_logs(self, *, actor: Optional[str] = None, actor_type: Optional[str] = None, action: Optional[str] = None, subject_type: Optional[str] = None, subject_id: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[AuditLogEntry]:
        """List audit log entries. GET /v1/audit-logs

        Every change recorded in the org, newest first: who did it (`actor`, `actorType`), what (`action`; a trailing `*` matches a prefix such as `payout.*`) and to what (`subjectType`, `subjectId`). Filter by any of those and by `created[gte]`/`created[lte]`.

        **Auth:** an API key with `audit:read` (or `full`), or a session with role `owner`, `admin`.

        actor: Actor id: a user, API key or connection id.
        action: Exact action, or a prefix ending in * (e.g. payout.*).
        starting_after: An entry id: return the entries after it.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/audit-logs", query={"actor": actor, "actorType": actor_type, "action": action, "subjectType": subject_type, "subjectId": subject_id, "created[gte]": created_gte, "created[lte]": created_lte, "limit": limit, "starting_after": starting_after, "ending_before": ending_before}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_audit_logs_iter(self, *, actor: Optional[str] = None, actor_type: Optional[str] = None, action: Optional[str] = None, subject_type: Optional[str] = None, subject_id: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, limit: Optional[int] = None, ending_before: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[AuditLogEntry]:
        """Every item of ``get_audit_logs``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_audit_logs(actor=actor, actor_type=actor_type, action=action, subject_type=subject_type, subject_id=subject_id, created_gte=created_gte, created_lte=created_lte, limit=limit, ending_before=ending_before, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_auth_connections(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[AuthConnection]:
        """List auth connections. GET /v1/auth/connections

        Auth-platform connections with provider, program, status, signature version and rotation state. Secrets are never returned.

        **Auth:** an API key with `integrations:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/auth/connections", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_auth_connections_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[AuthConnection]:
        """Every item of ``get_auth_connections``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_auth_connections(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_auth_connections_id_export(self, id: str, *, customer_ref: str, idempotency_key: Optional[str] = None) -> GetAuthConnectionsIdExportResponse:
        """Export a user (signed protocol). GET /v1/auth/connections/{id}/export

        An access request the platform forwards: everything filed under the customer and their partner record. Signed with the connection secret in `x-referalli-signature: t=<unix>,v1=…,v2=…` (v2 also signs the request line; once a connection has seen v2 it requires it), with a unique `x-referalli-id` per call. Calls older than 5 minutes, reused ids (`409 replay`), paused connections (`423 connection_paused`) and unknown fields (`422`) are refused.

        **Auth:** a signature (see above); no API key.
        """
        return await self._request("GET", f"/v1/auth/connections/{_seg(id)}/export", query={"customerRef": customer_ref}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_auth_providers(self, *, idempotency_key: Optional[str] = None) -> GetAuthProvidersResponse:
        """List sign-in providers. GET /v1/auth/providers

        The identity providers configured on this deployment, for rendering sign-in buttons.

        **Auth:** none.
        """
        return await self._request("GET", f"/v1/auth/providers", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_billing_connections(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[BillingConnection]:
        """List billing connections. GET /v1/billing/connections

        Billing connections (deleted ones excluded), with status, whether credentials are needed and set, the value mapping and secret-rotation state.

        **Auth:** an API key with `billing:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/billing/connections", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_billing_connections_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[BillingConnection]:
        """Every item of ``get_billing_connections``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_billing_connections(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_billing_connections_id(self, id: str, *, idempotency_key: Optional[str] = None) -> BillingConnection:
        """Get a billing connection. GET /v1/billing/connections/{id}

        One billing connection, without its secrets.

        **Auth:** an API key with `billing:read` (or `full`), or a session of any role.
        """
        return await self._request("GET", f"/v1/billing/connections/{_seg(id)}", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_billing_events(self, *, customer_ref: Optional[str] = None, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[BillingEvent]:
        """List billing events. GET /v1/billing/events

        Payments, refunds and other billing events received from every connection, newest first. Filter with `customerRef`.

        **Auth:** an API key with `billing:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/billing/events", query={"customerRef": customer_ref, "limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_billing_events_iter(self, *, customer_ref: Optional[str] = None, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[BillingEvent]:
        """Every item of ``get_billing_events``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_billing_events(customer_ref=customer_ref, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_billing_plan(self, *, idempotency_key: Optional[str] = None) -> GetBillingPlanResponse:
        """Get the plan. GET /v1/billing/plan

        The org's Referalli plan and status, its limits and current usage (programs, partners), the plan catalog, whether there is a subscription to manage and whether this caller may activate a plan without checkout.

        **Auth:** an API key with `billing:read` (or `full`), or a session of any role.
        """
        return await self._request("GET", f"/v1/billing/plan", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_branding(self, *, idempotency_key: Optional[str] = None) -> GetBrandingResponse:
        """Get branding. GET /v1/branding

        The org's logo, theme tokens, sender address, and its custom portal and link domains with their status (`none`, `pending` DNS, `provisioning` a certificate, `active`).

        **Auth:** an API key with `org:read` (or `full`), or a session of any role.
        """
        return await self._request("GET", f"/v1/branding", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_cleanroom_consent(self, *, customer_ref: str, idempotency_key: Optional[str] = None) -> GetCleanroomConsentResponse:
        """Get a customer's consent. GET /v1/cleanroom/consent

        A customer's recorded consent: whether granted, its purposes, the attributes they declared and when it changed. `consent: null` when none is recorded.

        **Auth:** an API key with `growth:read` (or `full`), or a session of any role.
        """
        return await self._request("GET", f"/v1/cleanroom/consent", query={"customerRef": customer_ref}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_cleanroom_query(self, *, dimension: str, idempotency_key: Optional[str] = None) -> GetCleanroomQueryResponse:
        """Query the clean room. GET /v1/cleanroom/query

        Aggregates over consenting customers only, grouped by a zero-party attribute they declared (`dimension`): customers, converted customers and referred revenue per value. Cohorts smaller than 5 are suppressed (k-anonymity); individual rows never leave.

        **Auth:** an API key with `growth:read` (or `full`), or a session of any role.
        """
        return await self._request("GET", f"/v1/cleanroom/query", query={"dimension": dimension}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_cli_device_codes_user_code(self, user_code: str, *, idempotency_key: Optional[str] = None) -> GetCliDeviceCodesUserCodeResponse:
        """Get a pending CLI sign-in. GET /v1/cli/device-codes/{userCode}

        For the approval page: the pending code, which CLI asked and when it expires. Needs a signed-in person (owner or admin). 404 when expired or used.

        **Auth:** an API key with `team:read` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("GET", f"/v1/cli/device-codes/{_seg(user_code)}", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_cli_listeners_id_events(self, id: str, *, wait: Optional[int] = None, idempotency_key: Optional[str] = None) -> GetCliListenersIdEventsResponse:
        """Receive listener events. GET /v1/cli/listeners/{id}/events

        Up to 50 queued events for the listener, oldest first, each with its body and signed headers. `wait` long-polls up to 25 seconds for the first event. Polling keeps the listener alive.

        **Auth:** an API key with `webhooks:read` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("GET", f"/v1/cli/listeners/{_seg(id)}/events", query={"wait": wait}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_cli_logs(self, *, after: Optional[int] = None, wait: Optional[int] = None, limit: Optional[int] = None, idempotency_key: Optional[str] = None) -> GetCliLogsResponse:
        """Tail the request log. GET /v1/cli/logs

        The CLI's `logs tail` command: the org's recent API requests (method, path without query string, status, latency, actor). The first call returns the latest 20 and a `cursor`; pass it as `after` (with `wait` to long-poll up to 25 seconds) for newer entries. Kept for a day.

        **Auth:** an API key with `audit:read` (or `full`), or a session with role `owner`, `admin`.

        after: Return entries after this cursor.
        """
        return await self._request("GET", f"/v1/cli/logs", query={"after": after, "wait": wait, "limit": limit}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_cli_topics(self, *, idempotency_key: Optional[str] = None) -> GetCliTopicsResponse:
        """List triggerable topics. GET /v1/cli/topics

        The event topics `POST /v1/cli/trigger` can send.

        **Auth:** an API key with `webhooks:read` (or `full`), or a session of any role.
        """
        return await self._request("GET", f"/v1/cli/topics", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_commission_rules(self, *, program_id: Optional[str] = None, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[CommissionRule]:
        """List commission rules. GET /v1/commission-rules

        Every rule version, by program and newest version first. Filter with `programId`.

        **Auth:** an API key with `commissions:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/commission-rules", query={"programId": program_id, "limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_commission_rules_iter(self, *, program_id: Optional[str] = None, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[CommissionRule]:
        """Every item of ``get_commission_rules``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_commission_rules(program_id=program_id, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_commissions(self, *, partner_id: Optional[str] = None, program_id: Optional[str] = None, type_: Optional[Literal["earned", "adjusted", "reversed", "approved", "paid"]] = None, referral_id: Optional[str] = None, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[CommissionEvent]:
        """List commission ledger events. GET /v1/commissions

        The append-only commission ledger, newest first: `earned` lines and the `approved`, `paid`, `reversed` and `adjusted` events recorded against them (`relatedCommissionId`). Filter by `partnerId`, `programId`, `type` or `referralId`.

        **Auth:** an API key with `commissions:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/commissions", query={"partnerId": partner_id, "programId": program_id, "type": type_, "referralId": referral_id, "limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_commissions_iter(self, *, partner_id: Optional[str] = None, program_id: Optional[str] = None, type_: Optional[Literal["earned", "adjusted", "reversed", "approved", "paid"]] = None, referral_id: Optional[str] = None, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[CommissionEvent]:
        """Every item of ``get_commissions``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_commissions(partner_id=partner_id, program_id=program_id, type_=type_, referral_id=referral_id, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_commissions_id(self, id: str, *, idempotency_key: Optional[str] = None) -> CommissionLine:
        """Get a commission. GET /v1/commissions/{id}

        One ledger event. An `earned` line also carries its billing event, its net after reversals and adjustments, its state (`pending`, `approved` or `paid`) and every event recorded against it.

        **Auth:** an API key with `commissions:read` (or `full`), or a session of any role.
        """
        return await self._request("GET", f"/v1/commissions/{_seg(id)}", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_contracts(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetContractsResponseDataItem]:
        """List partner contracts. GET /v1/contracts

        The org's contracts and their status (`draft`, `sent`, `accepted`, `declined`, `void`).

        **Auth:** an API key with `partners:read` (or `full`), or a session with role `owner`, `admin`.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/contracts", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_contracts_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[GetContractsResponseDataItem]:
        """Every item of ``get_contracts``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_contracts(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_coupons(self, *, program_id: Optional[str] = None, partner_id: Optional[str] = None, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[Coupon]:
        """List coupon codes. GET /v1/coupons

        Coupon codes, filtered by `programId` and/or `partnerId`.

        **Auth:** an API key with `links:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/coupons", query={"programId": program_id, "partnerId": partner_id, "limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_coupons_iter(self, *, program_id: Optional[str] = None, partner_id: Optional[str] = None, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[Coupon]:
        """Every item of ``get_coupons``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_coupons(program_id=program_id, partner_id=partner_id, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_creators(self, *, q: Optional[str] = None, category: Optional[str] = None, channel: Optional[str] = None, min_audience: Optional[int] = None, min_engagement_bps: Optional[int] = None, audience_country: Optional[str] = None, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[CreatorProfile]:
        """Search creators. GET /v1/creators

        Published creator profiles, most engaged first, filtered by text (`q`), `category`, `channel`, minimum audience, minimum engagement and audience country. Each carries verified stats and whether this org already invited them. Emails are never returned.

        **Auth:** an API key with `growth:read` (or `full`), or a session with role `owner`, `admin`.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/creators", query={"q": q, "category": category, "channel": channel, "minAudience": min_audience, "minEngagementBps": min_engagement_bps, "audienceCountry": audience_country, "limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_creators_iter(self, *, q: Optional[str] = None, category: Optional[str] = None, channel: Optional[str] = None, min_audience: Optional[int] = None, min_engagement_bps: Optional[int] = None, audience_country: Optional[str] = None, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[CreatorProfile]:
        """Every item of ``get_creators``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_creators(q=q, category=category, channel=channel, min_audience=min_audience, min_engagement_bps=min_engagement_bps, audience_country=audience_country, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_creators_account_id(self, account_id: str, *, idempotency_key: Optional[str] = None) -> CreatorProfile:
        """Get a creator. GET /v1/creators/{accountId}

        One published creator profile with verified stats. 404 when not listed.

        **Auth:** an API key with `growth:read` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("GET", f"/v1/creators/{_seg(account_id)}", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_deals(self, *, status: Optional[Literal["submitted", "approved", "rejected", "won", "lost"]] = None, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetDealsResponseDataItem]:
        """List registered deals. GET /v1/deals

        Deals partners registered, newest first. Filter with `status` (`submitted`, `approved`, `rejected`, `won`, `lost`).

        **Auth:** an API key with `growth:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/deals", query={"status": status, "limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_deals_iter(self, *, status: Optional[Literal["submitted", "approved", "rejected", "won", "lost"]] = None, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[GetDealsResponseDataItem]:
        """Every item of ``get_deals``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_deals(status=status, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_disputes(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetDisputesResponseDataItem]:
        """List partner disputes. GET /v1/disputes

        Disputes partners filed with this org, newest first.

        **Auth:** an API key with `commissions:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/disputes", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_disputes_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[GetDisputesResponseDataItem]:
        """Every item of ``get_disputes``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_disputes(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_email_settings(self, *, idempotency_key: Optional[str] = None) -> EmailSettings:
        """Get email settings. GET /v1/email/settings

        The org's own email provider (`resend`, `brevo` or `postmark`), sender identity, branding and sending-domain status. The API key is never returned.

        **Auth:** an API key with `org:read` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("GET", f"/v1/email/settings", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_email_templates(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[EmailTemplateEvent]:
        """List email templates. GET /v1/email/templates

        Every email event with its placeholders and, per locale, the default template and the org's override if any.

        **Auth:** an API key with `org:read` (or `full`), or a session with role `owner`, `admin`.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/email/templates", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_email_templates_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[EmailTemplateEvent]:
        """Every item of ``get_email_templates``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_email_templates(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_embed_summary(self, *, idempotency_key: Optional[str] = None) -> GetEmbedSummaryResponse:
        """Read embedded partner stats. GET /v1/embed/summary

        Called by the embed component with `Authorization: Bearer <embed token>`: the partner's name, eligible clicks, active referrals, balances and link codes. 401 for a missing, invalid or expired token.

        **Auth:** none.
        """
        return await self._request("GET", f"/v1/embed/summary", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_export_accounting(self, *, format_: Optional[Literal["quickbooks", "xero"]] = None, year: int, idempotency_key: Optional[str] = None) -> str:
        """Export payouts for accounting. GET /v1/export/accounting

        A year's sent payouts as a CSV that QuickBooks (`format=quickbooks`, the default) or Xero imports.

        **Auth:** an API key with `payouts:read` (or `full`), or a session with role `owner`, `admin`, `finance`.
        """
        return await self._request("GET", f"/v1/export/accounting", query={"format": format_, "year": year}, body=None, idempotency_key=idempotency_key, kind="text")

    async def get_export_full(self, *, idempotency_key: Optional[str] = None) -> str:
        """Export all org data. GET /v1/export/full

        Every tenant table of the org as NDJSON (one JSON object per line, tagged with its table), streamed so any size works. Owner or admin.

        **Auth:** an API key with `analytics:read` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("GET", f"/v1/export/full", query={}, body=None, idempotency_key=idempotency_key, kind="text")

    async def get_fraud_cases(self, *, status: Optional[Literal["open", "dismissed", "actioned"]] = None, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[FraudCase]:
        """List fraud cases. GET /v1/fraud/cases

        The fraud case queue (self-referrals, quality, rings, value patterns, identity risk), newest first, with the evidence. Filter with `status`.

        **Auth:** an API key with `fraud:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/fraud/cases", query={"status": status, "limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_fraud_cases_iter(self, *, status: Optional[Literal["open", "dismissed", "actioned"]] = None, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[FraudCase]:
        """Every item of ``get_fraud_cases``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_fraud_cases(status=status, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_fx_rates(self, *, base: Optional[str] = None, quote: Optional[str] = None, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[FxRate]:
        """List FX rates. GET /v1/fx-rates

        The org's rates first, then the platform fallback, newest per pair first. A payout uses the org's latest rate at or before the run, else the platform's. Filter by `base` and `quote`.

        **Auth:** an API key with `payouts:read` (or `full`), or a session with role `owner`, `admin`, `finance`.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/fx-rates", query={"base": base, "quote": quote, "limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_fx_rates_iter(self, *, base: Optional[str] = None, quote: Optional[str] = None, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[FxRate]:
        """Every item of ``get_fx_rates``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_fx_rates(base=base, quote=quote, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_graphql(self, *, idempotency_key: Optional[str] = None) -> GetGraphqlResponse:
        """Query the GraphQL read layer. GET /v1/graphql

        A read-only GraphQL endpoint over the same org-scoped data as REST (programs, partners, referrals, analytics), with the same authentication. Mutations stay in REST.

        **Auth:** an API key with `analytics:read` (or `full`), or a session of any role.
        """
        return await self._request("GET", f"/v1/graphql", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_health(self, *, idempotency_key: Optional[str] = None) -> Ok:
        """Check API health. GET /v1/health

        `200 { "ok": true }` when this instance can serve requests: both database pools answer and it is not shutting down. Otherwise `503` with `reason` (`shutting_down`, with `Retry-After`, or `database_unreachable`).

        **Auth:** none.
        """
        return await self._request("GET", f"/v1/health", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_hosts_current(self, *, idempotency_key: Optional[str] = None) -> GetHostsCurrentResponse:
        """Describe the current host. GET /v1/hosts/current

        What the request's host is: a merchant's verified portal domain (with the org's name, branding and public programs), a merchant link domain, or Referalli's own app. Used by the web app before anyone signs in.

        **Auth:** none.
        """
        return await self._request("GET", f"/v1/hosts/current", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_hosts_current_theme_css(self, *, idempotency_key: Optional[str] = None) -> str:
        """Get the current host's theme stylesheet. GET /v1/hosts/current/theme.css

        On a merchant's portal domain, the org's theme tokens as a `:root` stylesheet; empty elsewhere.

        **Auth:** none.
        """
        return await self._request("GET", f"/v1/hosts/current/theme.css", query={}, body=None, idempotency_key=idempotency_key, kind="text")

    async def get_incrementality(self, *, program_id: str, idempotency_key: Optional[str] = None) -> GetIncrementalityResponse:
        """Get incrementality results. GET /v1/incrementality

        For a program's active referrals: treatment and control counts, conversion rates and lift, overall and per partner.

        **Auth:** an API key with `analytics:read` (or `full`), or a session of any role.
        """
        return await self._request("GET", f"/v1/incrementality", query={"programId": program_id}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_integrations(self, *, idempotency_key: Optional[str] = None) -> GetIntegrationsResponse:
        """List integrations. GET /v1/integrations

        The HubSpot and Segment connections with status, settings and the last test result. Credentials are never returned.

        **Auth:** an API key with `integrations:read` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("GET", f"/v1/integrations", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_integrations_deliveries(self, *, kind: Optional[Literal["zapier", "hubspot", "segment"]] = None, status: Optional[Literal["pending", "sent", "failed", "skipped"]] = None, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[IntegrationDelivery]:
        """List integration deliveries. GET /v1/integrations/deliveries

        What was sent to Zapier, HubSpot and Segment, newest first, filtered by `kind` and `status`.

        **Auth:** an API key with `integrations:read` (or `full`), or a session with role `owner`, `admin`.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/integrations/deliveries", query={"kind": kind, "status": status, "limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_integrations_deliveries_iter(self, *, kind: Optional[Literal["zapier", "hubspot", "segment"]] = None, status: Optional[Literal["pending", "sent", "failed", "skipped"]] = None, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[IntegrationDelivery]:
        """Every item of ``get_integrations_deliveries``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_integrations_deliveries(kind=kind, status=status, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_invitations(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetInvitationsResponseDataItem]:
        """List creator invitations. GET /v1/invitations

        The org's creator invitations and their status (`pending`, `accepted`, `declined`, `withdrawn`).

        **Auth:** an API key with `partners:read` (or `full`), or a session with role `owner`, `admin`.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/invitations", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_invitations_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[GetInvitationsResponseDataItem]:
        """Every item of ``get_invitations``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_invitations(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_links(self, *, program_id: Optional[str] = None, partner_id: Optional[str] = None, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[Link]:
        """List links. GET /v1/links

        Tracked links with their short URL and click count, filtered by `programId` and/or `partnerId`.

        **Auth:** an API key with `links:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/links", query={"programId": program_id, "partnerId": partner_id, "limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_links_iter(self, *, program_id: Optional[str] = None, partner_id: Optional[str] = None, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[Link]:
        """Every item of ``get_links``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_links(program_id=program_id, partner_id=partner_id, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_links_id_qr(self, id: str, *, idempotency_key: Optional[str] = None) -> str:
        """Get a link's QR code. GET /v1/links/{id}/qr

        An SVG QR code for the link's short URL.

        **Auth:** an API key with `links:read` (or `full`), or a session of any role.
        """
        return await self._request("GET", f"/v1/links/{_seg(id)}/qr", query={}, body=None, idempotency_key=idempotency_key, kind="text")

    async def get_marketplace_listing(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetMarketplaceListingResponseDataItem]:
        """List the org's marketplace listings. GET /v1/marketplace/listing

        The org's listings with their platform-computed stats: eligible clicks, active referrals, earnings per click, conversion rate, payout reliability and approval latency.

        **Auth:** an API key with `growth:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/marketplace/listing", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_marketplace_listing_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[GetMarketplaceListingResponseDataItem]:
        """Every item of ``get_marketplace_listing``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_marketplace_listing(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_me(self, *, idempotency_key: Optional[str] = None) -> GetMeResponse:
        """Get the current caller. GET /v1/me

        Who is calling. With a user session: the user and their org memberships (no `x-org-id` needed). With an API key: the key (name, prefix, scopes, pinned version, mode, owner, expiry) and its org.

        **Auth:** an API key with `team:read` (or `full`), or a session of any role.
        """
        return await self._request("GET", f"/v1/me", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_negotiations(self, *, program_id: Optional[str] = None, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetNegotiationsResponseDataItem]:
        """List negotiation rounds. GET /v1/negotiations

        Agent negotiation rounds and their decisions, newest first, optionally for one program.

        **Auth:** an API key with `growth:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/negotiations", query={"programId": program_id, "limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_negotiations_iter(self, *, program_id: Optional[str] = None, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[GetNegotiationsResponseDataItem]:
        """Every item of ``get_negotiations``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_negotiations(program_id=program_id, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_network_journey(self, *, email_hash: str, model: Optional[Literal["linear", "first", "last", "time_decay"]] = None, idempotency_key: Optional[str] = None) -> GetNetworkJourneyResponse:
        """Get a customer's network journey. GET /v1/network/journey

        For a hashed customer email, the partner accounts that touched them at any opted-in merchant (never which merchant) and each one's credit under `model`. 403 unless the org has joined the network.

        **Auth:** an API key with `growth:read` (or `full`), or a session of any role.
        """
        return await self._request("GET", f"/v1/network/journey", query={"emailHash": email_hash, "model": model}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_network_settings(self, *, idempotency_key: Optional[str] = None) -> GetNetworkSettingsResponse:
        """Get network membership. GET /v1/network/settings

        Whether the org contributes to (and can read) the attribution network.

        **Auth:** an API key with `growth:read` (or `full`), or a session of any role.
        """
        return await self._request("GET", f"/v1/network/settings", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_notifications(self, *, unread: Optional[Literal["true", "false"]] = None, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[Notification]:
        """List notifications. GET /v1/notifications

        The org's in-app notifications (failing webhooks, anomalies, answered invitations…), newest first. `unread=true` for unread only.

        **Auth:** an API key with `org:read` (or `full`), or a session of any role.

        unread: true: unread notifications only.
        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/notifications", query={"unread": unread, "limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_notifications_iter(self, *, unread: Optional[Literal["true", "false"]] = None, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[Notification]:
        """Every item of ``get_notifications``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_notifications(unread=unread, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_onchain_connections(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetOnchainConnectionsResponseDataItem]:
        """List on-chain connections. GET /v1/onchain/connections

        The org's on-chain conversion connections.

        **Auth:** an API key with `billing:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/onchain/connections", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_onchain_connections_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[GetOnchainConnectionsResponseDataItem]:
        """Every item of ``get_onchain_connections``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_onchain_connections(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_openapi_json(self, *, idempotency_key: Optional[str] = None) -> GetOpenapiJsonResponse:
        """Get the OpenAPI document. GET /v1/openapi.json

        This reference as an OpenAPI 3.1 document (JSON).

        **Auth:** none.
        """
        return await self._request("GET", f"/v1/openapi.json", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_openapi_yaml(self, *, idempotency_key: Optional[str] = None) -> str:
        """Get the OpenAPI document as YAML. GET /v1/openapi.yaml

        The same OpenAPI 3.1 document as `GET /v1/openapi.json`, serialized as YAML.

        **Auth:** none.
        """
        return await self._request("GET", f"/v1/openapi.yaml", query={}, body=None, idempotency_key=idempotency_key, kind="text")

    async def get_org(self, *, idempotency_key: Optional[str] = None) -> Org:
        """Get the organization. GET /v1/org

        The current org: name, plan, settings, public `trackingToken`, payout KYC requirement and mode (`livemode`; test orgs also carry `liveOrgId`).

        **Auth:** an API key with `org:read` (or `full`), or a session of any role.
        """
        return await self._request("GET", f"/v1/org", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_org_fx_feed(self, *, idempotency_key: Optional[str] = None) -> GetOrgFxFeedResponse:
        """Get the FX feed setting. GET /v1/org/fx-feed

        Whether the daily ECB reference-rate feed is on for this org, and the date of its latest rate.

        **Auth:** an API key with `org:read` (or `full`), or a session with role `owner`, `admin`, `finance`.
        """
        return await self._request("GET", f"/v1/org/fx-feed", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_org_members(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[Member]:
        """List team members. GET /v1/org/members

        Members of the org with their role and email, oldest first.

        **Auth:** an API key with `team:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/org/members", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_org_members_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[Member]:
        """Every item of ``get_org_members``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_org_members(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_org_payout_schedule(self, *, idempotency_key: Optional[str] = None) -> GetOrgPayoutScheduleResponse:
        """Get payout schedules. GET /v1/org/payout-schedule

        The org schedule and its next run date, plus each program's override (`{ kind: 'off' }`, its own schedule, or `null` to follow the org) and next run date.

        **Auth:** an API key with `payouts:read` (or `full`), or a session of any role.
        """
        return await self._request("GET", f"/v1/org/payout-schedule", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_org_referral_params(self, *, idempotency_key: Optional[str] = None) -> GetOrgReferralParamsResponse:
        """Get referral query parameters. GET /v1/org/referral-params

        The query parameters aff.js reads a referral code from: the built-in ones (`via`, `ref`, `aff`) and the org's extra ones.

        **Auth:** an API key with `org:read` (or `full`), or a session of any role.
        """
        return await self._request("GET", f"/v1/org/referral-params", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_org_retention(self, *, idempotency_key: Optional[str] = None) -> Retention:
        """Get the data retention policy. GET /v1/org/retention

        How many days each kind of raw data is kept before the nightly purge, the allowed minimum and default per kind, and the last purge run.

        **Auth:** an API key with `org:read` (or `full`), or a session of any role.
        """
        return await self._request("GET", f"/v1/org/retention", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_org_sso(self, *, idempotency_key: Optional[str] = None) -> GetOrgSsoResponse:
        """Get SSO settings. GET /v1/org/sso

        Single sign-on for the org: whether SSO is configured on this deployment and linked to a directory tenant, its connections and domains, whether SSO is required, the role mapping, recent setup tickets and any provider error.

        **Auth:** an API key with `org:read` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("GET", f"/v1/org/sso", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_org_sso_connections_id_saml_metadata(self, id: str, *, idempotency_key: Optional[str] = None) -> GetOrgSsoConnectionsIdSamlMetadataResponse:
        """Get SAML metadata. GET /v1/org/sso/connections/{id}/saml-metadata

        The SAML service-provider metadata for one of the org's SSO connections, to give the identity provider.

        **Auth:** an API key with `org:read` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("GET", f"/v1/org/sso/connections/{_seg(id)}/saml-metadata", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_org_tax_profile(self, *, idempotency_key: Optional[str] = None) -> TaxProfile:
        """Get the tax profile. GET /v1/org/tax-profile

        The org's legal name, address, country, VAT id, EIN, domestic VAT rate, whether partner VAT ids are checked against EU VIES, and the 1099 filing provider.

        **Auth:** an API key with `org:read` (or `full`), or a session with role `owner`, `admin`, `finance`.
        """
        return await self._request("GET", f"/v1/org/tax-profile", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_outreach(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetOutreachResponseDataItem]:
        """List outreach messages. GET /v1/outreach

        Drafted, approved and sent outreach messages, newest first.

        **Auth:** an API key with `growth:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/outreach", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_outreach_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[GetOutreachResponseDataItem]:
        """Every item of ``get_outreach``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_outreach(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_partner_achievements(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetPartnerAchievementsResponseDataItem]:
        """List my achievements. GET /v1/partner/achievements

        Badges computed from the ledger (first click, referral milestones, first payout, $1,000 earned), each with progress toward its target.

        **Auth:** a partner session.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/partner/achievements", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_partner_achievements_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[GetPartnerAchievementsResponseDataItem]:
        """Every item of ``get_partner_achievements``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_partner_achievements(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_partner_advance(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetPartnerAdvanceResponseDataItem]:
        """List my advances. GET /v1/partner/advance

        The partner's advances with what remains to repay.

        **Auth:** a partner session.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/partner/advance", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_partner_advance_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[GetPartnerAdvanceResponseDataItem]:
        """Every item of ``get_partner_advance``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_partner_advance(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_partner_advance_offer(self, *, idempotency_key: Optional[str] = None) -> GetPartnerAdvanceOfferResponse:
        """Get my advance offer. GET /v1/partner/advance/offer

        How much the partner could receive now against future commissions (`maxAdvanceMinor`), from their recent run rate and quality score, and the fee.

        **Auth:** a partner session.
        """
        return await self._request("GET", f"/v1/partner/advance/offer", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_partner_assets(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetPartnerAssetsResponseDataItem]:
        """List marketing assets. GET /v1/partner/assets

        Marketing assets (copy, images, banners) of the programs the partner is approved in; group-only assets show only to that group's members.

        **Auth:** a partner session.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/partner/assets", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_partner_assets_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[GetPartnerAssetsResponseDataItem]:
        """Every item of ``get_partner_assets``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_partner_assets(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_partner_contracts(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetPartnerContractsResponseDataItem]:
        """List my contracts. GET /v1/partner/contracts

        Contracts merchants sent the partner.

        **Auth:** a partner session.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/partner/contracts", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_partner_contracts_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[GetPartnerContractsResponseDataItem]:
        """Every item of ``get_partner_contracts``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_partner_contracts(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_partner_deals(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetPartnerDealsResponseDataItem]:
        """List my deals. GET /v1/partner/deals

        The partner's registered deals across merchants, newest first.

        **Auth:** a partner session.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/partner/deals", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_partner_deals_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[GetPartnerDealsResponseDataItem]:
        """Every item of ``get_partner_deals``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_partner_deals(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_partner_disputes(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetPartnerDisputesResponseDataItem]:
        """List my disputes. GET /v1/partner/disputes

        Disputes the partner filed about missing or wrong credit, newest first, with the merchant's resolution.

        **Auth:** a partner session.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/partner/disputes", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_partner_disputes_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[GetPartnerDisputesResponseDataItem]:
        """Every item of ``get_partner_disputes``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_partner_disputes(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_partner_groups(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetPartnerGroupsResponseDataItem]:
        """List my groups. GET /v1/partner/groups

        The partner's groups across programs, with their onboarding and payout terms.

        **Auth:** a partner session.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/partner/groups", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_partner_groups_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[GetPartnerGroupsResponseDataItem]:
        """Every item of ``get_partner_groups``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_partner_groups(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_partner_invitations(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetPartnerInvitationsResponseDataItem]:
        """List my invitations. GET /v1/partner/invitations

        Program invitations merchants sent the partner.

        **Auth:** a partner session.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/partner/invitations", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_partner_invitations_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[GetPartnerInvitationsResponseDataItem]:
        """Every item of ``get_partner_invitations``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_partner_invitations(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_partner_kyc_status(self, *, idempotency_key: Optional[str] = None) -> GetPartnerKycStatusResponse:
        """Get my identity verification status. GET /v1/partner/kyc/status

        The partner account's KYC status (`unverified`, `pending`, `verified`, `rejected`), sanctions screening status and when it was verified.

        **Auth:** a partner session.
        """
        return await self._request("GET", f"/v1/partner/kyc/status", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_partner_links(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetPartnerLinksResponseDataItem]:
        """List my links. GET /v1/partner/links

        The partner's tracked links across merchants, newest first, with the short URL, the `?via=` parameter for direct links and eligible clicks.

        **Auth:** a partner session.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/partner/links", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_partner_links_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[GetPartnerLinksResponseDataItem]:
        """Every item of ``get_partner_links``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_partner_links(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_partner_links_id_qr(self, id: str, *, idempotency_key: Optional[str] = None) -> str:
        """Get my link's QR code. GET /v1/partner/links/{id}/qr

        An SVG QR code for one of the partner's links.

        **Auth:** a partner session.
        """
        return await self._request("GET", f"/v1/partner/links/{_seg(id)}/qr", query={}, body=None, idempotency_key=idempotency_key, kind="text")

    async def get_partner_marketplace(self, *, category: Optional[str] = None, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetPartnerMarketplaceResponseDataItem]:
        """Browse the marketplace. GET /v1/partner/marketplace

        Public listings of active live programs across every merchant, sponsored first, with commission terms and platform-computed stats. Filter with `category`. Partner session only.

        **Auth:** a partner session.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/partner/marketplace", query={"category": category, "limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_partner_marketplace_iter(self, *, category: Optional[str] = None, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[GetPartnerMarketplaceResponseDataItem]:
        """Every item of ``get_partner_marketplace``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_partner_marketplace(category=category, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_partner_me(self, *, idempotency_key: Optional[str] = None) -> GetPartnerMeResponse:
        """Get my account and memberships. GET /v1/partner/me

        The partner account and every merchant it partners with, each with its programs and enrollment status.

        **Auth:** a partner session.
        """
        return await self._request("GET", f"/v1/partner/me", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_partner_notifications(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[Notification]:
        """List my notifications. GET /v1/partner/notifications

        The partner account's notifications, newest first.

        **Auth:** a partner session.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/partner/notifications", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_partner_notifications_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[Notification]:
        """Every item of ``get_partner_notifications``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_partner_notifications(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_partner_orgs_org_id_self_billing(self, org_id: str, *, idempotency_key: Optional[str] = None) -> GetPartnerOrgsOrgIdSelfBillingResponse:
        """Get self-billing status. GET /v1/partner/orgs/{orgId}/self-billing

        The partner's VAT details with this merchant and whether they accepted the current self-billing agreement (`currentVersion`).

        **Auth:** a partner session.
        """
        return await self._request("GET", f"/v1/partner/orgs/{_seg(org_id)}/self-billing", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_partner_passport(self, *, idempotency_key: Optional[str] = None) -> Passport:
        """Get my reputation passport. GET /v1/partner/passport

        A signed, portable passport of the partner's verified performance across every program (programs, eligible clicks, referrals, repeat-payer rate, average quality), valid for 90 days.

        **Auth:** a partner session.
        """
        return await self._request("GET", f"/v1/partner/passport", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_partner_payouts(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetPartnerPayoutsResponseDataItem]:
        """List my payouts. GET /v1/partner/payouts

        The partner's payouts across merchants, newest first.

        **Auth:** a partner session.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/partner/payouts", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_partner_payouts_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[GetPartnerPayoutsResponseDataItem]:
        """Every item of ``get_partner_payouts``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_partner_payouts(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_partner_payouts_id_invoice(self, id: str, *, format_: Optional[Literal["json", "html"]] = None, idempotency_key: Optional[str] = None) -> Invoice:
        """Get my payout invoice. GET /v1/partner/payouts/{id}/invoice

        The invoice for one of the partner's payouts, as JSON or (`format=html`) a printable page.

        **Auth:** a partner session.
        """
        return await self._request("GET", f"/v1/partner/payouts/{_seg(id)}/invoice", query={"format": format_}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_partner_postback_logs(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetPartnerPostbackLogsResponseDataItem]:
        """List my postback calls. GET /v1/partner/postback-logs

        Recent postback calls with the topic, URL and the status code the partner's server answered.

        **Auth:** a partner session.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/partner/postback-logs", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_partner_postback_logs_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[GetPartnerPostbackLogsResponseDataItem]:
        """Every item of ``get_partner_postback_logs``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_partner_postback_logs(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_partner_profile(self, *, idempotency_key: Optional[str] = None) -> CreatorProfile:
        """Get my creator profile. GET /v1/partner/profile

        The partner's creator profile (headline, bio, channels, audience, engagement) and verified stats.

        **Auth:** a partner session.
        """
        return await self._request("GET", f"/v1/partner/profile", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_partner_profile_verified(self, *, idempotency_key: Optional[str] = None) -> GetPartnerProfileVerifiedResponse:
        """Get my verified performance. GET /v1/partner/profile/verified

        The partner's performance across all programs, computed by the platform from the ledger rather than self-reported: programs, eligible clicks, active referrals and repeat-payer rate.

        **Auth:** a partner session.
        """
        return await self._request("GET", f"/v1/partner/profile/verified", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_partner_programs_program_id_leaderboard(self, program_id: str, *, idempotency_key: Optional[str] = None) -> GetPartnerProgramsProgramIdLeaderboardResponse:
        """Get a program leaderboard. GET /v1/partner/programs/{programId}/leaderboard

        Top 25 partners by approved commission in the program (during the active contest, if any). Other partners' names are masked; the partner's own row is marked `you`. 403 when the program has no leaderboard.

        **Auth:** a partner session.
        """
        return await self._request("GET", f"/v1/partner/programs/{_seg(program_id)}/leaderboard", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_partner_recruit(self, *, idempotency_key: Optional[str] = None) -> GetPartnerRecruitResponse:
        """Get my recruiting link. GET /v1/partner/recruit

        The partner's recruit code and sign-up URL. Partners who sign up through it become their sub-affiliates where both partner the same merchant.

        **Auth:** a partner session.
        """
        return await self._request("GET", f"/v1/partner/recruit", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_partner_referrals(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetPartnerReferralsResponseDataItem]:
        """List my referrals. GET /v1/partner/referrals

        The partner's referrals across merchants, newest first. Customer ids are redacted to their last 4 characters.

        **Auth:** a partner session.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/partner/referrals", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_partner_referrals_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[GetPartnerReferralsResponseDataItem]:
        """Every item of ``get_partner_referrals``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_partner_referrals(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_partner_referrals_id_transparency(self, id: str, *, idempotency_key: Optional[str] = None) -> GetPartnerReferralsIdTransparencyResponse:
        """Explain a referral. GET /v1/partner/referrals/{id}/transparency

        Why a referral credited the partner (or did not fully): the model, window, touchpoints considered, the partner's share of the credit and the reasoning notes. No customer data.

        **Auth:** a partner session.
        """
        return await self._request("GET", f"/v1/partner/referrals/{_seg(id)}/transparency", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_partners(self, *, email: Optional[str] = None, external_ref: Optional[str] = None, status: Optional[Literal["active", "suspended", "banned", "archived"]] = None, include_archived: Optional[Literal["true", "false"]] = None, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[Partner]:
        """List partners. GET /v1/partners

        Partners, newest first. Filter by `email`, `externalRef` or `status`. Archived partners are hidden unless you ask for them with `status=archived` or `includeArchived=true`.

        **Auth:** an API key with `partners:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/partners", query={"email": email, "externalRef": external_ref, "status": status, "includeArchived": include_archived, "limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_partners_iter(self, *, email: Optional[str] = None, external_ref: Optional[str] = None, status: Optional[Literal["active", "suspended", "banned", "archived"]] = None, include_archived: Optional[Literal["true", "false"]] = None, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[Partner]:
        """Every item of ``get_partners``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_partners(email=email, external_ref=external_ref, status=status, include_archived=include_archived, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_partner_security(self, *, idempotency_key: Optional[str] = None) -> GetPartnerSecurityResponse:
        """Get my security settings. GET /v1/partner/security

        Whether two-factor sign-in is on for the partner account.

        **Auth:** a partner session.
        """
        return await self._request("GET", f"/v1/partner/security", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_partners_id(self, id: str, *, idempotency_key: Optional[str] = None) -> GetPartnersIdResponse:
        """Get a partner. GET /v1/partners/{id}

        One partner, with a cross-network warning when the same account is flagged or banned by other merchants (it never says which).

        **Auth:** an API key with `partners:read` (or `full`), or a session of any role.
        """
        return await self._request("GET", f"/v1/partners/{_seg(id)}", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_partners_id_balances(self, id: str, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[Balance]:
        """Get a partner's balances. GET /v1/partners/{id}/balances

        The partner's commission balances per currency: pending (in hold), approved (payable), paid and reversed.

        **Auth:** an API key with `commissions:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/partners/{_seg(id)}/balances", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_partners_id_balances_iter(self, id: str, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[Balance]:
        """Every item of ``get_partners_id_balances``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_partners_id_balances(id, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_partners_id_enrollments(self, id: str, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetPartnersIdEnrollmentsResponseDataItem]:
        """List a partner's enrollments. GET /v1/partners/{id}/enrollments

        The programs a partner is enrolled in or applied to, with status and group.

        **Auth:** an API key with `partners:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/partners/{_seg(id)}/enrollments", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_partners_id_enrollments_iter(self, id: str, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[GetPartnersIdEnrollmentsResponseDataItem]:
        """Every item of ``get_partners_id_enrollments``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_partners_id_enrollments(id, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_partners_id_payout_profile(self, id: str, *, idempotency_key: Optional[str] = None) -> PayoutProfile:
        """Get a partner's payout profile. GET /v1/partners/{id}/payout-profile

        The partner's payout method, currency, threshold and tax form status. Method details are not returned. 404 when none is set.

        **Auth:** an API key with `payouts:read` (or `full`), or a session of any role.
        """
        return await self._request("GET", f"/v1/partners/{_seg(id)}/payout-profile", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_partners_id_quality(self, id: str, *, idempotency_key: Optional[str] = None) -> GetPartnersIdQualityResponse:
        """Get a partner's quality score. GET /v1/partners/{id}/quality

        The partner's quality score computed now (with its metrics) and the last stored snapshot.

        **Auth:** an API key with `partners:read` (or `full`), or a session of any role.
        """
        return await self._request("GET", f"/v1/partners/{_seg(id)}/quality", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_partner_stats(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetPartnerStatsResponseDataItem]:
        """Get my stats. GET /v1/partner/stats

        Per merchant: eligible clicks, active referrals, payments and commission balances.

        **Auth:** a partner session.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/partner/stats", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_partner_stats_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[GetPartnerStatsResponseDataItem]:
        """Every item of ``get_partner_stats``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_partner_stats(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_partner_tax_documents(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetPartnerTaxDocumentsResponseDataItem]:
        """List my tax documents. GET /v1/partner/tax-documents

        Tax forms delivered to the partner by every merchant they work with, newest year first.

        **Auth:** a partner session.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/partner/tax-documents", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_partner_tax_documents_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[GetPartnerTaxDocumentsResponseDataItem]:
        """Every item of ``get_partner_tax_documents``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_partner_tax_documents(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_partner_tax_documents_id(self, id: str, *, idempotency_key: Optional[str] = None) -> str:
        """Get my tax document. GET /v1/partner/tax-documents/{id}

        The recipient copy of a delivered tax form, as an HTML page.

        **Auth:** a partner session.
        """
        return await self._request("GET", f"/v1/partner/tax-documents/{_seg(id)}", query={}, body=None, idempotency_key=idempotency_key, kind="text")

    async def get_partner_terms(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetPartnerTermsResponseDataItem]:
        """List program terms. GET /v1/partner/terms

        The latest terms version of each program the partner is approved in, and whether they accepted it.

        **Auth:** a partner session.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/partner/terms", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_partner_terms_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[GetPartnerTermsResponseDataItem]:
        """Every item of ``get_partner_terms``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_partner_terms(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_passport_public_key(self, *, idempotency_key: Optional[str] = None) -> GetPassportPublicKeyResponse:
        """Get the passport signing key. GET /v1/passport/public-key

        The ed25519 public key partner passports are signed with, so anyone can verify one offline.

        **Auth:** none.
        """
        return await self._request("GET", f"/v1/passport/public-key", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_payout_connections(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetPayoutConnectionsResponseDataItem]:
        """List payout provider connections. GET /v1/payout-connections

        The payout providers the org connected with its own credentials (PayPal, Stripe, Circle, Wise, Payoneer, Tremendous), with environment and status. Secrets are never returned.

        **Auth:** an API key with `payouts:read` (or `full`), or a session with role `owner`, `admin`, `finance`.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/payout-connections", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_payout_connections_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[GetPayoutConnectionsResponseDataItem]:
        """Every item of ``get_payout_connections``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_payout_connections(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_payout_runs(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[PayoutRun]:
        """List payout runs. GET /v1/payout-runs

        Payout runs, newest first, with their status and summary.

        **Auth:** an API key with `payouts:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/payout-runs", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_payout_runs_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[PayoutRun]:
        """Every item of ``get_payout_runs``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_payout_runs(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_payouts(self, *, partner_id: Optional[str] = None, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[Payout]:
        """List payouts. GET /v1/payouts

        Individual payouts, newest first, with rail, provider reference and failure reason. Filter with `partnerId`.

        **Auth:** an API key with `payouts:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/payouts", query={"partnerId": partner_id, "limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_payouts_iter(self, *, partner_id: Optional[str] = None, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[Payout]:
        """Every item of ``get_payouts``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_payouts(partner_id=partner_id, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_payouts_id_invoice(self, id: str, *, format_: Optional[Literal["json", "html"]] = None, idempotency_key: Optional[str] = None) -> Invoice:
        """Get a payout's invoice. GET /v1/payouts/{id}/invoice

        The self-billing invoice issued for a payout, as JSON or (`format=html`) a printable page. 404 when the payout has no invoice.

        **Auth:** an API key with `payouts:read` (or `full`), or a session of any role.
        """
        return await self._request("GET", f"/v1/payouts/{_seg(id)}/invoice", query={"format": format_}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_privacy_export(self, *, customer_ref: str, idempotency_key: Optional[str] = None) -> CustomerExport:
        """Export a customer's data. GET /v1/privacy/export

        Every stored row that references the customer, for a data-subject access request.

        **Auth:** an API key with `privacy:read` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("GET", f"/v1/privacy/export", query={"customerRef": customer_ref}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_privacy_requests(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[PrivacyRequest]:
        """List data-subject requests. GET /v1/privacy/requests

        Access and erasure requests, newest first, with their status.

        **Auth:** an API key with `privacy:read` (or `full`), or a session with role `owner`, `admin`.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/privacy/requests", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_privacy_requests_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[PrivacyRequest]:
        """Every item of ``get_privacy_requests``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_privacy_requests(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_privacy_requests_id(self, id: str, *, idempotency_key: Optional[str] = None) -> PrivacyRequest:
        """Get a data-subject request. GET /v1/privacy/requests/{id}

        Poll one request: `pending`, `completed` or `failed`, and whether data was found.

        **Auth:** an API key with `privacy:read` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("GET", f"/v1/privacy/requests/{_seg(id)}", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_privacy_requests_id_result(self, id: str, *, idempotency_key: Optional[str] = None) -> GetPrivacyRequestsIdResultResponse:
        """Get a data-subject request result. GET /v1/privacy/requests/{id}/result

        The full result of a completed request; for access requests, the exported data. 400 until it is completed.

        **Auth:** an API key with `privacy:read` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("GET", f"/v1/privacy/requests/{_seg(id)}/result", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_profitability_products(self, *, idempotency_key: Optional[str] = None) -> GetProfitabilityProductsResponse:
        """List product margins. GET /v1/profitability/products

        The margin catalog: per product, a margin (bps) or a unit cost, used to turn revenue into profit.

        **Auth:** an API key with `analytics:read` (or `full`), or a session of any role.
        """
        return await self._request("GET", f"/v1/profitability/products", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_profitability_products_product_ref(self, product_ref: str, *, idempotency_key: Optional[str] = None) -> GetProfitabilityProductsProductRefResponse:
        """Get a product margin. GET /v1/profitability/products/{productRef}

        One product of the margin catalog.

        **Auth:** an API key with `analytics:read` (or `full`), or a session of any role.
        """
        return await self._request("GET", f"/v1/profitability/products/{_seg(product_ref)}", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_profitability_rebuild_job_id(self, job_id: str, *, idempotency_key: Optional[str] = None) -> GetProfitabilityRebuildJobIdResponse:
        """Get a rebuild job. GET /v1/profitability/rebuild/{jobId}

        Progress of a rebuild: `queued`, `running`, `done` or `failed` (a job untouched for an hour reports `failed` with `error: "stale"`), with processed and total counts.

        **Auth:** an API key with `analytics:read` (or `full`), or a session of any role.
        """
        return await self._request("GET", f"/v1/profitability/rebuild/{_seg(job_id)}", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_profitability_settings(self, *, program_id: Optional[str] = None, idempotency_key: Optional[str] = None) -> GetProfitabilitySettingsResponse:
        """Get profitability settings. GET /v1/profitability/settings

        The economics credit ROI is computed with: reporting currency, default margin, how a credit's cost is modelled, how credit use is inferred, attribution and churn windows, target ROI and more. With `programId`, the program's overrides merged over the org's.

        **Auth:** an API key with `analytics:read` (or `full`), or a session of any role.
        """
        return await self._request("GET", f"/v1/profitability/settings", query={"programId": program_id}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_programs(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[Program]:
        """List programs. GET /v1/programs

        The org's programs, oldest first, with their settings.

        **Auth:** an API key with `programs:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/programs", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_programs_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[Program]:
        """Every item of ``get_programs``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_programs(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_programs_id(self, id: str, *, idempotency_key: Optional[str] = None) -> Program:
        """Get a program. GET /v1/programs/{id}

        One program with its settings (defaults filled in) and public page.

        **Auth:** an API key with `programs:read` (or `full`), or a session of any role.
        """
        return await self._request("GET", f"/v1/programs/{_seg(id)}", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_programs_id_autopricing(self, id: str, *, idempotency_key: Optional[str] = None) -> GetProgramsIdAutopricingResponse:
        """Get autopricing settings. GET /v1/programs/{id}/autopricing

        The program's autopricing configuration, or `null` when it's off.

        **Auth:** an API key with `programs:read` (or `full`), or a session of any role.
        """
        return await self._request("GET", f"/v1/programs/{_seg(id)}/autopricing", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_programs_id_enrollments(self, id: str, *, status: Optional[Literal["applied", "approved", "rejected", "removed"]] = None, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetProgramsIdEnrollmentsResponseDataItem]:
        """List program enrollments. GET /v1/programs/{id}/enrollments

        The program's enrollments and applications, newest first, each with the partner and a cross-network warning when other merchants banned the same account. Filter with `status`.

        **Auth:** an API key with `programs:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/programs/{_seg(id)}/enrollments", query={"status": status, "limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_programs_id_enrollments_iter(self, id: str, *, status: Optional[Literal["applied", "approved", "rejected", "removed"]] = None, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[GetProgramsIdEnrollmentsResponseDataItem]:
        """Every item of ``get_programs_id_enrollments``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_programs_id_enrollments(id, status=status, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_programs_id_graph(self, id: str, *, root: str, depth: Optional[int] = None, idempotency_key: Optional[str] = None) -> GetProgramsIdGraphResponse:
        """Get the referral tree. GET /v1/programs/{id}/graph

        Who referred whom from one partner (`root`) down, with revenue and net commission per node. Where customers are partners too (customerRef equals a partner's externalRef), the tree continues up to `depth` partner levels. Stops at 5,000 referrals and says so.

        **Auth:** an API key with `programs:read` (or `full`), or a session of any role.
        """
        return await self._request("GET", f"/v1/programs/{_seg(id)}/graph", query={"root": root, "depth": depth}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_programs_id_groups(self, id: str, *, include_archived: Optional[Literal["true", "false"]] = None, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[PartnerGroup]:
        """List partner groups. GET /v1/programs/{id}/groups

        The program's partner groups with member counts. Archived groups are hidden unless `includeArchived=true`.

        **Auth:** an API key with `programs:read` (or `full`), or a session of any role.

        includeArchived: true: include archived groups.
        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/programs/{_seg(id)}/groups", query={"includeArchived": include_archived, "limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_programs_id_groups_iter(self, id: str, *, include_archived: Optional[Literal["true", "false"]] = None, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[PartnerGroup]:
        """Every item of ``get_programs_id_groups``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_programs_id_groups(id, include_archived=include_archived, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_programs_id_negotiation_policy(self, id: str, *, idempotency_key: Optional[str] = None) -> GetProgramsIdNegotiationPolicyResponse:
        """Get the agent negotiation policy. GET /v1/programs/{id}/negotiation-policy

        The program's negotiation policy, or `null` when it isn't open to negotiation.

        **Auth:** an API key with `programs:read` (or `full`), or a session of any role.
        """
        return await self._request("GET", f"/v1/programs/{_seg(id)}/negotiation-policy", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_programs_id_promotions(self, id: str, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[Promotion]:
        """List promotions. GET /v1/programs/{id}/promotions

        The program's promotions, latest start first.

        **Auth:** an API key with `programs:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/programs/{_seg(id)}/promotions", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_programs_id_promotions_iter(self, id: str, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[Promotion]:
        """Every item of ``get_programs_id_promotions``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_programs_id_promotions(id, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_programs_id_referee_reward(self, id: str, *, idempotency_key: Optional[str] = None) -> GetProgramsIdRefereeRewardResponse:
        """Get the referee reward. GET /v1/programs/{id}/referee-reward

        The program's reward for referred customers (the friend's side of a double-sided program), or `null` when it has none.

        **Auth:** an API key with `programs:read` (or `full`), or a session of any role.
        """
        return await self._request("GET", f"/v1/programs/{_seg(id)}/referee-reward", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_programs_id_terms_acceptances(self, id: str, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetProgramsIdTermsAcceptancesResponseDataItem]:
        """List terms acceptances. GET /v1/programs/{id}/terms-acceptances

        Which partner accepted which version of the program's terms, newest first.

        **Auth:** an API key with `programs:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/programs/{_seg(id)}/terms-acceptances", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_programs_id_terms_acceptances_iter(self, id: str, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[GetProgramsIdTermsAcceptancesResponseDataItem]:
        """Every item of ``get_programs_id_terms_acceptances``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_programs_id_terms_acceptances(id, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_prospects(self, *, status: Optional[Literal["identified", "queued", "contacted", "replied", "interested", "declined", "converted"]] = None, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetProspectsResponseDataItem]:
        """List prospects. GET /v1/prospects

        Prospects, best fit first, with channel, audience, evidence and outreach status. Filter with `status`.

        **Auth:** an API key with `growth:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/prospects", query={"status": status, "limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_prospects_iter(self, *, status: Optional[Literal["identified", "queued", "contacted", "replied", "interested", "declined", "converted"]] = None, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[GetProspectsResponseDataItem]:
        """Every item of ``get_prospects``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_prospects(status=status, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_public_programs_handle(self, handle: str, *, idempotency_key: Optional[str] = None) -> GetPublicProgramsHandleResponse:
        """Get a program's public page. GET /v1/public/programs/{handle}

        What a program's public join page shows: the program and merchant names, pitch, cookie window, terms, base commission, branding and whether joining is approved at once. No authentication; only active live programs with a `publicHandle` are found.

        **Auth:** none.
        """
        return await self._request("GET", f"/v1/public/programs/{_seg(handle)}", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_referrals(self, *, program_id: Optional[str] = None, partner_id: Optional[str] = None, status: Optional[Literal["active", "pending_review", "paused", "void"]] = None, customer_ref: Optional[str] = None, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[Referral]:
        """List referrals. GET /v1/referrals

        Referrals, newest first, filtered by `programId`, `partnerId`, `status` or `customerRef`.

        **Auth:** an API key with `referrals:read` (or `full`), or a session of any role.

        customerRef: Your id for the referred customer.
        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/referrals", query={"programId": program_id, "partnerId": partner_id, "status": status, "customerRef": customer_ref, "limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_referrals_iter(self, *, program_id: Optional[str] = None, partner_id: Optional[str] = None, status: Optional[Literal["active", "pending_review", "paused", "void"]] = None, customer_ref: Optional[str] = None, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[Referral]:
        """Every item of ``get_referrals``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_referrals(program_id=program_id, partner_id=partner_id, status=status, customer_ref=customer_ref, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_referrals_id(self, id: str, *, idempotency_key: Optional[str] = None) -> Referral:
        """Get a referral. GET /v1/referrals/{id}

        One referral with its touch credits and attribution reasoning.

        **Auth:** an API key with `referrals:read` (or `full`), or a session of any role.
        """
        return await self._request("GET", f"/v1/referrals/{_seg(id)}", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_referrals_id_journey(self, id: str, *, idempotency_key: Optional[str] = None) -> GetReferralsIdJourneyResponse:
        """Get the attribution journey. GET /v1/referrals/{id}/journey

        The referral with every touchpoint considered: each click's time, URL, fraud score, eligibility, credit weight and which one won.

        **Auth:** an API key with `referrals:read` (or `full`), or a session of any role.
        """
        return await self._request("GET", f"/v1/referrals/{_seg(id)}/journey", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_reports_filtered_clicks(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetReportsFilteredClicksResponseDataItem]:
        """Report filtered clicks. GET /v1/reports/filtered-clicks

        Per day, newest first: total clicks, clicks excluded from attribution (bots, rate limits, invalid traffic) and the average fraud score.

        **Auth:** an API key with `analytics:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/reports/filtered-clicks", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_reports_filtered_clicks_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[GetReportsFilteredClicksResponseDataItem]:
        """Every item of ``get_reports_filtered_clicks``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_reports_filtered_clicks(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_reports_partner_performance(self, *, format_: Optional[Literal["json", "csv"]] = None, idempotency_key: Optional[str] = None) -> GetReportsPartnerPerformanceResponse:
        """Get partner performance. GET /v1/reports/partner-performance

        Per partner, highest revenue first: clicks, referrals, payments, referred revenue, commission earned and reversed. `format=csv` returns the same as a CSV file.

        **Auth:** an API key with `analytics:read` (or `full`), or a session of any role.

        format: csv: the same rows as a CSV file.
        """
        return await self._request("GET", f"/v1/reports/partner-performance", query={"format": format_}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_rewards(self, *, status: Optional[Literal["issued", "redeemed", "void"]] = None, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetRewardsResponseDataItem]:
        """List issued referee rewards. GET /v1/rewards

        Rewards issued to referred customers, newest first, with code and status (`issued`, `redeemed`, `void`). Filter with `status`.

        **Auth:** an API key with `commissions:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/rewards", query={"status": status, "limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_rewards_iter(self, *, status: Optional[Literal["issued", "redeemed", "void"]] = None, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[GetRewardsResponseDataItem]:
        """Every item of ``get_rewards``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_rewards(status=status, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_rewards_lookup_code(self, code: str, *, idempotency_key: Optional[str] = None) -> GetRewardsLookupCodeResponse:
        """Look up a reward code. GET /v1/rewards/lookup/{code}

        Whether a reward code is valid (issued and unredeemed), with its kind and amount, so your checkout can apply it. Unknown codes answer `{ "valid": false }`.

        **Auth:** an API key with `commissions:read` (or `full`), or a session of any role.
        """
        return await self._request("GET", f"/v1/rewards/lookup/{_seg(code)}", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_roi_breakdown(self, *, from_: Optional[str] = None, to: Optional[str] = None, program_id: Optional[str] = None, partner_id: Optional[str] = None, window_days: Optional[int] = None, currency: Optional[str] = None, format_: Optional[Literal["json", "csv"]] = None, by: Literal["program", "partner", "cohort", "source", "role"], limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetRoiBreakdownResponseDataItem]:
        """Get the ROI breakdown. GET /v1/roi/breakdown

        The summary figures grouped `by` program, partner, cohort (grant month), source or role, best ROI first (cohorts in date order). Partner and program rows also carry their referrals' combined figures. `from`/`to` select grants by grant date (a date covers its whole UTC day), `programId` and `partnerId` narrow them, `windowDays` overrides each program's attribution window (30, 90, 180, 365, or 0 for lifetime), and `currency` views one native currency instead of the reporting currency. `format=csv` returns the same as a CSV file.

        **Auth:** an API key with `analytics:read` (or `full`), or a session of any role.

        from: Grants (or referrals) from this instant or date, inclusive.
        to: Up to this instant, or through the end of this date (UTC), inclusive.
        partnerId: The grant's partner: the referrer, or the partner of the referee's referral.
        windowDays: Attribution window; default each program's setting. 0 = lifetime.
        currency: Default the reporting currency (converted); another code gives that currency only.
        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/roi/breakdown", query={"from": from_, "to": to, "programId": program_id, "partnerId": partner_id, "windowDays": window_days, "currency": currency, "format": format_, "by": by, "limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_roi_breakdown_iter(self, *, from_: Optional[str] = None, to: Optional[str] = None, program_id: Optional[str] = None, partner_id: Optional[str] = None, window_days: Optional[int] = None, currency: Optional[str] = None, format_: Optional[Literal["json", "csv"]] = None, by: Literal["program", "partner", "cohort", "source", "role"], limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[GetRoiBreakdownResponseDataItem]:
        """Every item of ``get_roi_breakdown``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_roi_breakdown(from_=from_, to=to, program_id=program_id, partner_id=partner_id, window_days=window_days, currency=currency, format_=format_, by=by, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_roi_data_quality(self, *, from_: Optional[str] = None, to: Optional[str] = None, format_: Optional[Literal["json", "csv"]] = None, idempotency_key: Optional[str] = None) -> GetRoiDataQualityResponse:
        """Get ROI data quality. GET /v1/roi/data-quality

        How complete the inputs to ROI are over `from`/`to`: payments with credit-applied info, products with a margin, partners linked to their own customer id, events excluded for a missing FX rate, and a list of gaps with how to fix each.

        **Auth:** an API key with `analytics:read` (or `full`), or a session of any role.

        from: Grants (or referrals) from this instant or date, inclusive.
        to: Up to this instant, or through the end of this date (UTC), inclusive.
        """
        return await self._request("GET", f"/v1/roi/data-quality", query={"from": from_, "to": to, "format": format_}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_roi_grants(self, *, from_: Optional[str] = None, to: Optional[str] = None, program_id: Optional[str] = None, partner_id: Optional[str] = None, window_days: Optional[int] = None, currency: Optional[str] = None, format_: Optional[Literal["json", "csv"]] = None, status: Optional[Literal["open", "used", "expired", "revoked"]] = None, role: Optional[Literal["referee", "referrer"]] = None, paid_back: Optional[Literal["true", "false"]] = None, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[RoiGrant]:
        """List credit grants. GET /v1/roi/grants

        Each credit grant in view with its status (`open`, `used`, `expired`, `revoked`) and figures, newest first. Filter by `status`, `role` (`referee` or `referrer`) and `paidBack`. `from`/`to` select grants by grant date (a date covers its whole UTC day), `programId` and `partnerId` narrow them, `windowDays` overrides each program's attribution window (30, 90, 180, 365, or 0 for lifetime), and `currency` views one native currency instead of the reporting currency. `format=csv` returns the same as a CSV file. CSV returns every grant, unpaged.

        **Auth:** an API key with `analytics:read` (or `full`), or a session of any role.

        from: Grants (or referrals) from this instant or date, inclusive.
        to: Up to this instant, or through the end of this date (UTC), inclusive.
        partnerId: The grant's partner: the referrer, or the partner of the referee's referral.
        windowDays: Attribution window; default each program's setting. 0 = lifetime.
        currency: Default the reporting currency (converted); another code gives that currency only.
        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/roi/grants", query={"from": from_, "to": to, "programId": program_id, "partnerId": partner_id, "windowDays": window_days, "currency": currency, "format": format_, "status": status, "role": role, "paidBack": paid_back, "limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_roi_grants_iter(self, *, from_: Optional[str] = None, to: Optional[str] = None, program_id: Optional[str] = None, partner_id: Optional[str] = None, window_days: Optional[int] = None, currency: Optional[str] = None, format_: Optional[Literal["json", "csv"]] = None, status: Optional[Literal["open", "used", "expired", "revoked"]] = None, role: Optional[Literal["referee", "referrer"]] = None, paid_back: Optional[Literal["true", "false"]] = None, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[RoiGrant]:
        """Every item of ``get_roi_grants``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_roi_grants(from_=from_, to=to, program_id=program_id, partner_id=partner_id, window_days=window_days, currency=currency, format_=format_, status=status, role=role, paid_back=paid_back, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_roi_partners_id_trace(self, id: str, *, window_days: Optional[int] = None, format_: Optional[Literal["json", "csv"]] = None, idempotency_key: Optional[str] = None) -> RoiTrace:
        """Trace a partner's value. GET /v1/roi/partners/{id}/trace

        The same trace for a partner's own customer identity (through their externalRef).

        **Auth:** an API key with `analytics:read` (or `full`), or a session of any role.

        windowDays: Attribution window; default each program's setting. 0 = lifetime.
        """
        return await self._request("GET", f"/v1/roi/partners/{_seg(id)}/trace", query={"windowDays": window_days, "format": format_}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_roi_patterns(self, *, idempotency_key: Optional[str] = None) -> GetRoiPatternsResponse:
        """List value patterns. GET /v1/roi/patterns

        Every value pattern from one detection run, with the matching subjects: `credit_only` (a referee used their credit and paid no cash after within the window), `churn_at_exhaustion` (used it up, paid, then stopped), `bonus_collector` (a partner holding commission credit who never spends their own cash) and `negative_partner` (a partner whose referrals net below zero). Matches wait until the evidence is in, so young customers are never flagged.

        **Auth:** an API key with `analytics:read` (or `full`), or a session of any role.
        """
        return await self._request("GET", f"/v1/roi/patterns", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_roi_patterns_pattern(self, pattern: str, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[RoiPatternEntry]:
        """Get a value pattern. GET /v1/roi/patterns/{pattern}

        The subjects currently matching one pattern, with the detail of each match.

        **Auth:** an API key with `analytics:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/roi/patterns/{_seg(pattern)}", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_roi_patterns_pattern_iter(self, pattern: str, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[RoiPatternEntry]:
        """Every item of ``get_roi_patterns_pattern``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_roi_patterns_pattern(pattern, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_roi_summary(self, *, from_: Optional[str] = None, to: Optional[str] = None, program_id: Optional[str] = None, partner_id: Optional[str] = None, window_days: Optional[int] = None, currency: Optional[str] = None, format_: Optional[Literal["json", "csv"]] = None, model: Optional[Literal["naive", "incremental"]] = None, include_projection: Optional[Literal["true", "false"]] = None, idempotency_key: Optional[str] = None) -> RoiSummary:
        """Get the ROI summary. GET /v1/roi/summary

        Credit ROI for the grants in view: credit cost, cash and profit from the recipients after each grant, net, ROI, payback share and median days, outstanding credit and how much of it is measured rather than inferred. With `programId`, also status against the program's target ROI. `model=incremental` adds the lift against the program's holdout group; `includeProjection=true` adds the expected payback of open grants. `from`/`to` select grants by grant date (a date covers its whole UTC day), `programId` and `partnerId` narrow them, `windowDays` overrides each program's attribution window (30, 90, 180, 365, or 0 for lifetime), and `currency` views one native currency instead of the reporting currency. `format=csv` returns the same as a CSV file.

        **Auth:** an API key with `analytics:read` (or `full`), or a session of any role.

        from: Grants (or referrals) from this instant or date, inclusive.
        to: Up to this instant, or through the end of this date (UTC), inclusive.
        partnerId: The grant's partner: the referrer, or the partner of the referee's referral.
        windowDays: Attribution window; default each program's setting. 0 = lifetime.
        currency: Default the reporting currency (converted); another code gives that currency only.
        model: naive (default): ROI of every grant. incremental: also `incremental`, the program's credit-caused lift against its recorded holdout (requires programId; reporting currency; from/to select referrals by first qualifying payment).
        includeProjection: true: also `projection`, the expected payback of the open grants in view from their program-and-role cohort's median curve (labelled 'projection'; needs 50 closed grants per cohort).
        """
        return await self._request("GET", f"/v1/roi/summary", query={"from": from_, "to": to, "programId": program_id, "partnerId": partner_id, "windowDays": window_days, "currency": currency, "format": format_, "model": model, "includeProjection": include_projection}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_roi_trace_customer_ref(self, customer_ref: str, *, window_days: Optional[int] = None, format_: Optional[Literal["json", "csv"]] = None, idempotency_key: Optional[str] = None) -> RoiTrace:
        """Trace a customer's value. GET /v1/roi/trace/{customerRef}

        Every value event of a customer (and the identities linked to them) in order, with the running net, to see exactly how their ROI was computed. `format=csv` for a file.

        **Auth:** an API key with `analytics:read` (or `full`), or a session of any role.

        windowDays: Attribution window; default each program's setting. 0 = lifetime.
        """
        return await self._request("GET", f"/v1/roi/trace/{_seg(customer_ref)}", query={"windowDays": window_days, "format": format_}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_setup_status(self, *, idempotency_key: Optional[str] = None) -> GetSetupStatusResponse:
        """Get setup progress. GET /v1/setup/status

        The install checker: which integration steps are done (auth or associate, program and rule, partner, snippet or click, billing, a payable partner, webhooks) and the next steps as hints.

        **Auth:** an API key with `analytics:read` (or `full`), or a session of any role.
        """
        return await self._request("GET", f"/v1/setup/status", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_status(self, *, idempotency_key: Optional[str] = None) -> GetStatusResponse:
        """Get platform status. GET /v1/status

        Overall state (`operational`, `degraded` or `major_outage`), each component's health and the open incidents. Cached 30 seconds.

        **Auth:** none.
        """
        return await self._request("GET", f"/v1/status", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_status_incidents(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[Incident]:
        """List status incidents. GET /v1/status/incidents

        Recent incidents, newest first, with their updates.

        **Auth:** none.

        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/status/incidents", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_status_incidents_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[Incident]:
        """Every item of ``get_status_incidents``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_status_incidents(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_status_incidents_atom(self, *, idempotency_key: Optional[str] = None) -> str:
        """Get the incidents feed. GET /v1/status/incidents.atom

        The 50 most recent incidents as an Atom feed.

        **Auth:** none.
        """
        return await self._request("GET", f"/v1/status/incidents.atom", query={}, body=None, idempotency_key=idempotency_key, kind="text")

    async def get_status_incidents_id(self, id: str, *, idempotency_key: Optional[str] = None) -> Incident:
        """Get a status incident. GET /v1/status/incidents/{id}

        One incident with its updates.

        **Auth:** none.
        """
        return await self._request("GET", f"/v1/status/incidents/{_seg(id)}", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_tax1099(self, *, year: int, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetTax1099ResponseDataItem]:
        """Export 1099-NEC data. GET /v1/tax/1099

        For each partner with a W-9 on file: the total actually paid in the tax year, in USD at recorded FX rates, and whether a form is required (US$600 or more, or a currency that couldn't be converted, listed in `fxMissingCurrencies` for review).

        **Auth:** an API key with `payouts:read` (or `full`), or a session with role `owner`, `admin`, `finance`.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/tax/1099", query={"year": year, "limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_tax1099_iter(self, *, year: int, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[GetTax1099ResponseDataItem]:
        """Every item of ``get_tax1099``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_tax1099(year=year, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_tax1099_filings(self, *, year: int, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetTax1099FilingsResponseDataItem]:
        """List 1099 filings. GET /v1/tax/1099/filings

        A tax year's filings with their provider status and the documents in each.

        **Auth:** an API key with `payouts:read` (or `full`), or a session with role `owner`, `admin`, `finance`.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/tax/1099/filings", query={"year": year, "limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_tax1099_filings_iter(self, *, year: int, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[GetTax1099FilingsResponseDataItem]:
        """Every item of ``get_tax1099_filings``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_tax1099_filings(year=year, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_tax1099_preview(self, *, year: int, idempotency_key: Optional[str] = None) -> NecPreview:
        """Preview 1099-NEC filings. GET /v1/tax/1099/preview

        Which partners would get a 1099-NEC for a tax year, with amounts and anything missing (W-9s, TINs), without filing.

        **Auth:** an API key with `payouts:read` (or `full`), or a session with role `owner`, `admin`, `finance`.
        """
        return await self._request("GET", f"/v1/tax/1099/preview", query={"year": year}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_test_clock(self, *, idempotency_key: Optional[str] = None) -> GetTestClockResponse:
        """Get the test clock. GET /v1/test_clock

        Test mode only (`409 test_mode_only` otherwise). The test org's current time and how far it has been advanced.

        **Auth:** an API key with `org:read` (or `full`), or a session of any role.
        """
        return await self._request("GET", f"/v1/test_clock", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_test_emails(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[GetTestEmailsResponseDataItem]:
        """List captured test emails. GET /v1/test/emails

        Test mode only. Emails the test org would have sent, captured instead of delivered, newest first.

        **Auth:** an API key with `org:read` (or `full`), or a session of any role.

        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/test/emails", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_test_emails_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[GetTestEmailsResponseDataItem]:
        """Every item of ``get_test_emails``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_test_emails(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_value_import_job_id(self, job_id: str, *, idempotency_key: Optional[str] = None) -> GetValueImportJobIdResponse:
        """Get a value import job. GET /v1/value/import/{jobId}

        Progress and result of a background import: status, processed and total rows, recorded and duplicate counts and row errors.

        **Auth:** an API key with `analytics:read` (or `full`), or a session of any role.
        """
        return await self._request("GET", f"/v1/value/import/{_seg(job_id)}", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_versions(self, *, idempotency_key: Optional[str] = None) -> GetVersionsResponse:
        """List API versions. GET /v1/versions

        Every API version, newest first, with what changed in it, the latest version and the deprecation policy. Pin a version with the `Referalli-Version` header or on the API key.

        **Auth:** none.
        """
        return await self._request("GET", f"/v1/versions", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_webhook_deliveries(self, *, endpoint_id: Optional[str] = None, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[WebhookDelivery]:
        """List webhook deliveries. GET /v1/webhook-deliveries

        Deliveries to every endpoint, newest first: topic, status (`pending`, `delivered`, `failed`), attempts, the last response code and, while pending, when the next attempt is. Filter with `endpointId`.

        **Auth:** an API key with `webhooks:read` (or `full`), or a session of any role.

        endpointId: Only deliveries to this endpoint.
        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/webhook-deliveries", query={"endpointId": endpoint_id, "limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_webhook_deliveries_iter(self, *, endpoint_id: Optional[str] = None, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[WebhookDelivery]:
        """Every item of ``get_webhook_deliveries``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_webhook_deliveries(endpoint_id=endpoint_id, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_webhook_deliveries_id(self, id: str, *, idempotency_key: Optional[str] = None) -> GetWebhookDeliveriesIdResponse:
        """Get a webhook delivery. GET /v1/webhook-deliveries/{id}

        One delivery in full: the exact `payload` sent, its `eventId`, and what the endpoint answered last (`lastStatusCode`, the first 2,000 characters of `lastResponseBody`, or `lastError` when there was no response).

        **Auth:** an API key with `webhooks:read` (or `full`), or a session of any role.
        """
        return await self._request("GET", f"/v1/webhook-deliveries/{_seg(id)}", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_webhook_endpoints(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[WebhookEndpoint]:
        """List webhook endpoints. GET /v1/webhook-endpoints

        Endpoints with their topics, programs, status (`active`, `paused`, `disabled`), secret-rotation state and failure state. Secrets are never returned.

        **Auth:** an API key with `webhooks:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/webhook-endpoints", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_webhook_endpoints_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[WebhookEndpoint]:
        """Every item of ``get_webhook_endpoints``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_webhook_endpoints(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_webhook_endpoints_id(self, id: str, *, idempotency_key: Optional[str] = None) -> WebhookEndpoint:
        """Get a webhook endpoint. GET /v1/webhook-endpoints/{id}

        One endpoint with its status, rotation and failure state.

        **Auth:** an API key with `webhooks:read` (or `full`), or a session of any role.
        """
        return await self._request("GET", f"/v1/webhook-endpoints/{_seg(id)}", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_webhook_endpoints_id_deliveries(self, id: str, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[WebhookDelivery]:
        """List an endpoint's deliveries. GET /v1/webhook-endpoints/{id}/deliveries

        What one endpoint was sent, newest first.

        **Auth:** an API key with `webhooks:read` (or `full`), or a session of any role.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/webhook-endpoints/{_seg(id)}/deliveries", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_webhook_endpoints_id_deliveries_iter(self, id: str, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[WebhookDelivery]:
        """Every item of ``get_webhook_endpoints_id_deliveries``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_webhook_endpoints_id_deliveries(id, limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_zapier_events(self, *, idempotency_key: Optional[str] = None) -> GetZapierEventsResponse:
        """List Zapier trigger events. GET /v1/zapier/events

        The event keys Zapier triggers can subscribe to.

        **Auth:** an API key with `integrations:read` (or `full`), or a session of any role.
        """
        return await self._request("GET", f"/v1/zapier/events", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def get_zapier_hooks(self, *, limit: Optional[int] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> Page[ZapierHook]:
        """List Zapier hooks. GET /v1/zapier/hooks

        Active Zapier REST hook subscriptions, newest first.

        **Auth:** an API key with `integrations:read` (or `full`), or a session with role `owner`, `admin`.

        limit: Items per page, 1 to 100 (default 50). From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        starting_after: A cursor: the id of an item (the previous page's `next_cursor`); returns the items after it. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        ending_before: A cursor: returns the items before this item id (the previous page). Not with `starting_after`. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[gte]: Only items created at or after this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        created[lte]: Only items created at or before this time (ISO 8601), on lists of timestamped records. From API version 2026-11-01; ignored under 2026-10-21, where lists are a capped plain array.
        """
        return await self._request("GET", f"/v1/zapier/hooks", query={"limit": limit, "starting_after": starting_after, "ending_before": ending_before, "created[gte]": created_gte, "created[lte]": created_lte}, body=None, idempotency_key=idempotency_key, kind="list")

    def get_zapier_hooks_iter(self, *, limit: Optional[int] = None, ending_before: Optional[str] = None, created_gte: Optional[str] = None, created_lte: Optional[str] = None, idempotency_key: Optional[str] = None) -> AsyncIterator[ZapierHook]:
        """Every item of ``get_zapier_hooks``, following the pages (use ``async for``)."""
        return self._paginate(lambda cursor: self.get_zapier_hooks(limit=limit, ending_before=ending_before, created_gte=created_gte, created_lte=created_lte, starting_after=cursor, idempotency_key=idempotency_key))

    async def get_zapier_triggers_event(self, event: str, *, limit: Optional[int] = None, idempotency_key: Optional[str] = None) -> GetZapierTriggersEventResponse:
        """Poll a Zapier trigger. GET /v1/zapier/triggers/{event}

        Zapier polling and sample data: the latest `limit` events of that kind, newest first, in the shape the hook delivers. Always a plain array (Zapier's contract), whatever the API version.

        **Auth:** an API key with `integrations:read` (or `full`), or a session of any role.
        """
        return await self._request("GET", f"/v1/zapier/triggers/{_seg(event)}", query={"limit": limit}, body=None, idempotency_key=idempotency_key, kind="json")

    async def patch_admin_status_incidents_id(self, id: str, body: PatchAdminStatusIncidentsIdBody, *, idempotency_key: Optional[str] = None) -> Incident:
        """Edit a status incident. PATCH /v1/admin/status/incidents/{id}

        Platform admins only. Changes an incident's title, severity, state, body or affected components. Setting `state: "resolved"` stamps `resolvedAt`.

        **Auth:** a platform admin session.
        """
        return await self._request("PATCH", f"/v1/admin/status/incidents/{_seg(id)}", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def patch_api_keys_id(self, id: str, body: PatchApiKeysIdBody, *, idempotency_key: Optional[str] = None) -> PatchApiKeysIdResponse:
        """Update an API key. PATCH /v1/api-keys/{id}

        Changes a key's pinned `apiVersion`, `owner` or expiry (`expiresInDays` from now; `null` removes it). Revoked keys are 404. Needs an owner or admin session, or an API key with the `admin` scope. Audited.

        **Auth:** an API key with `team:write` (or `full`), or a session of any role.
        """
        return await self._request("PATCH", f"/v1/api-keys/{_seg(id)}", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def patch_auth_connections_id(self, id: str, body: PatchAuthConnectionsIdBody, *, idempotency_key: Optional[str] = None) -> PatchAuthConnectionsIdResponse:
        """Update an auth connection. PATCH /v1/auth/connections/{id}

        Pauses or resumes a connection, renames it, changes `autoEnrollUsers` or the destination of auto-created links, or (signed-protocol connections) sets `signatureVersion`: `v2` to require request-line signatures, `v1+v2` to accept both again.

        **Auth:** an API key with `integrations:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("PATCH", f"/v1/auth/connections/{_seg(id)}", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def patch_billing_connections_id(self, id: str, body: PatchBillingConnectionsIdBody, *, idempotency_key: Optional[str] = None) -> BillingConnection:
        """Update a billing connection. PATCH /v1/billing/connections/{id}

        Renames a connection or sets `status`: `paused` makes its webhook URL refuse events until set back to `active`. Audited.

        **Auth:** an API key with `billing:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("PATCH", f"/v1/billing/connections/{_seg(id)}", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def patch_org(self, body: PatchOrgBody, *, idempotency_key: Optional[str] = None) -> PatchOrgResponse:
        """Update the organization. PATCH /v1/org

        Changes the org name, merges keys into `settings` (a free-form map) and turns `payoutKycRequired` on or off. Audited.

        **Auth:** an API key with `org:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("PATCH", f"/v1/org", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def patch_org_members_user_id(self, user_id: str, body: PatchOrgMembersUserIdBody, *, idempotency_key: Optional[str] = None) -> PatchOrgMembersUserIdResponse:
        """Change a member's role. PATCH /v1/org/members/{userId}

        Changes a member's role. Only owners change owner roles, and the last owner can't be demoted (409). Audited. Live mode only.

        **Auth:** an API key with `team:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("PATCH", f"/v1/org/members/{_seg(user_id)}", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def patch_org_sso(self, body: PatchOrgSsoBody, *, idempotency_key: Optional[str] = None) -> PatchOrgSsoResponse:
        """Update SSO settings. PATCH /v1/org/sso

        Requires SSO for members on the org's SSO domains (`requireSso`; needs an active connection and the owner signed in through SSO, so nobody is locked out) and maps identity-provider roles to Referalli roles. Owner only. Live mode only.

        **Auth:** an API key with `org:write` (or `full`), or a session with role `owner`.
        """
        return await self._request("PATCH", f"/v1/org/sso", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def patch_partner_groups_id(self, id: str, body: PatchPartnerGroupsIdBody, *, idempotency_key: Optional[str] = None) -> PartnerGroup:
        """Update a partner group. PATCH /v1/partner-groups/{id}

        Changes a group's terms, or archives it (`archived: true`); archived groups take no new members.

        **Auth:** an API key with `programs:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("PATCH", f"/v1/partner-groups/{_seg(id)}", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def patch_partners_id(self, id: str, body: PatchPartnersIdBody, *, idempotency_key: Optional[str] = None) -> Partner:
        """Update a partner. PATCH /v1/partners/{id}

        Changes the display name, status (`active`, `suspended`, `banned`, `archived`), tags, notes or externalRef (`null` clears it). Suspended partners keep earning but are not paid; banned ones stop attributing. 409 when another partner has the externalRef. Audited.

        **Auth:** an API key with `partners:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("PATCH", f"/v1/partners/{_seg(id)}", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def patch_partners_id_payout_profile(self, id: str, body: PatchPartnersIdPayoutProfileBody, *, idempotency_key: Optional[str] = None) -> PatchPartnersIdPayoutProfileResponse:
        """Change a partner's payout threshold. PATCH /v1/partners/{id}/payout-profile

        Changes only the minimum balance before a payout (`minThresholdMinor`). 404 when the partner has no profile. Audited.

        **Auth:** an API key with `payouts:write` (or `full`), or a session with role `owner`, `admin`, `finance`.
        """
        return await self._request("PATCH", f"/v1/partners/{_seg(id)}/payout-profile", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def patch_programs_id(self, id: str, body: PatchProgramsIdBody, *, idempotency_key: Optional[str] = None) -> Program:
        """Update a program. PATCH /v1/programs/{id}

        Changes any program field or setting; omitted fields keep their value, and `publicPage` is merged. Changing `termsMd` records a new terms version. Setting `status` to `paused` or `archived` stops new attribution. `mobileApp` (iOS Team ID and bundle id, Android package and signing-certificate fingerprints) publishes the program's apps in the universal-links and App Links files on the org's link hosts. Audited.

        **Auth:** an API key with `programs:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("PATCH", f"/v1/programs/{_seg(id)}", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def patch_referrals_id(self, id: str, body: PatchReferralsIdBody, *, idempotency_key: Optional[str] = None) -> Referral:
        """Pause or resume a referral. PATCH /v1/referrals/{id}

        Sets `status` to `paused` (no new commissions) or back to `active`. Only active referrals can be paused and only paused ones resumed (409 otherwise); setting the current status is a no-op. Publishes `referral.paused` or `referral.resumed`. Audited.

        **Auth:** an API key with `referrals:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("PATCH", f"/v1/referrals/{_seg(id)}", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def patch_webhook_endpoints_id(self, id: str, body: PatchWebhookEndpointsIdBody, *, idempotency_key: Optional[str] = None) -> WebhookEndpoint:
        """Update a webhook endpoint. PATCH /v1/webhook-endpoints/{id}

        Changes the URL, topics, programs (`null` or `[]` for every program) or legacy signature, or pauses it (`status: "paused"`, deliveries held). Setting `active` re-enables a paused or auto-disabled endpoint: held deliveries resume and the failure clock starts over. Audited.

        **Auth:** an API key with `webhooks:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("PATCH", f"/v1/webhook-endpoints/{_seg(id)}", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_admin_orgs_id_plan(self, id: str, body: PostAdminOrgsIdPlanBody, *, idempotency_key: Optional[str] = None) -> PostAdminOrgsIdPlanResponse:
        """Set an organization's plan. POST /v1/admin/orgs/{id}/plan

        Platform admins only. Moves an org to a plan without checkout.

        **Auth:** a platform admin session.
        """
        return await self._request("POST", f"/v1/admin/orgs/{_seg(id)}/plan", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_admin_orgs_id_suspend(self, id: str, body: PostAdminOrgsIdSuspendBody, *, idempotency_key: Optional[str] = None) -> PostAdminOrgsIdSuspendResponse:
        """Suspend an organization. POST /v1/admin/orgs/{id}/suspend

        Platform admins only. Suspends an org with a reason; its members and keys get 403 until it's unsuspended.

        **Auth:** a platform admin session.
        """
        return await self._request("POST", f"/v1/admin/orgs/{_seg(id)}/suspend", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_admin_orgs_id_unsuspend(self, id: str, *, idempotency_key: Optional[str] = None) -> PostAdminOrgsIdUnsuspendResponse:
        """Unsuspend an organization. POST /v1/admin/orgs/{id}/unsuspend

        Platform admins only. Lifts a suspension.

        **Auth:** a platform admin session.
        """
        return await self._request("POST", f"/v1/admin/orgs/{_seg(id)}/unsuspend", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def post_admin_partner_accounts_id_ban(self, id: str, *, idempotency_key: Optional[str] = None) -> PostAdminPartnerAccountsIdBanResponse:
        """Ban a partner account. POST /v1/admin/partner-accounts/{id}/ban

        Platform admins only. Bans a partner account across the platform and signs it out everywhere.

        **Auth:** a platform admin session.
        """
        return await self._request("POST", f"/v1/admin/partner-accounts/{_seg(id)}/ban", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def post_admin_partner_accounts_id_unban(self, id: str, *, idempotency_key: Optional[str] = None) -> PostAdminPartnerAccountsIdUnbanResponse:
        """Unban a partner account. POST /v1/admin/partner-accounts/{id}/unban

        Platform admins only. Lifts a platform ban.

        **Auth:** a platform admin session.
        """
        return await self._request("POST", f"/v1/admin/partner-accounts/{_seg(id)}/unban", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def post_admin_status_incidents(self, body: PostAdminStatusIncidentsBody, *, idempotency_key: Optional[str] = None) -> Incident:
        """Open a status incident. POST /v1/admin/status/incidents

        Platform admins only. Opens an incident on the status page (and mirrors it to the hosted status space when configured).

        **Auth:** a platform admin session.
        """
        return await self._request("POST", f"/v1/admin/status/incidents", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_admin_status_incidents_id_updates(self, id: str, body: PostAdminStatusIncidentsIdUpdatesBody, *, idempotency_key: Optional[str] = None) -> Incident:
        """Post an incident update. POST /v1/admin/status/incidents/{id}/updates

        Platform admins only. Adds a timestamped update to an incident and moves it to the given state.

        **Auth:** a platform admin session.
        """
        return await self._request("POST", f"/v1/admin/status/incidents/{_seg(id)}/updates", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_agents_register(self, body: PostAgentsRegisterBody, *, idempotency_key: Optional[str] = None) -> PostAgentsRegisterResponse:
        """Register an AI agent. POST /v1/agents/register

        Registers (or updates) an AI agent identity, proven by a wallet signature over a nonce from `POST /v1/partner/auth/wallet/nonce`. The nonce is single use and valid for 10 minutes. `instantPayout` pays the agent per outcome on the crypto rail. No API key: the signature is the credential.

        **Auth:** none.
        """
        return await self._request("POST", f"/v1/agents/register", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_anomalies_scan(self, *, idempotency_key: Optional[str] = None) -> PostAnomaliesScanResponse:
        """Scan for anomalies. POST /v1/anomalies/scan

        Compares the last 24 hours of clicks, sign-ups and revenue with the trailing 7-day average and returns this org's spikes (3x or more) and drops (under 20%). Findings also become notifications; nothing is changed automatically. Also runs hourly.

        **Auth:** an API key with `analytics:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/anomalies/scan", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def post_api_keys(self, body: PostApiKeysBody, *, idempotency_key: Optional[str] = None) -> PostApiKeysResponse:
        """Create an API key. POST /v1/api-keys

        Mints a secret key (`rk_live_…` / `rk_test_…`), shown only in this response. `scopes` defaults to `full`; a key can't grant scopes it doesn't hold. `mode` picks live, test or a matching pair of both (`both` returns `{ pairId, live, test }`); a test-mode caller can mint test keys only. `publishable: true` mints a browser-safe `rk_pub_` key limited to `programs:read` and `events:write` from `allowedOrigins`. `apiVersion` pins the key (default: latest). Needs an owner or admin session, or an API key with the `admin` scope. Audited.

        **Auth:** an API key with `team:write` (or `full`), or a session of any role.
        """
        return await self._request("POST", f"/v1/api-keys", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_assets(self, body: PostAssetsBody, *, idempotency_key: Optional[str] = None) -> PostAssetsResponse:
        """Create a marketing asset. POST /v1/assets

        Adds a marketing asset (`banner`, `copy`, `video` or `logo`) to a program for its approved partners, or only for one group's members with `groupId`.

        **Auth:** an API key with `partners:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/assets", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_attribution_replay(self, body: PostAttributionReplayBody, *, idempotency_key: Optional[str] = None) -> PostAttributionReplayResponse:
        """Replay attribution. POST /v1/attribution/replay

        Deterministically recomputes attribution for a program's referrals from the recorded clicks and identity links, under its current model. Returns what changed. Audited.

        **Auth:** an API key with `referrals:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/attribution/replay", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_auth_connections(self, body: PostAuthConnectionsBody, *, idempotency_key: Optional[str] = None) -> CreatedAuthConnection:
        """Connect an auth platform. POST /v1/auth/connections

        Connects your sign-up system so new users are attributed server-side without calling associate: `clerk`, `supabase`, `workos` or `generic` receive the platform's user webhooks at the returned URL; `atlas` and `custom` call the signed protocol endpoints under `/v1/auth/connections/{id}/`. `autoEnrollUsers` makes every new user a partner too. Returns the signing secret once. 409 when an Atlas instance already has a connection.

        **Auth:** an API key with `integrations:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/auth/connections", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_auth_connections_id_aliases(self, id: str, body: PostAuthConnectionsIdAliasesBody, *, idempotency_key: Optional[str] = None) -> PostAuthConnectionsIdAliasesResponse:
        """Change a user's id (signed protocol). POST /v1/auth/connections/{id}/aliases

        The app stamped or changed a user's id after the sign-up was filed: referrals and identity move from `fromCustomerRef` to `toCustomerRef`. Publishes `customer.aliased`. Signed with the connection secret in `x-referalli-signature: t=<unix>,v1=…,v2=…` (v2 also signs the request line; once a connection has seen v2 it requires it), with a unique `x-referalli-id` per call. Calls older than 5 minutes, reused ids (`409 replay`), paused connections (`423 connection_paused`) and unknown fields (`422`) are refused.

        **Auth:** a signature (see above); no API key.
        """
        return await self._request("POST", f"/v1/auth/connections/{_seg(id)}/aliases", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_auth_connections_id_erase(self, id: str, body: PostAuthConnectionsIdEraseBody, *, idempotency_key: Optional[str] = None) -> PostAuthConnectionsIdEraseResponse:
        """Erase a user (signed protocol). POST /v1/auth/connections/{id}/erase

        The platform deleted a user or fulfilled an erasure request: the customer's referral data and their partner record are erased. An unknown user succeeds with nothing erased. Signed with the connection secret in `x-referalli-signature: t=<unix>,v1=…,v2=…` (v2 also signs the request line; once a connection has seen v2 it requires it), with a unique `x-referalli-id` per call. Calls older than 5 minutes, reused ids (`409 replay`), paused connections (`423 connection_paused`) and unknown fields (`422`) are refused.

        **Auth:** a signature (see above); no API key.
        """
        return await self._request("POST", f"/v1/auth/connections/{_seg(id)}/erase", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_auth_connections_id_ping(self, id: str, body: Dict[str, Any], *, idempotency_key: Optional[str] = None) -> PostAuthConnectionsIdPingResponse:
        """Test an auth connection (signed protocol). POST /v1/auth/connections/{id}/ping

        Proves the secret works: returns the connection, its program and org and the server time, to check clock skew. Signed with the connection secret in `x-referalli-signature: t=<unix>,v1=…,v2=…` (v2 also signs the request line; once a connection has seen v2 it requires it), with a unique `x-referalli-id` per call. Calls older than 5 minutes, reused ids (`409 replay`), paused connections (`423 connection_paused`) and unknown fields (`422`) are refused.

        **Auth:** a signature (see above); no API key.
        """
        return await self._request("POST", f"/v1/auth/connections/{_seg(id)}/ping", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_auth_connections_id_revoke_previous_secret(self, id: str, *, idempotency_key: Optional[str] = None) -> PostAuthConnectionsIdRevokePreviousSecretResponse:
        """Revoke the previous auth secret. POST /v1/auth/connections/{id}/revoke-previous-secret

        Ends the rotation overlap at once: only the newest secret verifies from now on.

        **Auth:** an API key with `integrations:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/auth/connections/{_seg(id)}/revoke-previous-secret", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def post_auth_connections_id_rotate_secret(self, id: str, *, idempotency_key: Optional[str] = None) -> PostAuthConnectionsIdRotateSecretResponse:
        """Rotate an auth connection secret. POST /v1/auth/connections/{id}/rotate-secret

        Issues a new signing secret, returned once. The previous one keeps verifying for 24 hours, or until revoked.

        **Auth:** an API key with `integrations:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/auth/connections/{_seg(id)}/rotate-secret", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def post_auth_connections_id_signals(self, id: str, body: PostAuthConnectionsIdSignalsBody, *, idempotency_key: Optional[str] = None) -> PostAuthConnectionsIdSignalsResponse:
        """Report a user signal (signed protocol). POST /v1/auth/connections/{id}/signals

        A later verdict about a user: `email_verified` releases a hold for an unverified email, `fraud_confirmed` or `self_referral` voids their referral, `banned`/`unbanned` follow on their partner record. `details` is kept as evidence. Signed with the connection secret in `x-referalli-signature: t=<unix>,v1=…,v2=…` (v2 also signs the request line; once a connection has seen v2 it requires it), with a unique `x-referalli-id` per call. Calls older than 5 minutes, reused ids (`409 replay`), paused connections (`423 connection_paused`) and unknown fields (`422`) are refused.

        **Auth:** a signature (see above); no API key.
        """
        return await self._request("POST", f"/v1/auth/connections/{_seg(id)}/signals", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_auth_connections_id_signups(self, id: str, body: PostAuthConnectionsIdSignupsBody, *, idempotency_key: Optional[str] = None) -> PostAuthConnectionsIdSignupsResponse:
        """Attribute a new user (signed protocol). POST /v1/auth/connections/{id}/signups

        The auth platform reports a new user with the referral context captured at sign-up (`referral.code`, or with cookie consent `clickId`/`anonId`) and optional risk signals. The user is attributed (risky sign-ups are held for review), optionally made a partner with their own link, and the answer says why with reason codes. `test: true` or `atlas-test: 1` simulates without storing. Repeating the same user is idempotent. Signed with the connection secret in `x-referalli-signature: t=<unix>,v1=…,v2=…` (v2 also signs the request line; once a connection has seen v2 it requires it), with a unique `x-referalli-id` per call. Calls older than 5 minutes, reused ids (`409 replay`), paused connections (`423 connection_paused`) and unknown fields (`422`) are refused.

        **Auth:** a signature (see above); no API key.
        """
        return await self._request("POST", f"/v1/auth/connections/{_seg(id)}/signups", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_auth_connections_id_users(self, id: str, body: PostAuthConnectionsIdUsersBody, *, idempotency_key: Optional[str] = None) -> PostAuthConnectionsIdUsersResponse:
        """Update a user (signed protocol). POST /v1/auth/connections/{id}/users

        The user changed: email and name follow to their partner record, `suspended` suspends it, `deleted` erases. Signed with the connection secret in `x-referalli-signature: t=<unix>,v1=…,v2=…` (v2 also signs the request line; once a connection has seen v2 it requires it), with a unique `x-referalli-id` per call. Calls older than 5 minutes, reused ids (`409 replay`), paused connections (`423 connection_paused`) and unknown fields (`422`) are refused.

        **Auth:** a signature (see above); no API key.
        """
        return await self._request("POST", f"/v1/auth/connections/{_seg(id)}/users", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_auth_logout(self, *, idempotency_key: Optional[str] = None) -> PostAuthLogoutResponse:
        """Sign out. POST /v1/auth/logout

        Ends the browser session (and any portal-domain sessions handed off from it) and clears the cookies. Returns the identity provider's `logoutUrl` to end the provider session too, or `null`.

        **Auth:** none.
        """
        return await self._request("POST", f"/v1/auth/logout", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def post_billing_activate(self, body: PostBillingActivateBody, *, idempotency_key: Optional[str] = None) -> PostBillingActivateResponse:
        """Activate a plan directly. POST /v1/billing/activate

        Moves the org to a plan without checkout: anyone may move to Free (after cancelling a subscription); paid plans only for platform admins or self-hosted deployments (403 otherwise). Owner only. Audited.

        **Auth:** an API key with `billing:write` (or `full`), or a session with role `owner`.
        """
        return await self._request("POST", f"/v1/billing/activate", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_billing_checkout(self, body: PostBillingCheckoutBody, *, idempotency_key: Optional[str] = None) -> PostBillingCheckoutResponse:
        """Start a plan checkout. POST /v1/billing/checkout

        Creates a checkout session for a paid plan and returns its `url` to redirect to. 400 when billing is not configured on this deployment.

        **Auth:** an API key with `billing:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/billing/checkout", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_billing_connections(self, body: PostBillingConnectionsBody, *, idempotency_key: Optional[str] = None) -> CreatedBillingConnection:
        """Create a billing connection. POST /v1/billing/connections

        Connects a billing provider (`stripe`, `paddle`, `lemonsqueezy`, `polar`, `chargebee`, `shopify`, `recurly`, `braintree`, `woocommerce`, `bigcommerce` or `generic`) so its payment webhooks become commissions. Returns the `webhookUrl` path to register with the provider and its signing secret (generated unless you pass the provider's own `webhookSecret`); the secret is returned only here. Audited.

        **Auth:** an API key with `billing:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/billing/connections", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_billing_connections_id_rotate_secret(self, id: str, *, idempotency_key: Optional[str] = None) -> PostBillingConnectionsIdRotateSecretResponse:
        """Rotate the webhook signing secret. POST /v1/billing/connections/{id}/rotate-secret

        Generates a new signing secret, returned once. The previous one keeps verifying until `previousSecretExpiresAt` (24 hours). Audited.

        **Auth:** an API key with `billing:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/billing/connections/{_seg(id)}/rotate-secret", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def post_billing_connections_id_value_mapping_preview(self, id: str, body: PostBillingConnectionsIdValueMappingPreviewBody, *, idempotency_key: Optional[str] = None) -> ValueMappingPreview:
        """Preview the value mapping. POST /v1/billing/connections/{id}/value-mapping/preview

        Applies the saved mapping (or a draft `mapping`) to a sample `payload` and returns what would be recorded. Writes nothing. A generic-connector body with `events` gets one result per event.

        **Auth:** an API key with `billing:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/billing/connections/{_seg(id)}/value-mapping/preview", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_billing_portal(self, *, idempotency_key: Optional[str] = None) -> PostBillingPortalResponse:
        """Open the subscription portal. POST /v1/billing/portal

        Returns the `url` of the billing portal where the owner manages or cancels the subscription. 400 before there is a subscription.

        **Auth:** an API key with `billing:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/billing/portal", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def post_branding_domain(self, body: PostBrandingDomainBody, *, idempotency_key: Optional[str] = None) -> PostBrandingDomainResponse:
        """Set a custom portal domain. POST /v1/branding/domain

        Starts serving the partner portal on your own domain (such as `partners.example.com`), in your branding: returns the CNAME and TXT records to add. Needs a plan with custom domains (402 otherwise).

        **Auth:** an API key with `org:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/branding/domain", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_branding_domain_verify(self, *, idempotency_key: Optional[str] = None) -> PostBrandingLinkDomainVerifyResponse:
        """Verify the portal domain. POST /v1/branding/domain/verify

        Checks the portal domain's TXT record and CNAME, routes it and reports `provisioning` or `active` as for the link domain.

        **Auth:** an API key with `org:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/branding/domain/verify", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def post_branding_link_domain(self, body: PostBrandingLinkDomainBody, *, idempotency_key: Optional[str] = None) -> PostBrandingLinkDomainResponse:
        """Set a custom link domain. POST /v1/branding/link-domain

        Starts using your own domain (such as `go.example.com`) for partner links: returns the CNAME target and the TXT record that proves you control it. Links move onto it once verified. Needs a plan with custom domains (402 otherwise); 409 when the domain is in use.

        **Auth:** an API key with `org:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/branding/link-domain", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_branding_link_domain_verify(self, *, idempotency_key: Optional[str] = None) -> PostBrandingLinkDomainVerifyResponse:
        """Verify the link domain. POST /v1/branding/link-domain/verify

        Checks the TXT record and the CNAME. When both are right the domain is routed here; it is `active` once HTTPS answers on it (`provisioning` while the certificate is issued, which finishes on its own). 400 with what is missing otherwise.

        **Auth:** an API key with `org:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/branding/link-domain/verify", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def post_cli_device_codes(self, body: PostCliDeviceCodesBody, *, idempotency_key: Optional[str] = None) -> PostCliDeviceCodesResponse:
        """Start a CLI sign-in. POST /v1/cli/device-codes

        The CLI `login` command calls this to start a device sign-in: returns a `deviceCode` for polling and a `userCode` for the person to approve at `verificationUri`. Codes expire after 10 minutes. No authentication; limited per IP.

        **Auth:** none.
        """
        return await self._request("POST", f"/v1/cli/device-codes", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_cli_device_codes_token(self, body: PostCliDeviceCodesTokenBody, *, idempotency_key: Optional[str] = None) -> PostCliDeviceCodesTokenResponse:
        """Poll a CLI sign-in. POST /v1/cli/device-codes/token

        Polled by the CLI every `interval` seconds with its `deviceCode`. Answers `pending`, `expired`, `denied` or `consumed`, or once approved, `approved` with the new API key (returned once). Polling faster than allowed is `429`.

        **Auth:** none.
        """
        return await self._request("POST", f"/v1/cli/device-codes/token", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_cli_device_codes_user_code_approve(self, user_code: str, body: PostCliDeviceCodesUserCodeApproveBody, *, idempotency_key: Optional[str] = None) -> PostCliDeviceCodesUserCodeApproveResponse:
        """Approve a CLI sign-in. POST /v1/cli/device-codes/{userCode}/approve

        Approves the sign-in and mints its API key in this org. `access` picks the scopes: `cli` (webhooks write and read access to the rest, the default), `read` or `full`. Needs a signed-in owner or admin. Audited.

        **Auth:** an API key with `team:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/cli/device-codes/{_seg(user_code)}/approve", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_cli_device_codes_user_code_deny(self, user_code: str, *, idempotency_key: Optional[str] = None) -> Ok:
        """Deny a CLI sign-in. POST /v1/cli/device-codes/{userCode}/deny

        Refuses a pending sign-in; the CLI then sees `denied`.

        **Auth:** an API key with `team:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/cli/device-codes/{_seg(user_code)}/deny", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def post_cli_listeners(self, body: PostCliListenersBody, *, idempotency_key: Optional[str] = None) -> PostCliListenersResponse:
        """Open a CLI event listener. POST /v1/cli/listeners

        The CLI `listen` command opens a listener for some `topics` (default every topic). Events are queued for it while it polls at least every 2 minutes, and each comes with Standard Webhooks headers signed with the returned `secret`, so the CLI can forward them to a local server.

        **Auth:** an API key with `webhooks:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/cli/listeners", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_cli_trigger(self, body: PostCliTriggerBody, *, idempotency_key: Optional[str] = None) -> PostCliTriggerResponse:
        """Send a test event. POST /v1/cli/trigger

        The CLI `trigger` command sends a realistic sample event (ids `*_test_…`, `test: true`) to the org's listeners and webhook endpoints. `data` overrides fields of the sample. 400 for a topic with no sample; `GET /v1/cli/topics` lists them.

        **Auth:** an API key with `webhooks:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/cli/trigger", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_commission_rules(self, body: PostCommissionRulesBody, *, idempotency_key: Optional[str] = None) -> PostCommissionRulesResponse:
        """Publish a commission rule. POST /v1/commission-rules

        Publishes a new version of a program's commission rule; the latest version applies to new payments, and past lines keep the version that earned them. A rule has a `base` (percent in basis points, or a fixed amount), what it applies to (gross or net of tax or fees), how long it recurs, a hold before lines can be paid (`holdDays`, default 30), and optional conditions, per-partner/link/product overrides, volume tiers, event bounties, sub-affiliate levels and new-vs-expansion rates. Unknown fields at any depth are rejected. Audited.

        **Auth:** an API key with `commissions:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/commission-rules", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_commissions_approve_due(self, *, idempotency_key: Optional[str] = None) -> PostCommissionsApproveDueResponse:
        """Approve due commissions. POST /v1/commissions/approve-due

        Approves every pending line whose hold has elapsed (this also runs on a schedule). Returns how many were approved. Audited.

        **Auth:** an API key with `commissions:write` (or `full`), or a session with role `owner`, `admin`, `finance`.
        """
        return await self._request("POST", f"/v1/commissions/approve-due", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def post_commissions_id_adjust(self, id: str, body: PostCommissionsIdAdjustBody, *, idempotency_key: Optional[str] = None) -> PostCommissionsIdAdjustResponse:
        """Adjust a commission. POST /v1/commissions/{id}/adjust

        Records an `adjusted` event against an earned line (a correction; the ledger is append-only). `amountMinor` is signed. An adjustment that would take the line below zero is refused unless `allowNegative`. Audited.

        **Auth:** an API key with `commissions:write` (or `full`), or a session with role `owner`, `admin`, `finance`.
        """
        return await self._request("POST", f"/v1/commissions/{_seg(id)}/adjust", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_commissions_id_settle(self, id: str, body: PostCommissionsIdSettleBody, *, idempotency_key: Optional[str] = None) -> Settlement:
        """Settle a commission yourself. POST /v1/commissions/{id}/settle

        Marks an earned line paid because you credited the partner yourself (for example as store credit), with your `reference`: records `approved` (if it isn't yet) and `paid`, and publishes `commission.settled`. The line never reaches a payout run or the 1099 export. Repeating the same reference returns the original settlement; a line already paid otherwise is 409. Audited.

        **Auth:** an API key with `commissions:write` (or `full`), or a session with role `owner`, `admin`, `finance`.
        """
        return await self._request("POST", f"/v1/commissions/{_seg(id)}/settle", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_contracts(self, body: PostContractsBody, *, idempotency_key: Optional[str] = None) -> PostContractsResponse:
        """Create a partner contract. POST /v1/contracts

        A contract offering one partner custom terms (`termsMd`) and `compensation` (percent or fixed) in a program, as a draft or sent at once (`send: true`). When accepted, the compensation becomes a partner override on a new rule version. Audited.

        **Auth:** an API key with `partners:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/contracts", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_contracts_id_send(self, id: str, *, idempotency_key: Optional[str] = None) -> OkStatus:
        """Send a contract. POST /v1/contracts/{id}/send

        Sends a draft contract to the partner. 400 when it is not a draft.

        **Auth:** an API key with `partners:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/contracts/{_seg(id)}/send", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def post_coupons(self, body: PostCouponsBody, *, idempotency_key: Optional[str] = None) -> PostCouponsResponse:
        """Create a coupon code. POST /v1/coupons

        Registers a coupon code for a partner in a program, so checkouts that use it attribute to them (coupon codes win over clicks). Codes match case-insensitively and are unique per org (409).

        **Auth:** an API key with `links:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/coupons", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_creators_account_id_invite(self, account_id: str, body: PostCreatorsAccountIdInviteBody, *, idempotency_key: Optional[str] = None) -> PostCreatorsAccountIdInviteResponse:
        """Invite a creator. POST /v1/creators/{accountId}/invite

        Invites a listed creator to a program with an optional message. 400 when they do not accept invitations or were already invited to that program.

        **Auth:** an API key with `growth:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/creators/{_seg(account_id)}/invite", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_deals_id_approve(self, id: str, body: PostDealsIdApproveBody, *, idempotency_key: Optional[str] = None) -> PostDealsIdApproveResponse:
        """Approve a deal. POST /v1/deals/{id}/approve

        Approves a submitted deal and protects it for the partner for `protectionDays` (default 90). 404 when there's no submitted deal with that id.

        **Auth:** an API key with `growth:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/deals/{_seg(id)}/approve", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_deals_id_reject(self, id: str, *, idempotency_key: Optional[str] = None) -> PostDealsIdRejectResponse:
        """Reject a deal. POST /v1/deals/{id}/reject

        Rejects a submitted deal.

        **Auth:** an API key with `growth:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/deals/{_seg(id)}/reject", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def post_deals_id_won(self, id: str, body: PostDealsIdWonBody, *, idempotency_key: Optional[str] = None) -> PostDealsIdWonResponse:
        """Mark a deal won. POST /v1/deals/{id}/won

        Marks an approved deal won, within its protection window: creates the referral for `customerRef` so the customer's payments earn the partner commission. Publishes `referral.created`.

        **Auth:** an API key with `growth:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/deals/{_seg(id)}/won", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_discovery_corpus(self, body: PostDiscoveryCorpusBody, *, idempotency_key: Optional[str] = None) -> PostDiscoveryCorpusResponse:
        """Ingest prospects. POST /v1/discovery/corpus

        Adds up to 500 prospects from your own crawl or data source. Raw page `html` is scanned for affiliate footprints (the competitor programs it recognizes) to enrich the evidence; `keywords` scores fit. Duplicate URLs are skipped. Needs a plan with discovery (402 otherwise).

        **Auth:** an API key with `growth:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/discovery/corpus", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_discovery_search(self, body: PostDiscoverySearchBody, *, idempotency_key: Optional[str] = None) -> PostDiscoverySearchResponse:
        """Search for prospective partners. POST /v1/discovery/search

        Searches the configured corpus for creators and sites matching `keywords` (and `category`), scores their fit and saves them as prospects. Needs a plan with discovery (402 otherwise).

        **Auth:** an API key with `growth:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/discovery/search", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_disputes_id_resolve(self, id: str, body: PostDisputesIdResolveBody, *, idempotency_key: Optional[str] = None) -> Ok:
        """Resolve a dispute. POST /v1/disputes/{id}/resolve

        Resolves an open dispute with a `resolution` note, which the partner sees. Publishes `dispute.resolved`. 404 when not open. Audited.

        **Auth:** an API key with `commissions:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/disputes/{_seg(id)}/resolve", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_email_preview(self, body: PostEmailPreviewBody, *, idempotency_key: Optional[str] = None) -> EmailRendered:
        """Preview an email. POST /v1/email/preview

        Renders an event's email with sample values, from the stored template or an unsaved draft.

        **Auth:** an API key with `org:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/email/preview", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_email_settings_verify_domain(self, *, idempotency_key: Optional[str] = None) -> PostEmailSettingsVerifyDomainResponse:
        """Check the sending domain. POST /v1/email/settings/verify-domain

        Asks the email provider whether the from address's domain is verified for sending, and stores the result. 400 until a provider, key and from address are set.

        **Auth:** an API key with `org:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/email/settings/verify-domain", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def post_email_test(self, body: PostEmailTestBody, *, idempotency_key: Optional[str] = None) -> PostEmailTestResponse:
        """Send a test email. POST /v1/email/test

        Sends one email with sample values to `to` through the org's provider. 400 without a provider or when the provider refuses it.

        **Auth:** an API key with `org:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/email/test", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_embed_tokens(self, body: PostEmbedTokensBody, *, idempotency_key: Optional[str] = None) -> PostEmbedTokensResponse:
        """Mint a partner embed token. POST /v1/embed/tokens

        A 15-minute token for the partner with this email, for the partner stats web component (`/embed.js`) in your app.

        **Auth:** an API key with `links:write` (or `full`), or a session of any role.
        """
        return await self._request("POST", f"/v1/embed/tokens", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_fraud_cases_id_resolve(self, id: str, body: PostFraudCasesIdResolveBody, *, idempotency_key: Optional[str] = None) -> Ok:
        """Resolve a fraud case. POST /v1/fraud/cases/{id}/resolve

        Closes a case with an `action`: `dismiss` (a held referral is approved), `void_referral`, `suspend_partner` or `ban_partner`. The matching `referral.*` events are published. Audited.

        **Auth:** an API key with `fraud:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/fraud/cases/{_seg(id)}/resolve", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_fraud_detect_rings(self, *, idempotency_key: Optional[str] = None) -> PostFraudDetectRingsResponse:
        """Detect referral rings. POST /v1/fraud/detect-rings

        Looks for partners who are likely one operator with many accounts (a shared payout destination or a shared non-freemail sign-up domain) and opens a `ring` case for each group.

        **Auth:** an API key with `fraud:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/fraud/detect-rings", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def post_fraud_invalid_traffic_scan(self, body: PostFraudInvalidTrafficScanBody, *, idempotency_key: Optional[str] = None) -> PostFraudInvalidTrafficScanResponse:
        """Scan for invalid traffic. POST /v1/fraud/invalid-traffic/scan

        Scores each partner's clicks over the last `windowHours` (1 to 168, default 24) for invalid traffic and returns the probability, label and contributing signals per partner, plus how many were flagged.

        **Auth:** an API key with `fraud:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/fraud/invalid-traffic/scan", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_fx_rates(self, body: PostFxRatesBody, *, idempotency_key: Optional[str] = None) -> FxRate:
        """Record an FX rate. POST /v1/fx-rates

        Records the rate cross-currency payouts convert at, for a currency pair, as a decimal string (`"1.0825"`), effective now or at `effectiveAt`. A manual rate pins its pair over the daily feed until cleared. Audited.

        **Auth:** an API key with `payouts:write` (or `full`), or a session with role `owner`, `admin`, `finance`.
        """
        return await self._request("POST", f"/v1/fx-rates", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_fx_rates_clear_override(self, body: PostFxRatesClearOverrideBody, *, idempotency_key: Optional[str] = None) -> PostFxRatesClearOverrideResponse:
        """Clear a manual FX rate. POST /v1/fx-rates/clear-override

        Retires the manual rates for a pair, handing it back to the feed. Returns how many were cleared. Audited.

        **Auth:** an API key with `payouts:write` (or `full`), or a session with role `owner`, `admin`, `finance`.
        """
        return await self._request("POST", f"/v1/fx-rates/clear-override", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_fx_rates_sync(self, *, idempotency_key: Optional[str] = None) -> PostFxRatesSyncResponse:
        """Sync the FX feed now. POST /v1/fx-rates/sync

        Fetches the latest ECB reference rates for this org now, instead of waiting for the daily sync.

        **Auth:** an API key with `payouts:write` (or `full`), or a session with role `owner`, `admin`, `finance`.
        """
        return await self._request("POST", f"/v1/fx-rates/sync", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def post_graphql(self, body: PostGraphqlBody, *, idempotency_key: Optional[str] = None) -> PostGraphqlResponse:
        """Query the GraphQL read layer (POST). POST /v1/graphql

        The GraphQL endpoint with the query in a JSON body. Read-only, so a read-scoped API key may call it.

        **Auth:** an API key with `analytics:read` (or `full`), or a session of any role.
        """
        return await self._request("POST", f"/v1/graphql", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_import_provider(self, provider: str, body: PostImportProviderBody, *, program_id: str, dry_run: Optional[bool] = None, destination_url: Optional[str] = None, idempotency_key: Optional[str] = None) -> PostImportProviderResponse:
        """Import partners from another tool. POST /v1/import/{provider}

        Imports partners, links and codes from a Rewardful, FirstPromoter, Tolt or PartnerStack CSV export (as a `text/csv` body or `{ "csv": "…" }`) into a program. `dryRun=true` reports what would happen; `destinationUrl` is used when the export has no link column. The tool's referral parameter is added to aff.js so shared links keep crediting. Audited.

        **Auth:** an API key with `integrations:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/import/{_seg(provider)}", query={"programId": program_id, "dryRun": dry_run, "destinationUrl": destination_url}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_integrations_deliveries_id_retry(self, id: str, *, idempotency_key: Optional[str] = None) -> IntegrationDelivery:
        """Retry an integration delivery. POST /v1/integrations/deliveries/{id}/retry

        Queues a failed or skipped delivery again. 404 when there is no failed or skipped delivery with that id.

        **Auth:** an API key with `integrations:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/integrations/deliveries/{_seg(id)}/retry", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def post_integrations_hubspot_test(self, body: PostIntegrationsHubspotTestBody, *, idempotency_key: Optional[str] = None) -> PostIntegrationsHubspotTestResponse:
        """Test the HubSpot connection. POST /v1/integrations/hubspot/test

        Checks the token against HubSpot and (unless `setupProperties: false`) creates the custom properties the sync uses. Returns `ok` and the error, if any, rather than failing.

        **Auth:** an API key with `integrations:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/integrations/hubspot/test", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_integrations_segment_test(self, *, idempotency_key: Optional[str] = None) -> PostIntegrationsSegmentTestResponse:
        """Test the Segment connection. POST /v1/integrations/segment/test

        Sends one test track event with the write key and reports whether Segment accepted it.

        **Auth:** an API key with `integrations:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/integrations/segment/test", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def post_invitations_id_withdraw(self, id: str, *, idempotency_key: Optional[str] = None) -> OkStatus:
        """Withdraw an invitation. POST /v1/invitations/{id}/withdraw

        Withdraws a pending creator invitation. 400 when it was already answered or withdrawn.

        **Auth:** an API key with `partners:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/invitations/{_seg(id)}/withdraw", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def post_links(self, body: PostLinksBody, *, idempotency_key: Optional[str] = None) -> CreatedLink:
        """Create a tracked link. POST /v1/links

        Creates a partner's tracked link in a program. `code` (letters, digits, `-`; stored lowercase) is unique per org and generated when omitted. Returns the `shortUrl` to share, on the org's verified link domain when it has one. 409 when the code is taken. Audited.

        **Auth:** an API key with `links:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/links", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_mobile_purchases(self, body: PostMobilePurchasesBody, *, idempotency_key: Optional[str] = None) -> PostMobilePurchasesResponse:
        """Report an in-app purchase. POST /v1/mobile/purchases

        Your backend reports a validated App Store or Play purchase (or refund), after checking the receipt; it flows through the same commission engine as web billing. Idempotent per `eventId`. Never call this from the app itself.

        **Auth:** an API key with `billing:write` (or `full`), or a session with role `owner`, `admin`, `finance`.
        """
        return await self._request("POST", f"/v1/mobile/purchases", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_notifications_id_read(self, id: str, *, idempotency_key: Optional[str] = None) -> Ok:
        """Mark a notification read. POST /v1/notifications/{id}/read

        Marks one notification read. Unknown or already-read ids are a no-op.

        **Auth:** an API key with `org:write` (or `full`), or a session of any role.
        """
        return await self._request("POST", f"/v1/notifications/{_seg(id)}/read", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def post_onchain_connections(self, body: PostOnchainConnectionsBody, *, idempotency_key: Optional[str] = None) -> PostOnchainConnectionsResponse:
        """Create an on-chain connection. POST /v1/onchain/connections

        Connects an on-chain indexer: on-chain conversions posted to its webhook URL become billing events. Returns the webhook URL and signing secret.

        **Auth:** an API key with `billing:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/onchain/connections", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_org_members(self, body: PostOrgMembersBody, *, idempotency_key: Optional[str] = None) -> PostOrgMembersResponse:
        """Add a team member. POST /v1/org/members

        Adds an existing Referalli user (by email) with a role: `owner`, `admin`, `finance`, `analyst` or `support`. Only an owner can add an owner. 404 when no user has that email; 409 when already a member. Live mode only.

        **Auth:** an API key with `team:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/org/members", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_orgs(self, body: PostOrgsBody, *, idempotency_key: Optional[str] = None) -> PostOrgsResponse:
        """Create an organization. POST /v1/orgs

        Creates an organization with the signed-in user as its owner. Needs a user session (not an API key) but no `x-org-id`. Limited to 20 per hour per user. Live mode only.

        **Auth:** an API key with `team:write` (or `full`), or a session of any role.
        """
        return await self._request("POST", f"/v1/orgs", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_org_sso_link(self, *, idempotency_key: Optional[str] = None) -> PostOrgSsoLinkResponse:
        """Link the org to SSO. POST /v1/org/sso/link

        Creates the org's directory tenant at the SSO provider, with the calling owner (who must have signed in with the provider) as its first admin. Owner session only. 409 when already linked elsewhere. Live mode only.

        **Auth:** an API key with `org:write` (or `full`), or a session with role `owner`.
        """
        return await self._request("POST", f"/v1/org/sso/link", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def post_org_sso_tickets(self, body: PostOrgSsoTicketsBody, *, idempotency_key: Optional[str] = None) -> PostOrgSsoTicketsResponse:
        """Create an SSO setup link. POST /v1/org/sso/tickets

        A one-time link (valid `expiresInDays`, default 3) for the customer's IT admin to configure SAML or OIDC (and SCIM) on the provider's hosted page. The URL is returned once and never stored. Live mode only.

        **Auth:** an API key with `org:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/org/sso/tickets", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_org_sso_tickets_id_revoke(self, id: str, *, idempotency_key: Optional[str] = None) -> PostOrgSsoTicketsIdRevokeResponse:
        """Revoke an SSO setup link. POST /v1/org/sso/tickets/{id}/revoke

        Revokes a pending setup link. Live mode only.

        **Auth:** an API key with `org:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/org/sso/tickets/{_seg(id)}/revoke", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def post_outreach_draft(self, body: PostOutreachDraftBody, *, idempotency_key: Optional[str] = None) -> PostOutreachDraftResponse:
        """Draft an outreach sequence. POST /v1/outreach/draft

        Drafts a recruiting email sequence for a prospect. Drafts are only sent after you approve them.

        **Auth:** an API key with `growth:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/outreach/draft", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_outreach_id_approve(self, id: str, *, idempotency_key: Optional[str] = None) -> Ok:
        """Approve an outreach message. POST /v1/outreach/{id}/approve

        Approves a drafted message so `POST /v1/outreach/send-due` sends it when due. Audited.

        **Auth:** an API key with `growth:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/outreach/{_seg(id)}/approve", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def post_outreach_send_due(self, *, idempotency_key: Optional[str] = None) -> PostOutreachSendDueResponse:
        """Send due outreach. POST /v1/outreach/send-due

        Sends approved outreach messages that are due, skipping prospects without an email and addresses on the do-not-contact list (unsubscribed).

        **Auth:** an API key with `growth:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/outreach/send-due", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def post_partner_advance_accept(self, body: PostPartnerAdvanceAcceptBody, *, idempotency_key: Optional[str] = None) -> PostPartnerAdvanceAcceptResponse:
        """Take a commission advance. POST /v1/partner/advance/accept

        Takes an advance of `amountMinor` (up to the offer). The principal plus fee is repaid by withholding future commissions from payouts.

        **Auth:** a partner session.
        """
        return await self._request("POST", f"/v1/partner/advance/accept", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_partner_auth_wallet_nonce(self, body: PostPartnerAuthWalletNonceBody, *, idempotency_key: Optional[str] = None) -> PostPartnerAuthWalletNonceResponse:
        """Get a wallet sign-in nonce. POST /v1/partner/auth/wallet/nonce

        Starts wallet sign-in (and AI agent registration): returns a single-use nonce, valid 10 minutes, and the message to sign with the wallet.

        **Auth:** none.
        """
        return await self._request("POST", f"/v1/partner/auth/wallet/nonce", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_partner_auth_wallet_verify(self, body: PostPartnerAuthWalletVerifyBody, *, idempotency_key: Optional[str] = None) -> PostPartnerAuthWalletVerifyResponse:
        """Sign in with a wallet. POST /v1/partner/auth/wallet/verify

        Verifies the wallet's signature over the nonce message and signs the partner in (creating the account on first use), setting the session cookie. 401 for an expired nonce or a signature that does not match.

        **Auth:** none.
        """
        return await self._request("POST", f"/v1/partner/auth/wallet/verify", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_partner_contracts_id_accept(self, id: str, *, idempotency_key: Optional[str] = None) -> OkStatus:
        """Accept a contract. POST /v1/partner/contracts/{id}/accept

        Accepts a sent contract; its compensation then applies to the partner's commissions in that program.

        **Auth:** a partner session.
        """
        return await self._request("POST", f"/v1/partner/contracts/{_seg(id)}/accept", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def post_partner_contracts_id_decline(self, id: str, *, idempotency_key: Optional[str] = None) -> OkStatus:
        """Decline a contract. POST /v1/partner/contracts/{id}/decline

        Declines a sent contract.

        **Auth:** a partner session.
        """
        return await self._request("POST", f"/v1/partner/contracts/{_seg(id)}/decline", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def post_partner_deals(self, body: PostPartnerDealsBody, *, idempotency_key: Optional[str] = None) -> PostPartnerDealsResponse:
        """Register a deal. POST /v1/partner/deals

        A partner registers a B2B deal (company, contact, expected value) in a program they are approved in, for the merchant to approve. Publishes `deal.submitted`.

        **Auth:** a partner session.
        """
        return await self._request("POST", f"/v1/partner/deals", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_partner_disputes(self, body: PostPartnerDisputesBody, *, idempotency_key: Optional[str] = None) -> PostPartnerDisputesResponse:
        """File a dispute. POST /v1/partner/disputes

        Files a dispute with a merchant about a missing attribution or an unpaid commission, optionally for a referral. The merchant resolves it.

        **Auth:** a partner session.
        """
        return await self._request("POST", f"/v1/partner/disputes", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_partner_invitations_id_accept(self, id: str, *, idempotency_key: Optional[str] = None) -> OkStatus:
        """Accept an invitation. POST /v1/partner/invitations/{id}/accept

        Accepts a pending invitation: the partner is created in the merchant's org if needed and enrolled, approved. The merchant is notified.

        **Auth:** a partner session.
        """
        return await self._request("POST", f"/v1/partner/invitations/{_seg(id)}/accept", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def post_partner_invitations_id_decline(self, id: str, *, idempotency_key: Optional[str] = None) -> OkStatus:
        """Decline an invitation. POST /v1/partner/invitations/{id}/decline

        Declines a pending invitation. The merchant is notified.

        **Auth:** a partner session.
        """
        return await self._request("POST", f"/v1/partner/invitations/{_seg(id)}/decline", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def post_partner_kyc_submit(self, body: PostPartnerKycSubmitBody, *, idempotency_key: Optional[str] = None) -> PostPartnerKycSubmitResponse:
        """Submit identity verification. POST /v1/partner/kyc/submit

        Submits the partner's legal name, country and optional date of birth and document reference for identity verification and sanctions screening. Merchants that require KYC pay only verified partners. Limited to 5 per hour per IP.

        **Auth:** a partner session.
        """
        return await self._request("POST", f"/v1/partner/kyc/submit", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_partner_links(self, body: PostPartnerLinksBody, *, idempotency_key: Optional[str] = None) -> CreatedLink:
        """Create a link. POST /v1/partner/links

        Creates a tracked link in a program the partner is approved in (403 otherwise), optionally for one of the program's marketing assets. `code` is generated when omitted; 409 when taken.

        **Auth:** a partner session.
        """
        return await self._request("POST", f"/v1/partner/links", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_partner_notifications_id_read(self, id: str, *, idempotency_key: Optional[str] = None) -> Ok:
        """Mark my notification read. POST /v1/partner/notifications/{id}/read

        Marks one of the partner's notifications read.

        **Auth:** a partner session.
        """
        return await self._request("POST", f"/v1/partner/notifications/{_seg(id)}/read", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def post_partner_orgs_org_id_self_billing(self, org_id: str, body: PostPartnerOrgsOrgIdSelfBillingBody, *, idempotency_key: Optional[str] = None) -> PostPartnerOrgsOrgIdSelfBillingResponse:
        """Accept self-billing. POST /v1/partner/orgs/{orgId}/self-billing

        Accepts the current self-billing agreement with this merchant (`{ "accept": true }`), so the merchant issues the invoices for the partner's payouts. 404 until payout details exist.

        **Auth:** a partner session.
        """
        return await self._request("POST", f"/v1/partner/orgs/{_seg(org_id)}/self-billing", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_partner_orgs_org_id_tax_form(self, org_id: str, body: PostPartnerOrgsOrgIdTaxFormBody, *, idempotency_key: Optional[str] = None) -> Ok:
        """Submit my tax form. POST /v1/partner/orgs/{orgId}/tax-form

        Submits a W-9, W-8BEN or W-8BEN-E to this merchant. A tax form is required before the partner is included in payouts.

        **Auth:** a partner session.
        """
        return await self._request("POST", f"/v1/partner/orgs/{_seg(org_id)}/tax-form", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_partner_programs_program_id_apply(self, program_id: str, *, idempotency_key: Optional[str] = None) -> PostPartnerProgramsProgramIdApplyResponse:
        """Apply to a program. POST /v1/partner/programs/{programId}/apply

        Applies to an active program (for example from the marketplace), creating the partner in that merchant's org if needed. The merchant approves or rejects it. Publishes `partner.applied`. 403 for blocked accounts.

        **Auth:** a partner session.
        """
        return await self._request("POST", f"/v1/partner/programs/{_seg(program_id)}/apply", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def post_partners(self, body: PostPartnersBody, *, idempotency_key: Optional[str] = None) -> Partner:
        """Create a partner. POST /v1/partners

        Creates a partner. `email` is unique per org, and so is `externalRef` (your own id for them, such as a user id). With `upsert: true` an existing partner matching the email or externalRef is returned instead of a 409 (and gets the externalRef if it had none). Over the plan's partner limit this is `402 payment_required`. Audited.

        **Auth:** an API key with `partners:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/partners", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_partner_security_totp_disable(self, body: PostPartnerSecurityTotpDisableBody, *, idempotency_key: Optional[str] = None) -> PostPartnerSecurityTotpDisableResponse:
        """Turn off two-factor. POST /v1/partner/security/totp/disable

        Turns two-factor off; needs a valid current `code`. 401 for a wrong code.

        **Auth:** a partner session.
        """
        return await self._request("POST", f"/v1/partner/security/totp/disable", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_partner_security_totp_enable(self, body: PostPartnerSecurityTotpEnableBody, *, idempotency_key: Optional[str] = None) -> PostPartnerSecurityTotpEnableResponse:
        """Turn on two-factor. POST /v1/partner/security/totp/enable

        Confirms setup with a current 6-digit `code`. From then on, changing payout details needs a code in `x-totp-code`. 401 for a wrong code.

        **Auth:** a partner session.
        """
        return await self._request("POST", f"/v1/partner/security/totp/enable", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_partner_security_totp_setup(self, *, idempotency_key: Optional[str] = None) -> PostPartnerSecurityTotpSetupResponse:
        """Start two-factor setup. POST /v1/partner/security/totp/setup

        Generates a TOTP secret and its `otpauth://` URI for an authenticator app. 400 when two-factor is already on.

        **Auth:** a partner session.
        """
        return await self._request("POST", f"/v1/partner/security/totp/setup", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def post_partners_id_tax_form(self, id: str, body: PostPartnersIdTaxFormBody, *, idempotency_key: Optional[str] = None) -> Ok:
        """Record a partner's tax form. POST /v1/partners/{id}/tax-form

        Records a W-9, W-8BEN or W-8BEN-E for the partner (`data` is the form's fields). A tax form on file is required before a partner is included in a payout run.

        **Auth:** an API key with `payouts:write` (or `full`), or a session with role `owner`, `admin`, `finance`.
        """
        return await self._request("POST", f"/v1/partners/{_seg(id)}/tax-form", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_partner_terms_version_id_accept(self, version_id: str, *, idempotency_key: Optional[str] = None) -> Ok:
        """Accept program terms. POST /v1/partner/terms/{versionId}/accept

        Records the partner's acceptance of a terms version. Repeating it is a no-op.

        **Auth:** a partner session.
        """
        return await self._request("POST", f"/v1/partner/terms/{_seg(version_id)}/accept", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def post_passport_verify(self, body: PostPassportVerifyBody, *, idempotency_key: Optional[str] = None) -> PostPassportVerifyResponse:
        """Verify a partner passport. POST /v1/passport/verify

        Checks a partner's signed reputation passport: `valid: true` with its claims, or `valid: false` with the reason (bad signature, expired). No authentication.

        **Auth:** none.
        """
        return await self._request("POST", f"/v1/passport/verify", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_payout_runs(self, *, idempotency_key: Optional[str] = None) -> PayoutRunCreated:
        """Create a payout run. POST /v1/payout-runs

        Builds a draft run: one payout per partner who has a payout profile, a tax form and an approved, unpaid balance over their threshold, converted into their payout currency at recorded FX, each with a self-billing invoice. Partners left out are listed in `skipped` with the reason. Nothing is paid until you execute it. Audited.

        **Auth:** an API key with `payouts:write` (or `full`), or a session with role `owner`, `admin`, `finance`.
        """
        return await self._request("POST", f"/v1/payout-runs", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def post_payout_runs_id_cancel(self, id: str, *, idempotency_key: Optional[str] = None) -> PostPayoutRunsIdCancelResponse:
        """Cancel a payout run. POST /v1/payout-runs/{id}/cancel

        Cancels a run that hasn't paid out and releases its lines back to the partners' approved balances. A run with money in flight is 409. Publishes `payout.cancelled` per payout. Audited.

        **Auth:** an API key with `payouts:write` (or `full`), or a session with role `owner`, `admin`, `finance`.
        """
        return await self._request("POST", f"/v1/payout-runs/{_seg(id)}/cancel", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def post_payout_runs_id_execute(self, id: str, *, idempotency_key: Optional[str] = None) -> PostPayoutRunsIdExecuteResponse:
        """Execute a payout run. POST /v1/payout-runs/{id}/execute

        Pays a draft run through the org's own connected payout providers (methods with no connection are simulated and logged; test mode uses the test rail). Returns how many were sent, submitted (settling asynchronously) and failed; each outcome publishes `payout.sent`, `payout.submitted` or `payout.failed`. Audited.

        **Auth:** an API key with `payouts:write` (or `full`), or a session with role `owner`, `admin`, `finance`.
        """
        return await self._request("POST", f"/v1/payout-runs/{_seg(id)}/execute", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def post_payout_runs_run_scheduled(self, *, idempotency_key: Optional[str] = None) -> PostPayoutRunsRunScheduledResponse:
        """Run due payout schedules. POST /v1/payout-runs/run-scheduled

        Creates and executes payout runs for every schedule (org or program) that is due now. This also runs hourly on its own.

        **Auth:** an API key with `payouts:write` (or `full`), or a session with role `owner`, `admin`, `finance`.
        """
        return await self._request("POST", f"/v1/payout-runs/run-scheduled", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def post_privacy_forget(self, body: PostPrivacyForgetBody, *, idempotency_key: Optional[str] = None) -> PostPrivacyForgetResponse:
        """Erase a data subject. POST /v1/privacy/forget

        Erases (pseudonymizes, keeping the ledger balanced) a customer by `customerRef`, a partner by `partnerId`, or by `email` both the partner with that email and every customer stored under its hash. Send exactly one. 400 when nothing is found. Audited.

        **Auth:** an API key with `privacy:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/privacy/forget", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_privacy_lookup(self, body: PostPrivacyLookupBody, *, idempotency_key: Optional[str] = None) -> PostPrivacyLookupResponse:
        """Find a data subject by email. POST /v1/privacy/lookup

        Which customers and partners an email refers to. The email is hashed on the server and never stored.

        **Auth:** an API key with `privacy:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/privacy/lookup", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_privacy_requests(self, body: PostPrivacyRequestsBody, *, idempotency_key: Optional[str] = None) -> PostPrivacyRequestsResponse:
        """Open a data-subject request. POST /v1/privacy/requests

        Opens an `access` or `erasure` request for one subject (`email`, `customerRef` or `partnerId`) and answers `202` with the request to poll. Publishes `privacy.request_completed` when done.

        **Auth:** an API key with `privacy:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/privacy/requests", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_profitability_rebuild(self, *, idempotency_key: Optional[str] = None) -> PostProfitabilityRebuildResponse:
        """Rebuild ROI figures. POST /v1/profitability/rebuild

        Recomputes every stored ROI figure from the value events with the current settings and mappings, in the background. Returns a `jobId` to poll; while one rebuild is running, the same job is returned. Audited.

        **Auth:** an API key with `analytics:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/profitability/rebuild", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def post_programs(self, body: PostProgramsBody, *, idempotency_key: Optional[str] = None) -> Program:
        """Create a program. POST /v1/programs

        Creates an affiliate program: its attribution model, cookie window, how long after sign-up a conversion still counts, terms, public page and settings. `slug` is unique per org. Terms are versioned so partners can be asked to accept new ones. Over the plan's program limit this is `402 payment_required`.

        **Auth:** an API key with `programs:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/programs", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_programs_id_apply_leveling(self, id: str, *, idempotency_key: Optional[str] = None) -> PostProgramsIdApplyLevelingResponse:
        """Apply partner levels. POST /v1/programs/{id}/apply-leveling

        Promotes the program's partners to the highest level their referral count qualifies for (never demotes). Publishes `partner.level_up` per promotion.

        **Auth:** an API key with `programs:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/programs/{_seg(id)}/apply-leveling", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def post_programs_id_autoprice_run(self, id: str, body: PostProgramsIdAutopriceRunBody, *, idempotency_key: Optional[str] = None) -> PostProgramsIdAutopriceRunResponse:
        """Run autopricing. POST /v1/programs/{id}/autoprice/run

        Moves each partner's rate toward the target and publishes the new rates as partner overrides on a new rule version. Objective `roas` compares attributed revenue to commission; `roi` uses each partner's matured referral ROI, holding partners with too few matured referrals or an unknown ROI (listed in `held`). 400 when autopricing is off, the program has no percent-based rule, or no partner has a known ROI under `roi`.

        **Auth:** an API key with `programs:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/programs/{_seg(id)}/autoprice/run", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_programs_id_enrollments(self, id: str, body: PostProgramsIdEnrollmentsBody, *, idempotency_key: Optional[str] = None) -> Enrollment:
        """Enroll a partner. POST /v1/programs/{id}/enrollments

        Enrolls an existing partner in the program, approved at once. Publishes `partner.enrolled`. 409 when already enrolled.

        **Auth:** an API key with `programs:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/programs/{_seg(id)}/enrollments", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_programs_id_enrollments_enrollment_id_approve(self, id: str, enrollment_id: str, *, idempotency_key: Optional[str] = None) -> PostProgramsIdEnrollmentsEnrollmentIdApproveResponse:
        """Approve an application. POST /v1/programs/{id}/enrollments/{enrollmentId}/approve

        Approves a pending application (`status: "applied"`). Publishes `partner.approved`. 404 when there is no pending application with that id. Audited.

        **Auth:** an API key with `programs:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/programs/{_seg(id)}/enrollments/{_seg(enrollment_id)}/approve", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def post_programs_id_enrollments_enrollment_id_reject(self, id: str, enrollment_id: str, *, idempotency_key: Optional[str] = None) -> PostProgramsIdEnrollmentsEnrollmentIdRejectResponse:
        """Reject an application. POST /v1/programs/{id}/enrollments/{enrollmentId}/reject

        Rejects a pending application. 404 when there is no pending application with that id. Audited.

        **Auth:** an API key with `programs:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/programs/{_seg(id)}/enrollments/{_seg(enrollment_id)}/reject", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def post_programs_id_groups(self, id: str, body: PostProgramsIdGroupsBody, *, idempotency_key: Optional[str] = None) -> PartnerGroup:
        """Create a partner group. POST /v1/programs/{id}/groups

        A group of partners in a program with its own commission base (or `null` to keep the program rule's), hold days, payout threshold, payout currency, onboarding message and checklist. Names are unique per program (409).

        **Auth:** an API key with `programs:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/programs/{_seg(id)}/groups", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_programs_id_promotions(self, id: str, body: PostProgramsIdPromotionsBody, *, idempotency_key: Optional[str] = None) -> Promotion:
        """Create a promotion. POST /v1/programs/{id}/promotions

        A time-boxed commission change for the whole program or one group: `replace` the base rate, or `boost` it by `bps`, between `startsAt` and `endsAt`. Payments in that window get it.

        **Auth:** an API key with `programs:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/programs/{_seg(id)}/promotions", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_promotions_id_end(self, id: str, *, idempotency_key: Optional[str] = None) -> Promotion:
        """End a promotion. POST /v1/promotions/{id}/end

        Ends a promotion now: payments from this moment on no longer get it.

        **Auth:** an API key with `programs:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/promotions/{_seg(id)}/end", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def post_public_programs_handle_join(self, handle: str, body: PostPublicProgramsHandleJoinBody, *, idempotency_key: Optional[str] = None) -> PostPublicProgramsHandleJoinResponse:
        """Join a program. POST /v1/public/programs/{handle}/join

        One-step join from the public page for a signed-in partner: creates (or claims, with a verified email) the partner in the merchant's org and enrolls them, approved with a first link when the program auto-approves, otherwise as an application. Publishes `partner.approved` or `partner.applied`. 409 when the merchant's partner with that email belongs to another account.

        **Auth:** a partner session.
        """
        return await self._request("POST", f"/v1/public/programs/{_seg(handle)}/join", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_quality_recompute(self, *, idempotency_key: Optional[str] = None) -> PostQualityRecomputeResponse:
        """Recompute quality scores. POST /v1/quality/recompute

        Snapshots every partner's quality score now; per the org's policy, low scores open a `quality` case or suspend the partner. Audited.

        **Auth:** an API key with `partners:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/quality/recompute", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def post_referrals_associate(self, body: PostReferralsAssociateBody, *, idempotency_key: Optional[str] = None) -> AssociateResponse:
        """Attribute a new customer. POST /v1/referrals/associate

        The key server-side call: tell Referalli a customer signed up, with whatever you know about where they came from (`referralToken`/`ref_click_id`, `anonId`, `couponCode`, `emailHash`, IP and user agent). The attribution engine picks the partner under the program's model and windows. `referral` is `null` when no partner matched (not an error); `reasoning.notes` says why. Repeating `idempotencyKey` returns the existing referral. `occurredAt` records a late call at the real sign-up time (up to 5 minutes of clock skew is tolerated) and backfills payments since. `emailDomain` lets burner-email sign-ups be held for review. Publishes `referral.created` (or `referral.held`).

        **Auth:** an API key with `referrals:write` (or `full`), or a session of any role.
        """
        return await self._request("POST", f"/v1/referrals/associate", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_referrals_id_approve(self, id: str, *, idempotency_key: Optional[str] = None) -> Referral:
        """Approve a held referral. POST /v1/referrals/{id}/approve

        Releases a referral held for review (`pending_review`) back to `active`. 404 when it isn't pending review. Publishes `referral.approved`. Audited.

        **Auth:** an API key with `referrals:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/referrals/{_seg(id)}/approve", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def post_referrals_id_reassign(self, id: str, body: PostReferralsIdReassignBody, *, idempotency_key: Optional[str] = None) -> Referral:
        """Reassign a referral. POST /v1/referrals/{id}/reassign

        Moves the referral to another partner (recorded as a manual match). Publishes `referral.reassigned` with the previous partner. Audited.

        **Auth:** an API key with `referrals:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/referrals/{_seg(id)}/reassign", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_referrals_id_void(self, id: str, *, idempotency_key: Optional[str] = None) -> Referral:
        """Void a referral. POST /v1/referrals/{id}/void

        Voids the referral so it earns nothing more. Publishes `referral.voided`. Audited.

        **Auth:** an API key with `referrals:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/referrals/{_seg(id)}/void", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def post_rewards_id_redeem(self, id: str, body: PostRewardsIdRedeemBody, *, idempotency_key: Optional[str] = None) -> PostRewardsRedeemByCodeResponse:
        """Redeem a reward. POST /v1/rewards/{id}/redeem

        Records a (possibly partial) redemption: `amountMinor` (default the remaining balance) is capped at what's left, and the reward becomes `redeemed` once it is used up. `externalId` makes it idempotent (409 if reused for another reward). Publishes `credit.redeemed`.

        **Auth:** an API key with `commissions:write` (or `full`), or a session with role `owner`, `admin`, `finance`.
        """
        return await self._request("POST", f"/v1/rewards/{_seg(id)}/redeem", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_rewards_redeem_by_code(self, body: PostRewardsRedeemByCodeBody, *, idempotency_key: Optional[str] = None) -> PostRewardsRedeemByCodeResponse:
        """Redeem a reward by code. POST /v1/rewards/redeem-by-code

        Records a redemption of the reward with this code; see `POST /v1/rewards/{id}/redeem`. 404 for an unknown code.

        **Auth:** an API key with `commissions:write` (or `full`), or a session with role `owner`, `admin`, `finance`.
        """
        return await self._request("POST", f"/v1/rewards/redeem-by-code", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_roi_patterns_pattern_review(self, pattern: str, body: PostRoiPatternsPatternReviewBody, *, idempotency_key: Optional[str] = None) -> FraudCase:
        """Open a review for a pattern match. POST /v1/roi/patterns/{pattern}/review

        Turns one live pattern match (by `customerRef` and/or `partnerId`, optionally `programId`) into a `value_pattern` fraud case against its partner, or returns the open case for the same match. Publishes `fraud.case_opened`. 404 when no such match exists. Audited.

        **Auth:** an API key with `analytics:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/roi/patterns/{_seg(pattern)}/review", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_sandbox_simulate(self, body: PostSandboxSimulateBody, *, idempotency_key: Optional[str] = None) -> PostSandboxSimulateResponse:
        """Simulate billing history. POST /v1/sandbox/simulate

        Generates deterministic billing history through the real commission pipeline, so you can see commissions flow without a provider: a new sandbox customer referred to the partner, `months` (default 3) of subscription payments at `priceMinor`, then for `scenario: "refund"` a half refund of the first invoice or for `churn` a cancellation. Returns the customer and what was created. Audited.

        **Auth:** an API key with `billing:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/sandbox/simulate", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_tax1099_documents_id_correct(self, id: str, *, idempotency_key: Optional[str] = None) -> TaxFiling:
        """File a corrected 1099. POST /v1/tax/1099/documents/{id}/correct

        Files a corrected form for one document with the partner's current amount. Audited.

        **Auth:** an API key with `payouts:write` (or `full`), or a session with role `owner`, `admin`, `finance`.
        """
        return await self._request("POST", f"/v1/tax/1099/documents/{_seg(id)}/correct", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def post_tax1099_filings(self, body: PostTax1099FilingsBody, *, idempotency_key: Optional[str] = None) -> TaxFiling:
        """File 1099-NEC forms. POST /v1/tax/1099/filings

        E-files the year's 1099-NEC forms through the connected provider and records one document per partner. Audited.

        **Auth:** an API key with `payouts:write` (or `full`), or a session with role `owner`, `admin`, `finance`.
        """
        return await self._request("POST", f"/v1/tax/1099/filings", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_tax1099_filings_id_refresh(self, id: str, *, idempotency_key: Optional[str] = None) -> PostTax1099FilingsIdRefreshResponse:
        """Refresh a filing status. POST /v1/tax/1099/filings/{id}/refresh

        Asks the filing provider for the latest status of a filing and its documents; accepted forms are then delivered to partners (`tax.form_delivered`).

        **Auth:** an API key with `payouts:write` (or `full`), or a session with role `owner`, `admin`, `finance`.
        """
        return await self._request("POST", f"/v1/tax/1099/filings/{_seg(id)}/refresh", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def post_test_clock_advance(self, body: PostTestClockAdvanceBody, *, idempotency_key: Optional[str] = None) -> PostTestClockAdvanceResponse:
        """Advance the test clock. POST /v1/test_clock/advance

        Test mode only. Moves the test org's clock forward by `seconds` (never back), then runs what came due: held commissions are approved, payout schedules fire and retention purges run. Returns the new time and what ran. Audited.

        **Auth:** an API key with `org:write` (or `full`), or a session with role `owner`, `admin`, `finance`.
        """
        return await self._request("POST", f"/v1/test_clock/advance", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_track_events(self, body: Union[PostTrackEventsBodyOption1, PostTrackEventsBodyOption2, PostTrackEventsBodyOption3], *, idempotency_key: Optional[str] = None) -> PostTrackEventsResponse:
        """Track an event. POST /v1/track/events

        Records one event. `type: "event"` is a product event for a known customer (`event`, such as `trial_started`) that can pay a bounty under the program's commission rule; it returns whether it was recorded and the commission. `idempotencyKey` deduplicates. `type: "click"` records a server-side click for a partner; `type: "custom"` records an audited custom event. Publishable keys may send only custom events.

        **Auth:** an API key with `events:write` (or `full`), or a session of any role.
        """
        return await self._request("POST", f"/v1/track/events", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_unsubscribe_token(self, token: str, *, idempotency_key: Optional[str] = None) -> PostUnsubscribeTokenResponse:
        """Unsubscribe from outreach. POST /v1/unsubscribe/{token}

        The one-click unsubscribe link in outreach emails. No authentication; the token identifies the recipient.

        **Auth:** none.
        """
        return await self._request("POST", f"/v1/unsubscribe/{_seg(token)}", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def post_value_events(self, body: PostValueEventsBody, *, idempotency_key: Optional[str] = None) -> PostValueEventsResponse:
        """Record value events. POST /v1/value/events

        Reports up to 500 value facts from your platform: `payment`, `refund`, `credit_granted`, `credit_redeemed`, `credit_expired`, `credit_revoked`, `cost` or `adjustment`. Each needs `kind`, `currency`, `externalId` (your stable id, which makes it idempotent) and `occurredAt`, plus the customer, partner (`partnerId` or `partnerExternalRef`), grant, program, product and amount fields (`cashMinor`, `creditAppliedMinor`, `discountMinor`, `taxMinor`, `feesMinor`, `costMinor`, `faceMinor`) that apply. Each event is validated and recorded on its own: `results` and `errors` are by index. A repeat of an `externalId` with new figures supersedes the earlier one.

        **Auth:** an API key with `analytics:write` (or `full`), or a session of any role.
        """
        return await self._request("POST", f"/v1/value/events", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_value_import(self, body: PostValueImportBody, *, idempotency_key: Optional[str] = None) -> PostValueImportResponse:
        """Import value events from CSV. POST /v1/value/import

        Imports value events from CSV text (up to 10,000 rows and 5 MB, else `413 payload_too_large`) with a `mapping` from column names to event fields (money as `<field>Minor` or `<field>Major`). `kind` applies to every row unless a column maps to it. Up to 500 rows are recorded before the response; a larger file answers `202` with a `jobId` to poll. `dryRun` returns the first 20 parsed rows and every row error without recording.

        **Auth:** an API key with `analytics:write` (or `full`), or a session of any role.
        """
        return await self._request("POST", f"/v1/value/import", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_webhook_deliveries_id_replay(self, id: str, *, idempotency_key: Optional[str] = None) -> Ok:
        """Replay a webhook delivery. POST /v1/webhook-deliveries/{id}/replay

        Queues the delivery again at once with its attempt count reset. It keeps its `webhook-id`, so receivers can deduplicate.

        **Auth:** an API key with `webhooks:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/webhook-deliveries/{_seg(id)}/replay", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def post_webhook_endpoints(self, body: PostWebhookEndpointsBody, *, idempotency_key: Optional[str] = None) -> PostWebhookEndpointsResponse:
        """Create a webhook endpoint. POST /v1/webhook-endpoints

        Subscribes an HTTPS URL to event topics (default `["*"]`, every event; see the `webhooks` section of this document for each topic's payload). `programIds` limits it to events about those programs (org-wide events such as payouts are then not sent). Deliveries are signed the Standard Webhooks way with the returned `secret` (`whsec_…`), shown only here. `legacySignature: true` also sends the deprecated body-only signature.

        **Auth:** an API key with `webhooks:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/webhook-endpoints", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_webhook_endpoints_id_rotate_secret(self, id: str, *, idempotency_key: Optional[str] = None) -> PostWebhookEndpointsIdRotateSecretResponse:
        """Rotate an endpoint secret. POST /v1/webhook-endpoints/{id}/rotate-secret

        Issues a new signing secret, returned once. For 24 hours (`previousSecretExpiresAt`) every delivery carries a signature from each secret, so receivers can switch without dropping any. Audited.

        **Auth:** an API key with `webhooks:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/webhook-endpoints/{_seg(id)}/rotate-secret", query={}, body=None, idempotency_key=idempotency_key, kind="json")

    async def post_widget_tokens(self, body: PostWidgetTokensBody, *, idempotency_key: Optional[str] = None) -> PostWidgetTokensResponse:
        """Mint a referral widget token. POST /v1/widget/tokens

        Your backend mints a short-lived token (60 to 3600 seconds, default 900) for a signed-in customer, identified by `customerRef` or `partnerExternalRef`, for the in-app referral widget. When the program has `settings.widget.autoEnroll`, a customer who isn't a partner yet is created on demand (send `email`). The token only reads that partner's own data.

        **Auth:** an API key with `partners:write` (or `full`), or a session of any role.
        """
        return await self._request("POST", f"/v1/widget/tokens", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_zapier_conversions(self, body: PostZapierConversionsBody, *, idempotency_key: Optional[str] = None) -> PostZapierConversionsResponse:
        """Record a conversion from Zapier. POST /v1/zapier/conversions

        Zapier's "Record conversion" action: a payment (or refund) for a customer through a generic billing connection (the org's first active one unless `connectionId`), with no signature needed. Idempotent by `providerEventId`. 400 without a generic billing connection.

        **Auth:** an API key with `billing:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/zapier/conversions", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def post_zapier_hooks(self, body: PostZapierHooksBody, *, idempotency_key: Optional[str] = None) -> ZapierHook:
        """Subscribe a Zapier hook. POST /v1/zapier/hooks

        REST hook subscribe, called by Zapier when a Zap turns on: events of `event` are posted to the HTTPS `target_url`.

        **Auth:** an API key with `integrations:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("POST", f"/v1/zapier/hooks", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def put_billing_connections_id_credentials(self, id: str, body: PutBillingConnectionsIdCredentialsBody, *, idempotency_key: Optional[str] = None) -> PutBillingConnectionsIdCredentialsResponse:
        """Set provider API credentials. PUT /v1/billing/connections/{id}/credentials

        For providers that send thin webhooks (Recurly, BigCommerce), the API credentials used to fetch the full event: `apiKey`, or `apiToken` plus `storeHash`, and `region`. Stored encrypted. 400 for providers that take no credentials or when a required field is missing. Audited.

        **Auth:** an API key with `billing:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("PUT", f"/v1/billing/connections/{_seg(id)}/credentials", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def put_billing_connections_id_secret(self, id: str, body: PutBillingConnectionsIdSecretBody, *, idempotency_key: Optional[str] = None) -> PutBillingConnectionsIdSecretResponse:
        """Set the webhook signing secret. PUT /v1/billing/connections/{id}/secret

        Replaces the connection's signing secret with the provider's own (at least 8 characters). The previous secret keeps verifying for 24 hours. Audited.

        **Auth:** an API key with `billing:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("PUT", f"/v1/billing/connections/{_seg(id)}/secret", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def put_billing_connections_id_value_mapping(self, id: str, body: PutBillingConnectionsIdValueMappingBody, *, idempotency_key: Optional[str] = None) -> PutBillingConnectionsIdValueMappingResponse:
        """Set the value mapping. PUT /v1/billing/connections/{id}/value-mapping

        Where cash, credit applied, discount, cost and product live in this connection's payloads, as dot paths (`[]` sums an array, for example `data.discounts[].amount`), and whether amounts are in minor or major units. Each save bumps the mapping version; a rebuild re-applies it to stored events. Audited.

        **Auth:** an API key with `billing:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("PUT", f"/v1/billing/connections/{_seg(id)}/value-mapping", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def put_branding(self, body: PutBrandingBody, *, idempotency_key: Optional[str] = None) -> Ok:
        """Update branding. PUT /v1/branding

        Sets the logo URL, theme (only the documented `--r-*` tokens, with plain CSS values) and email sender. Omitted fields keep their value.

        **Auth:** an API key with `org:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("PUT", f"/v1/branding", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def put_email_settings(self, body: PutEmailSettingsBody, *, idempotency_key: Optional[str] = None) -> EmailSettings:
        """Update email settings. PUT /v1/email/settings

        Sets the email provider and its API key (write-only: omit to keep it, `null` to remove), the from address and name, reply-to, logo and primary color for partner emails. Without a provider, no email is sent.

        **Auth:** an API key with `org:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("PUT", f"/v1/email/settings", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def put_email_templates_event_locale(self, event: str, locale: str, body: PutEmailTemplatesEventLocaleBody, *, idempotency_key: Optional[str] = None) -> PutEmailTemplatesEventLocaleResponse:
        """Override an email template. PUT /v1/email/templates/{event}/{locale}

        Replaces the subject, text and optional HTML of one event in one locale. 404 for an unknown event or locale.

        **Auth:** an API key with `org:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("PUT", f"/v1/email/templates/{_seg(event)}/{_seg(locale)}", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def put_integrations_hubspot(self, body: PutIntegrationsHubspotBody, *, idempotency_key: Optional[str] = None) -> IntegrationConnection:
        """Connect HubSpot. PUT /v1/integrations/hubspot

        Connects HubSpot with your private-app `token` (required the first time; omit to keep it) to sync partners as contacts and referrals as deals in `pipeline`, moving them to `paidDealStage` when they pay. `status: "paused"` stops syncing.

        **Auth:** an API key with `integrations:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("PUT", f"/v1/integrations/hubspot", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def put_integrations_segment(self, body: PutIntegrationsSegmentBody, *, idempotency_key: Optional[str] = None) -> IntegrationConnection:
        """Connect Segment. PUT /v1/integrations/segment

        Connects a Segment source with its `writeKey` (required the first time) and sends referral, commission, payout and partner events as track calls; `events` limits which topics (`null` for all).

        **Auth:** an API key with `integrations:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("PUT", f"/v1/integrations/segment", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def put_marketplace_listing(self, body: PutMarketplaceListingBody, *, idempotency_key: Optional[str] = None) -> Ok:
        """List a program in the marketplace. PUT /v1/marketplace/listing

        Creates or updates the marketplace listing of a program: visibility (`public` or `unlisted`), category, headline, description and sponsored placement. Audited.

        **Auth:** an API key with `growth:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("PUT", f"/v1/marketplace/listing", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def put_me_locale(self, body: PutMeLocaleBody, *, idempotency_key: Optional[str] = None) -> PutMeLocaleResponse:
        """Set my email language. PUT /v1/me/locale

        The signed-in user's preferred locale for emails. User session only.

        **Auth:** an API key with `team:write` (or `full`), or a session of any role.
        """
        return await self._request("PUT", f"/v1/me/locale", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def put_me_roi_digest(self, body: PutMeRoiDigestBody, *, idempotency_key: Optional[str] = None) -> PutMeRoiDigestResponse:
        """Turn my ROI digest on or off. PUT /v1/me/roi-digest

        Whether the signed-in member receives this org's periodic credit ROI digest email. User session only.

        **Auth:** an API key with `team:write` (or `full`), or a session of any role.
        """
        return await self._request("PUT", f"/v1/me/roi-digest", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def put_network_settings(self, body: PutNetworkSettingsBody, *, idempotency_key: Optional[str] = None) -> PutNetworkSettingsResponse:
        """Join or leave the attribution network. PUT /v1/network/settings

        Opts the org in or out of the cross-merchant attribution network: contributing its referral touchpoints (as hashed customer identities and partner accounts, never merchant identity or PII) and, in return, reading the network journey.

        **Auth:** an API key with `growth:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("PUT", f"/v1/network/settings", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def put_org_fx_feed(self, body: PutOrgFxFeedBody, *, idempotency_key: Optional[str] = None) -> PutOrgFxFeedResponse:
        """Turn the FX feed on or off. PUT /v1/org/fx-feed

        Turns the daily ECB reference-rate feed on or off. Turning it on syncs once at once and returns how many rates were inserted. Audited.

        **Auth:** an API key with `org:write` (or `full`), or a session with role `owner`, `admin`, `finance`.
        """
        return await self._request("PUT", f"/v1/org/fx-feed", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def put_org_payout_schedule(self, body: PutOrgPayoutScheduleBody, *, idempotency_key: Optional[str] = None) -> PutOrgPayoutScheduleResponse:
        """Set the org payout schedule. PUT /v1/org/payout-schedule

        When payouts run automatically for every program without its own schedule: a `schedule` (`monthly`, `weekly`, `twice_monthly` or `custom` dates), the older `dayOfMonth` form, or `null` to turn automatic payouts off. Send exactly one of `schedule` and `dayOfMonth`. Audited.

        **Auth:** an API key with `payouts:write` (or `full`), or a session with role `owner`, `admin`, `finance`.
        """
        return await self._request("PUT", f"/v1/org/payout-schedule", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def put_org_referral_params(self, body: PutOrgReferralParamsBody, *, idempotency_key: Optional[str] = None) -> GetOrgReferralParamsResponse:
        """Set referral query parameters. PUT /v1/org/referral-params

        Replaces the extra query parameters aff.js reads a referral code from (up to 10; lowercase letters, digits and `_`). Built-in names are dropped. Imports add the previous tool's parameter here so already-shared links keep crediting. Audited.

        **Auth:** an API key with `org:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("PUT", f"/v1/org/referral-params", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def put_org_retention(self, body: PutOrgRetentionBody, *, idempotency_key: Optional[str] = None) -> Retention:
        """Set the data retention policy. PUT /v1/org/retention

        Changes retention days for one or more kinds of raw data (others keep their value). Values below a kind's minimum are rejected. Audited.

        **Auth:** an API key with `org:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("PUT", f"/v1/org/retention", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def put_org_tax_filing(self, body: PutOrgTaxFilingBody, *, idempotency_key: Optional[str] = None) -> PutOrgTaxFilingResponse:
        """Connect a 1099 filing provider. PUT /v1/org/tax-filing

        Chooses who e-files 1099-NEC forms: `test` (simulated) or `tax1099` with your own API key (stored encrypted). Audited.

        **Auth:** an API key with `org:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("PUT", f"/v1/org/tax-filing", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def put_org_tax_profile(self, body: PutOrgTaxProfileBody, *, idempotency_key: Optional[str] = None) -> TaxProfile:
        """Update the tax profile. PUT /v1/org/tax-profile

        Sets any of the tax profile fields; `null` clears one. A VAT id must be a valid EU VAT number; an EIN looks like `12-3456789`. Audited.

        **Auth:** an API key with `org:write` (or `full`), or a session with role `owner`, `admin`, `finance`.
        """
        return await self._request("PUT", f"/v1/org/tax-profile", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def put_partner_locale(self, body: PutPartnerLocaleBody, *, idempotency_key: Optional[str] = None) -> PutPartnerLocaleResponse:
        """Set my email language (partner). PUT /v1/partner/locale

        The partner account's preferred locale for emails.

        **Auth:** a partner session.
        """
        return await self._request("PUT", f"/v1/partner/locale", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def put_partner_orgs_org_id_payout_profile(self, org_id: str, body: PutPartnerOrgsOrgIdPayoutProfileBody, *, idempotency_key: Optional[str] = None) -> PutPartnerOrgsOrgIdPayoutProfileResponse:
        """Set my payout details. PUT /v1/partner/orgs/{orgId}/payout-profile

        How this merchant pays the partner: the method, its details (checked for what the rail needs, such as a PayPal email or wallet address) and currency. When two-factor sign-in is on, send the current code in `x-totp-code` (`401 step_up_required` otherwise).

        **Auth:** a partner session.
        """
        return await self._request("PUT", f"/v1/partner/orgs/{_seg(org_id)}/payout-profile", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def put_partner_orgs_org_id_postback(self, org_id: str, body: PutPartnerOrgsOrgIdPostbackBody, *, idempotency_key: Optional[str] = None) -> PutPartnerOrgsOrgIdPostbackResponse:
        """Set my conversion postback. PUT /v1/partner/orgs/{orgId}/postback

        Registers a server-to-server postback URL the merchant calls on the partner's events, with macros `{topic}`, `{partner_id}`, `{referral_id}`, `{customer}`, `{amount}`, `{currency}`. Returns a new signing secret.

        **Auth:** a partner session.
        """
        return await self._request("PUT", f"/v1/partner/orgs/{_seg(org_id)}/postback", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def put_partner_orgs_org_id_vat(self, org_id: str, body: PutPartnerOrgsOrgIdVatBody, *, idempotency_key: Optional[str] = None) -> PutPartnersIdVatResponse:
        """Set my VAT number. PUT /v1/partner/orgs/{orgId}/vat

        Sets the partner's own EU VAT number with this merchant, checked against VIES when the merchant requires it.

        **Auth:** a partner session.
        """
        return await self._request("PUT", f"/v1/partner/orgs/{_seg(org_id)}/vat", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def put_partner_profile(self, body: PutPartnerProfileBody, *, idempotency_key: Optional[str] = None) -> Ok:
        """Update my creator profile. PUT /v1/partner/profile

        Updates the creator profile merchants search. `published: true` lists it in creator search; `acceptsInvites` controls whether merchants can invite the partner.

        **Auth:** a partner session.
        """
        return await self._request("PUT", f"/v1/partner/profile", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def put_partners_id_payout_profile(self, id: str, body: PutPartnersIdPayoutProfileBody, *, idempotency_key: Optional[str] = None) -> PutPartnersIdPayoutProfileResponse:
        """Set a partner's payout profile. PUT /v1/partners/{id}/payout-profile

        How the partner is paid: `method` (`paypal`, `wise`, `stripe_connect`, `ach`, `crypto`, `payoneer`, `tremendous` or `csv`), method `details` (a free-form map such as `{ "paypalEmail": … }`), the currency to pay in and the minimum balance before a payout. Partners can also set this themselves in the portal.

        **Auth:** an API key with `payouts:write` (or `full`), or a session with role `owner`, `admin`, `finance`.
        """
        return await self._request("PUT", f"/v1/partners/{_seg(id)}/payout-profile", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def put_partners_id_vat(self, id: str, body: PutPartnersIdVatBody, *, idempotency_key: Optional[str] = None) -> PutPartnersIdVatResponse:
        """Set a partner's VAT number. PUT /v1/partners/{id}/vat

        Sets (or clears with `null`) the partner's EU VAT number on their payout profile. With `viesCheck` on, VIES must list it as registered. 404 until the partner has payout details. Audited.

        **Auth:** an API key with `partners:write` (or `full`), or a session with role `owner`, `admin`, `finance`.
        """
        return await self._request("PUT", f"/v1/partners/{_seg(id)}/vat", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def put_payout_connections_provider(self, provider: str, body: Union[PutPayoutConnectionsProviderBodyOption1, PutPayoutConnectionsProviderBodyOption2, PutPayoutConnectionsProviderBodyOption3, PutPayoutConnectionsProviderBodyOption4, PutPayoutConnectionsProviderBodyOption5, PutPayoutConnectionsProviderBodyOption6], *, idempotency_key: Optional[str] = None) -> PutPayoutConnectionsProviderResponse:
        """Connect a payout provider. PUT /v1/payout-connections/{provider}

        Connects (or replaces) your own account with a payout provider, so payouts move money from your account: `paypal` (`clientId`, `secret`), `stripe` (`secretKey`), `circle` (`apiKey`, `walletId`), `wise` (`apiToken`, `profileId`), `payoneer` (`clientId`, `secret`, `programId`) or `tremendous` (`apiKey`, `fundingSourceId`), each with `env`. Stored encrypted and never echoed. Live mode only (`409 test_mode_unsupported` in test mode). Audited.

        **Auth:** an API key with `payouts:write` (or `full`), or a session with role `owner`, `admin`, `finance`.
        """
        return await self._request("PUT", f"/v1/payout-connections/{_seg(provider)}", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def put_profitability_products_product_ref(self, product_ref: str, body: PutProfitabilityProductsProductRefBody, *, idempotency_key: Optional[str] = None) -> GetProfitabilityProductsProductRefResponse:
        """Set a product margin. PUT /v1/profitability/products/{productRef}

        Sets a product's margin (`marginBps`) or unit cost (`unitCostMinor`, in `currency`, default the reporting currency); exactly one of the two. Audited.

        **Auth:** an API key with `analytics:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("PUT", f"/v1/profitability/products/{_seg(product_ref)}", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def put_profitability_settings(self, body: PutProfitabilitySettingsBody, *, idempotency_key: Optional[str] = None) -> GetProfitabilitySettingsResponse:
        """Update profitability settings. PUT /v1/profitability/settings

        Changes the org's economics settings, or with `programId` that program's overrides (a program can't override org-only fields such as the reporting currency). Returns the resolved settings. Re-run `POST /v1/profitability/rebuild` to apply changes to past figures. Audited.

        **Auth:** an API key with `analytics:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("PUT", f"/v1/profitability/settings", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def put_programs_id_autopricing(self, id: str, body: PutProgramsIdAutopricingBody, *, idempotency_key: Optional[str] = None) -> PutProgramsIdAutopricingResponse:
        """Configure autopricing. PUT /v1/programs/{id}/autopricing

        Self-pricing commissions: a target (`targetRoas`, or with `objective: "roi"` a `targetRoi`) and the `minBps`/`maxBps` band partner rates may move within. `enabled: false` turns it off.

        **Auth:** an API key with `programs:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("PUT", f"/v1/programs/{_seg(id)}/autopricing", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def put_programs_id_incrementality(self, id: str, body: PutProgramsIdIncrementalityBody, *, idempotency_key: Optional[str] = None) -> PutProgramsIdIncrementalityResponse:
        """Set the incrementality holdout. PUT /v1/programs/{id}/incrementality

        Holds out a random control share of referrals (`holdoutBps`, up to 5000 = 50%) from being commissioned, so comparing control and treatment conversion measures the true lift partners cause. 0 turns it off.

        **Auth:** an API key with `programs:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("PUT", f"/v1/programs/{_seg(id)}/incrementality", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def put_programs_id_negotiation_policy(self, id: str, body: PutProgramsIdNegotiationPolicyBody, *, idempotency_key: Optional[str] = None) -> PutProgramsIdNegotiationPolicyResponse:
        """Set the agent negotiation policy. PUT /v1/programs/{id}/negotiation-policy

        What an agent may negotiate to in this program: rates between `minBps` and `maxBps`, accepted automatically up to `autoAcceptMaxBps`. Requires `minBps <= autoAcceptMaxBps <= maxBps`. `enabled: false` closes the program to negotiation.

        **Auth:** an API key with `programs:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("PUT", f"/v1/programs/{_seg(id)}/negotiation-policy", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def put_programs_id_partners_partner_id_group(self, id: str, partner_id: str, body: PutProgramsIdPartnersPartnerIdGroupBody, *, idempotency_key: Optional[str] = None) -> PutProgramsIdPartnersPartnerIdGroupResponse:
        """Set a partner's group. PUT /v1/programs/{id}/partners/{partnerId}/group

        Puts an enrolled partner in one of the program's groups, or none (`groupId: null`). A partner is in at most one group per program.

        **Auth:** an API key with `programs:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("PUT", f"/v1/programs/{_seg(id)}/partners/{_seg(partner_id)}/group", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def put_programs_id_payout_schedule(self, id: str, body: PutProgramsIdPayoutScheduleBody, *, idempotency_key: Optional[str] = None) -> PutProgramsIdPayoutScheduleResponse:
        """Set a program's payout schedule. PUT /v1/programs/{id}/payout-schedule

        Overrides the org payout schedule for this program: a schedule, `{ "kind": "off" }` to never pay it automatically, or `null` to follow the org schedule again. Returns the next run date. Audited.

        **Auth:** an API key with `programs:write` (or `full`), or a session with role `owner`, `admin`, `finance`.
        """
        return await self._request("PUT", f"/v1/programs/{_seg(id)}/payout-schedule", query={}, body=body, idempotency_key=idempotency_key, kind="json")

    async def put_programs_id_referee_reward(self, id: str, body: PutProgramsIdRefereeRewardBody, *, idempotency_key: Optional[str] = None) -> PutProgramsIdRefereeRewardResponse:
        """Set the referee reward. PUT /v1/programs/{id}/referee-reward

        What a referred customer gets: `store_credit`, a `coupon` or a `gift_card`, either a flat `amountMinor` or a percent (`bps`, optionally capped with `capMinor`) of their first payment, issued on their first commission or first payment. A percent reward needs `on: "first_payment"`. `enabled: false` removes it. Each reward issued publishes `referee_reward.earned`.

        **Auth:** an API key with `programs:write` (or `full`), or a session with role `owner`, `admin`.
        """
        return await self._request("PUT", f"/v1/programs/{_seg(id)}/referee-reward", query={}, body=body, idempotency_key=idempotency_key, kind="json")


#: Every operation: id → (method, path, path params, query params (wire, python), has body, response kind, method name).
OPERATIONS: Dict[str, tuple] = {
    "deleteApiKeysId": ("DELETE", "/v1/api-keys/{id}", ["id"], [["cascade","cascade"],["pair","pair"]], False, "json", "delete_api_keys_id"),
    "deleteAssetsId": ("DELETE", "/v1/assets/{id}", ["id"], [], False, "json", "delete_assets_id"),
    "deleteAuthConnectionsId": ("DELETE", "/v1/auth/connections/{id}", ["id"], [], False, "json", "delete_auth_connections_id"),
    "deleteBillingConnectionsId": ("DELETE", "/v1/billing/connections/{id}", ["id"], [], False, "json", "delete_billing_connections_id"),
    "deleteBrandingDomain": ("DELETE", "/v1/branding/domain", [], [], False, "json", "delete_branding_domain"),
    "deleteBrandingLinkDomain": ("DELETE", "/v1/branding/link-domain", [], [], False, "json", "delete_branding_link_domain"),
    "deleteCliListenersId": ("DELETE", "/v1/cli/listeners/{id}", ["id"], [], False, "json", "delete_cli_listeners_id"),
    "deleteEmailTemplatesEventLocale": ("DELETE", "/v1/email/templates/{event}/{locale}", ["event","locale"], [], False, "json", "delete_email_templates_event_locale"),
    "deleteIntegrationsKind": ("DELETE", "/v1/integrations/{kind}", ["kind"], [], False, "json", "delete_integrations_kind"),
    "deleteOrgMembersUserId": ("DELETE", "/v1/org/members/{userId}", ["userId"], [], False, "json", "delete_org_members_user_id"),
    "deletePartnersId": ("DELETE", "/v1/partners/{id}", ["id"], [], False, "json", "delete_partners_id"),
    "deletePayoutConnectionsProvider": ("DELETE", "/v1/payout-connections/{provider}", ["provider"], [], False, "json", "delete_payout_connections_provider"),
    "deleteProfitabilityProductsProductRef": ("DELETE", "/v1/profitability/products/{productRef}", ["productRef"], [], False, "json", "delete_profitability_products_product_ref"),
    "deleteWebhookEndpointsId": ("DELETE", "/v1/webhook-endpoints/{id}", ["id"], [], False, "json", "delete_webhook_endpoints_id"),
    "deleteZapierHooksId": ("DELETE", "/v1/zapier/hooks/{id}", ["id"], [], False, "json", "delete_zapier_hooks_id"),
    "getAdminMetrics": ("GET", "/v1/admin/metrics", [], [], False, "json", "get_admin_metrics"),
    "getAdminOrgs": ("GET", "/v1/admin/orgs", [], [["q","q"],["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_admin_orgs"),
    "getAdminPartnerAccounts": ("GET", "/v1/admin/partner-accounts", [], [["flagged","flagged"],["q","q"],["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_admin_partner_accounts"),
    "getAgents": ("GET", "/v1/agents", [], [["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_agents"),
    "getAgentsRecommendations": ("GET", "/v1/agents/recommendations", [], [["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_agents_recommendations"),
    "getAnalyticsByChannel": ("GET", "/v1/analytics/by-channel", [], [["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_analytics_by_channel"),
    "getAnalyticsByGeo": ("GET", "/v1/analytics/by-geo", [], [["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_analytics_by_geo"),
    "getAnalyticsCohortLtv": ("GET", "/v1/analytics/cohort-ltv", [], [["months","months"],["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_analytics_cohort_ltv"),
    "getAnalyticsCouponPerformance": ("GET", "/v1/analytics/coupon-performance", [], [["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_analytics_coupon_performance"),
    "getAnalyticsOverview": ("GET", "/v1/analytics/overview", [], [["programId","program_id"],["days","days"]], False, "json", "get_analytics_overview"),
    "getAnalyticsTimeseries": ("GET", "/v1/analytics/timeseries", [], [["metric","metric"],["days","days"],["programId","program_id"],["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_analytics_timeseries"),
    "getApiKeys": ("GET", "/v1/api-keys", [], [["mode","mode"],["owner","owner"],["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_api_keys"),
    "getApiKeysId": ("GET", "/v1/api-keys/{id}", ["id"], [], False, "json", "get_api_keys_id"),
    "getAssets": ("GET", "/v1/assets", [], [["programId","program_id"],["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_assets"),
    "getAssistantSuggestions": ("GET", "/v1/assistant/suggestions", [], [["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_assistant_suggestions"),
    "getAuditLogs": ("GET", "/v1/audit-logs", [], [["actor","actor"],["actorType","actor_type"],["action","action"],["subjectType","subject_type"],["subjectId","subject_id"],["created[gte]","created_gte"],["created[lte]","created_lte"],["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"]], False, "list", "get_audit_logs"),
    "getAuthConnections": ("GET", "/v1/auth/connections", [], [["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_auth_connections"),
    "getAuthConnectionsIdExport": ("GET", "/v1/auth/connections/{id}/export", ["id"], [["customerRef","customer_ref"]], False, "json", "get_auth_connections_id_export"),
    "getAuthProviders": ("GET", "/v1/auth/providers", [], [], False, "json", "get_auth_providers"),
    "getBillingConnections": ("GET", "/v1/billing/connections", [], [["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_billing_connections"),
    "getBillingConnectionsId": ("GET", "/v1/billing/connections/{id}", ["id"], [], False, "json", "get_billing_connections_id"),
    "getBillingEvents": ("GET", "/v1/billing/events", [], [["customerRef","customer_ref"],["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_billing_events"),
    "getBillingPlan": ("GET", "/v1/billing/plan", [], [], False, "json", "get_billing_plan"),
    "getBranding": ("GET", "/v1/branding", [], [], False, "json", "get_branding"),
    "getCleanroomConsent": ("GET", "/v1/cleanroom/consent", [], [["customerRef","customer_ref"]], False, "json", "get_cleanroom_consent"),
    "getCleanroomQuery": ("GET", "/v1/cleanroom/query", [], [["dimension","dimension"]], False, "json", "get_cleanroom_query"),
    "getCliDeviceCodesUserCode": ("GET", "/v1/cli/device-codes/{userCode}", ["userCode"], [], False, "json", "get_cli_device_codes_user_code"),
    "getCliListenersIdEvents": ("GET", "/v1/cli/listeners/{id}/events", ["id"], [["wait","wait"]], False, "json", "get_cli_listeners_id_events"),
    "getCliLogs": ("GET", "/v1/cli/logs", [], [["after","after"],["wait","wait"],["limit","limit"]], False, "json", "get_cli_logs"),
    "getCliTopics": ("GET", "/v1/cli/topics", [], [], False, "json", "get_cli_topics"),
    "getCommissionRules": ("GET", "/v1/commission-rules", [], [["programId","program_id"],["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_commission_rules"),
    "getCommissions": ("GET", "/v1/commissions", [], [["partnerId","partner_id"],["programId","program_id"],["type","type_"],["referralId","referral_id"],["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_commissions"),
    "getCommissionsId": ("GET", "/v1/commissions/{id}", ["id"], [], False, "json", "get_commissions_id"),
    "getContracts": ("GET", "/v1/contracts", [], [["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_contracts"),
    "getCoupons": ("GET", "/v1/coupons", [], [["programId","program_id"],["partnerId","partner_id"],["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_coupons"),
    "getCreators": ("GET", "/v1/creators", [], [["q","q"],["category","category"],["channel","channel"],["minAudience","min_audience"],["minEngagementBps","min_engagement_bps"],["audienceCountry","audience_country"],["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_creators"),
    "getCreatorsAccountId": ("GET", "/v1/creators/{accountId}", ["accountId"], [], False, "json", "get_creators_account_id"),
    "getDeals": ("GET", "/v1/deals", [], [["status","status"],["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_deals"),
    "getDisputes": ("GET", "/v1/disputes", [], [["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_disputes"),
    "getEmailSettings": ("GET", "/v1/email/settings", [], [], False, "json", "get_email_settings"),
    "getEmailTemplates": ("GET", "/v1/email/templates", [], [["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_email_templates"),
    "getEmbedSummary": ("GET", "/v1/embed/summary", [], [], False, "json", "get_embed_summary"),
    "getExportAccounting": ("GET", "/v1/export/accounting", [], [["format","format_"],["year","year"]], False, "text", "get_export_accounting"),
    "getExportFull": ("GET", "/v1/export/full", [], [], False, "text", "get_export_full"),
    "getFraudCases": ("GET", "/v1/fraud/cases", [], [["status","status"],["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_fraud_cases"),
    "getFxRates": ("GET", "/v1/fx-rates", [], [["base","base"],["quote","quote"],["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_fx_rates"),
    "getGraphql": ("GET", "/v1/graphql", [], [], False, "json", "get_graphql"),
    "getHealth": ("GET", "/v1/health", [], [], False, "json", "get_health"),
    "getHostsCurrent": ("GET", "/v1/hosts/current", [], [], False, "json", "get_hosts_current"),
    "getHostsCurrentThemeCss": ("GET", "/v1/hosts/current/theme.css", [], [], False, "text", "get_hosts_current_theme_css"),
    "getIncrementality": ("GET", "/v1/incrementality", [], [["programId","program_id"]], False, "json", "get_incrementality"),
    "getIntegrations": ("GET", "/v1/integrations", [], [], False, "json", "get_integrations"),
    "getIntegrationsDeliveries": ("GET", "/v1/integrations/deliveries", [], [["kind","kind"],["status","status"],["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_integrations_deliveries"),
    "getInvitations": ("GET", "/v1/invitations", [], [["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_invitations"),
    "getLinks": ("GET", "/v1/links", [], [["programId","program_id"],["partnerId","partner_id"],["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_links"),
    "getLinksIdQr": ("GET", "/v1/links/{id}/qr", ["id"], [], False, "text", "get_links_id_qr"),
    "getMarketplaceListing": ("GET", "/v1/marketplace/listing", [], [["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_marketplace_listing"),
    "getMe": ("GET", "/v1/me", [], [], False, "json", "get_me"),
    "getNegotiations": ("GET", "/v1/negotiations", [], [["programId","program_id"],["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_negotiations"),
    "getNetworkJourney": ("GET", "/v1/network/journey", [], [["emailHash","email_hash"],["model","model"]], False, "json", "get_network_journey"),
    "getNetworkSettings": ("GET", "/v1/network/settings", [], [], False, "json", "get_network_settings"),
    "getNotifications": ("GET", "/v1/notifications", [], [["unread","unread"],["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_notifications"),
    "getOnchainConnections": ("GET", "/v1/onchain/connections", [], [["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_onchain_connections"),
    "getOpenapiJson": ("GET", "/v1/openapi.json", [], [], False, "json", "get_openapi_json"),
    "getOpenapiYaml": ("GET", "/v1/openapi.yaml", [], [], False, "text", "get_openapi_yaml"),
    "getOrg": ("GET", "/v1/org", [], [], False, "json", "get_org"),
    "getOrgFxFeed": ("GET", "/v1/org/fx-feed", [], [], False, "json", "get_org_fx_feed"),
    "getOrgMembers": ("GET", "/v1/org/members", [], [["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_org_members"),
    "getOrgPayoutSchedule": ("GET", "/v1/org/payout-schedule", [], [], False, "json", "get_org_payout_schedule"),
    "getOrgReferralParams": ("GET", "/v1/org/referral-params", [], [], False, "json", "get_org_referral_params"),
    "getOrgRetention": ("GET", "/v1/org/retention", [], [], False, "json", "get_org_retention"),
    "getOrgSso": ("GET", "/v1/org/sso", [], [], False, "json", "get_org_sso"),
    "getOrgSsoConnectionsIdSamlMetadata": ("GET", "/v1/org/sso/connections/{id}/saml-metadata", ["id"], [], False, "json", "get_org_sso_connections_id_saml_metadata"),
    "getOrgTaxProfile": ("GET", "/v1/org/tax-profile", [], [], False, "json", "get_org_tax_profile"),
    "getOutreach": ("GET", "/v1/outreach", [], [["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_outreach"),
    "getPartnerAchievements": ("GET", "/v1/partner/achievements", [], [["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_partner_achievements"),
    "getPartnerAdvance": ("GET", "/v1/partner/advance", [], [["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_partner_advance"),
    "getPartnerAdvanceOffer": ("GET", "/v1/partner/advance/offer", [], [], False, "json", "get_partner_advance_offer"),
    "getPartnerAssets": ("GET", "/v1/partner/assets", [], [["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_partner_assets"),
    "getPartnerContracts": ("GET", "/v1/partner/contracts", [], [["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_partner_contracts"),
    "getPartnerDeals": ("GET", "/v1/partner/deals", [], [["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_partner_deals"),
    "getPartnerDisputes": ("GET", "/v1/partner/disputes", [], [["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_partner_disputes"),
    "getPartnerGroups": ("GET", "/v1/partner/groups", [], [["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_partner_groups"),
    "getPartnerInvitations": ("GET", "/v1/partner/invitations", [], [["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_partner_invitations"),
    "getPartnerKycStatus": ("GET", "/v1/partner/kyc/status", [], [], False, "json", "get_partner_kyc_status"),
    "getPartnerLinks": ("GET", "/v1/partner/links", [], [["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_partner_links"),
    "getPartnerLinksIdQr": ("GET", "/v1/partner/links/{id}/qr", ["id"], [], False, "text", "get_partner_links_id_qr"),
    "getPartnerMarketplace": ("GET", "/v1/partner/marketplace", [], [["category","category"],["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_partner_marketplace"),
    "getPartnerMe": ("GET", "/v1/partner/me", [], [], False, "json", "get_partner_me"),
    "getPartnerNotifications": ("GET", "/v1/partner/notifications", [], [["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_partner_notifications"),
    "getPartnerOrgsOrgIdSelfBilling": ("GET", "/v1/partner/orgs/{orgId}/self-billing", ["orgId"], [], False, "json", "get_partner_orgs_org_id_self_billing"),
    "getPartnerPassport": ("GET", "/v1/partner/passport", [], [], False, "json", "get_partner_passport"),
    "getPartnerPayouts": ("GET", "/v1/partner/payouts", [], [["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_partner_payouts"),
    "getPartnerPayoutsIdInvoice": ("GET", "/v1/partner/payouts/{id}/invoice", ["id"], [["format","format_"]], False, "json", "get_partner_payouts_id_invoice"),
    "getPartnerPostbackLogs": ("GET", "/v1/partner/postback-logs", [], [["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_partner_postback_logs"),
    "getPartnerProfile": ("GET", "/v1/partner/profile", [], [], False, "json", "get_partner_profile"),
    "getPartnerProfileVerified": ("GET", "/v1/partner/profile/verified", [], [], False, "json", "get_partner_profile_verified"),
    "getPartnerProgramsProgramIdLeaderboard": ("GET", "/v1/partner/programs/{programId}/leaderboard", ["programId"], [], False, "json", "get_partner_programs_program_id_leaderboard"),
    "getPartnerRecruit": ("GET", "/v1/partner/recruit", [], [], False, "json", "get_partner_recruit"),
    "getPartnerReferrals": ("GET", "/v1/partner/referrals", [], [["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_partner_referrals"),
    "getPartnerReferralsIdTransparency": ("GET", "/v1/partner/referrals/{id}/transparency", ["id"], [], False, "json", "get_partner_referrals_id_transparency"),
    "getPartners": ("GET", "/v1/partners", [], [["email","email"],["externalRef","external_ref"],["status","status"],["includeArchived","include_archived"],["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_partners"),
    "getPartnerSecurity": ("GET", "/v1/partner/security", [], [], False, "json", "get_partner_security"),
    "getPartnersId": ("GET", "/v1/partners/{id}", ["id"], [], False, "json", "get_partners_id"),
    "getPartnersIdBalances": ("GET", "/v1/partners/{id}/balances", ["id"], [["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_partners_id_balances"),
    "getPartnersIdEnrollments": ("GET", "/v1/partners/{id}/enrollments", ["id"], [["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_partners_id_enrollments"),
    "getPartnersIdPayoutProfile": ("GET", "/v1/partners/{id}/payout-profile", ["id"], [], False, "json", "get_partners_id_payout_profile"),
    "getPartnersIdQuality": ("GET", "/v1/partners/{id}/quality", ["id"], [], False, "json", "get_partners_id_quality"),
    "getPartnerStats": ("GET", "/v1/partner/stats", [], [["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_partner_stats"),
    "getPartnerTaxDocuments": ("GET", "/v1/partner/tax-documents", [], [["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_partner_tax_documents"),
    "getPartnerTaxDocumentsId": ("GET", "/v1/partner/tax-documents/{id}", ["id"], [], False, "text", "get_partner_tax_documents_id"),
    "getPartnerTerms": ("GET", "/v1/partner/terms", [], [["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_partner_terms"),
    "getPassportPublicKey": ("GET", "/v1/passport/public-key", [], [], False, "json", "get_passport_public_key"),
    "getPayoutConnections": ("GET", "/v1/payout-connections", [], [["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_payout_connections"),
    "getPayoutRuns": ("GET", "/v1/payout-runs", [], [["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_payout_runs"),
    "getPayouts": ("GET", "/v1/payouts", [], [["partnerId","partner_id"],["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_payouts"),
    "getPayoutsIdInvoice": ("GET", "/v1/payouts/{id}/invoice", ["id"], [["format","format_"]], False, "json", "get_payouts_id_invoice"),
    "getPrivacyExport": ("GET", "/v1/privacy/export", [], [["customerRef","customer_ref"]], False, "json", "get_privacy_export"),
    "getPrivacyRequests": ("GET", "/v1/privacy/requests", [], [["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_privacy_requests"),
    "getPrivacyRequestsId": ("GET", "/v1/privacy/requests/{id}", ["id"], [], False, "json", "get_privacy_requests_id"),
    "getPrivacyRequestsIdResult": ("GET", "/v1/privacy/requests/{id}/result", ["id"], [], False, "json", "get_privacy_requests_id_result"),
    "getProfitabilityProducts": ("GET", "/v1/profitability/products", [], [], False, "json", "get_profitability_products"),
    "getProfitabilityProductsProductRef": ("GET", "/v1/profitability/products/{productRef}", ["productRef"], [], False, "json", "get_profitability_products_product_ref"),
    "getProfitabilityRebuildJobId": ("GET", "/v1/profitability/rebuild/{jobId}", ["jobId"], [], False, "json", "get_profitability_rebuild_job_id"),
    "getProfitabilitySettings": ("GET", "/v1/profitability/settings", [], [["programId","program_id"]], False, "json", "get_profitability_settings"),
    "getPrograms": ("GET", "/v1/programs", [], [["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_programs"),
    "getProgramsId": ("GET", "/v1/programs/{id}", ["id"], [], False, "json", "get_programs_id"),
    "getProgramsIdAutopricing": ("GET", "/v1/programs/{id}/autopricing", ["id"], [], False, "json", "get_programs_id_autopricing"),
    "getProgramsIdEnrollments": ("GET", "/v1/programs/{id}/enrollments", ["id"], [["status","status"],["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_programs_id_enrollments"),
    "getProgramsIdGraph": ("GET", "/v1/programs/{id}/graph", ["id"], [["root","root"],["depth","depth"]], False, "json", "get_programs_id_graph"),
    "getProgramsIdGroups": ("GET", "/v1/programs/{id}/groups", ["id"], [["includeArchived","include_archived"],["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_programs_id_groups"),
    "getProgramsIdNegotiationPolicy": ("GET", "/v1/programs/{id}/negotiation-policy", ["id"], [], False, "json", "get_programs_id_negotiation_policy"),
    "getProgramsIdPromotions": ("GET", "/v1/programs/{id}/promotions", ["id"], [["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_programs_id_promotions"),
    "getProgramsIdRefereeReward": ("GET", "/v1/programs/{id}/referee-reward", ["id"], [], False, "json", "get_programs_id_referee_reward"),
    "getProgramsIdTermsAcceptances": ("GET", "/v1/programs/{id}/terms-acceptances", ["id"], [["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_programs_id_terms_acceptances"),
    "getProspects": ("GET", "/v1/prospects", [], [["status","status"],["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_prospects"),
    "getPublicProgramsHandle": ("GET", "/v1/public/programs/{handle}", ["handle"], [], False, "json", "get_public_programs_handle"),
    "getReferrals": ("GET", "/v1/referrals", [], [["programId","program_id"],["partnerId","partner_id"],["status","status"],["customerRef","customer_ref"],["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_referrals"),
    "getReferralsId": ("GET", "/v1/referrals/{id}", ["id"], [], False, "json", "get_referrals_id"),
    "getReferralsIdJourney": ("GET", "/v1/referrals/{id}/journey", ["id"], [], False, "json", "get_referrals_id_journey"),
    "getReportsFilteredClicks": ("GET", "/v1/reports/filtered-clicks", [], [["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_reports_filtered_clicks"),
    "getReportsPartnerPerformance": ("GET", "/v1/reports/partner-performance", [], [["format","format_"]], False, "json", "get_reports_partner_performance"),
    "getRewards": ("GET", "/v1/rewards", [], [["status","status"],["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_rewards"),
    "getRewardsLookupCode": ("GET", "/v1/rewards/lookup/{code}", ["code"], [], False, "json", "get_rewards_lookup_code"),
    "getRoiBreakdown": ("GET", "/v1/roi/breakdown", [], [["from","from_"],["to","to"],["programId","program_id"],["partnerId","partner_id"],["windowDays","window_days"],["currency","currency"],["format","format_"],["by","by"],["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_roi_breakdown"),
    "getRoiDataQuality": ("GET", "/v1/roi/data-quality", [], [["from","from_"],["to","to"],["format","format_"]], False, "json", "get_roi_data_quality"),
    "getRoiGrants": ("GET", "/v1/roi/grants", [], [["from","from_"],["to","to"],["programId","program_id"],["partnerId","partner_id"],["windowDays","window_days"],["currency","currency"],["format","format_"],["status","status"],["role","role"],["paidBack","paid_back"],["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_roi_grants"),
    "getRoiPartnersIdTrace": ("GET", "/v1/roi/partners/{id}/trace", ["id"], [["windowDays","window_days"],["format","format_"]], False, "json", "get_roi_partners_id_trace"),
    "getRoiPatterns": ("GET", "/v1/roi/patterns", [], [], False, "json", "get_roi_patterns"),
    "getRoiPatternsPattern": ("GET", "/v1/roi/patterns/{pattern}", ["pattern"], [["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_roi_patterns_pattern"),
    "getRoiSummary": ("GET", "/v1/roi/summary", [], [["from","from_"],["to","to"],["programId","program_id"],["partnerId","partner_id"],["windowDays","window_days"],["currency","currency"],["format","format_"],["model","model"],["includeProjection","include_projection"]], False, "json", "get_roi_summary"),
    "getRoiTraceCustomerRef": ("GET", "/v1/roi/trace/{customerRef}", ["customerRef"], [["windowDays","window_days"],["format","format_"]], False, "json", "get_roi_trace_customer_ref"),
    "getSetupStatus": ("GET", "/v1/setup/status", [], [], False, "json", "get_setup_status"),
    "getStatus": ("GET", "/v1/status", [], [], False, "json", "get_status"),
    "getStatusIncidents": ("GET", "/v1/status/incidents", [], [["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_status_incidents"),
    "getStatusIncidentsAtom": ("GET", "/v1/status/incidents.atom", [], [], False, "text", "get_status_incidents_atom"),
    "getStatusIncidentsId": ("GET", "/v1/status/incidents/{id}", ["id"], [], False, "json", "get_status_incidents_id"),
    "getTax1099": ("GET", "/v1/tax/1099", [], [["year","year"],["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_tax1099"),
    "getTax1099Filings": ("GET", "/v1/tax/1099/filings", [], [["year","year"],["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_tax1099_filings"),
    "getTax1099Preview": ("GET", "/v1/tax/1099/preview", [], [["year","year"]], False, "json", "get_tax1099_preview"),
    "getTestClock": ("GET", "/v1/test_clock", [], [], False, "json", "get_test_clock"),
    "getTestEmails": ("GET", "/v1/test/emails", [], [["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_test_emails"),
    "getValueImportJobId": ("GET", "/v1/value/import/{jobId}", ["jobId"], [], False, "json", "get_value_import_job_id"),
    "getVersions": ("GET", "/v1/versions", [], [], False, "json", "get_versions"),
    "getWebhookDeliveries": ("GET", "/v1/webhook-deliveries", [], [["endpointId","endpoint_id"],["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_webhook_deliveries"),
    "getWebhookDeliveriesId": ("GET", "/v1/webhook-deliveries/{id}", ["id"], [], False, "json", "get_webhook_deliveries_id"),
    "getWebhookEndpoints": ("GET", "/v1/webhook-endpoints", [], [["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_webhook_endpoints"),
    "getWebhookEndpointsId": ("GET", "/v1/webhook-endpoints/{id}", ["id"], [], False, "json", "get_webhook_endpoints_id"),
    "getWebhookEndpointsIdDeliveries": ("GET", "/v1/webhook-endpoints/{id}/deliveries", ["id"], [["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_webhook_endpoints_id_deliveries"),
    "getZapierEvents": ("GET", "/v1/zapier/events", [], [], False, "json", "get_zapier_events"),
    "getZapierHooks": ("GET", "/v1/zapier/hooks", [], [["limit","limit"],["starting_after","starting_after"],["ending_before","ending_before"],["created[gte]","created_gte"],["created[lte]","created_lte"]], False, "list", "get_zapier_hooks"),
    "getZapierTriggersEvent": ("GET", "/v1/zapier/triggers/{event}", ["event"], [["limit","limit"]], False, "json", "get_zapier_triggers_event"),
    "patchAdminStatusIncidentsId": ("PATCH", "/v1/admin/status/incidents/{id}", ["id"], [], True, "json", "patch_admin_status_incidents_id"),
    "patchApiKeysId": ("PATCH", "/v1/api-keys/{id}", ["id"], [], True, "json", "patch_api_keys_id"),
    "patchAuthConnectionsId": ("PATCH", "/v1/auth/connections/{id}", ["id"], [], True, "json", "patch_auth_connections_id"),
    "patchBillingConnectionsId": ("PATCH", "/v1/billing/connections/{id}", ["id"], [], True, "json", "patch_billing_connections_id"),
    "patchOrg": ("PATCH", "/v1/org", [], [], True, "json", "patch_org"),
    "patchOrgMembersUserId": ("PATCH", "/v1/org/members/{userId}", ["userId"], [], True, "json", "patch_org_members_user_id"),
    "patchOrgSso": ("PATCH", "/v1/org/sso", [], [], True, "json", "patch_org_sso"),
    "patchPartnerGroupsId": ("PATCH", "/v1/partner-groups/{id}", ["id"], [], True, "json", "patch_partner_groups_id"),
    "patchPartnersId": ("PATCH", "/v1/partners/{id}", ["id"], [], True, "json", "patch_partners_id"),
    "patchPartnersIdPayoutProfile": ("PATCH", "/v1/partners/{id}/payout-profile", ["id"], [], True, "json", "patch_partners_id_payout_profile"),
    "patchProgramsId": ("PATCH", "/v1/programs/{id}", ["id"], [], True, "json", "patch_programs_id"),
    "patchReferralsId": ("PATCH", "/v1/referrals/{id}", ["id"], [], True, "json", "patch_referrals_id"),
    "patchWebhookEndpointsId": ("PATCH", "/v1/webhook-endpoints/{id}", ["id"], [], True, "json", "patch_webhook_endpoints_id"),
    "postAdminOrgsIdPlan": ("POST", "/v1/admin/orgs/{id}/plan", ["id"], [], True, "json", "post_admin_orgs_id_plan"),
    "postAdminOrgsIdSuspend": ("POST", "/v1/admin/orgs/{id}/suspend", ["id"], [], True, "json", "post_admin_orgs_id_suspend"),
    "postAdminOrgsIdUnsuspend": ("POST", "/v1/admin/orgs/{id}/unsuspend", ["id"], [], False, "json", "post_admin_orgs_id_unsuspend"),
    "postAdminPartnerAccountsIdBan": ("POST", "/v1/admin/partner-accounts/{id}/ban", ["id"], [], False, "json", "post_admin_partner_accounts_id_ban"),
    "postAdminPartnerAccountsIdUnban": ("POST", "/v1/admin/partner-accounts/{id}/unban", ["id"], [], False, "json", "post_admin_partner_accounts_id_unban"),
    "postAdminStatusIncidents": ("POST", "/v1/admin/status/incidents", [], [], True, "json", "post_admin_status_incidents"),
    "postAdminStatusIncidentsIdUpdates": ("POST", "/v1/admin/status/incidents/{id}/updates", ["id"], [], True, "json", "post_admin_status_incidents_id_updates"),
    "postAgentsRegister": ("POST", "/v1/agents/register", [], [], True, "json", "post_agents_register"),
    "postAnomaliesScan": ("POST", "/v1/anomalies/scan", [], [], False, "json", "post_anomalies_scan"),
    "postApiKeys": ("POST", "/v1/api-keys", [], [], True, "json", "post_api_keys"),
    "postAssets": ("POST", "/v1/assets", [], [], True, "json", "post_assets"),
    "postAttributionReplay": ("POST", "/v1/attribution/replay", [], [], True, "json", "post_attribution_replay"),
    "postAuthConnections": ("POST", "/v1/auth/connections", [], [], True, "json", "post_auth_connections"),
    "postAuthConnectionsIdAliases": ("POST", "/v1/auth/connections/{id}/aliases", ["id"], [], True, "json", "post_auth_connections_id_aliases"),
    "postAuthConnectionsIdErase": ("POST", "/v1/auth/connections/{id}/erase", ["id"], [], True, "json", "post_auth_connections_id_erase"),
    "postAuthConnectionsIdPing": ("POST", "/v1/auth/connections/{id}/ping", ["id"], [], True, "json", "post_auth_connections_id_ping"),
    "postAuthConnectionsIdRevokePreviousSecret": ("POST", "/v1/auth/connections/{id}/revoke-previous-secret", ["id"], [], False, "json", "post_auth_connections_id_revoke_previous_secret"),
    "postAuthConnectionsIdRotateSecret": ("POST", "/v1/auth/connections/{id}/rotate-secret", ["id"], [], False, "json", "post_auth_connections_id_rotate_secret"),
    "postAuthConnectionsIdSignals": ("POST", "/v1/auth/connections/{id}/signals", ["id"], [], True, "json", "post_auth_connections_id_signals"),
    "postAuthConnectionsIdSignups": ("POST", "/v1/auth/connections/{id}/signups", ["id"], [], True, "json", "post_auth_connections_id_signups"),
    "postAuthConnectionsIdUsers": ("POST", "/v1/auth/connections/{id}/users", ["id"], [], True, "json", "post_auth_connections_id_users"),
    "postAuthLogout": ("POST", "/v1/auth/logout", [], [], False, "json", "post_auth_logout"),
    "postBillingActivate": ("POST", "/v1/billing/activate", [], [], True, "json", "post_billing_activate"),
    "postBillingCheckout": ("POST", "/v1/billing/checkout", [], [], True, "json", "post_billing_checkout"),
    "postBillingConnections": ("POST", "/v1/billing/connections", [], [], True, "json", "post_billing_connections"),
    "postBillingConnectionsIdRotateSecret": ("POST", "/v1/billing/connections/{id}/rotate-secret", ["id"], [], False, "json", "post_billing_connections_id_rotate_secret"),
    "postBillingConnectionsIdValueMappingPreview": ("POST", "/v1/billing/connections/{id}/value-mapping/preview", ["id"], [], True, "json", "post_billing_connections_id_value_mapping_preview"),
    "postBillingPortal": ("POST", "/v1/billing/portal", [], [], False, "json", "post_billing_portal"),
    "postBrandingDomain": ("POST", "/v1/branding/domain", [], [], True, "json", "post_branding_domain"),
    "postBrandingDomainVerify": ("POST", "/v1/branding/domain/verify", [], [], False, "json", "post_branding_domain_verify"),
    "postBrandingLinkDomain": ("POST", "/v1/branding/link-domain", [], [], True, "json", "post_branding_link_domain"),
    "postBrandingLinkDomainVerify": ("POST", "/v1/branding/link-domain/verify", [], [], False, "json", "post_branding_link_domain_verify"),
    "postCliDeviceCodes": ("POST", "/v1/cli/device-codes", [], [], True, "json", "post_cli_device_codes"),
    "postCliDeviceCodesToken": ("POST", "/v1/cli/device-codes/token", [], [], True, "json", "post_cli_device_codes_token"),
    "postCliDeviceCodesUserCodeApprove": ("POST", "/v1/cli/device-codes/{userCode}/approve", ["userCode"], [], True, "json", "post_cli_device_codes_user_code_approve"),
    "postCliDeviceCodesUserCodeDeny": ("POST", "/v1/cli/device-codes/{userCode}/deny", ["userCode"], [], False, "json", "post_cli_device_codes_user_code_deny"),
    "postCliListeners": ("POST", "/v1/cli/listeners", [], [], True, "json", "post_cli_listeners"),
    "postCliTrigger": ("POST", "/v1/cli/trigger", [], [], True, "json", "post_cli_trigger"),
    "postCommissionRules": ("POST", "/v1/commission-rules", [], [], True, "json", "post_commission_rules"),
    "postCommissionsApproveDue": ("POST", "/v1/commissions/approve-due", [], [], False, "json", "post_commissions_approve_due"),
    "postCommissionsIdAdjust": ("POST", "/v1/commissions/{id}/adjust", ["id"], [], True, "json", "post_commissions_id_adjust"),
    "postCommissionsIdSettle": ("POST", "/v1/commissions/{id}/settle", ["id"], [], True, "json", "post_commissions_id_settle"),
    "postContracts": ("POST", "/v1/contracts", [], [], True, "json", "post_contracts"),
    "postContractsIdSend": ("POST", "/v1/contracts/{id}/send", ["id"], [], False, "json", "post_contracts_id_send"),
    "postCoupons": ("POST", "/v1/coupons", [], [], True, "json", "post_coupons"),
    "postCreatorsAccountIdInvite": ("POST", "/v1/creators/{accountId}/invite", ["accountId"], [], True, "json", "post_creators_account_id_invite"),
    "postDealsIdApprove": ("POST", "/v1/deals/{id}/approve", ["id"], [], True, "json", "post_deals_id_approve"),
    "postDealsIdReject": ("POST", "/v1/deals/{id}/reject", ["id"], [], False, "json", "post_deals_id_reject"),
    "postDealsIdWon": ("POST", "/v1/deals/{id}/won", ["id"], [], True, "json", "post_deals_id_won"),
    "postDiscoveryCorpus": ("POST", "/v1/discovery/corpus", [], [], True, "json", "post_discovery_corpus"),
    "postDiscoverySearch": ("POST", "/v1/discovery/search", [], [], True, "json", "post_discovery_search"),
    "postDisputesIdResolve": ("POST", "/v1/disputes/{id}/resolve", ["id"], [], True, "json", "post_disputes_id_resolve"),
    "postEmailPreview": ("POST", "/v1/email/preview", [], [], True, "json", "post_email_preview"),
    "postEmailSettingsVerifyDomain": ("POST", "/v1/email/settings/verify-domain", [], [], False, "json", "post_email_settings_verify_domain"),
    "postEmailTest": ("POST", "/v1/email/test", [], [], True, "json", "post_email_test"),
    "postEmbedTokens": ("POST", "/v1/embed/tokens", [], [], True, "json", "post_embed_tokens"),
    "postFraudCasesIdResolve": ("POST", "/v1/fraud/cases/{id}/resolve", ["id"], [], True, "json", "post_fraud_cases_id_resolve"),
    "postFraudDetectRings": ("POST", "/v1/fraud/detect-rings", [], [], False, "json", "post_fraud_detect_rings"),
    "postFraudInvalidTrafficScan": ("POST", "/v1/fraud/invalid-traffic/scan", [], [], True, "json", "post_fraud_invalid_traffic_scan"),
    "postFxRates": ("POST", "/v1/fx-rates", [], [], True, "json", "post_fx_rates"),
    "postFxRatesClearOverride": ("POST", "/v1/fx-rates/clear-override", [], [], True, "json", "post_fx_rates_clear_override"),
    "postFxRatesSync": ("POST", "/v1/fx-rates/sync", [], [], False, "json", "post_fx_rates_sync"),
    "postGraphql": ("POST", "/v1/graphql", [], [], True, "json", "post_graphql"),
    "postImportProvider": ("POST", "/v1/import/{provider}", ["provider"], [["programId","program_id"],["dryRun","dry_run"],["destinationUrl","destination_url"]], True, "json", "post_import_provider"),
    "postIntegrationsDeliveriesIdRetry": ("POST", "/v1/integrations/deliveries/{id}/retry", ["id"], [], False, "json", "post_integrations_deliveries_id_retry"),
    "postIntegrationsHubspotTest": ("POST", "/v1/integrations/hubspot/test", [], [], True, "json", "post_integrations_hubspot_test"),
    "postIntegrationsSegmentTest": ("POST", "/v1/integrations/segment/test", [], [], False, "json", "post_integrations_segment_test"),
    "postInvitationsIdWithdraw": ("POST", "/v1/invitations/{id}/withdraw", ["id"], [], False, "json", "post_invitations_id_withdraw"),
    "postLinks": ("POST", "/v1/links", [], [], True, "json", "post_links"),
    "postMobilePurchases": ("POST", "/v1/mobile/purchases", [], [], True, "json", "post_mobile_purchases"),
    "postNotificationsIdRead": ("POST", "/v1/notifications/{id}/read", ["id"], [], False, "json", "post_notifications_id_read"),
    "postOnchainConnections": ("POST", "/v1/onchain/connections", [], [], True, "json", "post_onchain_connections"),
    "postOrgMembers": ("POST", "/v1/org/members", [], [], True, "json", "post_org_members"),
    "postOrgs": ("POST", "/v1/orgs", [], [], True, "json", "post_orgs"),
    "postOrgSsoLink": ("POST", "/v1/org/sso/link", [], [], False, "json", "post_org_sso_link"),
    "postOrgSsoTickets": ("POST", "/v1/org/sso/tickets", [], [], True, "json", "post_org_sso_tickets"),
    "postOrgSsoTicketsIdRevoke": ("POST", "/v1/org/sso/tickets/{id}/revoke", ["id"], [], False, "json", "post_org_sso_tickets_id_revoke"),
    "postOutreachDraft": ("POST", "/v1/outreach/draft", [], [], True, "json", "post_outreach_draft"),
    "postOutreachIdApprove": ("POST", "/v1/outreach/{id}/approve", ["id"], [], False, "json", "post_outreach_id_approve"),
    "postOutreachSendDue": ("POST", "/v1/outreach/send-due", [], [], False, "json", "post_outreach_send_due"),
    "postPartnerAdvanceAccept": ("POST", "/v1/partner/advance/accept", [], [], True, "json", "post_partner_advance_accept"),
    "postPartnerAuthWalletNonce": ("POST", "/v1/partner/auth/wallet/nonce", [], [], True, "json", "post_partner_auth_wallet_nonce"),
    "postPartnerAuthWalletVerify": ("POST", "/v1/partner/auth/wallet/verify", [], [], True, "json", "post_partner_auth_wallet_verify"),
    "postPartnerContractsIdAccept": ("POST", "/v1/partner/contracts/{id}/accept", ["id"], [], False, "json", "post_partner_contracts_id_accept"),
    "postPartnerContractsIdDecline": ("POST", "/v1/partner/contracts/{id}/decline", ["id"], [], False, "json", "post_partner_contracts_id_decline"),
    "postPartnerDeals": ("POST", "/v1/partner/deals", [], [], True, "json", "post_partner_deals"),
    "postPartnerDisputes": ("POST", "/v1/partner/disputes", [], [], True, "json", "post_partner_disputes"),
    "postPartnerInvitationsIdAccept": ("POST", "/v1/partner/invitations/{id}/accept", ["id"], [], False, "json", "post_partner_invitations_id_accept"),
    "postPartnerInvitationsIdDecline": ("POST", "/v1/partner/invitations/{id}/decline", ["id"], [], False, "json", "post_partner_invitations_id_decline"),
    "postPartnerKycSubmit": ("POST", "/v1/partner/kyc/submit", [], [], True, "json", "post_partner_kyc_submit"),
    "postPartnerLinks": ("POST", "/v1/partner/links", [], [], True, "json", "post_partner_links"),
    "postPartnerNotificationsIdRead": ("POST", "/v1/partner/notifications/{id}/read", ["id"], [], False, "json", "post_partner_notifications_id_read"),
    "postPartnerOrgsOrgIdSelfBilling": ("POST", "/v1/partner/orgs/{orgId}/self-billing", ["orgId"], [], True, "json", "post_partner_orgs_org_id_self_billing"),
    "postPartnerOrgsOrgIdTaxForm": ("POST", "/v1/partner/orgs/{orgId}/tax-form", ["orgId"], [], True, "json", "post_partner_orgs_org_id_tax_form"),
    "postPartnerProgramsProgramIdApply": ("POST", "/v1/partner/programs/{programId}/apply", ["programId"], [], False, "json", "post_partner_programs_program_id_apply"),
    "postPartners": ("POST", "/v1/partners", [], [], True, "json", "post_partners"),
    "postPartnerSecurityTotpDisable": ("POST", "/v1/partner/security/totp/disable", [], [], True, "json", "post_partner_security_totp_disable"),
    "postPartnerSecurityTotpEnable": ("POST", "/v1/partner/security/totp/enable", [], [], True, "json", "post_partner_security_totp_enable"),
    "postPartnerSecurityTotpSetup": ("POST", "/v1/partner/security/totp/setup", [], [], False, "json", "post_partner_security_totp_setup"),
    "postPartnersIdTaxForm": ("POST", "/v1/partners/{id}/tax-form", ["id"], [], True, "json", "post_partners_id_tax_form"),
    "postPartnerTermsVersionIdAccept": ("POST", "/v1/partner/terms/{versionId}/accept", ["versionId"], [], False, "json", "post_partner_terms_version_id_accept"),
    "postPassportVerify": ("POST", "/v1/passport/verify", [], [], True, "json", "post_passport_verify"),
    "postPayoutRuns": ("POST", "/v1/payout-runs", [], [], False, "json", "post_payout_runs"),
    "postPayoutRunsIdCancel": ("POST", "/v1/payout-runs/{id}/cancel", ["id"], [], False, "json", "post_payout_runs_id_cancel"),
    "postPayoutRunsIdExecute": ("POST", "/v1/payout-runs/{id}/execute", ["id"], [], False, "json", "post_payout_runs_id_execute"),
    "postPayoutRunsRunScheduled": ("POST", "/v1/payout-runs/run-scheduled", [], [], False, "json", "post_payout_runs_run_scheduled"),
    "postPrivacyForget": ("POST", "/v1/privacy/forget", [], [], True, "json", "post_privacy_forget"),
    "postPrivacyLookup": ("POST", "/v1/privacy/lookup", [], [], True, "json", "post_privacy_lookup"),
    "postPrivacyRequests": ("POST", "/v1/privacy/requests", [], [], True, "json", "post_privacy_requests"),
    "postProfitabilityRebuild": ("POST", "/v1/profitability/rebuild", [], [], False, "json", "post_profitability_rebuild"),
    "postPrograms": ("POST", "/v1/programs", [], [], True, "json", "post_programs"),
    "postProgramsIdApplyLeveling": ("POST", "/v1/programs/{id}/apply-leveling", ["id"], [], False, "json", "post_programs_id_apply_leveling"),
    "postProgramsIdAutopriceRun": ("POST", "/v1/programs/{id}/autoprice/run", ["id"], [], True, "json", "post_programs_id_autoprice_run"),
    "postProgramsIdEnrollments": ("POST", "/v1/programs/{id}/enrollments", ["id"], [], True, "json", "post_programs_id_enrollments"),
    "postProgramsIdEnrollmentsEnrollmentIdApprove": ("POST", "/v1/programs/{id}/enrollments/{enrollmentId}/approve", ["id","enrollmentId"], [], False, "json", "post_programs_id_enrollments_enrollment_id_approve"),
    "postProgramsIdEnrollmentsEnrollmentIdReject": ("POST", "/v1/programs/{id}/enrollments/{enrollmentId}/reject", ["id","enrollmentId"], [], False, "json", "post_programs_id_enrollments_enrollment_id_reject"),
    "postProgramsIdGroups": ("POST", "/v1/programs/{id}/groups", ["id"], [], True, "json", "post_programs_id_groups"),
    "postProgramsIdPromotions": ("POST", "/v1/programs/{id}/promotions", ["id"], [], True, "json", "post_programs_id_promotions"),
    "postPromotionsIdEnd": ("POST", "/v1/promotions/{id}/end", ["id"], [], False, "json", "post_promotions_id_end"),
    "postPublicProgramsHandleJoin": ("POST", "/v1/public/programs/{handle}/join", ["handle"], [], True, "json", "post_public_programs_handle_join"),
    "postQualityRecompute": ("POST", "/v1/quality/recompute", [], [], False, "json", "post_quality_recompute"),
    "postReferralsAssociate": ("POST", "/v1/referrals/associate", [], [], True, "json", "post_referrals_associate"),
    "postReferralsIdApprove": ("POST", "/v1/referrals/{id}/approve", ["id"], [], False, "json", "post_referrals_id_approve"),
    "postReferralsIdReassign": ("POST", "/v1/referrals/{id}/reassign", ["id"], [], True, "json", "post_referrals_id_reassign"),
    "postReferralsIdVoid": ("POST", "/v1/referrals/{id}/void", ["id"], [], False, "json", "post_referrals_id_void"),
    "postRewardsIdRedeem": ("POST", "/v1/rewards/{id}/redeem", ["id"], [], True, "json", "post_rewards_id_redeem"),
    "postRewardsRedeemByCode": ("POST", "/v1/rewards/redeem-by-code", [], [], True, "json", "post_rewards_redeem_by_code"),
    "postRoiPatternsPatternReview": ("POST", "/v1/roi/patterns/{pattern}/review", ["pattern"], [], True, "json", "post_roi_patterns_pattern_review"),
    "postSandboxSimulate": ("POST", "/v1/sandbox/simulate", [], [], True, "json", "post_sandbox_simulate"),
    "postTax1099DocumentsIdCorrect": ("POST", "/v1/tax/1099/documents/{id}/correct", ["id"], [], False, "json", "post_tax1099_documents_id_correct"),
    "postTax1099Filings": ("POST", "/v1/tax/1099/filings", [], [], True, "json", "post_tax1099_filings"),
    "postTax1099FilingsIdRefresh": ("POST", "/v1/tax/1099/filings/{id}/refresh", ["id"], [], False, "json", "post_tax1099_filings_id_refresh"),
    "postTestClockAdvance": ("POST", "/v1/test_clock/advance", [], [], True, "json", "post_test_clock_advance"),
    "postTrackEvents": ("POST", "/v1/track/events", [], [], True, "json", "post_track_events"),
    "postUnsubscribeToken": ("POST", "/v1/unsubscribe/{token}", ["token"], [], False, "json", "post_unsubscribe_token"),
    "postValueEvents": ("POST", "/v1/value/events", [], [], True, "json", "post_value_events"),
    "postValueImport": ("POST", "/v1/value/import", [], [], True, "json", "post_value_import"),
    "postWebhookDeliveriesIdReplay": ("POST", "/v1/webhook-deliveries/{id}/replay", ["id"], [], False, "json", "post_webhook_deliveries_id_replay"),
    "postWebhookEndpoints": ("POST", "/v1/webhook-endpoints", [], [], True, "json", "post_webhook_endpoints"),
    "postWebhookEndpointsIdRotateSecret": ("POST", "/v1/webhook-endpoints/{id}/rotate-secret", ["id"], [], False, "json", "post_webhook_endpoints_id_rotate_secret"),
    "postWidgetTokens": ("POST", "/v1/widget/tokens", [], [], True, "json", "post_widget_tokens"),
    "postZapierConversions": ("POST", "/v1/zapier/conversions", [], [], True, "json", "post_zapier_conversions"),
    "postZapierHooks": ("POST", "/v1/zapier/hooks", [], [], True, "json", "post_zapier_hooks"),
    "putBillingConnectionsIdCredentials": ("PUT", "/v1/billing/connections/{id}/credentials", ["id"], [], True, "json", "put_billing_connections_id_credentials"),
    "putBillingConnectionsIdSecret": ("PUT", "/v1/billing/connections/{id}/secret", ["id"], [], True, "json", "put_billing_connections_id_secret"),
    "putBillingConnectionsIdValueMapping": ("PUT", "/v1/billing/connections/{id}/value-mapping", ["id"], [], True, "json", "put_billing_connections_id_value_mapping"),
    "putBranding": ("PUT", "/v1/branding", [], [], True, "json", "put_branding"),
    "putEmailSettings": ("PUT", "/v1/email/settings", [], [], True, "json", "put_email_settings"),
    "putEmailTemplatesEventLocale": ("PUT", "/v1/email/templates/{event}/{locale}", ["event","locale"], [], True, "json", "put_email_templates_event_locale"),
    "putIntegrationsHubspot": ("PUT", "/v1/integrations/hubspot", [], [], True, "json", "put_integrations_hubspot"),
    "putIntegrationsSegment": ("PUT", "/v1/integrations/segment", [], [], True, "json", "put_integrations_segment"),
    "putMarketplaceListing": ("PUT", "/v1/marketplace/listing", [], [], True, "json", "put_marketplace_listing"),
    "putMeLocale": ("PUT", "/v1/me/locale", [], [], True, "json", "put_me_locale"),
    "putMeRoiDigest": ("PUT", "/v1/me/roi-digest", [], [], True, "json", "put_me_roi_digest"),
    "putNetworkSettings": ("PUT", "/v1/network/settings", [], [], True, "json", "put_network_settings"),
    "putOrgFxFeed": ("PUT", "/v1/org/fx-feed", [], [], True, "json", "put_org_fx_feed"),
    "putOrgPayoutSchedule": ("PUT", "/v1/org/payout-schedule", [], [], True, "json", "put_org_payout_schedule"),
    "putOrgReferralParams": ("PUT", "/v1/org/referral-params", [], [], True, "json", "put_org_referral_params"),
    "putOrgRetention": ("PUT", "/v1/org/retention", [], [], True, "json", "put_org_retention"),
    "putOrgTaxFiling": ("PUT", "/v1/org/tax-filing", [], [], True, "json", "put_org_tax_filing"),
    "putOrgTaxProfile": ("PUT", "/v1/org/tax-profile", [], [], True, "json", "put_org_tax_profile"),
    "putPartnerLocale": ("PUT", "/v1/partner/locale", [], [], True, "json", "put_partner_locale"),
    "putPartnerOrgsOrgIdPayoutProfile": ("PUT", "/v1/partner/orgs/{orgId}/payout-profile", ["orgId"], [], True, "json", "put_partner_orgs_org_id_payout_profile"),
    "putPartnerOrgsOrgIdPostback": ("PUT", "/v1/partner/orgs/{orgId}/postback", ["orgId"], [], True, "json", "put_partner_orgs_org_id_postback"),
    "putPartnerOrgsOrgIdVat": ("PUT", "/v1/partner/orgs/{orgId}/vat", ["orgId"], [], True, "json", "put_partner_orgs_org_id_vat"),
    "putPartnerProfile": ("PUT", "/v1/partner/profile", [], [], True, "json", "put_partner_profile"),
    "putPartnersIdPayoutProfile": ("PUT", "/v1/partners/{id}/payout-profile", ["id"], [], True, "json", "put_partners_id_payout_profile"),
    "putPartnersIdVat": ("PUT", "/v1/partners/{id}/vat", ["id"], [], True, "json", "put_partners_id_vat"),
    "putPayoutConnectionsProvider": ("PUT", "/v1/payout-connections/{provider}", ["provider"], [], True, "json", "put_payout_connections_provider"),
    "putProfitabilityProductsProductRef": ("PUT", "/v1/profitability/products/{productRef}", ["productRef"], [], True, "json", "put_profitability_products_product_ref"),
    "putProfitabilitySettings": ("PUT", "/v1/profitability/settings", [], [], True, "json", "put_profitability_settings"),
    "putProgramsIdAutopricing": ("PUT", "/v1/programs/{id}/autopricing", ["id"], [], True, "json", "put_programs_id_autopricing"),
    "putProgramsIdIncrementality": ("PUT", "/v1/programs/{id}/incrementality", ["id"], [], True, "json", "put_programs_id_incrementality"),
    "putProgramsIdNegotiationPolicy": ("PUT", "/v1/programs/{id}/negotiation-policy", ["id"], [], True, "json", "put_programs_id_negotiation_policy"),
    "putProgramsIdPartnersPartnerIdGroup": ("PUT", "/v1/programs/{id}/partners/{partnerId}/group", ["id","partnerId"], [], True, "json", "put_programs_id_partners_partner_id_group"),
    "putProgramsIdPayoutSchedule": ("PUT", "/v1/programs/{id}/payout-schedule", ["id"], [], True, "json", "put_programs_id_payout_schedule"),
    "putProgramsIdRefereeReward": ("PUT", "/v1/programs/{id}/referee-reward", ["id"], [], True, "json", "put_programs_id_referee_reward"),
}
