# Code generated from the Referalli OpenAPI document. DO NOT EDIT.
# Changes belong in the generator, which overwrites this file.
"""Typed webhook events: one ``TypedDict`` per topic, told apart by ``event["topic"]``."""

from __future__ import annotations

from typing import Any, Dict, List, Literal, Optional, Tuple, TypedDict, Union

from .models import *  # noqa: F401,F403


class BaseWebhookEvent(TypedDict):
    """The envelope every delivery shares (also the type of a topic this SDK predates)."""

    id: str
    topic: str
    orgId: str
    livemode: bool
    createdAt: str
    data: Any


class BillingEventRecordedEvent(TypedDict):
    """``billing_event.recorded``: A billing event was recorded"""

    id: str
    topic: Literal["billing_event.recorded"]
    orgId: str
    livemode: bool
    createdAt: str
    data: "BillingEventRecordedEventData"


class ClickRecordedEvent(TypedDict):
    """``click.recorded``: A tracked click was recorded"""

    id: str
    topic: Literal["click.recorded"]
    orgId: str
    livemode: bool
    createdAt: str
    data: "ClickRecordedEventData"


class CommissionEarnedEvent(TypedDict):
    """``commission.earned``: A commission line was earned"""

    id: str
    topic: Literal["commission.earned"]
    orgId: str
    livemode: bool
    createdAt: str
    data: "CommissionEarnedEventData"


class CommissionReversedEvent(TypedDict):
    """``commission.reversed``: A commission line was reversed"""

    id: str
    topic: Literal["commission.reversed"]
    orgId: str
    livemode: bool
    createdAt: str
    data: "CommissionReversedEventData"


class CommissionSettledEvent(TypedDict):
    """``commission.settled``: A commission line was settled by the merchant"""

    id: str
    topic: Literal["commission.settled"]
    orgId: str
    livemode: bool
    createdAt: str
    data: "CommissionSettledEventData"


class CreditRedeemedEvent(TypedDict):
    """``credit.redeemed``: A referee reward was redeemed"""

    id: str
    topic: Literal["credit.redeemed"]
    orgId: str
    livemode: bool
    createdAt: str
    data: "CreditRedeemedEventData"


class CustomerAliasedEvent(TypedDict):
    """``customer.aliased``: A customer's id changed"""

    id: str
    topic: Literal["customer.aliased"]
    orgId: str
    livemode: bool
    createdAt: str
    data: "CustomerAliasedEventData"


class DealSubmittedEvent(TypedDict):
    """``deal.submitted``: A partner registered a deal"""

    id: str
    topic: Literal["deal.submitted"]
    orgId: str
    livemode: bool
    createdAt: str
    data: "DealSubmittedEventData"


class DisputeResolvedEvent(TypedDict):
    """``dispute.resolved``: A partner dispute was resolved"""

    id: str
    topic: Literal["dispute.resolved"]
    orgId: str
    livemode: bool
    createdAt: str
    data: "DisputeResolvedEventData"


class FraudCaseOpenedEvent(TypedDict):
    """``fraud.case_opened``: A fraud case was opened"""

    id: str
    topic: Literal["fraud.case_opened"]
    orgId: str
    livemode: bool
    createdAt: str
    data: "FraudCaseOpenedEventData"


class PartnerAppliedEvent(TypedDict):
    """``partner.applied``: A partner applied to a program"""

    id: str
    topic: Literal["partner.applied"]
    orgId: str
    livemode: bool
    createdAt: str
    data: "PartnerAppliedEventData"


class PartnerApprovedEvent(TypedDict):
    """``partner.approved``: A partner was approved"""

    id: str
    topic: Literal["partner.approved"]
    orgId: str
    livemode: bool
    createdAt: str
    data: "PartnerApprovedEventData"


class PartnerEnrolledEvent(TypedDict):
    """``partner.enrolled``: A partner was enrolled"""

    id: str
    topic: Literal["partner.enrolled"]
    orgId: str
    livemode: bool
    createdAt: str
    data: "PartnerEnrolledEventData"


class PartnerLevelUpEvent(TypedDict):
    """``partner.level_up``: A partner reached a new level"""

    id: str
    topic: Literal["partner.level_up"]
    orgId: str
    livemode: bool
    createdAt: str
    data: "PartnerLevelUpEventData"


class PayoutCancelledEvent(TypedDict):
    """``payout.cancelled``: A payout was cancelled"""

    id: str
    topic: Literal["payout.cancelled"]
    orgId: str
    livemode: bool
    createdAt: str
    data: "PayoutCancelledEventData"


class PayoutFailedEvent(TypedDict):
    """``payout.failed``: A payout failed"""

    id: str
    topic: Literal["payout.failed"]
    orgId: str
    livemode: bool
    createdAt: str
    data: "PayoutFailedEventData"


class PayoutScheduledEvent(TypedDict):
    """``payout.scheduled``: A payout was created in a run"""

    id: str
    topic: Literal["payout.scheduled"]
    orgId: str
    livemode: bool
    createdAt: str
    data: "PayoutScheduledEventData"


class PayoutSentEvent(TypedDict):
    """``payout.sent``: A payout was paid"""

    id: str
    topic: Literal["payout.sent"]
    orgId: str
    livemode: bool
    createdAt: str
    data: "PayoutSentEventData"


class PayoutSubmittedEvent(TypedDict):
    """``payout.submitted``: A payout was submitted to the provider"""

    id: str
    topic: Literal["payout.submitted"]
    orgId: str
    livemode: bool
    createdAt: str
    data: "PayoutSubmittedEventData"


class PrivacyRequestCompletedEvent(TypedDict):
    """``privacy.request_completed``: A data-subject request finished"""

    id: str
    topic: Literal["privacy.request_completed"]
    orgId: str
    livemode: bool
    createdAt: str
    data: "PrivacyRequestCompletedEventData"


class RefereeRewardEarnedEvent(TypedDict):
    """``referee_reward.earned``: A referred customer earned their reward"""

    id: str
    topic: Literal["referee_reward.earned"]
    orgId: str
    livemode: bool
    createdAt: str
    data: "RefereeRewardEarnedEventData"


class ReferralApprovedEvent(TypedDict):
    """``referral.approved``: A held referral was approved"""

    id: str
    topic: Literal["referral.approved"]
    orgId: str
    livemode: bool
    createdAt: str
    data: "ReferralApprovedEventData"


class ReferralCreatedEvent(TypedDict):
    """``referral.created``: A customer was attributed to a partner"""

    id: str
    topic: Literal["referral.created"]
    orgId: str
    livemode: bool
    createdAt: str
    data: "ReferralCreatedEventData"


class ReferralHeldEvent(TypedDict):
    """``referral.held``: A referral was held for review"""

    id: str
    topic: Literal["referral.held"]
    orgId: str
    livemode: bool
    createdAt: str
    data: "ReferralHeldEventData"


class ReferralPausedEvent(TypedDict):
    """``referral.paused``: A referral was paused"""

    id: str
    topic: Literal["referral.paused"]
    orgId: str
    livemode: bool
    createdAt: str
    data: "ReferralPausedEventData"


class ReferralReassignedEvent(TypedDict):
    """``referral.reassigned``: A referral moved to another partner"""

    id: str
    topic: Literal["referral.reassigned"]
    orgId: str
    livemode: bool
    createdAt: str
    data: "ReferralReassignedEventData"


class ReferralRejectedEvent(TypedDict):
    """``referral.rejected``: A self-referral was refused"""

    id: str
    topic: Literal["referral.rejected"]
    orgId: str
    livemode: bool
    createdAt: str
    data: "ReferralRejectedEventData"


class ReferralResumedEvent(TypedDict):
    """``referral.resumed``: A paused referral was resumed"""

    id: str
    topic: Literal["referral.resumed"]
    orgId: str
    livemode: bool
    createdAt: str
    data: "ReferralResumedEventData"


class ReferralVoidedEvent(TypedDict):
    """``referral.voided``: A referral was voided"""

    id: str
    topic: Literal["referral.voided"]
    orgId: str
    livemode: bool
    createdAt: str
    data: "ReferralVoidedEventData"


class RoiPatternDetectedEvent(TypedDict):
    """``roi.pattern_detected``: A value pattern changed"""

    id: str
    topic: Literal["roi.pattern_detected"]
    orgId: str
    livemode: bool
    createdAt: str
    data: "RoiPatternDetectedEventData"


class RoiPaybackReachedEvent(TypedDict):
    """``roi.payback_reached``: A credit grant paid back"""

    id: str
    topic: Literal["roi.payback_reached"]
    orgId: str
    livemode: bool
    createdAt: str
    data: "RoiPaybackReachedEventData"


class TaxFormDeliveredEvent(TypedDict):
    """``tax.form_delivered``: A tax form was delivered to a partner"""

    id: str
    topic: Literal["tax.form_delivered"]
    orgId: str
    livemode: bool
    createdAt: str
    data: "TaxFormDeliveredEventData"


class WebhookEndpointDisabledEvent(TypedDict):
    """``webhook_endpoint.disabled``: A failing webhook endpoint was disabled"""

    id: str
    topic: Literal["webhook_endpoint.disabled"]
    orgId: str
    livemode: bool
    createdAt: str
    data: "WebhookEndpointDisabledEventData"


#: Any webhook event. Narrow it on ``event["topic"]``.
WebhookEvent = Union[BillingEventRecordedEvent, ClickRecordedEvent, CommissionEarnedEvent, CommissionReversedEvent, CommissionSettledEvent, CreditRedeemedEvent, CustomerAliasedEvent, DealSubmittedEvent, DisputeResolvedEvent, FraudCaseOpenedEvent, PartnerAppliedEvent, PartnerApprovedEvent, PartnerEnrolledEvent, PartnerLevelUpEvent, PayoutCancelledEvent, PayoutFailedEvent, PayoutScheduledEvent, PayoutSentEvent, PayoutSubmittedEvent, PrivacyRequestCompletedEvent, RefereeRewardEarnedEvent, ReferralApprovedEvent, ReferralCreatedEvent, ReferralHeldEvent, ReferralPausedEvent, ReferralReassignedEvent, ReferralRejectedEvent, ReferralResumedEvent, ReferralVoidedEvent, RoiPatternDetectedEvent, RoiPaybackReachedEvent, TaxFormDeliveredEvent, WebhookEndpointDisabledEvent, BaseWebhookEvent]

#: Every topic the API publishes.
TOPICS: Tuple[str, ...] = ("billing_event.recorded", "click.recorded", "commission.earned", "commission.reversed", "commission.settled", "credit.redeemed", "customer.aliased", "deal.submitted", "dispute.resolved", "fraud.case_opened", "partner.applied", "partner.approved", "partner.enrolled", "partner.level_up", "payout.cancelled", "payout.failed", "payout.scheduled", "payout.sent", "payout.submitted", "privacy.request_completed", "referee_reward.earned", "referral.approved", "referral.created", "referral.held", "referral.paused", "referral.reassigned", "referral.rejected", "referral.resumed", "referral.voided", "roi.pattern_detected", "roi.payback_reached", "tax.form_delivered", "webhook_endpoint.disabled")
