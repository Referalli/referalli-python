# Code generated from the Referalli OpenAPI document. DO NOT EDIT.
# Changes belong in the generator, which overwrites this file.
"""Typed shapes of every Referalli API object (TypedDicts: responses are plain dicts)."""

from __future__ import annotations

from typing import Any, Dict, List, Literal, NotRequired, Optional, TypeAlias, TypedDict, Union

from ._page import Page  # noqa: F401

Ok = TypedDict("Ok", {
    "ok": bool,
})

OkStatus = TypedDict("OkStatus", {
    "ok": bool,
    "status": str,
})

AmountsValueItem = TypedDict("AmountsValueItem", {
    "currency": str,
    "amountMinor": int,
})

Amounts: TypeAlias = "List[AmountsValueItem]"

Balance = TypedDict("Balance", {
    "currency": str,
    "pending": int,
    "approved": int,
    "paid": int,
    "reversed": int,
})

ProgramSettingsRiskPolicy = TypedDict("ProgramSettingsRiskPolicy", {
    "holdBotScore": float,
    "holdDisposableEmail": bool,
    "holdVelocity": int,
    "holdUnverifiedEmail": bool,
    "holdSelfReferral": bool,
    "holdRiskScore": float,
    "holdHighRiskLevel": bool,
})

ProgramSettingsWidget = TypedDict("ProgramSettingsWidget", {
    "autoEnroll": bool,
    "destinationUrl": Optional[str],
})

ProgramSettingsMobileAppOption1IosOption1 = TypedDict("ProgramSettingsMobileAppOption1IosOption1", {
    "teamId": str,
    "bundleId": str,
})

ProgramSettingsMobileAppOption1AndroidOption1 = TypedDict("ProgramSettingsMobileAppOption1AndroidOption1", {
    "packageName": str,
    "sha256CertFingerprints": List[str],
})

ProgramSettingsMobileAppOption1 = TypedDict("ProgramSettingsMobileAppOption1", {
    "ios": NotRequired[Optional["ProgramSettingsMobileAppOption1IosOption1"]],
    "android": NotRequired[Optional["ProgramSettingsMobileAppOption1AndroidOption1"]],
})

ProgramSettings = TypedDict("ProgramSettings", {
    "probabilisticPolicy": str,
    "selfReferralPolicy": Literal["review", "reject"],
    "splitCommissions": bool,
    "utmTemplate": Dict[str, str],
    "allowPaidSearch": bool,
    "challengeLinks": bool,
    "settlement": Literal["payout", "merchant_credit"],
    "riskPolicy": "ProgramSettingsRiskPolicy",
    "widget": "ProgramSettingsWidget",
    "refereeReward": NotRequired[Optional["GetOpenapiJsonResponse"]],
    "mobileApp": Optional["ProgramSettingsMobileAppOption1"],
})

ProgramPublicPage = TypedDict("ProgramPublicPage", {
    "pitch": str,
    "autoApprove": bool,
})

Program = TypedDict("Program", {
    "id": str,
    "name": str,
    "slug": str,
    "attributionModel": Literal["last_click", "first_click", "position_based", "time_decay"],
    "cookieWindowDays": int,
    "signupToConversionDays": int,
    "termsMd": str,
    "status": Literal["draft", "active", "paused", "archived"],
    "publicHandle": Optional[str],
    "settings": "ProgramSettings",
    "publicPage": "ProgramPublicPage",
    "createdAt": str,
})

Partner = TypedDict("Partner", {
    "id": str,
    "email": str,
    "displayName": str,
    "externalRef": Optional[str],
    "status": Literal["active", "suspended", "banned", "archived"],
    "tags": List[str],
    "notes": Optional[str],
    "createdAt": str,
})

NetworkWarning = TypedDict("NetworkWarning", {
    "flagged": bool,
    "reason": Optional[Literal["platform_flagged", "banned_by_other_merchants"]],
    "bannedByOtherMerchants": int,
})

Enrollment = TypedDict("Enrollment", {
    "id": str,
    "programId": str,
    "partnerId": str,
    "status": Literal["applied", "approved", "rejected", "removed"],
})

Link = TypedDict("Link", {
    "id": str,
    "programId": str,
    "partnerId": str,
    "code": str,
    "destinationUrl": str,
    "shortUrl": str,
    "clicks": int,
    "createdAt": str,
})

CreatedLink = TypedDict("CreatedLink", {
    "id": str,
    "programId": str,
    "partnerId": str,
    "code": str,
    "destinationUrl": str,
    "shortUrl": NotRequired[str],
})

Coupon = TypedDict("Coupon", {
    "id": str,
    "programId": str,
    "partnerId": str,
    "code": str,
    "createdAt": str,
})

ReasonNote = TypedDict("ReasonNote", {
    "code": Literal["outside_window", "fraud_excluded", "coupon_priority", "email_hash_lead", "fingerprint_fallback", "self_referral_review"],
    "values": NotRequired[Dict[str, float]],
})

PayoutScheduleValueOption1 = TypedDict("PayoutScheduleValueOption1", {
    "kind": Literal["monthly"],
    "dayOfMonth": int,
})

PayoutScheduleValueOption2 = TypedDict("PayoutScheduleValueOption2", {
    "kind": Literal["weekly"],
    "dayOfWeek": int,
})

PayoutScheduleValueOption3 = TypedDict("PayoutScheduleValueOption3", {
    "kind": Literal["twice_monthly"],
    "days": List[int],
})

PayoutScheduleValueOption4 = TypedDict("PayoutScheduleValueOption4", {
    "kind": Literal["custom"],
    "dates": List[str],
})

PayoutSchedule: TypeAlias = "Union[PayoutScheduleValueOption1, PayoutScheduleValueOption2, PayoutScheduleValueOption3, PayoutScheduleValueOption4]"

AttributionReasoning = TypedDict("AttributionReasoning", {
    "model": NotRequired[str],
    "consideredTouchpoints": NotRequired[int],
    "windowDays": NotRequired[int],
    "notes": NotRequired[List[str]],
    "noteCodes": NotRequired[List["ReasonNote"]],
})

ReferralTouchCreditsItem = TypedDict("ReferralTouchCreditsItem", {
    "partnerId": str,
    "weight": float,
    "clickId": Optional[str],
})

Referral = TypedDict("Referral", {
    "id": str,
    "programId": str,
    "partnerId": str,
    "customerRef": str,
    "source": str,
    "matchedVia": str,
    "confidence": float,
    "clickId": Optional[str],
    "linkId": Optional[str],
    "status": Literal["active", "pending_review", "paused", "void"],
    "ts": str,
    "windowExpiresAt": str,
    "touchCredits": List["ReferralTouchCreditsItem"],
    "reasoning": "AttributionReasoning",
})

SignupReasonCode: TypeAlias = "Literal[\"consent_missing\", \"unknown_code\", \"customer_is_partner\", \"self_referral\", \"banned_partner\", \"archived_partner\", \"flagged_partner\", \"fingerprint_ignored\", \"risk_hold\", \"no_email_for_enroll\", \"enroll_email_taken\", \"enroll_code_unavailable\"]"

AssociateResponseReferralOption1TouchCreditsItem = TypedDict("AssociateResponseReferralOption1TouchCreditsItem", {
    "partnerId": str,
    "weight": float,
    "clickId": Optional[str],
})

AssociateResponseReferralOption1 = TypedDict("AssociateResponseReferralOption1", {
    "id": str,
    "programId": str,
    "partnerId": str,
    "customerRef": str,
    "source": str,
    "matchedVia": str,
    "confidence": float,
    "clickId": Optional[str],
    "linkId": Optional[str],
    "status": Literal["active", "pending_review", "paused", "void"],
    "ts": str,
    "windowExpiresAt": str,
    "touchCredits": List["AssociateResponseReferralOption1TouchCreditsItem"],
    "reasoning": "AttributionReasoning",
    "orgId": str,
})

AssociateResponseReasoning = TypedDict("AssociateResponseReasoning", {
    "notes": List[str],
})

AssociateResponse = TypedDict("AssociateResponse", {
    "referral": Optional["AssociateResponseReferralOption1"],
    "reasoning": NotRequired["AssociateResponseReasoning"],
})

CommissionEvent = TypedDict("CommissionEvent", {
    "id": str,
    "programId": str,
    "partnerId": str,
    "referralId": Optional[str],
    "type": Literal["earned", "approved", "paid", "reversed", "adjusted"],
    "amountMinor": int,
    "currency": str,
    "relatedCommissionId": Optional[str],
    "holdUntil": Optional[str],
    "level": Optional[int],
    "memo": Optional[str],
    "settlementMethod": NotRequired[Optional[str]],
    "settlementReference": NotRequired[Optional[str]],
    "ts": str,
})

# An earned line also carries its net, state and the events recorded against it.
CommissionLine = TypedDict("CommissionLine", {
    "id": str,
    "programId": str,
    "partnerId": str,
    "referralId": Optional[str],
    "type": Literal["earned", "approved", "paid", "reversed", "adjusted"],
    "amountMinor": int,
    "currency": str,
    "relatedCommissionId": Optional[str],
    "holdUntil": Optional[str],
    "level": Optional[int],
    "memo": Optional[str],
    "settlementMethod": NotRequired[Optional[str]],
    "settlementReference": NotRequired[Optional[str]],
    "ts": str,
    "billingEventId": NotRequired[Optional[str]],
    "netMinor": NotRequired[int],
    "state": NotRequired[Literal["pending", "approved", "paid"]],
    "events": NotRequired[List["CommissionEvent"]],
})

Settlement = TypedDict("Settlement", {
    "commissionId": str,
    "paidEventId": str,
    "partnerId": str,
    "programId": str,
    "amountMinor": int,
    "currency": str,
    "method": Literal["store_credit", "merchant_credit"],
    "reference": str,
    "status": Literal["paid"],
})

CommissionRule = TypedDict("CommissionRule", {
    "id": str,
    "programId": str,
    "version": int,
    "config": "GetOpenapiJsonResponse",
    "createdAt": str,
})

BillingFilter = TypedDict("BillingFilter", {
    "metadata": NotRequired[Dict[str, str]],
    "productIds": NotRequired[List[str]],
    "priceIds": NotRequired[List[str]],
    "skus": NotRequired[List[str]],
})

ValueMapping = TypedDict("ValueMapping", {
    "cash": NotRequired[str],
    "creditApplied": NotRequired[str],
    "discount": NotRequired[str],
    "cost": NotRequired[str],
    "productRef": NotRequired[str],
    "unit": Literal["minor", "major"],
    "version": int,
})

ValueMappingPreviewValue = TypedDict("ValueMappingPreviewValue", {
    "cashMinor": int,
    "creditAppliedMinor": int,
    "discountMinor": int,
    "costMinor": NotRequired[int],
    "productRef": NotRequired[str],
    "fields": Dict[str, float],
    "warnings": NotRequired[List[str]],
    "source": NotRequired[Literal["mapping"]],
    "mappingVersion": NotRequired[int],
})

ValueMappingPreviewWouldRecordItem = TypedDict("ValueMappingPreviewWouldRecordItem", {
    "kind": str,
    "currency": str,
    "confidence": str,
    "source": str,
    "extractionVersion": int,
    "cashMinor": NotRequired[int],
    "creditAppliedMinor": NotRequired[int],
    "discountMinor": NotRequired[int],
    "costMinor": NotRequired[int],
    "productRef": NotRequired[str],
})

ValueMappingPreviewEventsItemValue = TypedDict("ValueMappingPreviewEventsItemValue", {
    "cashMinor": int,
    "creditAppliedMinor": int,
    "discountMinor": int,
    "costMinor": NotRequired[int],
    "productRef": NotRequired[str],
    "fields": Dict[str, float],
    "warnings": NotRequired[List[str]],
    "source": NotRequired[Literal["mapping"]],
    "mappingVersion": NotRequired[int],
})

ValueMappingPreviewEventsItemWouldRecordItem = TypedDict("ValueMappingPreviewEventsItemWouldRecordItem", {
    "kind": str,
    "currency": str,
    "confidence": str,
    "source": str,
    "extractionVersion": int,
    "cashMinor": NotRequired[int],
    "creditAppliedMinor": NotRequired[int],
    "discountMinor": NotRequired[int],
    "costMinor": NotRequired[int],
    "productRef": NotRequired[str],
})

ValueMappingPreviewEventsItem = TypedDict("ValueMappingPreviewEventsItem", {
    "currency": str,
    "value": "ValueMappingPreviewEventsItemValue",
    "wouldRecord": List["ValueMappingPreviewEventsItemWouldRecordItem"],
    "index": int,
})

ValueMappingPreview = TypedDict("ValueMappingPreview", {
    "mappingVersion": int,
    "currency": NotRequired[str],
    "value": NotRequired["ValueMappingPreviewValue"],
    "wouldRecord": NotRequired[List["ValueMappingPreviewWouldRecordItem"]],
    "events": NotRequired[List["ValueMappingPreviewEventsItem"]],
})

BillingConnectionRotation = TypedDict("BillingConnectionRotation", {
    "inProgress": bool,
    "previousSecretExpiresAt": NotRequired[str],
})

BillingConnection = TypedDict("BillingConnection", {
    "id": str,
    "provider": str,
    "name": str,
    "status": Literal["active", "paused"],
    "createdAt": str,
    "webhookUrl": str,
    "needsCredentials": bool,
    "hasCredentials": bool,
    "valueMapping": Optional["ValueMapping"],
    "filter": Optional["BillingFilter"],
    "rotation": "BillingConnectionRotation",
})

CreatedBillingConnection = TypedDict("CreatedBillingConnection", {
    "id": str,
    "provider": str,
    "webhookSecret": str,
    "webhookUrl": str,
    "filter": Optional["BillingFilter"],
})

BillingEvent = TypedDict("BillingEvent", {
    "id": str,
    "provider": str,
    "type": str,
    "customerRef": str,
    "invoiceRef": Optional[str],
    "amountGross": int,
    "tax": int,
    "fees": int,
    "currency": str,
    "occurredAt": str,
    "connectionId": Optional[str],
    "productRef": str,
    "status": Literal["processed", "ignored_by_filter"],
    "ignoredReason": Optional[Literal["filter", "internal_customer"]],
    "catalog": Optional[Dict[str, List[str]]],
})

InternalCustomer = TypedDict("InternalCustomer", {
    "customerRef": str,
    "note": str,
    "createdAt": str,
})

IdentityProviderSampleHookOption1 = TypedDict("IdentityProviderSampleHookOption1", {
    "language": str,
    "filename": str,
    "code": str,
})

IdentityProviderMetadataPaths = TypedDict("IdentityProviderMetadataPaths", {
    "anonId": List[str],
    "clickId": List[str],
    "coupon": List[str],
})

IdentityProvider = TypedDict("IdentityProvider", {
    "id": str,
    "label": str,
    "mechanism": Literal["webhook", "protocol"],
    "status": Literal["ga", "beta"],
    "docsUrl": str,
    "vendorDocsUrl": str,
    "secretKind": Literal["hmac", "svix", "jwks", "bearer"],
    "secretIssuedBy": Literal["referalli", "vendor"],
    "vendorSteps": List[str],
    "sampleHook": Optional["IdentityProviderSampleHookOption1"],
    "metadataPaths": "IdentityProviderMetadataPaths",
})

WebhookEndpointRotation = TypedDict("WebhookEndpointRotation", {
    "inProgress": bool,
    "previousSecretExpiresAt": NotRequired[str],
})

WebhookEndpointLastFailureOption1 = TypedDict("WebhookEndpointLastFailureOption1", {
    "statusCode": Optional[int],
    "error": Optional[str],
    "at": str,
})

WebhookEndpoint = TypedDict("WebhookEndpoint", {
    "id": str,
    "url": str,
    "topics": List[str],
    "programIds": Optional[List[str]],
    "status": Literal["active", "paused", "disabled"],
    "legacySignature": bool,
    "rotation": "WebhookEndpointRotation",
    "failingSince": Optional[str],
    "disabledAt": Optional[str],
    "disabledReason": Optional[str],
    "health": Literal["healthy", "failing", "disabled", "paused"],
    "lastSuccessAt": Optional[str],
    "lastFailure": Optional["WebhookEndpointLastFailureOption1"],
    "consecutiveFailures": int,
    "alertContacts": List[str],
    "createdAt": str,
})

HealthCheck = TypedDict("HealthCheck", {
    "id": str,
    "ok": bool,
    "detail": str,
    "fix": NotRequired[str],
    "docs": NotRequired[str],
    "hop": NotRequired[str],
})

WebhookDelivery = TypedDict("WebhookDelivery", {
    "id": str,
    "endpointId": str,
    "topic": str,
    "status": str,
    "attempts": int,
    "lastStatusCode": Optional[int],
    "lastAttemptAt": Optional[str],
    "nextAt": Optional[str],
    "createdAt": str,
})

PayoutProfile = TypedDict("PayoutProfile", {
    "partnerId": str,
    "method": str,
    "payoutCurrency": str,
    "minThresholdMinor": int,
    "taxFormType": Optional[str],
    "taxFormSubmittedAt": Optional[str],
})

TaxProfile = TypedDict("TaxProfile", {
    "legalName": Optional[str],
    "address": Optional[str],
    "country": Optional[str],
    "vatId": Optional[str],
    "ein": Optional[str],
    "domesticVatBps": Optional[int],
    "viesCheck": bool,
    "filingProvider": str,
    "filingConnected": bool,
})

TaxFilingDocumentsItem = TypedDict("TaxFilingDocumentsItem", {
    "id": str,
    "partnerId": str,
    "amountMinor": int,
    "status": str,
})

TaxFiling = TypedDict("TaxFiling", {
    "id": str,
    "taxYear": int,
    "kind": Literal["original", "correction"],
    "provider": str,
    "providerFilingId": Optional[str],
    "status": Literal["submitting", "submitted", "accepted", "rejected"],
    "recipientCount": int,
    "totalMinor": int,
    "error": Optional[str],
    "documents": List["TaxFilingDocumentsItem"],
})

NecPreviewRecipientsItem = TypedDict("NecPreviewRecipientsItem", {
    "partnerId": str,
    "name": Optional[str],
    "email": Optional[str],
    "amountMinor": int,
    "issues": List[Literal["missing_tin", "missing_address", "fx_missing", "already_filed"]],
})

NecPreview = TypedDict("NecPreview", {
    "taxYear": int,
    "payerReady": bool,
    "payerIssues": List[Literal["missing_legal_name", "missing_ein", "missing_address"]],
    "recipients": List["NecPreviewRecipientsItem"],
})

# The partner. Absent on invoices issued before 2026-10.
InvoiceSupplier = TypedDict("InvoiceSupplier", {
    "name": Optional[str],
    "address": Optional[str],
    "country": Optional[str],
    "vatId": Optional[str],
})

# The merchant, issuing the invoice on the partner’s behalf.
InvoiceCustomer = TypedDict("InvoiceCustomer", {
    "name": Optional[str],
    "address": Optional[str],
    "country": Optional[str],
    "vatId": Optional[str],
})

InvoiceSelfBilling = TypedDict("InvoiceSelfBilling", {
    "agreementVersion": Optional[str],
    "acceptedAt": Optional[str],
})

Invoice = TypedDict("Invoice", {
    "number": str,
    "issuedAt": str,
    "lines": List[Any],
    "vatNote": str,
    "supplier": NotRequired["InvoiceSupplier"],
    "customer": NotRequired["InvoiceCustomer"],
    "currency": NotRequired[str],
    "netMinor": NotRequired[int],
    "vatTreatment": NotRequired[Literal["reverse_charge", "domestic", "outside_scope"]],
    "vatRateBps": NotRequired[Optional[int]],
    "vatMinor": NotRequired[int],
    "grossMinor": NotRequired[int],
    "selfBilling": NotRequired["InvoiceSelfBilling"],
})

PayoutRunCreatedPayoutsItemFxAppliedItem = TypedDict("PayoutRunCreatedPayoutsItemFxAppliedItem", {
    "from": str,
    "to": str,
    "rate": float,
    "ts": str,
})

PayoutRunCreatedPayoutsItem = TypedDict("PayoutRunCreatedPayoutsItem", {
    "payoutId": str,
    "partnerId": str,
    "amountMinor": int,
    "currency": str,
    "rail": str,
    "fxApplied": List["PayoutRunCreatedPayoutsItemFxAppliedItem"],
    "invoice": "Invoice",
})

PayoutRunCreatedSkippedItem = TypedDict("PayoutRunCreatedSkippedItem", {
    "partnerId": str,
    "reason": Literal["missing_tax_form", "below_threshold", "no_profile", "kyc_unverified", "sanctions_hold", "partner_inactive", "missing_fx_rate", "self_billing_agreement_missing"],
})

PayoutRunCreated = TypedDict("PayoutRunCreated", {
    "runId": str,
    "payouts": List["PayoutRunCreatedPayoutsItem"],
    "skipped": List["PayoutRunCreatedSkippedItem"],
})

PayoutRun = TypedDict("PayoutRun", {
    "id": str,
    "status": str,
    "summary": Optional["GetOpenapiJsonResponse"],
    "createdAt": str,
    "executedAt": Optional[str],
})

Payout = TypedDict("Payout", {
    "id": str,
    "runId": str,
    "partnerId": str,
    "amountMinor": int,
    "currency": str,
    "status": str,
    "rail": str,
    "railRef": Optional[str],
    "failureReason": Optional[str],
    "sentAt": Optional[str],
})

FxRate = TypedDict("FxRate", {
    "base": str,
    "quote": str,
    "rate": str,
    "effectiveAt": str,
    "source": str,
    "scope": Literal["org", "platform"],
    "retiredAt": Optional[str],
})

Org = TypedDict("Org", {
    "id": str,
    "name": str,
    "plan": str,
    "settings": "GetOpenapiJsonResponse",
    "trackingToken": str,
    "payoutKycRequired": bool,
    "livemode": bool,
    "liveOrgId": NotRequired[str],
})

Member = TypedDict("Member", {
    "userId": str,
    "role": Literal["owner", "admin", "finance", "analyst", "support"],
    "email": str,
    "name": Optional[str],
})

IssuedApiKey = TypedDict("IssuedApiKey", {
    "id": str,
    "key": str,
    "scopes": List[str],
    "publishable": bool,
    "allowedOrigins": List[str],
    "apiVersion": str,
    "livemode": bool,
    "owner": Optional[str],
    "expiresAt": Optional[str],
    "pairId": Optional[str],
})

ApiKeyCreatedByOption1 = TypedDict("ApiKeyCreatedByOption1", {
    "type": Literal["api_key", "user"],
    "id": str,
})

ApiKey = TypedDict("ApiKey", {
    "id": str,
    "name": str,
    "prefix": str,
    "scopes": List[str],
    "apiVersion": str,
    "publishable": bool,
    "allowedOrigins": List[str],
    "livemode": bool,
    "owner": Optional[str],
    "pairId": Optional[str],
    "createdBy": Optional["ApiKeyCreatedByOption1"],
    "expiresAt": Optional[str],
    "expired": bool,
    "lastUsedAt": Optional[str],
    "createdAt": str,
    "revokedAt": Optional[str],
})

AuthConnectionRotation = TypedDict("AuthConnectionRotation", {
    "inProgress": bool,
    "previousSecretExpiresAt": NotRequired[str],
})

AuthConnection = TypedDict("AuthConnection", {
    "id": str,
    "provider": Literal["clerk", "supabase", "workos", "generic", "atlas", "custom"],
    "programId": str,
    "name": str,
    "status": str,
    "createdAt": str,
    "rotation": "AuthConnectionRotation",
    "instanceId": NotRequired[Optional[str]],
    "autoEnrollUsers": NotRequired[bool],
    "destinationUrl": NotRequired[Optional[str]],
    "signatureVersion": NotRequired[Literal["v1+v2", "v2"]],
    "requiresV2": NotRequired[bool],
})

CreatedAuthConnection = TypedDict("CreatedAuthConnection", {
    "id": str,
    "provider": str,
    "secret": str,
    "webhookUrl": NotRequired[str],
    "docsUrl": NotRequired[Optional[str]],
    "metadataKeys": NotRequired[Dict[str, str]],
    "programId": NotRequired[str],
    "instanceId": NotRequired[str],
    "autoEnrollUsers": NotRequired[bool],
    "destinationUrl": NotRequired[Optional[str]],
    "signupsUrl": NotRequired[str],
    "eraseUrl": NotRequired[str],
    "exportUrl": NotRequired[str],
})

FraudCase = TypedDict("FraudCase", {
    "id": str,
    "partnerId": Optional[str],
    "referralId": Optional[str],
    "kind": str,
    "status": str,
    "evidence": Optional["GetOpenapiJsonResponse"],
    "action": Optional[str],
    "createdAt": str,
    "resolvedAt": Optional[str],
})

CustomerExport = TypedDict("CustomerExport", {
    "customerRef": str,
    "referrals": List["GetOpenapiJsonResponse"],
    "associations": List["GetOpenapiJsonResponse"],
    "identityLinks": List["GetOpenapiJsonResponse"],
    "billingEvents": List["GetOpenapiJsonResponse"],
    "conversionEvents": List["GetOpenapiJsonResponse"],
})

PartnerExport = TypedDict("PartnerExport", {
    "partner": "GetOpenapiJsonResponse",
    "enrollments": List["GetOpenapiJsonResponse"],
    "links": List["GetOpenapiJsonResponse"],
    "coupons": List["GetOpenapiJsonResponse"],
    "payoutProfile": Optional["GetOpenapiJsonResponse"],
    "commissionEvents": List["GetOpenapiJsonResponse"],
    "payouts": List["GetOpenapiJsonResponse"],
})

PrivacyRequest = TypedDict("PrivacyRequest", {
    "id": str,
    "type": Literal["access", "erasure"],
    "subject": "GetOpenapiJsonResponse",
    "status": Literal["pending", "completed", "failed"],
    "error": Optional[str],
    "createdAt": str,
    "completedAt": Optional[str],
    "resultUrl": NotRequired[str],
    "result": NotRequired["GetOpenapiJsonResponse"],
})

GraphReferral = TypedDict("GraphReferral", {
    "referralId": str,
    "customerRef": str,
    "status": str,
    "matchedVia": str,
    "ts": str,
    "revenue": "Amounts",
    "commission": "Amounts",
    "partner": Optional["GraphPartner"],
})

GraphPartner = TypedDict("GraphPartner", {
    "partnerId": str,
    "displayName": str,
    "email": str,
    "externalRef": Optional[str],
    "status": str,
    "commission": "Amounts",
    "referrals": List["GraphReferral"],
})

CreatorProfileStats = TypedDict("CreatorProfileStats", {
    "programs": int,
    "clicks": int,
    "referrals": int,
    "repeatPayerRate": Optional[float],
})

CreatorProfile = TypedDict("CreatorProfile", {
    "accountId": str,
    "name": Optional[str],
    "email": NotRequired[str],
    "published": bool,
    "headline": str,
    "bio": str,
    "categories": List[str],
    "languages": List[str],
    "country": str,
    "channels": List["GetOpenapiJsonResponse"],
    "website": str,
    "minAudience": int,
    "acceptsInvites": bool,
    "audience": "GetOpenapiJsonResponse",
    "engagementBps": int,
    "stats": "CreatorProfileStats",
    "invited": NotRequired[bool],
})

EmailSettings = TypedDict("EmailSettings", {
    "provider": Optional[Literal["resend", "brevo", "postmark"]],
    "hasApiKey": bool,
    "fromAddress": Optional[str],
    "fromName": Optional[str],
    "replyTo": Optional[str],
    "defaultLocale": str,
    "logoUrl": Optional[str],
    "primaryColor": Optional[str],
    "domainStatus": Literal["unknown", "pending", "verified", "failed"],
    "domainCheckedAt": Optional[str],
})

EmailRendered = TypedDict("EmailRendered", {
    "locale": str,
    "subject": str,
    "text": str,
    "html": str,
    "source": Literal["override", "default"],
})

Notification = TypedDict("Notification", {
    "id": str,
    "topic": str,
    "message": str,
    "data": Optional["GetOpenapiJsonResponse"],
    "readAt": Optional[str],
    "createdAt": str,
})

Passport = TypedDict("Passport", {
    "claims": "GetOpenapiJsonResponse",
    "signature": str,
    "algorithm": Literal["ed25519"],
    "publicKey": str,
})

IncidentUpdatesItem = TypedDict("IncidentUpdatesItem", {
    "id": str,
    "body": str,
    "state": Literal["investigating", "identified", "monitoring", "resolved"],
    "createdAt": str,
})

Incident = TypedDict("Incident", {
    "id": str,
    "title": str,
    "state": Literal["investigating", "identified", "monitoring", "resolved"],
    "severity": Literal["notice", "minor", "major", "critical", "maintenance"],
    "body": str,
    "components": List[str],
    "startedAt": str,
    "resolvedAt": Optional[str],
    "updatedAt": str,
    "updates": List["IncidentUpdatesItem"],
})

RetentionPolicy = TypedDict("RetentionPolicy", {
    "clicks": Optional[int],
    "visits": Optional[int],
    "billingPayloads": Optional[int],
    "webhookDeliveries": Optional[int],
    "notifications": Optional[int],
    "auditLog": Optional[int],
})

RetentionLimitsValue = TypedDict("RetentionLimitsValue", {
    "minDays": int,
    "defaultDays": Optional[int],
})

RetentionLastRunOption1 = TypedDict("RetentionLastRunOption1", {
    "at": str,
    "result": "GetOpenapiJsonResponse",
})

Retention = TypedDict("Retention", {
    "policy": "RetentionPolicy",
    "limits": Dict[str, "RetentionLimitsValue"],
    "lastRun": Optional["RetentionLastRunOption1"],
})

PartnerGroupBaseOption1Option1 = TypedDict("PartnerGroupBaseOption1Option1", {
    "kind": Literal["percent"],
    "bps": int,
})

PartnerGroupBaseOption1Option2 = TypedDict("PartnerGroupBaseOption1Option2", {
    "kind": Literal["fixed"],
    "amountMinor": int,
    "currency": str,
})

PartnerGroup = TypedDict("PartnerGroup", {
    "id": str,
    "programId": str,
    "name": str,
    "base": Optional[Union["PartnerGroupBaseOption1Option1", "PartnerGroupBaseOption1Option2"]],
    "holdDays": Optional[int],
    "minThresholdMinor": Optional[int],
    "payoutCurrency": Optional[str],
    "onboardingMessage": Optional[str],
    "onboardingChecklist": List[str],
    "members": NotRequired[int],
    "archivedAt": Optional[str],
    "createdAt": str,
})

PromotionEffectOption1BaseOption1 = TypedDict("PromotionEffectOption1BaseOption1", {
    "kind": Literal["percent"],
    "bps": int,
})

PromotionEffectOption1BaseOption2 = TypedDict("PromotionEffectOption1BaseOption2", {
    "kind": Literal["fixed"],
    "amountMinor": int,
    "currency": str,
})

PromotionEffectOption1 = TypedDict("PromotionEffectOption1", {
    "kind": Literal["replace"],
    "base": Union["PromotionEffectOption1BaseOption1", "PromotionEffectOption1BaseOption2"],
})

PromotionEffectOption2 = TypedDict("PromotionEffectOption2", {
    "kind": Literal["boost"],
    "bps": int,
})

Promotion = TypedDict("Promotion", {
    "id": str,
    "programId": str,
    "name": str,
    "groupId": Optional[str],
    "effect": Union["PromotionEffectOption1", "PromotionEffectOption2"],
    "startsAt": str,
    "endsAt": str,
    "endedAt": Optional[str],
    "status": Literal["scheduled", "active", "ended"],
    "createdAt": str,
})

IntegrationConnection = TypedDict("IntegrationConnection", {
    "id": str,
    "kind": Literal["hubspot", "segment"],
    "status": Literal["active", "paused", "error"],
    "config": "GetOpenapiJsonResponse",
    "hasCredential": bool,
    "lastError": Optional[str],
    "lastSuccessAt": Optional[str],
    "pausedUntil": Optional[str],
    "createdAt": str,
    "updatedAt": str,
})

IntegrationDelivery = TypedDict("IntegrationDelivery", {
    "id": str,
    "kind": Literal["zapier", "hubspot", "segment"],
    "targetId": str,
    "eventId": str,
    "topic": str,
    "status": Literal["pending", "sent", "failed", "skipped"],
    "attempts": int,
    "nextAt": str,
    "lastError": Optional[str],
    "sentAt": Optional[str],
    "createdAt": str,
})

ZapierHook = TypedDict("ZapierHook", {
    "id": str,
    "event": str,
    "target_url": str,
    "createdAt": str,
})

# Recorded treatment referrals that got referee credit.
RoiIncrementalTreatment = TypedDict("RoiIncrementalTreatment", {
    "n": int,
    "cashAfterPerReferralMinor": int,
    "profitAfterPerReferralMinor": Optional[int],
})

# Recorded control (holdout) referrals: no credit.
RoiIncrementalControl = TypedDict("RoiIncrementalControl", {
    "n": int,
    "cashAfterPerReferralMinor": int,
    "profitAfterPerReferralMinor": Optional[int],
})

# Referrals in range left out of both groups, by reason.
RoiIncrementalExcludedReferrals = TypedDict("RoiIncrementalExcludedReferrals", {
    "unrecorded": int,
    "treatmentWithoutCredit": int,
    "controlWithCredit": int,
})

RoiIncrementalExcludedItem = TypedDict("RoiIncrementalExcludedItem", {
    "eventId": str,
    "currency": str,
    "reason": Literal["no_fx_rate"],
})

# Present with model=incremental.
RoiIncremental = TypedDict("RoiIncremental", {
    "currency": str,
    "windowDays": int,
    "holdoutBps": int,
    "treatment": "RoiIncrementalTreatment",
    "control": "RoiIncrementalControl",
    "liftMinorPerReferral": int,
    "liftProfitMinorPerReferral": Optional[int],
    "creditCostPerReferralMinor": int,
    "incrementalRoi": Optional[float],
    "eligible": bool,
    "reason": NotRequired[Literal["no_holdout", "too_few", "no_recorded_groups"]],
    "unrecordedReferrals": int,
    "excludedReferrals": "RoiIncrementalExcludedReferrals",
    "excluded": List["RoiIncrementalExcludedItem"],
})

RoiProjectionCohortsItem = TypedDict("RoiProjectionCohortsItem", {
    "programId": Optional[str],
    "role": Literal["referee", "referrer"],
    "eligible": bool,
    "reason": NotRequired[Literal["not_enough_history"]],
    "closedGrants": int,
    "openGrants": int,
    "medianCrossingDay": NotRequired[Optional[int]],
    "curveThroughDay": NotRequired[int],
    "noCrossingReason": NotRequired[Literal["cohort_not_paid_back", "insufficient_horizon"]],
    "behindCohort": NotRequired[int],
})

# Present with includeProjection=true.
RoiProjection = TypedDict("RoiProjection", {
    "label": Literal["projection"],
    "eligible": bool,
    "reason": NotRequired[Literal["not_enough_history"]],
    "closedGrants": int,
    "openGrants": int,
    "projectedGrants": int,
    "expectedPaidBackShareBps": Optional[int],
    "medianExpectedPaybackDays": Optional[int],
    "cohorts": List["RoiProjectionCohortsItem"],
})

RoiSummaryCoverage = TypedDict("RoiSummaryCoverage", {
    "creditAppliedReportedBps": Optional[int],
    "marginCoveredBps": Optional[int],
    "inferredShareBps": Optional[int],
})

RoiSummaryTargetOption1 = TypedDict("RoiSummaryTargetOption1", {
    "targetRoiBps": int,
    "status": Literal["on_track", "below", "unknown"],
})

RoiSummary = TypedDict("RoiSummary", {
    "currency": str,
    "creditCostMinor": int,
    "cashAfterMinor": int,
    "profitAfterMinor": Optional[int],
    "netMinor": Optional[int],
    "roi": Optional[float],
    "paidBackShareBps": Optional[int],
    "medianPaybackDays": Optional[float],
    "grants": int,
    "profitSources": Dict[str, int],
    "coverage": "RoiSummaryCoverage",
    "outstandingCreditMinor": int,
    "outstandingCostIfUsedMinor": Optional[int],
    "currencies": List[str],
    "incremental": NotRequired["RoiIncremental"],
    "projection": NotRequired["RoiProjection"],
    "target": NotRequired[Optional["RoiSummaryTargetOption1"]],
})

RoiGrantMetricsExcludedItem = TypedDict("RoiGrantMetricsExcludedItem", {
    "eventId": str,
    "currency": str,
    "reason": Literal["no_fx_rate"],
})

RoiGrantMetrics = TypedDict("RoiGrantMetrics", {
    "grantId": str,
    "role": Literal["referee", "referrer"],
    "currency": str,
    "faceMinor": int,
    "usedMinor": int,
    "costMinor": int,
    "cashAfterMinor": int,
    "profitAfterMinor": Optional[int],
    "netMinor": Optional[int],
    "roi": Optional[float],
    "paidBack": Optional[bool],
    "paybackDays": Optional[int],
    "profitSource": Literal["event", "cost_events", "catalog", "program", "org", "none", "mixed"],
    "inferredShareBps": int,
    "windowDays": int,
    "excluded": List["RoiGrantMetricsExcludedItem"],
})

RoiGrant = TypedDict("RoiGrant", {
    "id": str,
    "source": Literal["referee_reward", "commission_credit", "external", "manual"],
    "role": Literal["referee", "referrer"],
    "status": Literal["open", "used", "expired", "revoked"],
    "customerRef": Optional[str],
    "partnerId": Optional[str],
    "referralId": Optional[str],
    "programId": Optional[str],
    "grantCurrency": str,
    "grantedAt": str,
    "expiresAt": Optional[str],
    "currency": str,
    "faceMinor": int,
    "usedMinor": int,
    "costMinor": int,
    "cashAfterMinor": int,
    "profitAfterMinor": Optional[int],
    "netMinor": Optional[int],
    "roi": Optional[float],
    "paidBack": Optional[bool],
    "paybackDays": Optional[int],
    "profitSource": Literal["event", "cost_events", "catalog", "program", "org", "none", "mixed"],
    "inferredShareBps": int,
    "windowDays": int,
})

RoiPatternEntrySubject = TypedDict("RoiPatternEntrySubject", {
    "customerRef": NotRequired[str],
    "partnerId": NotRequired[str],
})

RoiPatternEntry = TypedDict("RoiPatternEntry", {
    "subject": "RoiPatternEntrySubject",
    "programId": Optional[str],
    "detail": Dict[str, Any],
})

RoiTraceSubject = TypedDict("RoiTraceSubject", {
    "type": Literal["customer", "partner"],
    "id": str,
    "customerRefs": List[str],
    "partnerId": Optional[str],
})

RoiTraceEventsItem = TypedDict("RoiTraceEventsItem", {
    "id": str,
    "kind": str,
    "occurredAt": str,
    "amounts": Dict[str, Optional[Union[str, float]]],
    "confidence": Literal["reported", "extracted", "inferred"],
    "source": str,
    "superseded": bool,
    "links": Dict[str, Optional[str]],
})

RoiTraceRunningNetItem = TypedDict("RoiTraceRunningNetItem", {
    "at": str,
    "netMinor": Optional[int],
})

RoiTraceExcludedItem = TypedDict("RoiTraceExcludedItem", {
    "eventId": str,
    "currency": str,
    "reason": Literal["no_fx_rate"],
})

RoiTrace = TypedDict("RoiTrace", {
    "subject": "RoiTraceSubject",
    "events": List["RoiTraceEventsItem"],
    "grants": List["RoiGrantMetrics"],
    "runningNet": List["RoiTraceRunningNetItem"],
    "excluded": List["RoiTraceExcludedItem"],
})

AuditLogEntry = TypedDict("AuditLogEntry", {
    "id": str,
    "actorType": str,
    "actorId": str,
    "action": str,
    "subjectType": str,
    "subjectId": str,
    "data": "GetOpenapiJsonResponse",
    "createdAt": str,
})

EmailTemplateEventLocalesItemDefault = TypedDict("EmailTemplateEventLocalesItemDefault", {
    "subject": str,
    "body": str,
    "cta": str,
})

EmailTemplateEventLocalesItemOverrideOption1 = TypedDict("EmailTemplateEventLocalesItemOverrideOption1", {
    "subject": str,
    "text": str,
    "html": Optional[str],
    "updatedAt": str,
})

EmailTemplateEventLocalesItem = TypedDict("EmailTemplateEventLocalesItem", {
    "locale": str,
    "default": "EmailTemplateEventLocalesItemDefault",
    "override": Optional["EmailTemplateEventLocalesItemOverrideOption1"],
})

EmailTemplateEvent = TypedDict("EmailTemplateEvent", {
    "event": str,
    "audience": Literal["partner", "merchant"],
    "placeholders": List[str],
    "locales": List["EmailTemplateEventLocalesItem"],
})

ErrorError = TypedDict("ErrorError", {
    "code": str,
    "message": str,
    "details": NotRequired[Any],
    "requestId": NotRequired[str],
    "docs_url": str,
})

Error = TypedDict("Error", {
    "error": "ErrorError",
})

# `data` of a `click.recorded` event: Fires for every click (tracked link redirects, `?via=` landings, server-side clicks). High volume: subscribe only if you need click-level data.
ClickRecordedEventData = TypedDict("ClickRecordedEventData", {
    "clickId": str,
    "programId": str,
    "partnerId": str,
    "linkId": Optional[str],
})

# A tracked click was recorded: the `click.recorded` delivery body.
ClickRecordedEvent = TypedDict("ClickRecordedEvent", {
    "id": str,
    "topic": Literal["click.recorded"],
    "orgId": str,
    "livemode": bool,
    "createdAt": str,
    "data": "ClickRecordedEventData",
})

# `data` of a `referral.created` event: A new referral: from `POST /v1/referrals/associate`, an auth-platform sign-up, a mobile install, a won deal or an agent attribution.
ReferralCreatedEventData = TypedDict("ReferralCreatedEventData", {
    "referralId": str,
    "programId": str,
    "partnerId": str,
    "partnerExternalRef": Optional[str],
    "customerRef": str,
    "status": Literal["active", "pending_review", "paused", "void"],
    "matchedVia": str,
})

# A customer was attributed to a partner: the `referral.created` delivery body.
ReferralCreatedEvent = TypedDict("ReferralCreatedEvent", {
    "id": str,
    "topic": Literal["referral.created"],
    "orgId": str,
    "livemode": bool,
    "createdAt": str,
    "data": "ReferralCreatedEventData",
})

# `data` of a `referral.held` event: A risk or self-referral check put the referral in `pending_review`; `reasons` says why and `caseId` is the fraud case opened for it.
ReferralHeldEventData = TypedDict("ReferralHeldEventData", {
    "referralId": str,
    "programId": str,
    "partnerId": str,
    "partnerExternalRef": Optional[str],
    "customerRef": str,
    "status": Literal["active", "pending_review", "paused", "void"],
    "reasons": List[str],
    "caseId": str,
})

# A referral was held for review: the `referral.held` delivery body.
ReferralHeldEvent = TypedDict("ReferralHeldEvent", {
    "id": str,
    "topic": Literal["referral.held"],
    "orgId": str,
    "livemode": bool,
    "createdAt": str,
    "data": "ReferralHeldEventData",
})

# `data` of a `referral.approved` event: Back to `active`: approved by the merchant, a fraud case dismissed (`reason: "fraud_case_dismissed"`, with `caseId`), or a hold released by email verification (`reason: "email_verified"`).
ReferralApprovedEventData = TypedDict("ReferralApprovedEventData", {
    "referralId": str,
    "programId": str,
    "partnerId": str,
    "partnerExternalRef": Optional[str],
    "customerRef": str,
    "status": Literal["active", "pending_review", "paused", "void"],
    "reason": NotRequired[str],
    "caseId": NotRequired[str],
})

# A held referral was approved: the `referral.approved` delivery body.
ReferralApprovedEvent = TypedDict("ReferralApprovedEvent", {
    "id": str,
    "topic": Literal["referral.approved"],
    "orgId": str,
    "livemode": bool,
    "createdAt": str,
    "data": "ReferralApprovedEventData",
})

# `data` of a `referral.voided` event: It earns nothing more: voided by the merchant, a fraud case (`reason` `fraud_case_voided` or `partner_banned`, with `caseId`) or an identity provider (`fraud_confirmed`).
ReferralVoidedEventData = TypedDict("ReferralVoidedEventData", {
    "referralId": str,
    "programId": str,
    "partnerId": str,
    "partnerExternalRef": Optional[str],
    "customerRef": str,
    "status": Literal["active", "pending_review", "paused", "void"],
    "reason": NotRequired[str],
    "caseId": NotRequired[str],
})

# A referral was voided: the `referral.voided` delivery body.
ReferralVoidedEvent = TypedDict("ReferralVoidedEvent", {
    "id": str,
    "topic": Literal["referral.voided"],
    "orgId": str,
    "livemode": bool,
    "createdAt": str,
    "data": "ReferralVoidedEventData",
})

# `data` of a `referral.paused` event: The merchant paused the referral: it earns no new commissions until resumed.
ReferralPausedEventData = TypedDict("ReferralPausedEventData", {
    "referralId": str,
    "programId": str,
    "partnerId": str,
    "partnerExternalRef": Optional[str],
    "customerRef": str,
    "status": Literal["active", "pending_review", "paused", "void"],
})

# A referral was paused: the `referral.paused` delivery body.
ReferralPausedEvent = TypedDict("ReferralPausedEvent", {
    "id": str,
    "topic": Literal["referral.paused"],
    "orgId": str,
    "livemode": bool,
    "createdAt": str,
    "data": "ReferralPausedEventData",
})

# `data` of a `referral.resumed` event: The referral is `active` again.
ReferralResumedEventData = TypedDict("ReferralResumedEventData", {
    "referralId": str,
    "programId": str,
    "partnerId": str,
    "partnerExternalRef": Optional[str],
    "customerRef": str,
    "status": Literal["active", "pending_review", "paused", "void"],
})

# A paused referral was resumed: the `referral.resumed` delivery body.
ReferralResumedEvent = TypedDict("ReferralResumedEvent", {
    "id": str,
    "topic": Literal["referral.resumed"],
    "orgId": str,
    "livemode": bool,
    "createdAt": str,
    "data": "ReferralResumedEventData",
})

# `data` of a `referral.reassigned` event: The merchant reassigned the referral; the payload names the new partner, with the previous one in `previousPartnerId` and `previousPartnerExternalRef`.
ReferralReassignedEventData = TypedDict("ReferralReassignedEventData", {
    "referralId": str,
    "programId": str,
    "partnerId": str,
    "partnerExternalRef": Optional[str],
    "customerRef": str,
    "status": Literal["active", "pending_review", "paused", "void"],
    "previousPartnerId": str,
    "previousPartnerExternalRef": Optional[str],
})

# A referral moved to another partner: the `referral.reassigned` delivery body.
ReferralReassignedEvent = TypedDict("ReferralReassignedEvent", {
    "id": str,
    "topic": Literal["referral.reassigned"],
    "orgId": str,
    "livemode": bool,
    "createdAt": str,
    "data": "ReferralReassignedEventData",
})

# `data` of a `referral.rejected` event: A self-referral the program's `selfReferralPolicy: "reject"` refused, so no referral exists. A `fraud.case_opened` follows.
ReferralRejectedEventData = TypedDict("ReferralRejectedEventData", {
    "programId": str,
    "partnerId": str,
    "customerRef": str,
    "reason": Literal["self_referral"],
})

# A self-referral was refused: the `referral.rejected` delivery body.
ReferralRejectedEvent = TypedDict("ReferralRejectedEvent", {
    "id": str,
    "topic": Literal["referral.rejected"],
    "orgId": str,
    "livemode": bool,
    "createdAt": str,
    "data": "ReferralRejectedEventData",
})

# `data` of a `customer.aliased` event: The app changed a user's id after their sign-up was filed (through an auth connection); their referrals now use `toCustomerRef`.
CustomerAliasedEventData = TypedDict("CustomerAliasedEventData", {
    "fromCustomerRef": str,
    "toCustomerRef": str,
    "referralIds": List[str],
    "partnerId": Optional[str],
})

# A customer's id changed: the `customer.aliased` delivery body.
CustomerAliasedEvent = TypedDict("CustomerAliasedEvent", {
    "id": str,
    "topic": Literal["customer.aliased"],
    "orgId": str,
    "livemode": bool,
    "createdAt": str,
    "data": "CustomerAliasedEventData",
})

# `data` of a `commission.earned` event: A payment (or a signup, trial or product-event bounty) earned a partner a commission line. Payment fields are null for bounties.
CommissionEarnedEventData = TypedDict("CommissionEarnedEventData", {
    "commissionId": str,
    "partnerId": str,
    "programId": str,
    "amountMinor": int,
    "currency": str,
    "referralId": Optional[str],
    "customerRef": Optional[str],
    "billingEventId": Optional[str],
    "providerEventId": Optional[str],
    "invoiceRef": Optional[str],
    "customerExternalRef": Optional[str],
    "partnerExternalRef": Optional[str],
    "level": int,
    "memo": str,
    "basisMinor": Optional[int],
})

# A commission line was earned: the `commission.earned` delivery body.
CommissionEarnedEvent = TypedDict("CommissionEarnedEvent", {
    "id": str,
    "topic": Literal["commission.earned"],
    "orgId": str,
    "livemode": bool,
    "createdAt": str,
    "data": "CommissionEarnedEventData",
})

# `data` of a `commission.reversed` event: A refund or dispute clawed back an earned line. `commissionId` and `relatedCommissionId` are the original line, `reversalId` the new `reversed` event; `amountMinor` is negative.
CommissionReversedEventData = TypedDict("CommissionReversedEventData", {
    "commissionId": str,
    "relatedCommissionId": str,
    "reversalId": str,
    "partnerId": str,
    "programId": str,
    "amountMinor": int,
    "currency": str,
    "referralId": Optional[str],
    "customerRef": Optional[str],
    "billingEventId": Optional[str],
    "providerEventId": Optional[str],
    "invoiceRef": Optional[str],
    "customerExternalRef": Optional[str],
    "partnerExternalRef": Optional[str],
    "level": int,
    "memo": str,
})

# A commission line was reversed: the `commission.reversed` delivery body.
CommissionReversedEvent = TypedDict("CommissionReversedEvent", {
    "id": str,
    "topic": Literal["commission.reversed"],
    "orgId": str,
    "livemode": bool,
    "createdAt": str,
    "data": "CommissionReversedEventData",
})

# `data` of a `commission.settled` event: The merchant paid the line itself (`store_credit`, or `merchant_credit` for programs that settle as they earn), outside payout runs.
CommissionSettledEventData = TypedDict("CommissionSettledEventData", {
    "commissionId": str,
    "partnerId": str,
    "programId": str,
    "referralId": Optional[str],
    "amountMinor": int,
    "currency": str,
    "method": Literal["store_credit", "merchant_credit"],
    "reference": str,
})

# A commission line was settled by the merchant: the `commission.settled` delivery body.
CommissionSettledEvent = TypedDict("CommissionSettledEvent", {
    "id": str,
    "topic": Literal["commission.settled"],
    "orgId": str,
    "livemode": bool,
    "createdAt": str,
    "data": "CommissionSettledEventData",
})

# `data` of a `partner.applied` event: An application waiting for approval. `enrollmentId` is absent for applications from the public program page.
PartnerAppliedEventData = TypedDict("PartnerAppliedEventData", {
    "programId": str,
    "partnerId": str,
    "enrollmentId": NotRequired[str],
})

# A partner applied to a program: the `partner.applied` delivery body.
PartnerAppliedEvent = TypedDict("PartnerAppliedEvent", {
    "id": str,
    "topic": Literal["partner.applied"],
    "orgId": str,
    "livemode": bool,
    "createdAt": str,
    "data": "PartnerAppliedEventData",
})

# `data` of a `partner.enrolled` event: The merchant (or an import) enrolled the partner in a program, approved at once.
PartnerEnrolledEventData = TypedDict("PartnerEnrolledEventData", {
    "programId": str,
    "partnerId": str,
    "enrollmentId": str,
})

# A partner was enrolled: the `partner.enrolled` delivery body.
PartnerEnrolledEvent = TypedDict("PartnerEnrolledEvent", {
    "id": str,
    "topic": Literal["partner.enrolled"],
    "orgId": str,
    "livemode": bool,
    "createdAt": str,
    "data": "PartnerEnrolledEventData",
})

# `data` of a `partner.approved` event: An application was approved, or a partner joined a program that approves at once. `enrollmentId` is present when approved from an application.
PartnerApprovedEventData = TypedDict("PartnerApprovedEventData", {
    "programId": str,
    "partnerId": str,
    "enrollmentId": NotRequired[str],
})

# A partner was approved: the `partner.approved` delivery body.
PartnerApprovedEvent = TypedDict("PartnerApprovedEvent", {
    "id": str,
    "topic": Literal["partner.approved"],
    "orgId": str,
    "livemode": bool,
    "createdAt": str,
    "data": "PartnerApprovedEventData",
})

# `data` of a `partner.level_up` event: Partner leveling promoted the partner; `referrals` is the count that qualified them.
PartnerLevelUpEventData = TypedDict("PartnerLevelUpEventData", {
    "programId": str,
    "partnerId": str,
    "level": str,
    "referrals": int,
})

# A partner reached a new level: the `partner.level_up` delivery body.
PartnerLevelUpEvent = TypedDict("PartnerLevelUpEvent", {
    "id": str,
    "topic": Literal["partner.level_up"],
    "orgId": str,
    "livemode": bool,
    "createdAt": str,
    "data": "PartnerLevelUpEventData",
})

# `data` of a `payout.scheduled` event: A payout run included the partner; nothing has been paid yet.
PayoutScheduledEventData = TypedDict("PayoutScheduledEventData", {
    "payoutId": str,
    "partnerId": str,
    "amountMinor": int,
    "currency": str,
})

# A payout was created in a run: the `payout.scheduled` delivery body.
PayoutScheduledEvent = TypedDict("PayoutScheduledEvent", {
    "id": str,
    "topic": Literal["payout.scheduled"],
    "orgId": str,
    "livemode": bool,
    "createdAt": str,
    "data": "PayoutScheduledEventData",
})

# `data` of a `payout.submitted` event: The payout provider accepted the payout and settles it asynchronously; `payout.sent` or `payout.failed` follows.
PayoutSubmittedEventData = TypedDict("PayoutSubmittedEventData", {
    "payoutId": str,
    "partnerId": str,
    "amountMinor": int,
    "currency": str,
})

# A payout was submitted to the provider: the `payout.submitted` delivery body.
PayoutSubmittedEvent = TypedDict("PayoutSubmittedEvent", {
    "id": str,
    "topic": Literal["payout.submitted"],
    "orgId": str,
    "livemode": bool,
    "createdAt": str,
    "data": "PayoutSubmittedEventData",
})

# `data` of a `payout.sent` event: The money left: the provider confirmed the payout (at once, or later through its settlement webhook).
PayoutSentEventData = TypedDict("PayoutSentEventData", {
    "payoutId": str,
    "partnerId": str,
    "amountMinor": int,
    "currency": str,
})

# A payout was paid: the `payout.sent` delivery body.
PayoutSentEvent = TypedDict("PayoutSentEvent", {
    "id": str,
    "topic": Literal["payout.sent"],
    "orgId": str,
    "livemode": bool,
    "createdAt": str,
    "data": "PayoutSentEventData",
})

# `data` of a `payout.failed` event: The provider refused or failed the payout; `reason` is its message. The lines go back to the partner's approved balance.
PayoutFailedEventData = TypedDict("PayoutFailedEventData", {
    "payoutId": str,
    "partnerId": str,
    "reason": str,
})

# A payout failed: the `payout.failed` delivery body.
PayoutFailedEvent = TypedDict("PayoutFailedEvent", {
    "id": str,
    "topic": Literal["payout.failed"],
    "orgId": str,
    "livemode": bool,
    "createdAt": str,
    "data": "PayoutFailedEventData",
})

# `data` of a `payout.cancelled` event: One per payout when an unexecuted payout run is cancelled.
PayoutCancelledEventData = TypedDict("PayoutCancelledEventData", {
    "payoutId": str,
    "partnerId": str,
})

# A payout was cancelled: the `payout.cancelled` delivery body.
PayoutCancelledEvent = TypedDict("PayoutCancelledEvent", {
    "id": str,
    "topic": Literal["payout.cancelled"],
    "orgId": str,
    "livemode": bool,
    "createdAt": str,
    "data": "PayoutCancelledEventData",
})

# `data` of a `tax.form_delivered` event: A filed 1099-NEC was accepted and delivered; `emailed` says whether the filing provider also emailed it.
TaxFormDeliveredEventData = TypedDict("TaxFormDeliveredEventData", {
    "documentId": str,
    "partnerId": str,
    "taxYear": int,
    "form": Literal["1099-nec"],
    "corrected": bool,
    "emailed": bool,
})

# A tax form was delivered to a partner: the `tax.form_delivered` delivery body.
TaxFormDeliveredEvent = TypedDict("TaxFormDeliveredEvent", {
    "id": str,
    "topic": Literal["tax.form_delivered"],
    "orgId": str,
    "livemode": bool,
    "createdAt": str,
    "data": "TaxFormDeliveredEventData",
})

# `data` of a `referee_reward.earned` event: The friend's side of a double-sided program: the referred customer's reward was issued.
RefereeRewardEarnedEventData = TypedDict("RefereeRewardEarnedEventData", {
    "rewardId": str,
    "referralId": str,
    "programId": str,
    "customerRef": str,
    "customerExternalRef": Optional[str],
    "kind": Literal["store_credit", "coupon", "gift_card"],
    "amountMinor": int,
    "currency": str,
    "code": Optional[str],
    "billingEventId": Optional[str],
    "commissionId": Optional[str],
})

# A referred customer earned their reward: the `referee_reward.earned` delivery body.
RefereeRewardEarnedEvent = TypedDict("RefereeRewardEarnedEvent", {
    "id": str,
    "topic": Literal["referee_reward.earned"],
    "orgId": str,
    "livemode": bool,
    "createdAt": str,
    "data": "RefereeRewardEarnedEventData",
})

# `data` of a `credit.redeemed` event: From `POST /v1/rewards/{id}/redeem` or `POST /v1/rewards/redeem-by-code`. `amountMinor` is what this redemption used (capped at the balance); a repeated `externalId` does not fire again.
CreditRedeemedEventData = TypedDict("CreditRedeemedEventData", {
    "grantId": str,
    "rewardId": str,
    "amountMinor": int,
    "remainingMinor": int,
})

# A referee reward was redeemed: the `credit.redeemed` delivery body.
CreditRedeemedEvent = TypedDict("CreditRedeemedEvent", {
    "id": str,
    "topic": Literal["credit.redeemed"],
    "orgId": str,
    "livemode": bool,
    "createdAt": str,
    "data": "CreditRedeemedEventData",
})

# `data` of a `billing_event.recorded` event: Fires once per newly recorded billing event from any connection, never for duplicates.
BillingEventRecordedEventData = TypedDict("BillingEventRecordedEventData", {
    "billingEventId": str,
    "type": str,
    "customerRef": str,
    "currency": str,
    "amountMinor": int,
})

# A billing event was recorded: the `billing_event.recorded` delivery body.
BillingEventRecordedEvent = TypedDict("BillingEventRecordedEvent", {
    "id": str,
    "topic": Literal["billing_event.recorded"],
    "orgId": str,
    "livemode": bool,
    "createdAt": str,
    "data": "BillingEventRecordedEventData",
})

# `data` of a `roi.payback_reached` event: Once per credit grant, the first time its recipient's profit after it covered its cost. A later refund that un-pays it doesn't fire it again.
RoiPaybackReachedEventData = TypedDict("RoiPaybackReachedEventData", {
    "grantId": str,
    "paybackDays": int,
    "netMinor": int,
    "currency": str,
})

# A credit grant paid back: the `roi.payback_reached` delivery body.
RoiPaybackReachedEvent = TypedDict("RoiPaybackReachedEvent", {
    "id": str,
    "topic": Literal["roi.payback_reached"],
    "orgId": str,
    "livemode": bool,
    "createdAt": str,
    "data": "RoiPaybackReachedEventData",
})

# `data` of a `roi.pattern_detected` event: A daily summary, at most once per pattern per day, only when the set of matching subjects changed and `count` is above zero. Read the full list from `GET /v1/roi/patterns/{pattern}`.
RoiPatternDetectedEventData = TypedDict("RoiPatternDetectedEventData", {
    "pattern": Literal["credit_only", "churn_at_exhaustion", "bonus_collector", "negative_partner"],
    "count": int,
    "newCount": int,
    "sample": List[str],
})

# A value pattern changed: the `roi.pattern_detected` delivery body.
RoiPatternDetectedEvent = TypedDict("RoiPatternDetectedEvent", {
    "id": str,
    "topic": Literal["roi.pattern_detected"],
    "orgId": str,
    "livemode": bool,
    "createdAt": str,
    "data": "RoiPatternDetectedEventData",
})

# `data` of a `fraud.case_opened` event: A case is waiting in the queue. `kind` is `self_referral`, `quality`, `ring`, `identity_risk` or `value_pattern`; the other fields depend on it (`partnerId`, `referralId`, ring `members`, identity-risk `reasons`, value `pattern`). A self-referral rejected by policy has `referralId: null` and `rejected: true`.
FraudCaseOpenedEventData = TypedDict("FraudCaseOpenedEventData", {
    "caseId": str,
    "kind": Literal["self_referral", "quality", "ring", "identity_risk", "value_pattern"],
    "partnerId": NotRequired[Optional[str]],
    "referralId": NotRequired[Optional[str]],
    "members": NotRequired[List[str]],
    "reasons": NotRequired[List[str]],
    "pattern": NotRequired[str],
    "rejected": NotRequired[bool],
})

# A fraud case was opened: the `fraud.case_opened` delivery body.
FraudCaseOpenedEvent = TypedDict("FraudCaseOpenedEvent", {
    "id": str,
    "topic": Literal["fraud.case_opened"],
    "orgId": str,
    "livemode": bool,
    "createdAt": str,
    "data": "FraudCaseOpenedEventData",
})

# `data` of a `deal.submitted` event: A B2B deal waiting for the merchant to approve.
DealSubmittedEventData = TypedDict("DealSubmittedEventData", {
    "dealId": str,
    "partnerId": str,
    "company": str,
})

# A partner registered a deal: the `deal.submitted` delivery body.
DealSubmittedEvent = TypedDict("DealSubmittedEvent", {
    "id": str,
    "topic": Literal["deal.submitted"],
    "orgId": str,
    "livemode": bool,
    "createdAt": str,
    "data": "DealSubmittedEventData",
})

# `data` of a `dispute.resolved` event: The merchant resolved a partner's dispute with the `resolution` note.
DisputeResolvedEventData = TypedDict("DisputeResolvedEventData", {
    "disputeId": str,
    "resolution": str,
})

# A partner dispute was resolved: the `dispute.resolved` delivery body.
DisputeResolvedEvent = TypedDict("DisputeResolvedEvent", {
    "id": str,
    "topic": Literal["dispute.resolved"],
    "orgId": str,
    "livemode": bool,
    "createdAt": str,
    "data": "DisputeResolvedEventData",
})

# `data` of a `privacy.request_completed` event: An access or erasure request opened with `POST /v1/privacy/requests` completed or failed; `found` is present when completed.
PrivacyRequestCompletedEventData = TypedDict("PrivacyRequestCompletedEventData", {
    "requestId": str,
    "type": Literal["access", "erasure"],
    "status": Literal["completed", "failed"],
    "found": NotRequired[bool],
})

# A data-subject request finished: the `privacy.request_completed` delivery body.
PrivacyRequestCompletedEvent = TypedDict("PrivacyRequestCompletedEvent", {
    "id": str,
    "topic": Literal["privacy.request_completed"],
    "orgId": str,
    "livemode": bool,
    "createdAt": str,
    "data": "PrivacyRequestCompletedEventData",
})

# `data` of a `webhook_endpoint.disabled` event: Sent to your other active endpoints when one is disabled after every delivery failed for 72 hours (or 1000 attempts in a row).
WebhookEndpointDisabledEventData = TypedDict("WebhookEndpointDisabledEventData", {
    "endpointId": str,
    "url": str,
    "reason": str,
    "lastStatusCode": Optional[int],
    "days": int,
})

# A failing webhook endpoint was disabled: the `webhook_endpoint.disabled` delivery body.
WebhookEndpointDisabledEvent = TypedDict("WebhookEndpointDisabledEvent", {
    "id": str,
    "topic": Literal["webhook_endpoint.disabled"],
    "orgId": str,
    "livemode": bool,
    "createdAt": str,
    "data": "WebhookEndpointDisabledEventData",
})

# `data` of a `webhook_endpoint.failing` event: Sent to your other active endpoints (never the failing one) when an endpoint has failed every delivery for 1 hour, and again at 24 hours. It's disabled at `disablesAt` unless a delivery succeeds first.
WebhookEndpointFailingEventData = TypedDict("WebhookEndpointFailingEventData", {
    "endpointId": str,
    "url": str,
    "stage": Literal["1h", "24h"],
    "failingSince": str,
    "consecutiveFailures": int,
    "lastStatusCode": Optional[int],
    "sampleError": Optional[str],
    "disablesAt": str,
})

# A webhook endpoint keeps failing: the `webhook_endpoint.failing` delivery body.
WebhookEndpointFailingEvent = TypedDict("WebhookEndpointFailingEvent", {
    "id": str,
    "topic": Literal["webhook_endpoint.failing"],
    "orgId": str,
    "livemode": bool,
    "createdAt": str,
    "data": "WebhookEndpointFailingEventData",
})

# `data` of a `webhook_endpoint.recovered` event: Sent to your active endpoints, including the recovered one, when a delivery succeeds after the endpoint was failing.
WebhookEndpointRecoveredEventData = TypedDict("WebhookEndpointRecoveredEventData", {
    "endpointId": str,
    "url": str,
    "failingSince": str,
    "downForMs": int,
})

# A failing webhook endpoint recovered: the `webhook_endpoint.recovered` delivery body.
WebhookEndpointRecoveredEvent = TypedDict("WebhookEndpointRecoveredEvent", {
    "id": str,
    "topic": Literal["webhook_endpoint.recovered"],
    "orgId": str,
    "livemode": bool,
    "createdAt": str,
    "data": "WebhookEndpointRecoveredEventData",
})

PostTOrgTokenVisitResponse = TypedDict("PostTOrgTokenVisitResponse", {
    "ok": bool,
    "clickId": Optional[str],
})

GetTOrgTokenCodesCodeResponseRefereeRewardOption1 = TypedDict("GetTOrgTokenCodesCodeResponseRefereeRewardOption1", {
    "kind": str,
    "bps": NotRequired[int],
    "amountMinor": NotRequired[int],
    "capMinor": NotRequired[int],
    "currency": str,
    "on": str,
})

GetTOrgTokenCodesCodeResponse = TypedDict("GetTOrgTokenCodesCodeResponse", {
    "valid": bool,
    "partnerDisplayName": str,
    "refereeReward": Optional["GetTOrgTokenCodesCodeResponseRefereeRewardOption1"],
})

GetTOrgTokenWidgetMeResponseProgram = TypedDict("GetTOrgTokenWidgetMeResponseProgram", {
    "id": str,
    "name": str,
})

GetTOrgTokenWidgetMeResponsePartner = TypedDict("GetTOrgTokenWidgetMeResponsePartner", {
    "displayName": str,
})

GetTOrgTokenWidgetMeResponseShareOption1 = TypedDict("GetTOrgTokenWidgetMeResponseShareOption1", {
    "x": str,
    "facebook": str,
    "linkedin": str,
    "whatsapp": str,
    "email": str,
})

GetTOrgTokenWidgetMeResponseProgress = TypedDict("GetTOrgTokenWidgetMeResponseProgress", {
    "clicks": int,
    "signups": int,
    "payingCustomers": int,
})

GetTOrgTokenWidgetMeResponseEarningsItem = TypedDict("GetTOrgTokenWidgetMeResponseEarningsItem", {
    "currency": str,
    "pending": int,
    "approved": int,
    "paid": int,
})

GetTOrgTokenWidgetMeResponseRefereeRewardOption1 = TypedDict("GetTOrgTokenWidgetMeResponseRefereeRewardOption1", {
    "kind": str,
    "bps": NotRequired[int],
    "amountMinor": NotRequired[int],
    "capMinor": NotRequired[int],
    "currency": str,
    "on": str,
})

GetTOrgTokenWidgetMeResponse = TypedDict("GetTOrgTokenWidgetMeResponse", {
    "program": "GetTOrgTokenWidgetMeResponseProgram",
    "partner": "GetTOrgTokenWidgetMeResponsePartner",
    "code": Optional[str],
    "coupon": Optional[str],
    "link": Optional[str],
    "share": Optional["GetTOrgTokenWidgetMeResponseShareOption1"],
    "progress": "GetTOrgTokenWidgetMeResponseProgress",
    "earnings": List["GetTOrgTokenWidgetMeResponseEarningsItem"],
    "refereeReward": Optional["GetTOrgTokenWidgetMeResponseRefereeRewardOption1"],
})

GetTOrgTokenMobileResolveResponse = TypedDict("GetTOrgTokenMobileResolveResponse", {
    "matched": bool,
    "clickId": NotRequired[str],
    "code": NotRequired[str],
    "destination": NotRequired[str],
    "programId": NotRequired[str],
    "matchType": NotRequired[Literal["user_agent", "device", "ip"]],
})

PostTOrgTokenMobileInstallResponse = TypedDict("PostTOrgTokenMobileInstallResponse", {
    "attributed": bool,
    "referralId": Optional[str],
    "partnerId": Optional[str],
    "programId": str,
})

GetWellKnownAppleAppSiteAssociationResponseApplinksDetailsItemComponentsItem = TypedDict("GetWellKnownAppleAppSiteAssociationResponseApplinksDetailsItemComponentsItem", {
    "/": str,
})

GetWellKnownAppleAppSiteAssociationResponseApplinksDetailsItem = TypedDict("GetWellKnownAppleAppSiteAssociationResponseApplinksDetailsItem", {
    "appIDs": List[str],
    "components": List["GetWellKnownAppleAppSiteAssociationResponseApplinksDetailsItemComponentsItem"],
})

GetWellKnownAppleAppSiteAssociationResponseApplinks = TypedDict("GetWellKnownAppleAppSiteAssociationResponseApplinks", {
    "details": List["GetWellKnownAppleAppSiteAssociationResponseApplinksDetailsItem"],
})

GetWellKnownAppleAppSiteAssociationResponse = TypedDict("GetWellKnownAppleAppSiteAssociationResponse", {
    "applinks": "GetWellKnownAppleAppSiteAssociationResponseApplinks",
})

GetWellKnownAssetlinksJsonResponseValueItemTarget = TypedDict("GetWellKnownAssetlinksJsonResponseValueItemTarget", {
    "namespace": Literal["android_app"],
    "package_name": str,
    "sha256_cert_fingerprints": List[str],
})

GetWellKnownAssetlinksJsonResponseValueItem = TypedDict("GetWellKnownAssetlinksJsonResponseValueItem", {
    "relation": List[str],
    "target": "GetWellKnownAssetlinksJsonResponseValueItemTarget",
})

GetWellKnownAssetlinksJsonResponse: TypeAlias = "List[GetWellKnownAssetlinksJsonResponseValueItem]"

GetWellKnownForgedeckEmbedJsonResponseCheckers = TypedDict("GetWellKnownForgedeckEmbedJsonResponseCheckers", {
    "userAgent": str,
    "egress": List[str],
})

GetWellKnownForgedeckEmbedJsonResponseSurfacesTrackingSnippetCookieDaysOption2 = TypedDict("GetWellKnownForgedeckEmbedJsonResponseSurfacesTrackingSnippetCookieDaysOption2", {
    "default": int,
    "max": int,
    "note": str,
})

GetWellKnownForgedeckEmbedJsonResponseSurfacesTrackingSnippetStorageItemPurpose = TypedDict("GetWellKnownForgedeckEmbedJsonResponseSurfacesTrackingSnippetStorageItemPurpose", {
    "en": str,
})

GetWellKnownForgedeckEmbedJsonResponseSurfacesTrackingSnippetStorageItem = TypedDict("GetWellKnownForgedeckEmbedJsonResponseSurfacesTrackingSnippetStorageItem", {
    "name": str,
    "type": Literal["cookie", "localStorage"],
    "category": str,
    "lifetime": str,
    "purpose": "GetWellKnownForgedeckEmbedJsonResponseSurfacesTrackingSnippetStorageItemPurpose",
    "legacy": NotRequired[bool],
})

GetWellKnownForgedeckEmbedJsonResponseSurfacesTrackingSnippet = TypedDict("GetWellKnownForgedeckEmbedJsonResponseSurfacesTrackingSnippet", {
    "script": str,
    "csp": Dict[str, List[str]],
    "consentCategory": str,
    "consentFallbackCategory": str,
    "consentAdapters": List[str],
    "consentDefault": NotRequired[Dict[str, Any]],
    "cookieDays": Union[int, "GetWellKnownForgedeckEmbedJsonResponseSurfacesTrackingSnippetCookieDaysOption2"],
    "storage": List["GetWellKnownForgedeckEmbedJsonResponseSurfacesTrackingSnippetStorageItem"],
})

GetWellKnownForgedeckEmbedJsonResponseSurfacesPortalEmbedStorageItemPurpose = TypedDict("GetWellKnownForgedeckEmbedJsonResponseSurfacesPortalEmbedStorageItemPurpose", {
    "en": str,
})

GetWellKnownForgedeckEmbedJsonResponseSurfacesPortalEmbedStorageItem = TypedDict("GetWellKnownForgedeckEmbedJsonResponseSurfacesPortalEmbedStorageItem", {
    "name": str,
    "type": Literal["cookie", "localStorage"],
    "category": str,
    "lifetime": str,
    "purpose": "GetWellKnownForgedeckEmbedJsonResponseSurfacesPortalEmbedStorageItemPurpose",
    "legacy": NotRequired[bool],
})

GetWellKnownForgedeckEmbedJsonResponseSurfacesPortalEmbed = TypedDict("GetWellKnownForgedeckEmbedJsonResponseSurfacesPortalEmbed", {
    "script": str,
    "csp": Dict[str, List[str]],
    "consentCategory": str,
    "storage": List["GetWellKnownForgedeckEmbedJsonResponseSurfacesPortalEmbedStorageItem"],
})

GetWellKnownForgedeckEmbedJsonResponseSurfaces = TypedDict("GetWellKnownForgedeckEmbedJsonResponseSurfaces", {
    "tracking-snippet": "GetWellKnownForgedeckEmbedJsonResponseSurfacesTrackingSnippet",
    "portal-embed": "GetWellKnownForgedeckEmbedJsonResponseSurfacesPortalEmbed",
})

GetWellKnownForgedeckEmbedJsonResponseChangesItem = TypedDict("GetWellKnownForgedeckEmbedJsonResponseChangesItem", {
    "effective": str,
    "surface": str,
    "add": NotRequired[List[str]],
    "remove": NotRequired[List[str]],
    "note": str,
})

GetWellKnownForgedeckEmbedJsonResponse = TypedDict("GetWellKnownForgedeckEmbedJsonResponse", {
    "schema": str,
    "product": Literal["referalli"],
    "updated": str,
    "openapi": str,
    "llms": str,
    "status": str,
    "docs": str,
    "checkers": "GetWellKnownForgedeckEmbedJsonResponseCheckers",
    "org": NotRequired[str],
    "surfaces": "GetWellKnownForgedeckEmbedJsonResponseSurfaces",
    "changes": List["GetWellKnownForgedeckEmbedJsonResponseChangesItem"],
})

PostAgentsRegisterResponse = TypedDict("PostAgentsRegisterResponse", {
    "agentId": str,
    "wallet": str,
    "instantPayout": bool,
})

PostTOrgTokenAgentAttributeResponse = TypedDict("PostTOrgTokenAgentAttributeResponse", {
    "attributed": bool,
    "referralId": str,
    "agentWallet": str,
})

PostTOrgTokenAgentNegotiateResponse = TypedDict("PostTOrgTokenAgentNegotiateResponse", {
    "decision": Literal["accept", "counter", "reject"],
    "rateBps": NotRequired[int],
    "counterBps": NotRequired[Optional[int]],
    "partnerId": NotRequired[str],
    "reason": str,
})

PostTOrgTokenConsentResponse = TypedDict("PostTOrgTokenConsentResponse", {
    "ok": bool,
    "customerRef": str,
    "granted": bool,
})

GetVersionsResponseVersionsItem = TypedDict("GetVersionsResponseVersionsItem", {
    "version": str,
    "released": str,
    "changes": List[str],
})

GetVersionsResponse = TypedDict("GetVersionsResponse", {
    "latest": str,
    "versions": List["GetVersionsResponseVersionsItem"],
    "deprecationPolicy": str,
})

GetAuthProvidersResponseDetailsItem = TypedDict("GetAuthProvidersResponseDetailsItem", {
    "id": Literal["instance", "atlasid"],
    "name": str,
    "atlas": bool,
})

GetAuthProvidersResponse = TypedDict("GetAuthProvidersResponse", {
    "providers": List[Literal["instance", "atlasid"]],
    "details": List["GetAuthProvidersResponseDetailsItem"],
})

PostAuthBackchannelLogoutResponse = TypedDict("PostAuthBackchannelLogoutResponse", {
    "ok": bool,
})

PostAuthLogoutResponse = TypedDict("PostAuthLogoutResponse", {
    "ok": bool,
    "logoutUrl": Optional[str],
})

PostOrgsResponse = TypedDict("PostOrgsResponse", {
    "orgId": str,
})

GetMeResponseUserOption1 = TypedDict("GetMeResponseUserOption1", {
    "id": str,
    "email": str,
    "name": Optional[str],
    "emailVerified": bool,
})

GetMeResponseMembershipsItem = TypedDict("GetMeResponseMembershipsItem", {
    "orgId": str,
    "role": str,
    "roiDigest": NotRequired[bool],
})

# Set when called with an API key (user is then null).
GetMeResponseApiKey = TypedDict("GetMeResponseApiKey", {
    "id": str,
    "name": str,
    "prefix": str,
    "scopes": List[str],
    "apiVersion": Optional[str],
    "livemode": bool,
    "publishable": bool,
    "owner": Optional[str],
    "expiresAt": Optional[str],
})

GetMeResponseOrg = TypedDict("GetMeResponseOrg", {
    "id": str,
    "name": str,
})

GetMeResponse = TypedDict("GetMeResponse", {
    "user": Optional["GetMeResponseUserOption1"],
    "memberships": List["GetMeResponseMembershipsItem"],
    "apiKey": NotRequired["GetMeResponseApiKey"],
    "org": NotRequired["GetMeResponseOrg"],
})

GetPortalAuthCurrentResponse = TypedDict("GetPortalAuthCurrentResponse", {
    "adapter": Literal["referalli", "oidc", "custom"],
    "name": Optional[str],
    "startUrl": Optional[str],
})

GetOrgPortalAuthResponseAdaptersItem = TypedDict("GetOrgPortalAuthResponseAdaptersItem", {
    "id": Literal["referalli", "oidc", "custom"],
    "label": str,
    "status": Literal["ga", "beta"],
    "docsUrl": str,
})

GetOrgPortalAuthResponse = TypedDict("GetOrgPortalAuthResponse", {
    "adapter": Literal["referalli", "oidc", "custom"],
    "config": Dict[str, Any],
    "adapters": List["GetOrgPortalAuthResponseAdaptersItem"],
    "jwtAudience": str,
    "jwtSignInUrl": str,
    "redirectUri": str,
    "hasSecret": bool,
    "status": str,
    "lastOkAt": Optional[str],
    "lastError": Optional[str],
})

PutOrgPortalAuthResponseAdaptersItem = TypedDict("PutOrgPortalAuthResponseAdaptersItem", {
    "id": Literal["referalli", "oidc", "custom"],
    "label": str,
    "status": Literal["ga", "beta"],
    "docsUrl": str,
})

PutOrgPortalAuthResponse = TypedDict("PutOrgPortalAuthResponse", {
    "adapter": Literal["referalli", "oidc", "custom"],
    "config": Dict[str, Any],
    "adapters": List["PutOrgPortalAuthResponseAdaptersItem"],
    "jwtAudience": str,
    "jwtSignInUrl": str,
    "redirectUri": str,
})

PostOrgPortalAuthTestResponse = TypedDict("PostOrgPortalAuthTestResponse", {
    "ok": bool,
    "detail": str,
    "fix": NotRequired[str],
})

GetHostsCurrentResponseValueOption1Branding = TypedDict("GetHostsCurrentResponseValueOption1Branding", {
    "logoUrl": str,
    "theme": Dict[str, str],
})

GetHostsCurrentResponseValueOption1ProgramsItem = TypedDict("GetHostsCurrentResponseValueOption1ProgramsItem", {
    "handle": str,
    "name": str,
})

GetHostsCurrentResponseValueOption1ConsentTagsItem = TypedDict("GetHostsCurrentResponseValueOption1ConsentTagsItem", {
    "tag": Literal["script"],
    "attrs": Dict[str, Union[str, bool]],
    "inline": NotRequired[str],
})

GetHostsCurrentResponseValueOption1ConsentSettingsLinkOption1 = TypedDict("GetHostsCurrentResponseValueOption1ConsentSettingsLinkOption1", {
    "call": NotRequired[str],
    "attrs": NotRequired[Dict[str, str]],
})

GetHostsCurrentResponseValueOption1ConsentBuiltin = TypedDict("GetHostsCurrentResponseValueOption1ConsentBuiltin", {
    "policyUrl": str,
    "text": NotRequired[Dict[str, str]],
})

GetHostsCurrentResponseValueOption1Consent = TypedDict("GetHostsCurrentResponseValueOption1Consent", {
    "mode": Literal["cookiemunch", "cmp", "builtin", "none"],
    "provider": str,
    "tags": List["GetHostsCurrentResponseValueOption1ConsentTagsItem"],
    "settingsLink": Optional["GetHostsCurrentResponseValueOption1ConsentSettingsLinkOption1"],
    "builtin": NotRequired["GetHostsCurrentResponseValueOption1ConsentBuiltin"],
})

GetHostsCurrentResponseValueOption1ChatOption1TagsItem = TypedDict("GetHostsCurrentResponseValueOption1ChatOption1TagsItem", {
    "tag": Literal["script"],
    "attrs": Dict[str, Union[str, bool]],
    "inline": NotRequired[str],
})

GetHostsCurrentResponseValueOption1ChatOption1 = TypedDict("GetHostsCurrentResponseValueOption1ChatOption1", {
    "provider": str,
    "tags": List["GetHostsCurrentResponseValueOption1ChatOption1TagsItem"],
})

GetHostsCurrentResponseValueOption1 = TypedDict("GetHostsCurrentResponseValueOption1", {
    "kind": Literal["portal"],
    "orgId": str,
    "orgName": str,
    "branding": "GetHostsCurrentResponseValueOption1Branding",
    "programs": List["GetHostsCurrentResponseValueOption1ProgramsItem"],
    "consent": "GetHostsCurrentResponseValueOption1Consent",
    "chat": Optional["GetHostsCurrentResponseValueOption1ChatOption1"],
    "csp": str,
})

GetHostsCurrentResponseValueOption2 = TypedDict("GetHostsCurrentResponseValueOption2", {
    "kind": Literal["link"],
    "csp": str,
})

GetHostsCurrentResponseValueOption3 = TypedDict("GetHostsCurrentResponseValueOption3", {
    "kind": Literal["app"],
})

GetHostsCurrentResponse: TypeAlias = "Union[GetHostsCurrentResponseValueOption1, GetHostsCurrentResponseValueOption2, GetHostsCurrentResponseValueOption3]"

GetChatlyIdentityResponseIdentityOption1 = TypedDict("GetChatlyIdentityResponseIdentityOption1", {
    "externalId": str,
    "email": str,
    "name": NotRequired[str],
    "userHash": str,
})

GetChatlyIdentityResponse = TypedDict("GetChatlyIdentityResponse", {
    "identity": Optional["GetChatlyIdentityResponseIdentityOption1"],
})

PostMobilePurchasesResponse = TypedDict("PostMobilePurchasesResponse", {
    "conversions": int,
    "linesCreated": int,
    "reversals": int,
})

PatchOrgResponse = TypedDict("PatchOrgResponse", {
    "id": str,
    "name": str,
    "plan": str,
    "settings": "GetOpenapiJsonResponse",
    "payout_kyc_required": bool,
})

GetOrgMembersResponse = TypedDict("GetOrgMembersResponse", {
    "object": Literal["list"],
    "data": List["Member"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

PostOrgMembersResponse = TypedDict("PostOrgMembersResponse", {
    "userId": str,
    "role": str,
})

PatchOrgMembersUserIdResponse = TypedDict("PatchOrgMembersUserIdResponse", {
    "userId": str,
    "role": str,
})

PutOrgPayoutScheduleResponse = TypedDict("PutOrgPayoutScheduleResponse", {
    "dayOfMonth": NotRequired[Optional[int]],
    "schedule": NotRequired[Optional["PayoutSchedule"]],
    "nextRunDate": NotRequired[Optional[str]],
})

GetOrgPayoutScheduleResponseProgramsItemOverrideOption1Option2 = TypedDict("GetOrgPayoutScheduleResponseProgramsItemOverrideOption1Option2", {
    "kind": Literal["off"],
})

GetOrgPayoutScheduleResponseProgramsItem = TypedDict("GetOrgPayoutScheduleResponseProgramsItem", {
    "programId": str,
    "name": str,
    "override": Optional[Union["PayoutSchedule", "GetOrgPayoutScheduleResponseProgramsItemOverrideOption1Option2"]],
    "nextRunDate": Optional[str],
})

GetOrgPayoutScheduleResponse = TypedDict("GetOrgPayoutScheduleResponse", {
    "schedule": Optional["PayoutSchedule"],
    "nextRunDate": Optional[str],
    "programs": List["GetOrgPayoutScheduleResponseProgramsItem"],
})

PutProgramsIdPayoutScheduleResponseScheduleOption1Option2 = TypedDict("PutProgramsIdPayoutScheduleResponseScheduleOption1Option2", {
    "kind": Literal["off"],
})

PutProgramsIdPayoutScheduleResponse = TypedDict("PutProgramsIdPayoutScheduleResponse", {
    "programId": str,
    "schedule": Optional[Union["PayoutSchedule", "PutProgramsIdPayoutScheduleResponseScheduleOption1Option2"]],
    "nextRunDate": Optional[str],
})

PutPartnersIdVatResponse = TypedDict("PutPartnersIdVatResponse", {
    "vatId": Optional[str],
    "vatCountry": Optional[str],
    "vatVerifiedAt": Optional[str],
    "selfBillingAcceptedAt": Optional[str],
    "selfBillingVersion": Optional[str],
})

GetPartnerOrgsOrgIdSelfBillingResponse = TypedDict("GetPartnerOrgsOrgIdSelfBillingResponse", {
    "vatId": Optional[str],
    "vatCountry": Optional[str],
    "vatVerifiedAt": Optional[str],
    "selfBillingAcceptedAt": Optional[str],
    "selfBillingVersion": Optional[str],
    "currentVersion": str,
})

PostPartnerOrgsOrgIdSelfBillingResponse = TypedDict("PostPartnerOrgsOrgIdSelfBillingResponse", {
    "vatId": Optional[str],
    "vatCountry": Optional[str],
    "vatVerifiedAt": Optional[str],
    "selfBillingAcceptedAt": Optional[str],
    "selfBillingVersion": Optional[str],
    "currentVersion": str,
})

PutOrgTaxFilingResponse = TypedDict("PutOrgTaxFilingResponse", {
    "provider": Literal["test", "tax1099"],
    "connected": bool,
})

GetTax1099FilingsResponseDataItemDocumentsItem = TypedDict("GetTax1099FilingsResponseDataItemDocumentsItem", {
    "id": str,
    "partnerId": str,
    "amountMinor": int,
    "status": str,
})

GetTax1099FilingsResponseDataItem = TypedDict("GetTax1099FilingsResponseDataItem", {
    "id": str,
    "taxYear": int,
    "kind": Literal["original", "correction"],
    "provider": str,
    "providerFilingId": Optional[str],
    "status": Literal["submitting", "submitted", "accepted", "rejected"],
    "recipientCount": int,
    "totalMinor": int,
    "error": Optional[str],
    "documents": List["GetTax1099FilingsResponseDataItemDocumentsItem"],
    "createdAt": str,
})

GetTax1099FilingsResponse = TypedDict("GetTax1099FilingsResponse", {
    "object": Literal["list"],
    "data": List["GetTax1099FilingsResponseDataItem"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

PostTax1099FilingsIdRefreshResponse = TypedDict("PostTax1099FilingsIdRefreshResponse", {
    "id": str,
    "status": Literal["submitting", "submitted", "accepted", "rejected"],
})

GetPartnerTaxDocumentsResponseDataItem = TypedDict("GetPartnerTaxDocumentsResponseDataItem", {
    "id": str,
    "partnerId": str,
    "taxYear": int,
    "form": str,
    "amountMinor": int,
    "status": Literal["pending", "filed", "accepted", "rejected", "delivered"],
    "correctionOf": Optional[str],
    "deliveredAt": Optional[str],
    "createdAt": str,
    "orgId": str,
    "orgName": str,
})

GetPartnerTaxDocumentsResponse = TypedDict("GetPartnerTaxDocumentsResponse", {
    "object": Literal["list"],
    "data": List["GetPartnerTaxDocumentsResponseDataItem"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

GetStatusResponseComponentsItem = TypedDict("GetStatusResponseComponentsItem", {
    "id": str,
    "state": Literal["operational", "degraded", "major_outage"],
    "detail": Dict[str, Any],
})

GetStatusResponse = TypedDict("GetStatusResponse", {
    "state": Literal["operational", "degraded", "major_outage"],
    "components": List["GetStatusResponseComponentsItem"],
    "openIncidents": List["Incident"],
    "checkedAt": str,
})

GetStatusIncidentsResponse = TypedDict("GetStatusIncidentsResponse", {
    "object": Literal["list"],
    "data": List["Incident"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

GetOrgReferralParamsResponse = TypedDict("GetOrgReferralParamsResponse", {
    "builtIn": List[str],
    "params": List[str],
})

GetProgramsResponse = TypedDict("GetProgramsResponse", {
    "object": Literal["list"],
    "data": List["Program"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

GetProgramsIdEnrollmentsResponseDataItem = TypedDict("GetProgramsIdEnrollmentsResponseDataItem", {
    "id": str,
    "partnerId": str,
    "partnerEmail": str,
    "partnerName": str,
    "status": str,
    "createdAt": str,
    "networkWarning": "NetworkWarning",
})

GetProgramsIdEnrollmentsResponse = TypedDict("GetProgramsIdEnrollmentsResponse", {
    "object": Literal["list"],
    "data": List["GetProgramsIdEnrollmentsResponseDataItem"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

PostProgramsIdEnrollmentsEnrollmentIdApproveResponse = TypedDict("PostProgramsIdEnrollmentsEnrollmentIdApproveResponse", {
    "id": str,
    "status": Literal["approved"],
})

PostProgramsIdEnrollmentsEnrollmentIdRejectResponse = TypedDict("PostProgramsIdEnrollmentsEnrollmentIdRejectResponse", {
    "id": str,
    "status": Literal["rejected"],
})

GetPartnersResponse = TypedDict("GetPartnersResponse", {
    "object": Literal["list"],
    "data": List["Partner"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

GetPartnersIdResponse: TypeAlias = "Any"

GetPartnersIdEnrollmentsResponseDataItem = TypedDict("GetPartnersIdEnrollmentsResponseDataItem", {
    "id": str,
    "programId": str,
    "programName": str,
    "status": str,
    "groupId": Optional[str],
    "createdAt": str,
})

GetPartnersIdEnrollmentsResponse = TypedDict("GetPartnersIdEnrollmentsResponse", {
    "object": Literal["list"],
    "data": List["GetPartnersIdEnrollmentsResponseDataItem"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

GetProgramsIdGraphResponse: TypeAlias = "Any"

# mode "both": the live and test twins.
PostApiKeysResponseValueOption2 = TypedDict("PostApiKeysResponseValueOption2", {
    "pairId": str,
    "live": "IssuedApiKey",
    "test": "IssuedApiKey",
})

PostApiKeysResponse: TypeAlias = "Union[IssuedApiKey, PostApiKeysResponseValueOption2]"

GetApiKeysResponse = TypedDict("GetApiKeysResponse", {
    "object": Literal["list"],
    "data": List["ApiKey"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

PatchApiKeysIdResponse = TypedDict("PatchApiKeysIdResponse", {
    "id": str,
    "apiVersion": str,
    "owner": Optional[str],
    "expiresAt": Optional[str],
})

DeleteApiKeysIdResponse = TypedDict("DeleteApiKeysIdResponse", {
    "ok": bool,
    "revoked": List[str],
})

GetAuditLogsResponse = TypedDict("GetAuditLogsResponse", {
    "object": Literal["list"],
    "data": List["AuditLogEntry"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

GetTestClockResponse = TypedDict("GetTestClockResponse", {
    "now": str,
    "offsetSeconds": int,
})

PostTestClockAdvanceResponse = TypedDict("PostTestClockAdvanceResponse", {
    "now": str,
    "offsetSeconds": int,
    "approved": int,
    "payoutRuns": int,
})

GetTestEmailsResponseDataItem = TypedDict("GetTestEmailsResponseDataItem", {
    "id": str,
    "event": str,
    "to": str,
    "subject": str,
    "text": str,
    "html": str,
    "createdAt": str,
})

GetTestEmailsResponse = TypedDict("GetTestEmailsResponse", {
    "object": Literal["list"],
    "data": List["GetTestEmailsResponseDataItem"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

PostCliDeviceCodesResponse = TypedDict("PostCliDeviceCodesResponse", {
    "deviceCode": str,
    "userCode": str,
    "verificationUri": str,
    "verificationUriComplete": str,
    "expiresIn": int,
    "interval": int,
})

PostCliDeviceCodesTokenResponse = TypedDict("PostCliDeviceCodesTokenResponse", {
    "status": Literal["pending", "approved", "denied", "expired", "consumed"],
    "key": NotRequired[str],
    "orgId": NotRequired[str],
    "orgName": NotRequired[str],
    "scopes": NotRequired[List[str]],
})

GetCliDeviceCodesUserCodeResponse = TypedDict("GetCliDeviceCodesUserCodeResponse", {
    "userCode": str,
    "clientName": Optional[str],
    "createdAt": str,
    "expiresAt": str,
})

PostCliDeviceCodesUserCodeApproveResponse = TypedDict("PostCliDeviceCodesUserCodeApproveResponse", {
    "ok": bool,
    "keyId": str,
    "scopes": List[str],
})

PostCliListenersResponse = TypedDict("PostCliListenersResponse", {
    "id": str,
    "secret": str,
    "topics": List[str],
    "idleTimeoutSec": int,
})

GetCliListenersIdEventsResponseEventsItem = TypedDict("GetCliListenersIdEventsResponseEventsItem", {
    "id": str,
    "eventId": str,
    "topic": str,
    "body": str,
    "headers": Dict[str, str],
})

GetCliListenersIdEventsResponse = TypedDict("GetCliListenersIdEventsResponse", {
    "events": List["GetCliListenersIdEventsResponseEventsItem"],
})

PostCliTriggerResponseDeliveredTo = TypedDict("PostCliTriggerResponseDeliveredTo", {
    "listeners": int,
    "endpoints": int,
})

PostCliTriggerResponse = TypedDict("PostCliTriggerResponse", {
    "eventId": str,
    "topic": str,
    "payload": "GetOpenapiJsonResponse",
    "deliveredTo": "PostCliTriggerResponseDeliveredTo",
})

GetCliTopicsResponse = TypedDict("GetCliTopicsResponse", {
    "topics": List[str],
})

GetCliLogsResponseEntriesItem = TypedDict("GetCliLogsResponseEntriesItem", {
    "seq": int,
    "requestId": str,
    "method": str,
    "path": str,
    "status": int,
    "latencyMs": int,
    "actorType": str,
    "actorId": Optional[str],
    "ts": str,
})

GetCliLogsResponse = TypedDict("GetCliLogsResponse", {
    "entries": List["GetCliLogsResponseEntriesItem"],
    "cursor": int,
})

GetLinksResponse = TypedDict("GetLinksResponse", {
    "object": Literal["list"],
    "data": List["Link"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

PostCouponsResponse = TypedDict("PostCouponsResponse", {
    "id": str,
    "code": str,
})

GetCouponsResponse = TypedDict("GetCouponsResponse", {
    "object": Literal["list"],
    "data": List["Coupon"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

PostWidgetTokensResponse = TypedDict("PostWidgetTokensResponse", {
    "token": str,
    "partnerId": str,
    "expiresAt": str,
})

GetReferralsResponse = TypedDict("GetReferralsResponse", {
    "object": Literal["list"],
    "data": List["Referral"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

GetReferralsIdJourneyResponseTouchCreditsItem = TypedDict("GetReferralsIdJourneyResponseTouchCreditsItem", {
    "partnerId": str,
    "weight": float,
    "clickId": Optional[str],
})

GetReferralsIdJourneyResponseTouchpointsItem = TypedDict("GetReferralsIdJourneyResponseTouchpointsItem", {
    "clickId": str,
    "ts": str,
    "url": Optional[str],
    "linkId": Optional[str],
    "fraudScore": int,
    "eligible": bool,
    "weight": float,
    "winner": bool,
})

GetReferralsIdJourneyResponse = TypedDict("GetReferralsIdJourneyResponse", {
    "id": str,
    "programId": str,
    "partnerId": str,
    "customerRef": str,
    "source": str,
    "matchedVia": str,
    "confidence": float,
    "clickId": Optional[str],
    "linkId": Optional[str],
    "status": Literal["active", "pending_review", "paused", "void"],
    "ts": str,
    "windowExpiresAt": str,
    "touchCredits": List["GetReferralsIdJourneyResponseTouchCreditsItem"],
    "reasoning": "AttributionReasoning",
    "touchpoints": List["GetReferralsIdJourneyResponseTouchpointsItem"],
})

PostAttributionReplayResponse = TypedDict("PostAttributionReplayResponse", {
    "recomputed": int,
    "changed": int,
})

PostTrackEventsResponse = TypedDict("PostTrackEventsResponse", {
    "clickId": NotRequired[str],
    "eventId": NotRequired[str],
    "event": NotRequired[str],
    "recorded": NotRequired[bool],
    "referralId": NotRequired[Optional[str]],
    "duplicate": NotRequired[bool],
    "commissionId": NotRequired[Optional[str]],
    "amountMinor": NotRequired[int],
    "currency": NotRequired[Optional[str]],
})

PostCommissionRulesResponse = TypedDict("PostCommissionRulesResponse", {
    "id": str,
    "programId": str,
    "version": int,
    "config": "GetOpenapiJsonResponse",
})

GetCommissionRulesResponse = TypedDict("GetCommissionRulesResponse", {
    "object": Literal["list"],
    "data": List["CommissionRule"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

GetCommissionsResponse = TypedDict("GetCommissionsResponse", {
    "object": Literal["list"],
    "data": List["CommissionEvent"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

GetPartnersIdBalancesResponse = TypedDict("GetPartnersIdBalancesResponse", {
    "object": Literal["list"],
    "data": List["Balance"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

PostCommissionsApproveDueResponse = TypedDict("PostCommissionsApproveDueResponse", {
    "approved": int,
})

PostCommissionsIdAdjustResponse = TypedDict("PostCommissionsIdAdjustResponse", {
    "id": str,
})

PutBillingConnectionsIdSecretResponse = TypedDict("PutBillingConnectionsIdSecretResponse", {
    "id": str,
    "provider": str,
    "ok": bool,
})

PutBillingConnectionsIdCredentialsResponse = TypedDict("PutBillingConnectionsIdCredentialsResponse", {
    "id": str,
    "provider": str,
    "ok": bool,
})

GetBillingConnectionsResponse = TypedDict("GetBillingConnectionsResponse", {
    "object": Literal["list"],
    "data": List["BillingConnection"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

PutBillingConnectionsIdValueMappingResponse = TypedDict("PutBillingConnectionsIdValueMappingResponse", {
    "id": str,
    "valueMapping": "ValueMapping",
})

PostBillingConnectionsIdRotateSecretResponse = TypedDict("PostBillingConnectionsIdRotateSecretResponse", {
    "id": str,
    "provider": str,
    "webhookSecret": str,
    "previousSecretExpiresAt": str,
})

GetBillingEventsResponse = TypedDict("GetBillingEventsResponse", {
    "object": Literal["list"],
    "data": List["BillingEvent"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

PostBillingInternalCustomersResponse = TypedDict("PostBillingInternalCustomersResponse", {
    "customerRef": str,
    "note": str,
})

PutPartnersIdPayoutProfileResponse = TypedDict("PutPartnersIdPayoutProfileResponse", {
    "id": str,
})

PatchPartnersIdPayoutProfileResponse = TypedDict("PatchPartnersIdPayoutProfileResponse", {
    "partnerId": str,
    "method": str,
    "payoutCurrency": str,
    "minThresholdMinor": int,
})

PostPayoutRunsIdExecuteResponse = TypedDict("PostPayoutRunsIdExecuteResponse", {
    "sent": int,
    "submitted": int,
    "failed": int,
})

PostPayoutRunsIdCancelResponse = TypedDict("PostPayoutRunsIdCancelResponse", {
    "cancelled": int,
})

GetPayoutRunsResponse = TypedDict("GetPayoutRunsResponse", {
    "object": Literal["list"],
    "data": List["PayoutRun"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

GetPayoutsResponse = TypedDict("GetPayoutsResponse", {
    "object": Literal["list"],
    "data": List["Payout"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

GetTax1099ResponseDataItem = TypedDict("GetTax1099ResponseDataItem", {
    "partnerId": str,
    "taxFormType": str,
    "totalPaidUsdMinor": int,
    "requiresForm": bool,
    "fxMissingCurrencies": List[str],
})

GetTax1099Response = TypedDict("GetTax1099Response", {
    "object": Literal["list"],
    "data": List["GetTax1099ResponseDataItem"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

GetFxRatesResponse = TypedDict("GetFxRatesResponse", {
    "object": Literal["list"],
    "data": List["FxRate"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

GetOrgFxFeedResponse = TypedDict("GetOrgFxFeedResponse", {
    "enabled": bool,
    "source": Literal["ecb"],
    "lastRateDate": Optional[str],
})

PutOrgFxFeedResponse = TypedDict("PutOrgFxFeedResponse", {
    "enabled": bool,
    "source": Literal["ecb"],
    "synced": int,
})

PostFxRatesSyncResponse = TypedDict("PostFxRatesSyncResponse", {
    "orgId": str,
    "date": Optional[str],
    "inserted": int,
})

PostFxRatesClearOverrideResponse = TypedDict("PostFxRatesClearOverrideResponse", {
    "base": str,
    "quote": str,
    "cleared": int,
})

GetPayoutConnectionsResponseDataItem = TypedDict("GetPayoutConnectionsResponseDataItem", {
    "provider": str,
    "env": str,
    "status": str,
    "connectedAt": str,
})

GetPayoutConnectionsResponse = TypedDict("GetPayoutConnectionsResponse", {
    "object": Literal["list"],
    "data": List["GetPayoutConnectionsResponseDataItem"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

PutPayoutConnectionsProviderResponse = TypedDict("PutPayoutConnectionsProviderResponse", {
    "provider": str,
    "env": str,
    "status": Literal["active"],
})

DeletePayoutConnectionsProviderResponse = TypedDict("DeletePayoutConnectionsProviderResponse", {
    "provider": str,
    "removed": bool,
})

PostFraudInvalidTrafficScanResponsePartnersItem = TypedDict("PostFraudInvalidTrafficScanResponsePartnersItem", {
    "partnerId": str,
    "clicks": int,
    "probability": float,
    "label": Literal["clean", "suspicious", "invalid"],
    "contributions": Dict[str, float],
})

PostFraudInvalidTrafficScanResponse = TypedDict("PostFraudInvalidTrafficScanResponse", {
    "window": str,
    "partners": List["PostFraudInvalidTrafficScanResponsePartnersItem"],
    "flagged": int,
})

GetFraudCasesResponse = TypedDict("GetFraudCasesResponse", {
    "object": Literal["list"],
    "data": List["FraudCase"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

GetPartnersIdQualityResponseLiveMetrics = TypedDict("GetPartnersIdQualityResponseLiveMetrics", {
    "customers": float,
    "repeatPayerRate": float,
    "refundRate": float,
    "disputeRate": float,
    "trialToPaidRate": float,
    "identityRiskRate": NotRequired[float],
    "valuePatternPenalty": NotRequired[float],
})

GetPartnersIdQualityResponseLive = TypedDict("GetPartnersIdQualityResponseLive", {
    "score": float,
    "metrics": "GetPartnersIdQualityResponseLiveMetrics",
})

GetPartnersIdQualityResponseLastSnapshotOption1 = TypedDict("GetPartnersIdQualityResponseLastSnapshotOption1", {
    "score": float,
    "metrics": "GetOpenapiJsonResponse",
    "computedAt": str,
})

GetPartnersIdQualityResponse = TypedDict("GetPartnersIdQualityResponse", {
    "partnerId": str,
    "live": "GetPartnersIdQualityResponseLive",
    "lastSnapshot": Optional["GetPartnersIdQualityResponseLastSnapshotOption1"],
})

PostQualityRecomputeResponse = TypedDict("PostQualityRecomputeResponse", {
    "partners": int,
    "casesOpened": int,
    "suspended": int,
})

PostFraudDetectRingsResponse = TypedDict("PostFraudDetectRingsResponse", {
    "ringsFound": int,
})

GetReportsFilteredClicksResponseDataItem = TypedDict("GetReportsFilteredClicksResponseDataItem", {
    "day": str,
    "filtered": int,
    "total": int,
    "avgScore": float,
})

GetReportsFilteredClicksResponse = TypedDict("GetReportsFilteredClicksResponse", {
    "object": Literal["list"],
    "data": List["GetReportsFilteredClicksResponseDataItem"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

GetAnalyticsOverviewResponseFunnel = TypedDict("GetAnalyticsOverviewResponseFunnel", {
    "clickToSignup": float,
    "signupToPaid": float,
})

GetAnalyticsOverviewResponse = TypedDict("GetAnalyticsOverviewResponse", {
    "clicks": int,
    "filteredClicks": int,
    "visitors": int,
    "signups": int,
    "payments": int,
    "revenueMinor": int,
    "commissionEarnedMinor": int,
    "commissionReversedMinor": int,
    "activePartners": int,
    "funnel": "GetAnalyticsOverviewResponseFunnel",
})

GetAnalyticsTimeseriesResponseDataItem = TypedDict("GetAnalyticsTimeseriesResponseDataItem", {
    "day": str,
    "value": float,
})

GetAnalyticsTimeseriesResponse = TypedDict("GetAnalyticsTimeseriesResponse", {
    "object": Literal["list"],
    "data": List["GetAnalyticsTimeseriesResponseDataItem"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

GetAnalyticsCohortLtvResponseDataItem = TypedDict("GetAnalyticsCohortLtvResponseDataItem", {
    "cohort": str,
    "customers": int,
    "revenueMinor": int,
    "ltvMinor": int,
})

GetAnalyticsCohortLtvResponse = TypedDict("GetAnalyticsCohortLtvResponse", {
    "object": Literal["list"],
    "data": List["GetAnalyticsCohortLtvResponseDataItem"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

GetAnalyticsByGeoResponseDataItem = TypedDict("GetAnalyticsByGeoResponseDataItem", {
    "geo": str,
    "referrals": int,
    "revenueMinor": int,
})

GetAnalyticsByGeoResponse = TypedDict("GetAnalyticsByGeoResponse", {
    "object": Literal["list"],
    "data": List["GetAnalyticsByGeoResponseDataItem"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

GetAnalyticsByChannelResponseDataItem = TypedDict("GetAnalyticsByChannelResponseDataItem", {
    "channel": str,
    "referrals": int,
    "revenueMinor": int,
})

GetAnalyticsByChannelResponse = TypedDict("GetAnalyticsByChannelResponse", {
    "object": Literal["list"],
    "data": List["GetAnalyticsByChannelResponseDataItem"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

GetAnalyticsCouponPerformanceResponseDataItem = TypedDict("GetAnalyticsCouponPerformanceResponseDataItem", {
    "code": str,
    "partnerId": str,
    "referrals": int,
    "revenueMinor": int,
})

GetAnalyticsCouponPerformanceResponse = TypedDict("GetAnalyticsCouponPerformanceResponse", {
    "object": Literal["list"],
    "data": List["GetAnalyticsCouponPerformanceResponseDataItem"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

GetReportsPartnerPerformanceResponseValueItem = TypedDict("GetReportsPartnerPerformanceResponseValueItem", {
    "partnerId": str,
    "displayName": str,
    "email": str,
    "status": str,
    "clicks": int,
    "referrals": int,
    "payments": int,
    "revenueMinor": int,
    "earnedMinor": int,
    "reversedMinor": int,
})

GetReportsPartnerPerformanceResponse: TypeAlias = "List[GetReportsPartnerPerformanceResponseValueItem]"

GetProfitabilitySettingsResponse = TypedDict("GetProfitabilitySettingsResponse", {
    "reportingCurrency": str,
    "defaultMarginBps": Optional[int],
    "creditCostModel": Literal["face", "margin", "fixed_ratio"],
    "creditCostRatioBps": NotRequired[int],
    "inference": Literal["fifo_next_payments", "report_only", "on_grant"],
    "creditDraw": Literal["grants_first", "pro_rata"],
    "windowDays": int,
    "churnWindowDays": int,
    "countReferrerSpend": bool,
    "costToServeMinorPerMonth": NotRequired[int],
    "taxFeesReduceProfit": bool,
    "valuePatternWeight": float,
    "targetRoiBps": NotRequired[Optional[int]],
})

GetProfitabilityProductsResponse = TypedDict("GetProfitabilityProductsResponse", {
    "data": List["GetProfitabilityProductsProductRefResponse"],
})

GetProfitabilityProductsProductRefResponse = TypedDict("GetProfitabilityProductsProductRefResponse", {
    "productRef": str,
    "marginBps": Optional[int],
    "unitCostMinor": Optional[int],
    "currency": str,
    "updatedAt": str,
})

PostProfitabilityRebuildResponse = TypedDict("PostProfitabilityRebuildResponse", {
    "jobId": str,
})

GetProfitabilityRebuildJobIdResponse = TypedDict("GetProfitabilityRebuildJobIdResponse", {
    "status": Literal["queued", "running", "done", "failed"],
    "processed": int,
    "total": int,
    "error": NotRequired[str],
})

GetRoiBreakdownResponseDataItemCoverage = TypedDict("GetRoiBreakdownResponseDataItemCoverage", {
    "creditAppliedReportedBps": Optional[int],
    "marginCoveredBps": Optional[int],
    "inferredShareBps": Optional[int],
})

# Partner and program rows: their referrals, both sides, commissions included.
GetRoiBreakdownResponseDataItemReferrals = TypedDict("GetRoiBreakdownResponseDataItemReferrals", {
    "count": int,
    "costMinor": int,
    "cashCommissionMinor": int,
    "netMinor": Optional[int],
    "roi": Optional[float],
})

GetRoiBreakdownResponseDataItem = TypedDict("GetRoiBreakdownResponseDataItem", {
    "currency": str,
    "creditCostMinor": int,
    "cashAfterMinor": int,
    "profitAfterMinor": Optional[int],
    "netMinor": Optional[int],
    "roi": Optional[float],
    "paidBackShareBps": Optional[int],
    "medianPaybackDays": Optional[float],
    "grants": int,
    "profitSources": Dict[str, int],
    "coverage": "GetRoiBreakdownResponseDataItemCoverage",
    "outstandingCreditMinor": int,
    "outstandingCostIfUsedMinor": Optional[int],
    "key": str,
    "label": str,
    "referrals": NotRequired["GetRoiBreakdownResponseDataItemReferrals"],
})

GetRoiBreakdownResponse = TypedDict("GetRoiBreakdownResponse", {
    "object": Literal["list"],
    "data": List["GetRoiBreakdownResponseDataItem"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

GetRoiGrantsResponse = TypedDict("GetRoiGrantsResponse", {
    "object": Literal["list"],
    "data": List["RoiGrant"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

GetRoiPatternsResponsePatterns = TypedDict("GetRoiPatternsResponsePatterns", {
    "credit_only": List["RoiPatternEntry"],
    "churn_at_exhaustion": List["RoiPatternEntry"],
    "bonus_collector": List["RoiPatternEntry"],
    "negative_partner": List["RoiPatternEntry"],
})

GetRoiPatternsResponse = TypedDict("GetRoiPatternsResponse", {
    "patterns": "GetRoiPatternsResponsePatterns",
})

GetRoiPatternsPatternResponse = TypedDict("GetRoiPatternsPatternResponse", {
    "object": Literal["list"],
    "data": List["RoiPatternEntry"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

GetRoiDataQualityResponseGapsItemFix = TypedDict("GetRoiDataQualityResponseGapsItemFix", {
    "text": str,
    "href": str,
})

GetRoiDataQualityResponseGapsItem = TypedDict("GetRoiDataQualityResponseGapsItem", {
    "code": Literal["margin_missing", "credit_applied_unreported", "partners_unlinked", "fx_rate_missing"],
    "count": int,
    "fix": "GetRoiDataQualityResponseGapsItemFix",
})

GetRoiDataQualityResponse = TypedDict("GetRoiDataQualityResponse", {
    "paymentsTotal": int,
    "paymentsWithCreditInfo": int,
    "productsWithMargin": int,
    "productsSeen": int,
    "partnersLinked": int,
    "partnersTotal": int,
    "excludedForFx": int,
    "gaps": List["GetRoiDataQualityResponseGapsItem"],
})

PostValueEventsResponseResultsItem = TypedDict("PostValueEventsResponseResultsItem", {
    "index": int,
    "id": str,
    "created": bool,
    "superseded": List[str],
})

PostValueEventsResponseErrorsItem = TypedDict("PostValueEventsResponseErrorsItem", {
    "index": int,
    "message": str,
})

PostValueEventsResponse = TypedDict("PostValueEventsResponse", {
    "results": List["PostValueEventsResponseResultsItem"],
    "errors": List["PostValueEventsResponseErrorsItem"],
})

PostValueImportResponseValueOption1ErrorsItem = TypedDict("PostValueImportResponseValueOption1ErrorsItem", {
    "row": int,
    "error": str,
})

PostValueImportResponseValueOption1 = TypedDict("PostValueImportResponseValueOption1", {
    "rows": List[Dict[str, Any]],
    "errors": List["PostValueImportResponseValueOption1ErrorsItem"],
    "total": int,
})

PostValueImportResponseValueOption2ErrorsItem = TypedDict("PostValueImportResponseValueOption2ErrorsItem", {
    "row": int,
    "error": str,
})

PostValueImportResponseValueOption2 = TypedDict("PostValueImportResponseValueOption2", {
    "recorded": int,
    "duplicates": int,
    "errors": List["PostValueImportResponseValueOption2ErrorsItem"],
})

PostValueImportResponseValueOption3 = TypedDict("PostValueImportResponseValueOption3", {
    "jobId": str,
})

PostValueImportResponse: TypeAlias = "Union[PostValueImportResponseValueOption1, PostValueImportResponseValueOption2, PostValueImportResponseValueOption3]"

GetValueImportJobIdResponseErrorsItem = TypedDict("GetValueImportJobIdResponseErrorsItem", {
    "row": int,
    "error": str,
})

GetValueImportJobIdResponse = TypedDict("GetValueImportJobIdResponse", {
    "status": Literal["queued", "running", "done", "failed"],
    "processed": int,
    "total": int,
    "recorded": int,
    "duplicates": int,
    "errors": List["GetValueImportJobIdResponseErrorsItem"],
    "error": NotRequired[str],
})

GetPartnerKycStatusResponse = TypedDict("GetPartnerKycStatusResponse", {
    "kycStatus": str,
    "sanctionsStatus": str,
    "verifiedAt": Optional[str],
})

PostPartnerKycSubmitResponse = TypedDict("PostPartnerKycSubmitResponse", {
    "kycStatus": Literal["verified", "pending", "rejected"],
    "sanctionsStatus": Literal["clear", "flagged"],
})

GetPartnerMeResponseAccount = TypedDict("GetPartnerMeResponseAccount", {
    "id": str,
    "email": str,
    "name": Optional[str],
})

GetPartnerMeResponseMembershipsItemProgramsItem = TypedDict("GetPartnerMeResponseMembershipsItemProgramsItem", {
    "programId": str,
    "name": str,
    "slug": str,
    "enrollmentId": str,
    "enrollmentStatus": str,
})

GetPartnerMeResponseMembershipsItem = TypedDict("GetPartnerMeResponseMembershipsItem", {
    "orgId": str,
    "orgName": str,
    "partnerId": str,
    "programs": List["GetPartnerMeResponseMembershipsItemProgramsItem"],
})

GetPartnerMeResponse = TypedDict("GetPartnerMeResponse", {
    "account": NotRequired["GetPartnerMeResponseAccount"],
    "memberships": List["GetPartnerMeResponseMembershipsItem"],
})

GetPartnerStatsResponseDataItem = TypedDict("GetPartnerStatsResponseDataItem", {
    "orgId": str,
    "partnerId": str,
    "clicks": int,
    "referrals": int,
    "payments": int,
    "balances": List["Balance"],
})

GetPartnerStatsResponse = TypedDict("GetPartnerStatsResponse", {
    "object": Literal["list"],
    "data": List["GetPartnerStatsResponseDataItem"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

GetPartnerLinksResponseDataItem = TypedDict("GetPartnerLinksResponseDataItem", {
    "id": str,
    "orgId": str,
    "programId": str,
    "code": str,
    "destinationUrl": str,
    "shortPath": str,
    "shortUrl": str,
    "directParam": str,
    "clicks": int,
})

GetPartnerLinksResponse = TypedDict("GetPartnerLinksResponse", {
    "object": Literal["list"],
    "data": List["GetPartnerLinksResponseDataItem"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

GetPartnerAssetsResponseDataItem = TypedDict("GetPartnerAssetsResponseDataItem", {
    "id": str,
    "orgId": str,
    "orgName": str,
    "programId": str,
    "programName": str,
    "kind": str,
    "title": str,
    "content": str,
    "dimensions": str,
    "createdAt": str,
})

GetPartnerAssetsResponse = TypedDict("GetPartnerAssetsResponse", {
    "object": Literal["list"],
    "data": List["GetPartnerAssetsResponseDataItem"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

GetPartnerDisputesResponseDataItem = TypedDict("GetPartnerDisputesResponseDataItem", {
    "id": str,
    "orgId": str,
    "orgName": str,
    "referralId": Optional[str],
    "kind": str,
    "status": str,
    "detail": str,
    "resolution": Optional[str],
    "createdAt": str,
    "resolvedAt": Optional[str],
})

GetPartnerDisputesResponse = TypedDict("GetPartnerDisputesResponse", {
    "object": Literal["list"],
    "data": List["GetPartnerDisputesResponseDataItem"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

GetPartnerReferralsResponseDataItem = TypedDict("GetPartnerReferralsResponseDataItem", {
    "id": str,
    "orgId": str,
    "programId": str,
    "customer": str,
    "status": str,
    "matchedVia": str,
    "ts": str,
})

GetPartnerReferralsResponse = TypedDict("GetPartnerReferralsResponse", {
    "object": Literal["list"],
    "data": List["GetPartnerReferralsResponseDataItem"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

GetPartnerReferralsIdTransparencyResponse = TypedDict("GetPartnerReferralsIdTransparencyResponse", {
    "referralId": str,
    "status": str,
    "matchedVia": str,
    "confidence": float,
    "model": Optional[str],
    "windowDays": Optional[int],
    "consideredTouchpoints": int,
    "yourCreditWeight": float,
    "notes": List[str],
    "noteCodes": List["ReasonNote"],
})

GetPartnerPayoutsResponseDataItem = TypedDict("GetPartnerPayoutsResponseDataItem", {
    "id": str,
    "orgId": str,
    "amountMinor": int,
    "currency": str,
    "status": str,
    "rail": str,
    "sentAt": Optional[str],
    "createdAt": str,
})

GetPartnerPayoutsResponse = TypedDict("GetPartnerPayoutsResponse", {
    "object": Literal["list"],
    "data": List["GetPartnerPayoutsResponseDataItem"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

PutPartnerOrgsOrgIdPayoutProfileResponse = TypedDict("PutPartnerOrgsOrgIdPayoutProfileResponse", {
    "id": str,
})

GetPartnerProgramsProgramIdLeaderboardResponseContestOption1 = TypedDict("GetPartnerProgramsProgramIdLeaderboardResponseContestOption1", {
    "startsAt": str,
    "endsAt": str,
    "prize": Optional[str],
})

GetPartnerProgramsProgramIdLeaderboardResponseRowsItem = TypedDict("GetPartnerProgramsProgramIdLeaderboardResponseRowsItem", {
    "rank": int,
    "name": str,
    "approvedMinor": int,
    "you": bool,
})

GetPartnerProgramsProgramIdLeaderboardResponse = TypedDict("GetPartnerProgramsProgramIdLeaderboardResponse", {
    "contest": Optional["GetPartnerProgramsProgramIdLeaderboardResponseContestOption1"],
    "rows": List["GetPartnerProgramsProgramIdLeaderboardResponseRowsItem"],
})

PostPartnerProgramsProgramIdApplyResponse = TypedDict("PostPartnerProgramsProgramIdApplyResponse", {
    "enrollmentId": str,
    "status": Literal["applied"],
})

PostWebhookEndpointsResponse = TypedDict("PostWebhookEndpointsResponse", {
    "id": str,
    "url": str,
    "topics": List[str],
    "programIds": Optional[List[str]],
    "legacySignature": bool,
    "alertContacts": List[str],
    "secret": str,
})

GetWebhookEndpointsResponse = TypedDict("GetWebhookEndpointsResponse", {
    "object": Literal["list"],
    "data": List["WebhookEndpoint"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

PatchWebhookEndpointsIdResponse: TypeAlias = "Any"

PostWebhookEndpointsIdRotateSecretResponse = TypedDict("PostWebhookEndpointsIdRotateSecretResponse", {
    "id": str,
    "secret": str,
    "previousSecretExpiresAt": str,
})

GetWebhookDeliveriesResponse = TypedDict("GetWebhookDeliveriesResponse", {
    "object": Literal["list"],
    "data": List["WebhookDelivery"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

GetWebhookEndpointsIdDeliveriesResponse = TypedDict("GetWebhookEndpointsIdDeliveriesResponse", {
    "object": Literal["list"],
    "data": List["WebhookDelivery"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

GetWebhookDeliveriesIdResponse: TypeAlias = "Any"

PostWebhookEndpointsIdReplayResponse = TypedDict("PostWebhookEndpointsIdReplayResponse", {
    "endpointId": str,
    "since": str,
    "replayed": int,
})

PostSandboxSimulateResponse = TypedDict("PostSandboxSimulateResponse", {
    "customerRef": str,
    "events": int,
    "conversions": int,
    "linesCreated": int,
    "reversals": int,
})

PostImportProviderResponse = TypedDict("PostImportProviderResponse", {
    "partnersCreated": int,
    "partnersSkipped": int,
    "linksCreated": int,
    "couponsCreated": int,
    "codesSkipped": List[str],
    "referralParams": List[str],
    "unpaidImportedMinor": int,
    "paidImportedMinor": int,
})

GetOpenapiJsonResponse: TypeAlias = "Dict[str, Any]"

GetBrandingResponseWarningsItem = TypedDict("GetBrandingResponseWarningsItem", {
    "code": Literal["low_contrast"],
    "foreground": str,
    "background": str,
    "ratio": float,
    "minimum": float,
    "message": str,
})

GetBrandingResponse = TypedDict("GetBrandingResponse", {
    "logoUrl": Optional[str],
    "theme": Optional["GetOpenapiJsonResponse"],
    "portalDomain": Optional[str],
    "portalDomainVerified": bool,
    "portalDomainStatus": Literal["none", "pending", "provisioning", "active"],
    "linkDomain": Optional[str],
    "linkDomainVerified": bool,
    "linkDomainStatus": Literal["none", "pending", "provisioning", "active"],
    "emailFrom": Optional[str],
    "warnings": List["GetBrandingResponseWarningsItem"],
})

PostBrandingLinkDomainResponse = TypedDict("PostBrandingLinkDomainResponse", {
    "domain": str,
    "cnameTarget": str,
    "txtRecord": str,
    "txtName": str,
    "verified": bool,
})

PostBrandingLinkDomainVerifyResponse = TypedDict("PostBrandingLinkDomainVerifyResponse", {
    "domain": str,
    "verified": bool,
    "status": Literal["provisioning", "active"],
    "message": NotRequired[str],
})

PostBrandingDomainResponse = TypedDict("PostBrandingDomainResponse", {
    "domain": str,
    "cnameTarget": str,
    "txtRecord": str,
    "txtName": str,
    "verified": bool,
    "instructions": str,
})

PutBrandingResponseWarningsItem = TypedDict("PutBrandingResponseWarningsItem", {
    "code": Literal["low_contrast"],
    "foreground": str,
    "background": str,
    "ratio": float,
    "minimum": float,
    "message": str,
})

PutBrandingResponse = TypedDict("PutBrandingResponse", {
    "ok": bool,
    "warnings": List["PutBrandingResponseWarningsItem"],
})

PostEmbedTokensResponse = TypedDict("PostEmbedTokensResponse", {
    "token": str,
    "expiresAt": str,
})

GetEmbedSummaryResponsePartner = TypedDict("GetEmbedSummaryResponsePartner", {
    "name": str,
    "email": str,
})

GetEmbedSummaryResponseBalancesItem = TypedDict("GetEmbedSummaryResponseBalancesItem", {
    "currency": str,
    "pending": int,
    "approved": int,
    "paid": int,
})

GetEmbedSummaryResponseLinksItem = TypedDict("GetEmbedSummaryResponseLinksItem", {
    "code": str,
    "destinationUrl": str,
})

GetEmbedSummaryResponse = TypedDict("GetEmbedSummaryResponse", {
    "partner": "GetEmbedSummaryResponsePartner",
    "clicks": int,
    "referrals": int,
    "balances": List["GetEmbedSummaryResponseBalancesItem"],
    "links": List["GetEmbedSummaryResponseLinksItem"],
})

PostDiscoverySearchResponse = TypedDict("PostDiscoverySearchResponse", {
    "found": int,
    "added": int,
})

PostDiscoveryCorpusResponse = TypedDict("PostDiscoveryCorpusResponse", {
    "received": int,
    "added": int,
})

GetProspectsResponseDataItem = TypedDict("GetProspectsResponseDataItem", {
    "id": str,
    "name": str,
    "url": str,
    "channel": str,
    "audienceSize": int,
    "evidence": Optional["GetOpenapiJsonResponse"],
    "fitScore": float,
    "contactEmail": Optional[str],
    "status": str,
})

GetProspectsResponse = TypedDict("GetProspectsResponse", {
    "object": Literal["list"],
    "data": List["GetProspectsResponseDataItem"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

PostOutreachDraftResponse = TypedDict("PostOutreachDraftResponse", {
    "messageIds": List[str],
})

GetOutreachResponseDataItem = TypedDict("GetOutreachResponseDataItem", {
    "id": str,
    "prospectId": str,
    "step": int,
    "subject": str,
    "status": str,
    "createdAt": str,
    "sentAt": Optional[str],
})

GetOutreachResponse = TypedDict("GetOutreachResponse", {
    "object": Literal["list"],
    "data": List["GetOutreachResponseDataItem"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

PostOutreachSendDueResponse = TypedDict("PostOutreachSendDueResponse", {
    "sent": int,
    "suppressed": int,
    "capped": bool,
    "failed": int,
})

PostUnsubscribeTokenResponse = TypedDict("PostUnsubscribeTokenResponse", {
    "ok": bool,
})

GetAssistantSuggestionsResponseDataItem = TypedDict("GetAssistantSuggestionsResponseDataItem", {
    "kind": str,
    "message": str,
    "suggestedAction": str,
    "data": Dict[str, Union[str, float]],
})

GetAssistantSuggestionsResponse = TypedDict("GetAssistantSuggestionsResponse", {
    "object": Literal["list"],
    "data": List["GetAssistantSuggestionsResponseDataItem"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

GetMarketplaceListingResponseDataItemStats = TypedDict("GetMarketplaceListingResponseDataItemStats", {
    "clicks": int,
    "referrals": int,
    "epcMinor": int,
    "conversionRate": float,
    "payoutReliability": Optional[float],
    "approvalLatencyHours": Optional[float],
})

GetMarketplaceListingResponseDataItem = TypedDict("GetMarketplaceListingResponseDataItem", {
    "programId": str,
    "visibility": str,
    "category": str,
    "headline": str,
    "stats": "GetMarketplaceListingResponseDataItemStats",
})

GetMarketplaceListingResponse = TypedDict("GetMarketplaceListingResponse", {
    "object": Literal["list"],
    "data": List["GetMarketplaceListingResponseDataItem"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

GetPartnerMarketplaceResponseDataItemStats = TypedDict("GetPartnerMarketplaceResponseDataItemStats", {
    "clicks": int,
    "referrals": int,
    "epcMinor": int,
    "conversionRate": float,
    "payoutReliability": Optional[float],
    "approvalLatencyHours": Optional[float],
})

GetPartnerMarketplaceResponseDataItem = TypedDict("GetPartnerMarketplaceResponseDataItem", {
    "programId": str,
    "programName": str,
    "merchant": str,
    "category": str,
    "headline": str,
    "sponsored": bool,
    "cookieWindowDays": int,
    "commissionSummary": Optional["GetOpenapiJsonResponse"],
    "stats": "GetPartnerMarketplaceResponseDataItemStats",
})

GetPartnerMarketplaceResponse = TypedDict("GetPartnerMarketplaceResponse", {
    "object": Literal["list"],
    "data": List["GetPartnerMarketplaceResponseDataItem"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

GetPartnerProfileVerifiedResponse = TypedDict("GetPartnerProfileVerifiedResponse", {
    "programs": int,
    "clicks": int,
    "referrals": int,
    "repeatPayerRate": Optional[float],
    "verified": bool,
})

PostPartnerDisputesResponse = TypedDict("PostPartnerDisputesResponse", {
    "id": str,
    "status": Literal["open"],
})

GetDisputesResponseDataItem = TypedDict("GetDisputesResponseDataItem", {
    "id": str,
    "partnerId": str,
    "partnerEmail": str,
    "referralId": Optional[str],
    "kind": str,
    "status": str,
    "detail": str,
    "resolution": Optional[str],
    "createdAt": str,
})

GetDisputesResponse = TypedDict("GetDisputesResponse", {
    "object": Literal["list"],
    "data": List["GetDisputesResponseDataItem"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

GetCreatorsResponse = TypedDict("GetCreatorsResponse", {
    "object": Literal["list"],
    "data": List["CreatorProfile"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

PostCreatorsAccountIdInviteResponse = TypedDict("PostCreatorsAccountIdInviteResponse", {
    "id": str,
    "program": str,
})

GetInvitationsResponseDataItem = TypedDict("GetInvitationsResponseDataItem", {
    "id": str,
    "creatorName": Optional[str],
    "accountId": str,
    "programId": str,
    "programName": str,
    "status": str,
    "message": str,
    "createdAt": str,
    "respondedAt": Optional[str],
})

GetInvitationsResponse = TypedDict("GetInvitationsResponse", {
    "object": Literal["list"],
    "data": List["GetInvitationsResponseDataItem"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

GetPartnerInvitationsResponseDataItem = TypedDict("GetPartnerInvitationsResponseDataItem", {
    "id": str,
    "merchant": str,
    "orgId": str,
    "programId": str,
    "programName": str,
    "status": str,
    "message": str,
    "createdAt": str,
})

GetPartnerInvitationsResponse = TypedDict("GetPartnerInvitationsResponse", {
    "object": Literal["list"],
    "data": List["GetPartnerInvitationsResponseDataItem"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

GetBillingPlanResponseUsage = TypedDict("GetBillingPlanResponseUsage", {
    "programs": int,
    "partners": int,
})

GetBillingPlanResponse = TypedDict("GetBillingPlanResponse", {
    "plan": str,
    "planStatus": str,
    "periodEnd": Optional[str],
    "limits": "GetOpenapiJsonResponse",
    "usage": "GetBillingPlanResponseUsage",
    "catalog": Dict[str, "GetOpenapiJsonResponse"],
    "subscribed": bool,
    "canActivate": bool,
})

PostBillingCheckoutResponse = TypedDict("PostBillingCheckoutResponse", {
    "url": NotRequired[str],
    "sessionId": NotRequired[str],
})

PostBillingPortalResponse = TypedDict("PostBillingPortalResponse", {
    "url": str,
})

PostBillingActivateResponse = TypedDict("PostBillingActivateResponse", {
    "plan": str,
    "planStatus": str,
})

GetProgramsIdRefereeRewardResponse = TypedDict("GetProgramsIdRefereeRewardResponse", {
    "refereeReward": Optional["GetOpenapiJsonResponse"],
})

PutProgramsIdRefereeRewardResponse = TypedDict("PutProgramsIdRefereeRewardResponse", {
    "ok": bool,
    "refereeReward": Optional["GetOpenapiJsonResponse"],
})

GetRewardsResponseDataItem = TypedDict("GetRewardsResponseDataItem", {
    "id": str,
    "programId": str,
    "referralId": str,
    "customerRef": str,
    "kind": str,
    "amountMinor": int,
    "currency": str,
    "code": Optional[str],
    "status": Literal["issued", "redeemed", "void"],
    "createdAt": str,
    "redeemedAt": Optional[str],
})

GetRewardsResponse = TypedDict("GetRewardsResponse", {
    "object": Literal["list"],
    "data": List["GetRewardsResponseDataItem"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

GetRewardsLookupCodeResponse = TypedDict("GetRewardsLookupCodeResponse", {
    "valid": bool,
    "rewardId": NotRequired[str],
    "kind": NotRequired[str],
    "amountMinor": NotRequired[int],
    "currency": NotRequired[str],
    "status": NotRequired[str],
})

PostRewardsRedeemByCodeResponse = TypedDict("PostRewardsRedeemByCodeResponse", {
    "ok": bool,
    "rewardId": str,
    "grantId": str,
    "status": Literal["issued", "redeemed"],
    "currency": str,
    "requestedMinor": int,
    "redeemedMinor": int,
    "remainingMinor": int,
    "capped": bool,
})

PostRewardsResponse = TypedDict("PostRewardsResponse", {
    "id": str,
    "partnerId": str,
    "programId": str,
    "ruleKey": Optional[str],
    "reason": str,
    "amountMinor": int,
    "currency": str,
    "commissionId": Optional[str],
    "idempotencyKey": str,
    "createdAt": str,
    "replayed": bool,
})

GetRewardsGrantedResponseValueItem = TypedDict("GetRewardsGrantedResponseValueItem", {
    "id": str,
    "partnerId": str,
    "programId": str,
    "ruleKey": Optional[str],
    "reason": str,
    "amountMinor": int,
    "currency": str,
    "commissionId": Optional[str],
    "idempotencyKey": str,
    "createdAt": str,
})

GetRewardsGrantedResponse: TypeAlias = "List[GetRewardsGrantedResponseValueItem]"

PutRewardsRulesKeyResponse = TypedDict("PutRewardsRulesKeyResponse", {
    "key": str,
    "event": Optional[str],
    "programId": Optional[str],
    "amountMinor": int,
    "currency": str,
    "reason": str,
    "enabled": bool,
    "updatedAt": str,
})

DeleteRewardsRulesKeyResponse = TypedDict("DeleteRewardsRulesKeyResponse", {
    "ok": bool,
})

GetProgramsIdGroupsResponse = TypedDict("GetProgramsIdGroupsResponse", {
    "object": Literal["list"],
    "data": List["PartnerGroup"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

PutProgramsIdPartnersPartnerIdGroupResponse = TypedDict("PutProgramsIdPartnersPartnerIdGroupResponse", {
    "partnerId": str,
    "programId": str,
    "groupId": Optional[str],
})

GetProgramsIdPromotionsResponse = TypedDict("GetProgramsIdPromotionsResponse", {
    "object": Literal["list"],
    "data": List["Promotion"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

GetPartnerGroupsResponseDataItem = TypedDict("GetPartnerGroupsResponseDataItem", {
    "groupId": str,
    "groupName": str,
    "orgName": str,
    "programId": str,
    "programName": str,
    "onboardingMessage": Optional[str],
    "onboardingChecklist": List[str],
    "holdDays": Optional[int],
    "minThresholdMinor": Optional[int],
    "payoutCurrency": Optional[str],
})

GetPartnerGroupsResponse = TypedDict("GetPartnerGroupsResponse", {
    "object": Literal["list"],
    "data": List["GetPartnerGroupsResponseDataItem"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

PostContractsResponse = TypedDict("PostContractsResponse", {
    "id": str,
    "status": Literal["draft", "sent"],
})

GetContractsResponseDataItem = TypedDict("GetContractsResponseDataItem", {
    "id": str,
    "programId": str,
    "partnerId": str,
    "title": str,
    "compensation": "GetOpenapiJsonResponse",
    "status": str,
    "createdAt": str,
    "respondedAt": Optional[str],
})

GetContractsResponse = TypedDict("GetContractsResponse", {
    "object": Literal["list"],
    "data": List["GetContractsResponseDataItem"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

GetPartnerContractsResponseDataItem = TypedDict("GetPartnerContractsResponseDataItem", {
    "id": str,
    "merchant": str,
    "program": str,
    "title": str,
    "termsMd": str,
    "compensation": "GetOpenapiJsonResponse",
    "status": str,
    "createdAt": str,
})

GetPartnerContractsResponse = TypedDict("GetPartnerContractsResponse", {
    "object": Literal["list"],
    "data": List["GetPartnerContractsResponseDataItem"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

PutProgramsIdIncrementalityResponse = TypedDict("PutProgramsIdIncrementalityResponse", {
    "ok": bool,
    "holdoutBps": int,
})

GetIncrementalityResponseTreatment = TypedDict("GetIncrementalityResponseTreatment", {
    "referrals": int,
    "converted": int,
    "rate": float,
})

GetIncrementalityResponseControl = TypedDict("GetIncrementalityResponseControl", {
    "referrals": int,
    "converted": int,
    "rate": float,
})

GetIncrementalityResponseByPartnerItem = TypedDict("GetIncrementalityResponseByPartnerItem", {
    "partnerId": str,
    "treatmentReferrals": int,
    "controlReferrals": int,
    "lift": float,
})

GetIncrementalityResponse = TypedDict("GetIncrementalityResponse", {
    "programId": str,
    "holdoutBps": int,
    "treatment": "GetIncrementalityResponseTreatment",
    "control": "GetIncrementalityResponseControl",
    "lift": float,
    "byPartner": List["GetIncrementalityResponseByPartnerItem"],
})

PutProgramsIdAutopricingResponse = TypedDict("PutProgramsIdAutopricingResponse", {
    "ok": bool,
    "autopricing": Optional["GetOpenapiJsonResponse"],
})

GetProgramsIdAutopricingResponseAutopricingOption1 = TypedDict("GetProgramsIdAutopricingResponseAutopricingOption1", {
    "enabled": bool,
    "targetRoas": float,
    "minBps": int,
    "maxBps": int,
    "objective": Literal["roas", "roi"],
    "targetRoi": float,
})

GetProgramsIdAutopricingResponse = TypedDict("GetProgramsIdAutopricingResponse", {
    "autopricing": Optional["GetProgramsIdAutopricingResponseAutopricingOption1"],
})

PostProgramsIdAutopriceRunResponseChangesItem = TypedDict("PostProgramsIdAutopriceRunResponseChangesItem", {
    "partnerId": str,
    "fromBps": int,
    "toBps": int,
    "realizedRoas": Optional[float],
    "realizedRoi": NotRequired[Optional[float]],
})

PostProgramsIdAutopriceRunResponseHeldItem = TypedDict("PostProgramsIdAutopriceRunResponseHeldItem", {
    "partnerId": str,
    "reason": Literal["roi_unknown", "too_few_matured"],
    "maturedGrants": int,
})

PostProgramsIdAutopriceRunResponse = TypedDict("PostProgramsIdAutopriceRunResponse", {
    "objective": Literal["roas", "roi"],
    "targetRoas": float,
    "targetRoi": NotRequired[float],
    "changes": List["PostProgramsIdAutopriceRunResponseChangesItem"],
    "held": NotRequired[List["PostProgramsIdAutopriceRunResponseHeldItem"]],
})

GetPassportPublicKeyResponse = TypedDict("GetPassportPublicKeyResponse", {
    "algorithm": Literal["ed25519"],
    "publicKey": str,
})

PostPassportVerifyResponse = TypedDict("PostPassportVerifyResponse", {
    "valid": bool,
    "claims": NotRequired["GetOpenapiJsonResponse"],
    "reason": NotRequired[str],
})

GetPartnerAdvanceOfferResponse = TypedDict("GetPartnerAdvanceOfferResponse", {
    "currency": str,
    "monthlyRunRateMinor": int,
    "projectedMinor": int,
    "maxAdvanceMinor": int,
    "feeBps": int,
    "qualityScore": float,
})

PostPartnerAdvanceAcceptResponse = TypedDict("PostPartnerAdvanceAcceptResponse", {
    "id": str,
    "principalMinor": int,
    "feeMinor": int,
    "outstandingMinor": int,
    "status": str,
})

GetPartnerAdvanceResponseDataItem = TypedDict("GetPartnerAdvanceResponseDataItem", {
    "id": str,
    "currency": str,
    "principalMinor": int,
    "feeMinor": int,
    "outstandingMinor": int,
    "status": str,
    "createdAt": str,
    "repaidAt": Optional[str],
})

GetPartnerAdvanceResponse = TypedDict("GetPartnerAdvanceResponse", {
    "object": Literal["list"],
    "data": List["GetPartnerAdvanceResponseDataItem"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

PutNetworkSettingsResponse = TypedDict("PutNetworkSettingsResponse", {
    "enabled": bool,
})

GetNetworkSettingsResponse = TypedDict("GetNetworkSettingsResponse", {
    "enabled": bool,
})

GetNetworkJourneyResponseTouchpointsItem = TypedDict("GetNetworkJourneyResponseTouchpointsItem", {
    "partnerAccountId": str,
    "ts": str,
    "credit": float,
})

GetNetworkJourneyResponse = TypedDict("GetNetworkJourneyResponse", {
    "emailHash": str,
    "model": str,
    "touchpoints": List["GetNetworkJourneyResponseTouchpointsItem"],
    "partners": int,
})

PutProgramsIdNegotiationPolicyResponse = TypedDict("PutProgramsIdNegotiationPolicyResponse", {
    "ok": bool,
    "negotiationPolicy": Optional["GetOpenapiJsonResponse"],
})

GetProgramsIdNegotiationPolicyResponse = TypedDict("GetProgramsIdNegotiationPolicyResponse", {
    "negotiationPolicy": Optional["GetOpenapiJsonResponse"],
})

GetNegotiationsResponseDataItem = TypedDict("GetNegotiationsResponseDataItem", {
    "id": str,
    "programId": str,
    "agentAccountId": str,
    "proposedBps": int,
    "decision": str,
    "rateBps": Optional[int],
    "round": int,
    "createdAt": str,
})

GetNegotiationsResponse = TypedDict("GetNegotiationsResponse", {
    "object": Literal["list"],
    "data": List["GetNegotiationsResponseDataItem"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

GetCleanroomConsentResponseConsentOption1 = TypedDict("GetCleanroomConsentResponseConsentOption1", {
    "granted": bool,
    "purposes": List[str],
    "declared": "GetOpenapiJsonResponse",
    "emailHash": Optional[str],
    "updatedAt": str,
})

GetCleanroomConsentResponse = TypedDict("GetCleanroomConsentResponse", {
    "customerRef": str,
    "consent": Optional["GetCleanroomConsentResponseConsentOption1"],
})

GetCleanroomQueryResponseCohortsItem = TypedDict("GetCleanroomQueryResponseCohortsItem", {
    "key": str,
    "count": int,
})

GetCleanroomQueryResponse = TypedDict("GetCleanroomQueryResponse", {
    "dimension": str,
    "k": int,
    "cohorts": List["GetCleanroomQueryResponseCohortsItem"],
    "suppressedCohorts": int,
    "suppressedRows": int,
})

GetAgentsResponseDataItem = TypedDict("GetAgentsResponseDataItem", {
    "partnerId": str,
    "accountId": str,
    "name": str,
    "wallet": Optional[str],
    "metadata": Optional["GetOpenapiJsonResponse"],
    "instantPayout": bool,
    "status": str,
    "recommendations": int,
})

GetAgentsResponse = TypedDict("GetAgentsResponse", {
    "object": Literal["list"],
    "data": List["GetAgentsResponseDataItem"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

GetAgentsRecommendationsResponseDataItem = TypedDict("GetAgentsRecommendationsResponseDataItem", {
    "id": str,
    "programId": str,
    "customerRef": str,
    "agent": str,
    "wallet": Optional[str],
    "createdAt": str,
})

GetAgentsRecommendationsResponse = TypedDict("GetAgentsRecommendationsResponse", {
    "object": Literal["list"],
    "data": List["GetAgentsRecommendationsResponseDataItem"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

GetAdminMetricsResponse = TypedDict("GetAdminMetricsResponse", {
    "orgs": int,
    "suspendedOrgs": int,
    "partnerAccounts": int,
    "bannedPartners": int,
    "programs": int,
    "commissionEarnedMinor": int,
    "payoutsSent": int,
    "openFraudCases": int,
})

GetAdminOrgsResponseDataItem = TypedDict("GetAdminOrgsResponseDataItem", {
    "id": str,
    "name": str,
    "plan": str,
    "planStatus": Optional[str],
    "suspended": bool,
    "createdAt": str,
    "programs": int,
    "partners": int,
})

GetAdminOrgsResponse = TypedDict("GetAdminOrgsResponse", {
    "object": Literal["list"],
    "data": List["GetAdminOrgsResponseDataItem"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

PostAdminOrgsIdSuspendResponse = TypedDict("PostAdminOrgsIdSuspendResponse", {
    "ok": bool,
    "suspended": bool,
})

PostAdminOrgsIdPlanResponse = TypedDict("PostAdminOrgsIdPlanResponse", {
    "plan": str,
    "planStatus": str,
})

PostAdminOrgsIdUnsuspendResponse = TypedDict("PostAdminOrgsIdUnsuspendResponse", {
    "ok": bool,
    "suspended": bool,
})

GetAdminPartnerAccountsResponseDataItem = TypedDict("GetAdminPartnerAccountsResponseDataItem", {
    "id": str,
    "email": str,
    "name": Optional[str],
    "banned": bool,
    "kycStatus": Optional[str],
    "sanctionsStatus": Optional[str],
    "createdAt": str,
})

GetAdminPartnerAccountsResponse = TypedDict("GetAdminPartnerAccountsResponse", {
    "object": Literal["list"],
    "data": List["GetAdminPartnerAccountsResponseDataItem"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

PostAdminPartnerAccountsIdBanResponse = TypedDict("PostAdminPartnerAccountsIdBanResponse", {
    "ok": bool,
    "banned": bool,
})

PostAdminPartnerAccountsIdUnbanResponse = TypedDict("PostAdminPartnerAccountsIdUnbanResponse", {
    "ok": bool,
    "banned": bool,
})

GetNotificationsResponse = TypedDict("GetNotificationsResponse", {
    "object": Literal["list"],
    "data": List["Notification"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

GetPartnerNotificationsResponse = TypedDict("GetPartnerNotificationsResponse", {
    "object": Literal["list"],
    "data": List["Notification"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

PostAssetsResponse = TypedDict("PostAssetsResponse", {
    "id": str,
    "programId": str,
    "kind": str,
    "title": str,
    "content": str,
    "dimensions": str,
    "groupId": NotRequired[Optional[str]],
})

GetAssetsResponseDataItem = TypedDict("GetAssetsResponseDataItem", {
    "id": str,
    "programId": str,
    "kind": str,
    "title": str,
    "content": str,
    "dimensions": str,
    "groupId": Optional[str],
    "clicks": int,
    "referrals": int,
    "createdAt": str,
})

GetAssetsResponse = TypedDict("GetAssetsResponse", {
    "object": Literal["list"],
    "data": List["GetAssetsResponseDataItem"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

PostPartnerDealsResponse = TypedDict("PostPartnerDealsResponse", {
    "id": str,
    "status": Literal["submitted"],
})

GetPartnerDealsResponseDataItem = TypedDict("GetPartnerDealsResponseDataItem", {
    "id": str,
    "orgId": str,
    "company": str,
    "valueMinor": int,
    "currency": str,
    "status": str,
    "protectionExpiresAt": Optional[str],
    "createdAt": str,
})

GetPartnerDealsResponse = TypedDict("GetPartnerDealsResponse", {
    "object": Literal["list"],
    "data": List["GetPartnerDealsResponseDataItem"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

GetDealsResponseDataItem = TypedDict("GetDealsResponseDataItem", {
    "id": str,
    "programId": str,
    "partnerId": str,
    "partnerEmail": str,
    "company": str,
    "contactEmail": str,
    "valueMinor": int,
    "currency": str,
    "status": str,
    "protectionExpiresAt": Optional[str],
    "referralId": Optional[str],
    "notes": str,
    "createdAt": str,
})

GetDealsResponse = TypedDict("GetDealsResponse", {
    "object": Literal["list"],
    "data": List["GetDealsResponseDataItem"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

PostDealsIdApproveResponse = TypedDict("PostDealsIdApproveResponse", {
    "id": str,
    "status": Literal["approved"],
    "protectionExpiresAt": str,
})

PostDealsIdRejectResponse = TypedDict("PostDealsIdRejectResponse", {
    "id": str,
    "status": Literal["rejected"],
})

PostDealsIdWonResponse = TypedDict("PostDealsIdWonResponse", {
    "id": str,
    "status": Literal["won"],
    "referralId": str,
})

PostProgramsIdApplyLevelingResponse = TypedDict("PostProgramsIdApplyLevelingResponse", {
    "evaluated": int,
    "promoted": int,
})

PostPayoutRunsRunScheduledResponseValueItem = TypedDict("PostPayoutRunsRunScheduledResponseValueItem", {
    "orgId": str,
    "runId": str,
    "payouts": int,
    "sent": int,
    "failed": int,
})

PostPayoutRunsRunScheduledResponse: TypeAlias = "List[PostPayoutRunsRunScheduledResponseValueItem]"

PutPartnerOrgsOrgIdPostbackResponse = TypedDict("PutPartnerOrgsOrgIdPostbackResponse", {
    "url": str,
    "secret": str,
    "macros": List[str],
})

GetPartnerPostbackLogsResponseDataItem = TypedDict("GetPartnerPostbackLogsResponseDataItem", {
    "topic": str,
    "url": str,
    "statusCode": Optional[int],
    "ts": str,
})

GetPartnerPostbackLogsResponse = TypedDict("GetPartnerPostbackLogsResponse", {
    "object": Literal["list"],
    "data": List["GetPartnerPostbackLogsResponseDataItem"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

GetPartnerRecruitResponse = TypedDict("GetPartnerRecruitResponse", {
    "code": str,
    "url": str,
})

GetPartnerAchievementsResponseDataItem = TypedDict("GetPartnerAchievementsResponseDataItem", {
    "id": str,
    "title": str,
    "unlocked": bool,
    "progress": int,
    "target": int,
})

GetPartnerAchievementsResponse = TypedDict("GetPartnerAchievementsResponse", {
    "object": Literal["list"],
    "data": List["GetPartnerAchievementsResponseDataItem"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

GetPartnerTermsResponseDataItem = TypedDict("GetPartnerTermsResponseDataItem", {
    "versionId": str,
    "programId": str,
    "programName": str,
    "version": int,
    "termsMd": str,
    "accepted": bool,
})

GetPartnerTermsResponse = TypedDict("GetPartnerTermsResponse", {
    "object": Literal["list"],
    "data": List["GetPartnerTermsResponseDataItem"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

GetProgramsIdTermsAcceptancesResponseDataItem = TypedDict("GetProgramsIdTermsAcceptancesResponseDataItem", {
    "version": int,
    "partnerEmail": str,
    "acceptedAt": str,
})

GetProgramsIdTermsAcceptancesResponse = TypedDict("GetProgramsIdTermsAcceptancesResponse", {
    "object": Literal["list"],
    "data": List["GetProgramsIdTermsAcceptancesResponseDataItem"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

GetSetupStatusResponse = TypedDict("GetSetupStatusResponse", {
    "checks": Dict[str, bool],
    "hints": List[str],
    "hintKeys": List[str],
    "progress": str,
})

PostAnomaliesScanResponseValueItem = TypedDict("PostAnomaliesScanResponseValueItem", {
    "orgId": str,
    "metric": Literal["clicks", "referrals", "refunds"],
    "kind": Literal["spike", "drop"],
    "last24h": float,
    "daily7dAvg": float,
})

PostAnomaliesScanResponse: TypeAlias = "List[PostAnomaliesScanResponseValueItem]"

PostPrivacyForgetResponsePartnersItem = TypedDict("PostPrivacyForgetResponsePartnersItem", {
    "partnerId": str,
    "alreadyForgotten": bool,
})

PostPrivacyForgetResponseCustomersItem = TypedDict("PostPrivacyForgetResponseCustomersItem", {
    "customerRef": str,
    "pseudonym": str,
})

PostPrivacyForgetResponse = TypedDict("PostPrivacyForgetResponse", {
    "ok": bool,
    "pseudonym": NotRequired[str],
    "partners": NotRequired[List["PostPrivacyForgetResponsePartnersItem"]],
    "customers": NotRequired[List["PostPrivacyForgetResponseCustomersItem"]],
})

PostPrivacyLookupResponse = TypedDict("PostPrivacyLookupResponse", {
    "found": bool,
    "customerRefs": List[str],
    "partnerId": Optional[str],
})

PostPrivacyRequestsResponse = TypedDict("PostPrivacyRequestsResponse", {
    "id": str,
    "status": Literal["completed", "failed"],
})

GetPrivacyRequestsResponse = TypedDict("GetPrivacyRequestsResponse", {
    "object": Literal["list"],
    "data": List["PrivacyRequest"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

GetPrivacyRequestsIdResultResponseCustomersItemOption2 = TypedDict("GetPrivacyRequestsIdResultResponseCustomersItemOption2", {
    "customerRef": str,
    "pseudonym": str,
})

GetPrivacyRequestsIdResultResponsePartnersItem = TypedDict("GetPrivacyRequestsIdResultResponsePartnersItem", {
    "partnerId": str,
    "alreadyForgotten": bool,
})

GetPrivacyRequestsIdResultResponse = TypedDict("GetPrivacyRequestsIdResultResponse", {
    "found": bool,
    "customers": List[Union["CustomerExport", "GetPrivacyRequestsIdResultResponseCustomersItemOption2"]],
    "partner": NotRequired[Optional["PartnerExport"]],
    "partners": NotRequired[List["GetPrivacyRequestsIdResultResponsePartnersItem"]],
})

PostEmailSettingsVerifyDomainResponse: TypeAlias = "Any"

GetEmailTemplatesResponse = TypedDict("GetEmailTemplatesResponse", {
    "object": Literal["list"],
    "data": List["EmailTemplateEvent"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

PutEmailTemplatesEventLocaleResponse = TypedDict("PutEmailTemplatesEventLocaleResponse", {
    "event": str,
    "locale": str,
    "subject": str,
    "text": str,
    "html": Optional[str],
    "updatedAt": str,
})

DeleteEmailTemplatesEventLocaleResponse = TypedDict("DeleteEmailTemplatesEventLocaleResponse", {
    "ok": bool,
    "reset": bool,
})

PostEmailTestResponse = TypedDict("PostEmailTestResponse", {
    "sent": bool,
    "id": str,
    "provider": str,
})

PutMeLocaleResponse = TypedDict("PutMeLocaleResponse", {
    "locale": str,
})

PutMeRoiDigestResponse = TypedDict("PutMeRoiDigestResponse", {
    "enabled": bool,
})

PutPartnerLocaleResponse = TypedDict("PutPartnerLocaleResponse", {
    "locale": str,
})

GetIntegrationsResponseZapier = TypedDict("GetIntegrationsResponseZapier", {
    "hooks": int,
    "events": List[str],
})

GetIntegrationsResponse = TypedDict("GetIntegrationsResponse", {
    "zapier": "GetIntegrationsResponseZapier",
    "hubspot": Optional["IntegrationConnection"],
    "segment": Optional["IntegrationConnection"],
})

PostIntegrationsHubspotTestResponse = TypedDict("PostIntegrationsHubspotTestResponse", {
    "ok": bool,
    "portalId": Optional[int],
    "createdProperties": List[str],
    "error": Optional[str],
})

PostIntegrationsSegmentTestResponse = TypedDict("PostIntegrationsSegmentTestResponse", {
    "ok": bool,
    "error": Optional[str],
})

GetIntegrationsDeliveriesResponse = TypedDict("GetIntegrationsDeliveriesResponse", {
    "object": Literal["list"],
    "data": List["IntegrationDelivery"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

GetZapierEventsResponseValueItem = TypedDict("GetZapierEventsResponseValueItem", {
    "key": str,
})

GetZapierEventsResponse: TypeAlias = "List[GetZapierEventsResponseValueItem]"

GetZapierHooksResponse = TypedDict("GetZapierHooksResponse", {
    "object": Literal["list"],
    "data": List["ZapierHook"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

# The event's payload fields, flattened, plus id (the event id), event and createdAt.
GetZapierTriggersEventResponseValueItem = TypedDict("GetZapierTriggersEventResponseValueItem", {
    "id": str,
    "event": str,
    "createdAt": str,
})

GetZapierTriggersEventResponse: TypeAlias = "List[GetZapierTriggersEventResponseValueItem]"

PostZapierConversionsResponse = TypedDict("PostZapierConversionsResponse", {
    "connectionId": str,
})

PostPartnerSecurityTotpSetupResponse = TypedDict("PostPartnerSecurityTotpSetupResponse", {
    "secret": str,
    "otpauthUrl": str,
})

PostPartnerSecurityTotpEnableResponse = TypedDict("PostPartnerSecurityTotpEnableResponse", {
    "enabled": bool,
})

PostPartnerSecurityTotpDisableResponse = TypedDict("PostPartnerSecurityTotpDisableResponse", {
    "enabled": bool,
})

GetPartnerSecurityResponse = TypedDict("GetPartnerSecurityResponse", {
    "totpEnabled": bool,
})

GetAuthConnectionsProvidersResponse = TypedDict("GetAuthConnectionsProvidersResponse", {
    "data": List["IdentityProvider"],
})

GetAuthConnectionsResponse = TypedDict("GetAuthConnectionsResponse", {
    "object": Literal["list"],
    "data": List["AuthConnection"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

PutAuthConnectionsIdSecretResponse = TypedDict("PutAuthConnectionsIdSecretResponse", {
    "id": str,
    "provider": str,
    "ok": bool,
})

PostAuthConnectionsIdRotateSecretResponse = TypedDict("PostAuthConnectionsIdRotateSecretResponse", {
    "id": str,
    "provider": str,
    "secret": str,
    "previousSecretExpiresAt": str,
})

PatchAuthConnectionsIdResponse = TypedDict("PatchAuthConnectionsIdResponse", {
    "id": str,
    "provider": str,
    "name": str,
    "status": Literal["active", "paused"],
    "autoEnrollUsers": NotRequired[bool],
    "destinationUrl": NotRequired[Optional[str]],
    "signatureVersion": NotRequired[Literal["v1+v2", "v2"]],
    "requiresV2": NotRequired[bool],
})

PostAuthConnectionsIdRevokePreviousSecretResponse = TypedDict("PostAuthConnectionsIdRevokePreviousSecretResponse", {
    "ok": bool,
    "revoked": bool,
})

PostAuthConnectionsIdSignupsResponseReferralOption1 = TypedDict("PostAuthConnectionsIdSignupsResponseReferralOption1", {
    "id": str,
    "partnerId": str,
    "partnerExternalRef": Optional[str],
    "matchedVia": str,
    "status": str,
    "persisted": NotRequired[bool],
})

PostAuthConnectionsIdSignupsResponseReasoning = TypedDict("PostAuthConnectionsIdSignupsResponseReasoning", {
    "notes": List[str],
    "codes": List["SignupReasonCode"],
})

PostAuthConnectionsIdSignupsResponsePartner = TypedDict("PostAuthConnectionsIdSignupsResponsePartner", {
    "id": str,
    "code": str,
    "link": Optional[str],
    "persisted": NotRequired[bool],
})

PostAuthConnectionsIdSignupsResponse = TypedDict("PostAuthConnectionsIdSignupsResponse", {
    "test": NotRequired[bool],
    "referral": Optional["PostAuthConnectionsIdSignupsResponseReferralOption1"],
    "reasoning": NotRequired["PostAuthConnectionsIdSignupsResponseReasoning"],
    "partner": NotRequired["PostAuthConnectionsIdSignupsResponsePartner"],
})

PostAuthConnectionsIdPartnersResponsePartner = TypedDict("PostAuthConnectionsIdPartnersResponsePartner", {
    "id": str,
    "code": str,
    "link": Optional[str],
})

PostAuthConnectionsIdPartnersResponse = TypedDict("PostAuthConnectionsIdPartnersResponse", {
    "partner": "PostAuthConnectionsIdPartnersResponsePartner",
})

PostAuthConnectionsIdEraseResponseCustomerOption1 = TypedDict("PostAuthConnectionsIdEraseResponseCustomerOption1", {
    "customerRef": str,
    "pseudonym": str,
})

PostAuthConnectionsIdEraseResponsePartnerOption1 = TypedDict("PostAuthConnectionsIdEraseResponsePartnerOption1", {
    "partnerId": str,
    "alreadyForgotten": bool,
})

PostAuthConnectionsIdEraseResponse = TypedDict("PostAuthConnectionsIdEraseResponse", {
    "ok": bool,
    "erased": bool,
    "customer": Optional["PostAuthConnectionsIdEraseResponseCustomerOption1"],
    "partner": Optional["PostAuthConnectionsIdEraseResponsePartnerOption1"],
})

GetAuthConnectionsIdExportResponse = TypedDict("GetAuthConnectionsIdExportResponse", {
    "customer": "CustomerExport",
    "partner": Optional["PartnerExport"],
})

PostAuthConnectionsIdPingResponse = TypedDict("PostAuthConnectionsIdPingResponse", {
    "ok": bool,
    "connectionId": str,
    "programId": str,
    "orgName": str,
    "autoEnrollUsers": bool,
    "serverTime": str,
})

PostAuthConnectionsIdAliasesResponse = TypedDict("PostAuthConnectionsIdAliasesResponse", {
    "ok": bool,
    "customerRef": str,
    "referralIds": List[str],
    "partnerId": Optional[str],
    "alreadyAliased": bool,
    "reprocessedPayments": int,
})

PostAuthConnectionsIdUsersResponseCustomerOption1 = TypedDict("PostAuthConnectionsIdUsersResponseCustomerOption1", {
    "customerRef": str,
    "pseudonym": str,
})

PostAuthConnectionsIdUsersResponsePartnerOption1Option1 = TypedDict("PostAuthConnectionsIdUsersResponsePartnerOption1Option1", {
    "partnerId": str,
    "alreadyForgotten": bool,
})

PostAuthConnectionsIdUsersResponsePartnerOption1Option2 = TypedDict("PostAuthConnectionsIdUsersResponsePartnerOption1Option2", {
    "id": str,
    "status": str,
})

PostAuthConnectionsIdUsersResponse = TypedDict("PostAuthConnectionsIdUsersResponse", {
    "ok": bool,
    "deleted": NotRequired[bool],
    "erased": NotRequired[bool],
    "customer": NotRequired[Optional["PostAuthConnectionsIdUsersResponseCustomerOption1"]],
    "partner": Optional[Union["PostAuthConnectionsIdUsersResponsePartnerOption1Option1", "PostAuthConnectionsIdUsersResponsePartnerOption1Option2"]],
    "updated": NotRequired[List[str]],
    "notes": NotRequired[List[str]],
})

PostAuthConnectionsIdSignalsResponseReferralsItem = TypedDict("PostAuthConnectionsIdSignalsResponseReferralsItem", {
    "id": str,
    "status": str,
})

PostAuthConnectionsIdSignalsResponseReversedItem = TypedDict("PostAuthConnectionsIdSignalsResponseReversedItem", {
    "lineId": str,
    "amountMinor": int,
    "currency": str,
})

PostAuthConnectionsIdSignalsResponsePartnerOption1 = TypedDict("PostAuthConnectionsIdSignalsResponsePartnerOption1", {
    "id": str,
    "status": str,
})

PostAuthConnectionsIdSignalsResponse = TypedDict("PostAuthConnectionsIdSignalsResponse", {
    "ok": bool,
    "signal": Literal["email_verified", "banned", "unbanned", "fraud_confirmed", "self_referral"],
    "referrals": List["PostAuthConnectionsIdSignalsResponseReferralsItem"],
    "reversed": List["PostAuthConnectionsIdSignalsResponseReversedItem"],
    "partner": Optional["PostAuthConnectionsIdSignalsResponsePartnerOption1"],
    "notes": NotRequired[List[str]],
})

PostAuthConnectionsInstallResponse = TypedDict("PostAuthConnectionsInstallResponse", {
    "redirectTo": str,
})

PostOauthTokenResponse = TypedDict("PostOauthTokenResponse", {
    "token_type": Literal["connection_secret"],
    "connectionId": str,
    "provider": str,
    "instanceId": str,
    "programId": str,
    "secret": str,
    "reinstalled": bool,
    "signupsUrl": str,
    "partnersUrl": str,
    "eraseUrl": str,
    "exportUrl": str,
})

GetOrgSsoResponseProviderOption1 = TypedDict("GetOrgSsoResponseProviderOption1", {
    "name": str,
    "label": str,
})

GetOrgSsoResponseConnectionsItem = TypedDict("GetOrgSsoResponseConnectionsItem", {
    "id": str,
    "type": str,
    "status": str,
    "allowedDomains": List[str],
})

GetOrgSsoResponseTicketsItem = TypedDict("GetOrgSsoResponseTicketsItem", {
    "id": str,
    "status": str,
    "expiresAt": str,
    "createdAt": str,
})

GetOrgSsoResponse = TypedDict("GetOrgSsoResponse", {
    "configured": bool,
    "provider": Optional["GetOrgSsoResponseProviderOption1"],
    "defaultRoleMapping": Dict[str, str],
    "linked": bool,
    "tenantId": Optional[str],
    "atlasOrgId": Optional[str],
    "connections": List["GetOrgSsoResponseConnectionsItem"],
    "domains": List[str],
    "requireSso": bool,
    "roleMapping": Dict[str, str],
    "tickets": List["GetOrgSsoResponseTicketsItem"],
    "providerError": Optional[str],
    "atlasError": Optional[str],
})

PostOrgSsoLinkResponse = TypedDict("PostOrgSsoLinkResponse", {
    "linked": bool,
    "provider": str,
    "tenantId": str,
    "atlasOrgId": Optional[str],
})

PostOrgSsoTicketsResponse = TypedDict("PostOrgSsoTicketsResponse", {
    "id": str,
    "url": str,
    "expiresAt": str,
})

PostOrgSsoTicketsIdRevokeResponse = TypedDict("PostOrgSsoTicketsIdRevokeResponse", {
    "id": str,
    "status": Literal["revoked"],
})

GetOrgSsoConnectionsIdSamlMetadataResponse = TypedDict("GetOrgSsoConnectionsIdSamlMetadataResponse", {
    "spEntityId": str,
    "acsUrl": str,
    "metadataXml": str,
})

PatchOrgSsoResponse = TypedDict("PatchOrgSsoResponse", {
    "requireSso": bool,
    "roleMapping": Dict[str, str],
})

PutOrgSsoDirectResponse = TypedDict("PutOrgSsoDirectResponse", {
    "adapter": Literal["oidc", "workos"],
    "config": Dict[str, Any],
    "hasSecret": bool,
    "signInUrl": str,
    "redirectUri": str,
})

DeleteOrgSsoDirectResponse = TypedDict("DeleteOrgSsoDirectResponse", {
    "removed": bool,
})

PostPartnerAuthWalletNonceResponse = TypedDict("PostPartnerAuthWalletNonceResponse", {
    "nonce": str,
    "message": str,
})

PostPartnerAuthWalletVerifyResponse = TypedDict("PostPartnerAuthWalletVerifyResponse", {
    "accountId": str,
    "wallet": str,
})

PostOnchainConnectionsResponse = TypedDict("PostOnchainConnectionsResponse", {
    "id": str,
    "secret": str,
    "webhookUrl": str,
})

GetOnchainConnectionsResponseDataItem = TypedDict("GetOnchainConnectionsResponseDataItem", {
    "id": str,
    "programId": str,
    "name": str,
    "status": str,
    "createdAt": str,
})

GetOnchainConnectionsResponse = TypedDict("GetOnchainConnectionsResponse", {
    "object": Literal["list"],
    "data": List["GetOnchainConnectionsResponseDataItem"],
    "has_more": bool,
    "next_cursor": Optional[str],
})

GetPublicProgramsHandleResponseBranding = TypedDict("GetPublicProgramsHandleResponseBranding", {
    "logoUrl": Optional[str],
    "theme": Optional["GetOpenapiJsonResponse"],
})

GetPublicProgramsHandleResponse = TypedDict("GetPublicProgramsHandleResponse", {
    "handle": str,
    "programId": str,
    "programName": str,
    "merchant": str,
    "trackingToken": str,
    "cookieWindowDays": int,
    "termsMd": str,
    "pitch": str,
    "autoApprove": bool,
    "commission": Optional["GetOpenapiJsonResponse"],
    "branding": "GetPublicProgramsHandleResponseBranding",
})

PostPublicProgramsHandleJoinResponse = TypedDict("PostPublicProgramsHandleJoinResponse", {
    "accountId": str,
    "status": Literal["approved", "applied"],
    "link": Optional[str],
    "linkUrl": Optional[str],
    "code": Optional[str],
    "portalUrl": str,
})

GetIntegrationHealthResponse = TypedDict("GetIntegrationHealthResponse", {
    "ok": bool,
    "checks": List["HealthCheck"],
    "generatedAt": str,
})

GetPlansResponsePlansItem = TypedDict("GetPlansResponsePlansItem", {
    "key": str,
    "label": str,
    "priceMinor": int,
    "currency": Literal["usd"],
    "interval": Literal["month"],
    "maxPrograms": Optional[int],
    "maxPartners": Optional[int],
    "marketplace": bool,
    "discovery": bool,
    "linkDomain": bool,
    "portalDomain": bool,
    "apiPerSec": int,
    "apiBurst": int,
})

GetPlansResponse = TypedDict("GetPlansResponse", {
    "plans": List["GetPlansResponsePlansItem"],
})

GetEventsResponseEventsItem = TypedDict("GetEventsResponseEventsItem", {
    "id": str,
    "topic": str,
    "orgId": str,
    "livemode": bool,
    "createdAt": str,
    "data": "GetOpenapiJsonResponse",
})

GetEventsResponse = TypedDict("GetEventsResponse", {
    "events": List["GetEventsResponseEventsItem"],
    "hasMore": bool,
    "nextCursor": Optional[str],
})

GetSupportContextResponsePartnerOption1 = TypedDict("GetSupportContextResponsePartnerOption1", {
    "id": str,
    "name": str,
    "status": str,
    "tier": Optional[str],
    "programs": List[str],
    "referralLink": Optional[str],
    "pendingMinor": int,
    "approvedMinor": int,
    "paidMinor": int,
    "currency": str,
    "nextPayoutAt": Optional[str],
    "flags": List[str],
})

GetSupportContextResponseCustomerOption1ReferredByOption1 = TypedDict("GetSupportContextResponseCustomerOption1ReferredByOption1", {
    "partnerId": str,
    "name": str,
})

GetSupportContextResponseCustomerOption1RewardStateOption1 = TypedDict("GetSupportContextResponseCustomerOption1RewardStateOption1", {
    "kind": str,
    "status": str,
    "amountMinor": int,
    "currency": str,
    "remainingMinor": int,
})

GetSupportContextResponseCustomerOption1 = TypedDict("GetSupportContextResponseCustomerOption1", {
    "referredBy": Optional["GetSupportContextResponseCustomerOption1ReferredByOption1"],
    "attributedAt": Optional[str],
    "rewardState": Optional["GetSupportContextResponseCustomerOption1RewardStateOption1"],
    "commissionsMinor": int,
    "currency": Optional[str],
})

GetSupportContextResponseLinks = TypedDict("GetSupportContextResponseLinks", {
    "dashboard": str,
    "partner": Optional[str],
    "referral": Optional[str],
})

GetSupportContextResponse = TypedDict("GetSupportContextResponse", {
    "partner": Optional["GetSupportContextResponsePartnerOption1"],
    "customer": Optional["GetSupportContextResponseCustomerOption1"],
    "links": "GetSupportContextResponseLinks",
})

GetSupportAppsResponseValueItemInstall = TypedDict("GetSupportAppsResponseValueItemInstall", {
    "kind": NotRequired[Literal["api", "manifest", "oauth"]],
    "steps": List[str],
    "manifestPath": NotRequired[str],
})

GetSupportAppsResponseValueItemConfigOption1 = TypedDict("GetSupportAppsResponseValueItemConfigOption1", {
    "subdomain": Any,
    "cardKey": Any,
    "hasPublicKey": bool,
})

GetSupportAppsResponseValueItem = TypedDict("GetSupportAppsResponseValueItem", {
    "id": str,
    "name": str,
    "status": Literal["ga", "beta"],
    "docsUrl": str,
    "vendorDocsUrl": str,
    "secretSource": Literal["vendor", "minted", "public_key"],
    "install": "GetSupportAppsResponseValueItemInstall",
    "cardUrl": str,
    "enabled": bool,
    "configured": bool,
    "config": Optional["GetSupportAppsResponseValueItemConfigOption1"],
    "lastOkAt": Optional[str],
    "lastError": Optional[str],
})

GetSupportAppsResponse: TypeAlias = "List[GetSupportAppsResponseValueItem]"

PutSupportAppsAdapterResponse = TypedDict("PutSupportAppsAdapterResponse", {
    "adapter": str,
    "enabled": bool,
    "cardUrl": str,
    "secret": NotRequired[str],
})

DeleteSupportAppsAdapterResponse = TypedDict("DeleteSupportAppsAdapterResponse", {
    "ok": bool,
})

PostSupportAppsAdapterTestResponse = TypedDict("PostSupportAppsAdapterTestResponse", {
    "found": bool,
    "context": Optional["GetSupportContextResponse"],
    "rendered": Any,
})

PostSupportCardsOrgIdAdapterResponse: TypeAlias = "Dict[str, Any]"

GetPrivacyExecutorsResponseValueItemInstall = TypedDict("GetPrivacyExecutorsResponseValueItemInstall", {
    "kind": NotRequired[Literal["api", "manifest", "oauth"]],
    "steps": List[str],
    "manifestPath": NotRequired[str],
})

GetPrivacyExecutorsResponseValueItemConfigOption1 = TypedDict("GetPrivacyExecutorsResponseValueItemConfigOption1", {
    "hasPublicKey": bool,
    "algorithm": Optional[str],
    "sombraUrl": Optional[str],
})

GetPrivacyExecutorsResponseValueItemHealth = TypedDict("GetPrivacyExecutorsResponseValueItemHealth", {
    "ok": bool,
    "detail": str,
    "fix": Optional[str],
})

GetPrivacyExecutorsResponseValueItem = TypedDict("GetPrivacyExecutorsResponseValueItem", {
    "id": str,
    "name": str,
    "status": Literal["ga", "beta"],
    "docsUrl": str,
    "vendorDocsUrl": str,
    "keyKind": Literal["bearer", "hmac", "standard-webhooks", "vendor-jwt"],
    "install": "GetPrivacyExecutorsResponseValueItemInstall",
    "url": str,
    "enabled": bool,
    "hasKey": bool,
    "hasVendorSecret": bool,
    "config": Optional["GetPrivacyExecutorsResponseValueItemConfigOption1"],
    "health": "GetPrivacyExecutorsResponseValueItemHealth",
    "lastOkAt": Optional[str],
    "lastError": Optional[str],
})

GetPrivacyExecutorsResponse: TypeAlias = "List[GetPrivacyExecutorsResponseValueItem]"

PostPrivacyExecutorKeysResponse = TypedDict("PostPrivacyExecutorKeysResponse", {
    "adapter": str,
    "url": str,
    "enabled": bool,
    "key": NotRequired[str],
})

DeletePrivacyExecutorsAdapterResponse = TypedDict("DeletePrivacyExecutorsAdapterResponse", {
    "ok": bool,
})

PostPrivacyExecutorsAdapterCheckResponse = TypedDict("PostPrivacyExecutorsAdapterCheckResponse", {
    "adapter": str,
    "ok": bool,
    "detail": str,
    "fix": Optional[str],
})

GetPrivacyExecutorRequestsResponseValueItem = TypedDict("GetPrivacyExecutorRequestsResponseValueItem", {
    "id": str,
    "adapter": str,
    "vendorRequestId": Optional[str],
    "op": str,
    "status": str,
    "createdAt": str,
    "completedAt": Optional[str],
})

GetPrivacyExecutorRequestsResponse: TypeAlias = "List[GetPrivacyExecutorRequestsResponseValueItem]"

PostAccountCloseResponse = TypedDict("PostAccountCloseResponse", {
    "closed": bool,
})

GetClicksConsentCoverageResponse = TypedDict("GetClicksConsentCoverageResponse", {
    "days": int,
    "since": str,
    "attributed": int,
    "withEvidence": int,
    "share": Optional[float],
})

GetClicksIdResponseConsentOption1 = TypedDict("GetClicksIdResponseConsentOption1", {
    "provider": str,
    "state": Literal["granted", "denied", "unknown"],
    "at": NotRequired[str],
    "stamp": NotRequired[str],
    "tcString": NotRequired[str],
    "gppString": NotRequired[str],
    "purposes": NotRequired[List[str]],
})

GetClicksIdResponse = TypedDict("GetClicksIdResponse", {
    "id": str,
    "programId": str,
    "partnerId": str,
    "linkId": Optional[str],
    "ts": str,
    "source": Literal["redirect", "snippet", "api"],
    "eligible": bool,
    "fraudScore": int,
    "anonId": Optional[str],
    "consent": Optional["GetClicksIdResponseConsentOption1"],
})

GetOrgTrackingConsentResponseAdaptersItem = TypedDict("GetOrgTrackingConsentResponseAdaptersItem", {
    "id": str,
    "name": str,
    "defaultCategory": Optional[str],
    "status": Literal["ga", "beta"],
    "docsUrl": str,
})

GetOrgTrackingConsentResponse = TypedDict("GetOrgTrackingConsentResponse", {
    "mode": str,
    "noCmp": NotRequired[Literal["persist", "memory"]],
    "category": NotRequired[str],
    "tcfVendorId": NotRequired[int],
    "gcmSignal": NotRequired[Literal["ad_storage", "analytics_storage"]],
    "configured": bool,
    "adapters": List["GetOrgTrackingConsentResponseAdaptersItem"],
})

GetOrgHostedPagesResponseConsent = TypedDict("GetOrgHostedPagesResponseConsent", {
    "adapter": str,
    "config": Dict[str, Any],
})

GetOrgHostedPagesResponseChatOption1 = TypedDict("GetOrgHostedPagesResponseChatOption1", {
    "adapter": str,
    "config": Dict[str, Any],
})

GetOrgHostedPagesResponseServedConsentTagsItem = TypedDict("GetOrgHostedPagesResponseServedConsentTagsItem", {
    "tag": Literal["script"],
    "attrs": Dict[str, Union[str, bool]],
    "inline": NotRequired[str],
})

GetOrgHostedPagesResponseServedConsentSettingsLinkOption1 = TypedDict("GetOrgHostedPagesResponseServedConsentSettingsLinkOption1", {
    "call": NotRequired[str],
    "attrs": NotRequired[Dict[str, str]],
})

GetOrgHostedPagesResponseServedConsentBuiltin = TypedDict("GetOrgHostedPagesResponseServedConsentBuiltin", {
    "policyUrl": str,
    "text": NotRequired[Dict[str, str]],
})

GetOrgHostedPagesResponseServedConsent = TypedDict("GetOrgHostedPagesResponseServedConsent", {
    "mode": Literal["cookiemunch", "cmp", "builtin", "none"],
    "provider": str,
    "tags": List["GetOrgHostedPagesResponseServedConsentTagsItem"],
    "settingsLink": Optional["GetOrgHostedPagesResponseServedConsentSettingsLinkOption1"],
    "builtin": NotRequired["GetOrgHostedPagesResponseServedConsentBuiltin"],
})

GetOrgHostedPagesResponseServedChatOption1TagsItem = TypedDict("GetOrgHostedPagesResponseServedChatOption1TagsItem", {
    "tag": Literal["script"],
    "attrs": Dict[str, Union[str, bool]],
    "inline": NotRequired[str],
})

GetOrgHostedPagesResponseServedChatOption1 = TypedDict("GetOrgHostedPagesResponseServedChatOption1", {
    "provider": str,
    "tags": List["GetOrgHostedPagesResponseServedChatOption1TagsItem"],
})

GetOrgHostedPagesResponseServed = TypedDict("GetOrgHostedPagesResponseServed", {
    "consent": "GetOrgHostedPagesResponseServedConsent",
    "chat": Optional["GetOrgHostedPagesResponseServedChatOption1"],
    "csp": str,
})

GetOrgHostedPagesResponseAdaptersConsentItem = TypedDict("GetOrgHostedPagesResponseAdaptersConsentItem", {
    "id": str,
    "name": str,
    "status": Literal["ga", "beta"],
    "docsUrl": str,
    "vendorDocsUrl": str,
})

GetOrgHostedPagesResponseAdaptersChatItem = TypedDict("GetOrgHostedPagesResponseAdaptersChatItem", {
    "id": str,
    "name": str,
    "status": Literal["ga", "beta"],
    "docsUrl": str,
    "vendorDocsUrl": str,
})

GetOrgHostedPagesResponseAdapters = TypedDict("GetOrgHostedPagesResponseAdapters", {
    "consent": List["GetOrgHostedPagesResponseAdaptersConsentItem"],
    "chat": List["GetOrgHostedPagesResponseAdaptersChatItem"],
})

GetOrgHostedPagesResponse = TypedDict("GetOrgHostedPagesResponse", {
    "consent": "GetOrgHostedPagesResponseConsent",
    "chat": Optional["GetOrgHostedPagesResponseChatOption1"],
    "customOrigins": Dict[str, List[str]],
    "status": Literal["unchecked", "ok", "error"],
    "lastOkAt": Optional[str],
    "lastError": Optional[str],
    "served": "GetOrgHostedPagesResponseServed",
    "adapters": "GetOrgHostedPagesResponseAdapters",
})

PostOrgHostedPagesCheckResponseChecksItem = TypedDict("PostOrgHostedPagesCheckResponseChecksItem", {
    "id": str,
    "ok": bool,
    "detail": str,
    "fix": NotRequired[str],
})

PostOrgHostedPagesCheckResponse = TypedDict("PostOrgHostedPagesCheckResponse", {
    "ok": bool,
    "checks": List["PostOrgHostedPagesCheckResponseChecksItem"],
})

PostWebhooksBillingConnectionIdResponseResultsItem = TypedDict("PostWebhooksBillingConnectionIdResponseResultsItem", {
    "duplicate": bool,
    "billingEventId": Optional[str],
    "conversions": int,
    "linesCreated": int,
    "reversals": int,
    "ignored": NotRequired[Literal["filter", "internal_customer"]],
})

PostWebhooksBillingConnectionIdResponse = TypedDict("PostWebhooksBillingConnectionIdResponse", {
    "received": int,
    "results": List["PostWebhooksBillingConnectionIdResponseResultsItem"],
})

PostWebhooksAuthConnectionIdResponseResultsItem = TypedDict("PostWebhooksAuthConnectionIdResponseResultsItem", {
    "customerRef": str,
    "attributed": bool,
    "reason": NotRequired[str],
    "partnerId": NotRequired[Optional[str]],
    "matchedVia": NotRequired[Optional[str]],
})

PostWebhooksAuthConnectionIdResponse = TypedDict("PostWebhooksAuthConnectionIdResponse", {
    "received": int,
    "results": List["PostWebhooksAuthConnectionIdResponseResultsItem"],
})

PostWebhooksSsoProviderResponse = TypedDict("PostWebhooksSsoProviderResponse", {
    "received": bool,
    "duplicate": bool,
    "handled": NotRequired[bool],
    "effects": NotRequired[List[str]],
})

PostWebhooksOnchainConnectionIdResponseResultsItem = TypedDict("PostWebhooksOnchainConnectionIdResponseResultsItem", {
    "txHash": str,
    "wallet": str,
    "amountMinor": int,
    "attributed": bool,
    "linesCreated": int,
    "duplicate": bool,
})

PostWebhooksOnchainConnectionIdResponse = TypedDict("PostWebhooksOnchainConnectionIdResponse", {
    "received": int,
    "results": List["PostWebhooksOnchainConnectionIdResponseResultsItem"],
})

PostWebhooksPayoutsProviderResponse = TypedDict("PostWebhooksPayoutsProviderResponse", {
    "ignored": NotRequired[bool],
    "reason": NotRequired[str],
    "finalized": NotRequired[bool],
    "status": NotRequired[str],
})

PostWebhooksStripeBillingResponse = TypedDict("PostWebhooksStripeBillingResponse", {
    "received": bool,
    "duplicate": NotRequired[bool],
    "ignored": NotRequired[bool],
    "reason": NotRequired[str],
    "orgId": NotRequired[str],
    "plan": NotRequired[str],
    "planStatus": NotRequired[str],
})

PostApiPrivacyLookupResponse = TypedDict("PostApiPrivacyLookupResponse", {
    "subjectId": Optional[str],
    "status": Literal["found", "no_match"],
})

PostApiPrivacyRequestsResponse = TypedDict("PostApiPrivacyRequestsResponse", {
    "id": str,
    "status": Literal["pending", "completed", "no_match", "rejected"],
    "eta": NotRequired[str],
    "detail": NotRequired[str],
})

GetApiPrivacyRequestsIdResponse = TypedDict("GetApiPrivacyRequestsIdResponse", {
    "id": str,
    "type": Literal["access", "deletion"],
    "status": Literal["pending", "completed", "no_match", "rejected"],
    "eta": NotRequired[str],
    "detail": NotRequired[str],
    "result": NotRequired["GetOpenapiJsonResponse"],
})

PostApiPrivacyOrgsOrgIdLookupResponse = TypedDict("PostApiPrivacyOrgsOrgIdLookupResponse", {
    "subjectId": Optional[str],
    "status": Literal["found", "no_match"],
})

PostApiPrivacyOrgsOrgIdRequestsResponse = TypedDict("PostApiPrivacyOrgsOrgIdRequestsResponse", {
    "id": str,
    "status": Literal["pending", "completed", "no_match", "rejected"],
    "detail": NotRequired[str],
})

GetApiPrivacyOrgsOrgIdRequestsIdResponse = TypedDict("GetApiPrivacyOrgsOrgIdRequestsIdResponse", {
    "id": str,
    "type": Literal["access", "deletion"],
    "status": Literal["pending", "completed", "no_match", "rejected"],
    "detail": NotRequired[str],
    "result": NotRequired["PostSupportCardsOrgIdAdapterResponse"],
})

GetGraphqlResponse = TypedDict("GetGraphqlResponse", {
    "data": NotRequired[Optional["GetOpenapiJsonResponse"]],
    "errors": NotRequired[List["GetOpenapiJsonResponse"]],
})

PostGraphqlResponse = TypedDict("PostGraphqlResponse", {
    "data": NotRequired[Optional["GetOpenapiJsonResponse"]],
    "errors": NotRequired[List["GetOpenapiJsonResponse"]],
})

PostAgentsRegisterBody = TypedDict("PostAgentsRegisterBody", {
    "walletAddress": str,
    "nonce": str,
    "signature": str,
    "name": NotRequired[str],
    "model": NotRequired[str],
    "operator": NotRequired[str],
    "instantPayout": NotRequired[bool],
})

PostAuthBackchannelLogoutBody = TypedDict("PostAuthBackchannelLogoutBody", {
    "logout_token": str,
})

PostOrgsBody = TypedDict("PostOrgsBody", {
    "name": str,
})

PutOrgPortalAuthBodyOption1 = TypedDict("PutOrgPortalAuthBodyOption1", {
    "adapter": Literal["referalli"],
})

PutOrgPortalAuthBodyOption2 = TypedDict("PutOrgPortalAuthBodyOption2", {
    "issuer": str,
    "clientId": str,
    "clientSecret": NotRequired[str],
    "scopes": NotRequired[str],
    "name": NotRequired[str],
    "trustEmailVerified": NotRequired[bool],
    "adapter": Literal["oidc"],
    "autoEnrollProgramId": NotRequired[Optional[str]],
})

PutOrgPortalAuthBodyOption3 = TypedDict("PutOrgPortalAuthBodyOption3", {
    "adapter": Literal["custom"],
    "issuer": str,
    "jwksUrl": str,
    "trustEmailVerified": NotRequired[bool],
    "autoEnrollProgramId": NotRequired[Optional[str]],
    "name": NotRequired[str],
    "loginUrl": NotRequired[str],
})

PostMobilePurchasesBody = TypedDict("PostMobilePurchasesBody", {
    "eventId": str,
    "customerRef": str,
    "type": NotRequired[Literal["purchase", "refund"]],
    "amountMinor": int,
    "currency": NotRequired[str],
    "productRef": NotRequired[str],
})

PatchOrgBody = TypedDict("PatchOrgBody", {
    "name": NotRequired[str],
    "settings": NotRequired[Dict[str, Any]],
    "payoutKycRequired": NotRequired[bool],
})

PostOrgMembersBody = TypedDict("PostOrgMembersBody", {
    "email": str,
    "role": Literal["owner", "admin", "finance", "analyst", "support"],
})

PatchOrgMembersUserIdBody = TypedDict("PatchOrgMembersUserIdBody", {
    "role": Literal["owner", "admin", "finance", "analyst", "support"],
})

PutOrgPayoutScheduleBodyScheduleOption1Option1 = TypedDict("PutOrgPayoutScheduleBodyScheduleOption1Option1", {
    "kind": Literal["monthly"],
    "dayOfMonth": int,
})

PutOrgPayoutScheduleBodyScheduleOption1Option2 = TypedDict("PutOrgPayoutScheduleBodyScheduleOption1Option2", {
    "kind": Literal["weekly"],
    "dayOfWeek": int,
})

PutOrgPayoutScheduleBodyScheduleOption1Option3 = TypedDict("PutOrgPayoutScheduleBodyScheduleOption1Option3", {
    "kind": Literal["twice_monthly"],
    "days": List[int],
})

PutOrgPayoutScheduleBodyScheduleOption1Option4 = TypedDict("PutOrgPayoutScheduleBodyScheduleOption1Option4", {
    "kind": Literal["custom"],
    "dates": List[str],
})

PutOrgPayoutScheduleBody = TypedDict("PutOrgPayoutScheduleBody", {
    "dayOfMonth": NotRequired[Optional[int]],
    "schedule": NotRequired[Optional[Union["PutOrgPayoutScheduleBodyScheduleOption1Option1", "PutOrgPayoutScheduleBodyScheduleOption1Option2", "PutOrgPayoutScheduleBodyScheduleOption1Option3", "PutOrgPayoutScheduleBodyScheduleOption1Option4"]]],
})

PutProgramsIdPayoutScheduleBodyScheduleOption1Option1Option1 = TypedDict("PutProgramsIdPayoutScheduleBodyScheduleOption1Option1Option1", {
    "kind": Literal["monthly"],
    "dayOfMonth": int,
})

PutProgramsIdPayoutScheduleBodyScheduleOption1Option1Option2 = TypedDict("PutProgramsIdPayoutScheduleBodyScheduleOption1Option1Option2", {
    "kind": Literal["weekly"],
    "dayOfWeek": int,
})

PutProgramsIdPayoutScheduleBodyScheduleOption1Option1Option3 = TypedDict("PutProgramsIdPayoutScheduleBodyScheduleOption1Option1Option3", {
    "kind": Literal["twice_monthly"],
    "days": List[int],
})

PutProgramsIdPayoutScheduleBodyScheduleOption1Option1Option4 = TypedDict("PutProgramsIdPayoutScheduleBodyScheduleOption1Option1Option4", {
    "kind": Literal["custom"],
    "dates": List[str],
})

PutProgramsIdPayoutScheduleBodyScheduleOption1Option2 = TypedDict("PutProgramsIdPayoutScheduleBodyScheduleOption1Option2", {
    "kind": Literal["off"],
})

PutProgramsIdPayoutScheduleBody = TypedDict("PutProgramsIdPayoutScheduleBody", {
    "schedule": Optional[Union[Union["PutProgramsIdPayoutScheduleBodyScheduleOption1Option1Option1", "PutProgramsIdPayoutScheduleBodyScheduleOption1Option1Option2", "PutProgramsIdPayoutScheduleBodyScheduleOption1Option1Option3", "PutProgramsIdPayoutScheduleBodyScheduleOption1Option1Option4"], "PutProgramsIdPayoutScheduleBodyScheduleOption1Option2"]],
})

PutOrgTaxProfileBody = TypedDict("PutOrgTaxProfileBody", {
    "legalName": NotRequired[Optional[str]],
    "address": NotRequired[Optional[str]],
    "country": NotRequired[Optional[str]],
    "vatId": NotRequired[Optional[str]],
    "ein": NotRequired[Optional[str]],
    "domesticVatBps": NotRequired[Optional[int]],
    "viesCheck": NotRequired[bool],
})

PutPartnersIdVatBody = TypedDict("PutPartnersIdVatBody", {
    "vatId": Optional[str],
})

PostPartnerOrgsOrgIdSelfBillingBody = TypedDict("PostPartnerOrgsOrgIdSelfBillingBody", {
    "accept": bool,
})

PutPartnerOrgsOrgIdVatBody = TypedDict("PutPartnerOrgsOrgIdVatBody", {
    "vatId": Optional[str],
})

PutOrgTaxFilingBodyCredentials = TypedDict("PutOrgTaxFilingBodyCredentials", {
    "apiKey": str,
    "baseUrl": NotRequired[str],
})

PutOrgTaxFilingBody = TypedDict("PutOrgTaxFilingBody", {
    "provider": Literal["test", "tax1099"],
    "credentials": NotRequired["PutOrgTaxFilingBodyCredentials"],
})

PostTax1099FilingsBody = TypedDict("PostTax1099FilingsBody", {
    "year": int,
})

PostAdminStatusIncidentsBody = TypedDict("PostAdminStatusIncidentsBody", {
    "title": str,
    "severity": NotRequired[Literal["notice", "minor", "major", "critical", "maintenance"]],
    "state": NotRequired[Literal["investigating", "identified", "monitoring", "resolved"]],
    "body": NotRequired[str],
    "components": NotRequired[List[Literal["api", "database", "webhooks", "background_jobs", "tracking", "payouts", "dashboard"]]],
    "startedAt": NotRequired[str],
})

PatchAdminStatusIncidentsIdBody = TypedDict("PatchAdminStatusIncidentsIdBody", {
    "title": NotRequired[str],
    "severity": NotRequired[Literal["notice", "minor", "major", "critical", "maintenance"]],
    "state": NotRequired[Literal["investigating", "identified", "monitoring", "resolved"]],
    "body": NotRequired[str],
    "components": NotRequired[List[Literal["api", "database", "webhooks", "background_jobs", "tracking", "payouts", "dashboard"]]],
})

PostAdminStatusIncidentsIdUpdatesBody = TypedDict("PostAdminStatusIncidentsIdUpdatesBody", {
    "body": str,
    "state": Literal["investigating", "identified", "monitoring", "resolved"],
})

PutOrgRetentionBody = TypedDict("PutOrgRetentionBody", {
    "clicks": NotRequired[Optional[int]],
    "visits": NotRequired[Optional[int]],
    "billingPayloads": NotRequired[Optional[int]],
    "webhookDeliveries": NotRequired[Optional[int]],
    "notifications": NotRequired[Optional[int]],
    "auditLog": NotRequired[Optional[int]],
})

PutOrgReferralParamsBody = TypedDict("PutOrgReferralParamsBody", {
    "params": List[str],
})

PostProgramsBodyPublicPage = TypedDict("PostProgramsBodyPublicPage", {
    "pitch": NotRequired[str],
    "autoApprove": NotRequired[bool],
})

PostProgramsBodyRiskPolicy = TypedDict("PostProgramsBodyRiskPolicy", {
    "holdBotScore": NotRequired[float],
    "holdRiskScore": NotRequired[float],
    "holdHighRiskLevel": NotRequired[bool],
    "holdDisposableEmail": NotRequired[bool],
    "holdVelocity": NotRequired[int],
    "holdUnverifiedEmail": NotRequired[bool],
    "holdSelfReferral": NotRequired[bool],
})

PostProgramsBodyWidget = TypedDict("PostProgramsBodyWidget", {
    "autoEnroll": NotRequired[bool],
    "destinationUrl": NotRequired[Optional[str]],
})

PostProgramsBodyMobileAppOption1IosOption1 = TypedDict("PostProgramsBodyMobileAppOption1IosOption1", {
    "teamId": str,
    "bundleId": str,
})

PostProgramsBodyMobileAppOption1AndroidOption1 = TypedDict("PostProgramsBodyMobileAppOption1AndroidOption1", {
    "packageName": str,
    "sha256CertFingerprints": List[str],
})

PostProgramsBodyMobileAppOption1 = TypedDict("PostProgramsBodyMobileAppOption1", {
    "ios": NotRequired[Optional["PostProgramsBodyMobileAppOption1IosOption1"]],
    "android": NotRequired[Optional["PostProgramsBodyMobileAppOption1AndroidOption1"]],
})

PostProgramsBody = TypedDict("PostProgramsBody", {
    "name": str,
    "slug": str,
    "attributionModel": NotRequired[Literal["last_click", "first_click", "position_based", "time_decay"]],
    "cookieWindowDays": NotRequired[int],
    "signupToConversionDays": NotRequired[int],
    "termsMd": NotRequired[str],
    "status": NotRequired[Literal["draft", "active", "paused", "archived"]],
    "publicHandle": NotRequired[Optional[str]],
    "publicPage": NotRequired["PostProgramsBodyPublicPage"],
    "probabilisticPolicy": NotRequired[Literal["auto", "review", "off"]],
    "selfReferralPolicy": NotRequired[Literal["review", "reject"]],
    "splitCommissions": NotRequired[bool],
    "utmTemplate": NotRequired[Dict[str, str]],
    "allowPaidSearch": NotRequired[bool],
    "challengeLinks": NotRequired[bool],
    "settlement": NotRequired[Literal["payout", "merchant_credit"]],
    "riskPolicy": NotRequired["PostProgramsBodyRiskPolicy"],
    "widget": NotRequired["PostProgramsBodyWidget"],
    "mobileApp": NotRequired[Optional["PostProgramsBodyMobileAppOption1"]],
})

PatchProgramsIdBodyPublicPage = TypedDict("PatchProgramsIdBodyPublicPage", {
    "pitch": NotRequired[str],
    "autoApprove": NotRequired[bool],
})

PatchProgramsIdBodyRiskPolicy = TypedDict("PatchProgramsIdBodyRiskPolicy", {
    "holdBotScore": NotRequired[float],
    "holdRiskScore": NotRequired[float],
    "holdHighRiskLevel": NotRequired[bool],
    "holdDisposableEmail": NotRequired[bool],
    "holdVelocity": NotRequired[int],
    "holdUnverifiedEmail": NotRequired[bool],
    "holdSelfReferral": NotRequired[bool],
})

PatchProgramsIdBodyWidget = TypedDict("PatchProgramsIdBodyWidget", {
    "autoEnroll": NotRequired[bool],
    "destinationUrl": NotRequired[Optional[str]],
})

PatchProgramsIdBodyMobileAppOption1IosOption1 = TypedDict("PatchProgramsIdBodyMobileAppOption1IosOption1", {
    "teamId": str,
    "bundleId": str,
})

PatchProgramsIdBodyMobileAppOption1AndroidOption1 = TypedDict("PatchProgramsIdBodyMobileAppOption1AndroidOption1", {
    "packageName": str,
    "sha256CertFingerprints": List[str],
})

PatchProgramsIdBodyMobileAppOption1 = TypedDict("PatchProgramsIdBodyMobileAppOption1", {
    "ios": NotRequired[Optional["PatchProgramsIdBodyMobileAppOption1IosOption1"]],
    "android": NotRequired[Optional["PatchProgramsIdBodyMobileAppOption1AndroidOption1"]],
})

PatchProgramsIdBody = TypedDict("PatchProgramsIdBody", {
    "name": NotRequired[str],
    "slug": NotRequired[str],
    "attributionModel": NotRequired[Literal["last_click", "first_click", "position_based", "time_decay"]],
    "cookieWindowDays": NotRequired[int],
    "signupToConversionDays": NotRequired[int],
    "termsMd": NotRequired[str],
    "status": NotRequired[Literal["draft", "active", "paused", "archived"]],
    "publicHandle": NotRequired[Optional[str]],
    "publicPage": NotRequired["PatchProgramsIdBodyPublicPage"],
    "probabilisticPolicy": NotRequired[Literal["auto", "review", "off"]],
    "selfReferralPolicy": NotRequired[Literal["review", "reject"]],
    "splitCommissions": NotRequired[bool],
    "utmTemplate": NotRequired[Dict[str, str]],
    "allowPaidSearch": NotRequired[bool],
    "challengeLinks": NotRequired[bool],
    "settlement": NotRequired[Literal["payout", "merchant_credit"]],
    "riskPolicy": NotRequired["PatchProgramsIdBodyRiskPolicy"],
    "widget": NotRequired["PatchProgramsIdBodyWidget"],
    "mobileApp": NotRequired[Optional["PatchProgramsIdBodyMobileAppOption1"]],
})

PostProgramsIdEnrollmentsBody = TypedDict("PostProgramsIdEnrollmentsBody", {
    "partnerId": str,
})

PostPartnersBody = TypedDict("PostPartnersBody", {
    "email": str,
    "displayName": NotRequired[str],
    "tags": NotRequired[List[str]],
    "notes": NotRequired[str],
    "externalRef": NotRequired[str],
    "upsert": NotRequired[bool],
})

PatchPartnersIdBody = TypedDict("PatchPartnersIdBody", {
    "displayName": NotRequired[str],
    "status": NotRequired[Literal["active", "suspended", "banned", "archived"]],
    "tags": NotRequired[List[str]],
    "notes": NotRequired[str],
    "externalRef": NotRequired[Optional[str]],
})

PostApiKeysBody = TypedDict("PostApiKeysBody", {
    "name": str,
    "scopes": NotRequired[List[Literal["admin", "full", "read", "programs:read", "programs:write", "partners:read", "partners:write", "links:read", "links:write", "events:read", "events:write", "referrals:read", "referrals:write", "commissions:read", "commissions:write", "payouts:read", "payouts:write", "billing:read", "billing:write", "webhooks:read", "webhooks:write", "analytics:read", "analytics:write", "fraud:read", "fraud:write", "privacy:read", "privacy:write", "team:read", "team:write", "org:read", "org:write", "integrations:read", "integrations:write", "growth:read", "growth:write", "audit:read", "audit:write"]]],
    "publishable": NotRequired[bool],
    "allowedOrigins": NotRequired[List[str]],
    "apiVersion": NotRequired[str],
    "mode": NotRequired[Literal["live", "test", "both"]],
    "owner": NotRequired[str],
    "expiresInDays": NotRequired[int],
})

PatchApiKeysIdBody = TypedDict("PatchApiKeysIdBody", {
    "apiVersion": NotRequired[str],
    "owner": NotRequired[Optional[str]],
    "expiresInDays": NotRequired[Optional[int]],
})

PostTestClockAdvanceBody = TypedDict("PostTestClockAdvanceBody", {
    "seconds": int,
})

PostCliDeviceCodesBody = TypedDict("PostCliDeviceCodesBody", {
    "clientName": NotRequired[str],
})

PostCliDeviceCodesTokenBody = TypedDict("PostCliDeviceCodesTokenBody", {
    "deviceCode": str,
})

PostCliDeviceCodesUserCodeApproveBody = TypedDict("PostCliDeviceCodesUserCodeApproveBody", {
    "access": NotRequired[Literal["full", "read", "cli"]],
    "name": NotRequired[str],
})

PostCliListenersBody = TypedDict("PostCliListenersBody", {
    "topics": NotRequired[List[str]],
    "forwardTo": NotRequired[str],
})

PostCliTriggerBody = TypedDict("PostCliTriggerBody", {
    "topic": str,
    "data": NotRequired[Dict[str, Any]],
})

PostLinksBody = TypedDict("PostLinksBody", {
    "programId": str,
    "partnerId": str,
    "code": NotRequired[str],
    "destinationUrl": str,
})

PostCouponsBody = TypedDict("PostCouponsBody", {
    "programId": str,
    "partnerId": str,
    "code": str,
})

PostWidgetTokensBody = TypedDict("PostWidgetTokensBody", {
    "programId": str,
    "customerRef": NotRequired[str],
    "partnerExternalRef": NotRequired[str],
    "email": NotRequired[str],
    "displayName": NotRequired[str],
    "ttlSeconds": NotRequired[int],
})

PostReferralsAssociateBodyConsent = TypedDict("PostReferralsAssociateBodyConsent", {
    "provider": str,
    "state": Literal["granted", "denied", "unknown"],
    "at": NotRequired[str],
    "stamp": NotRequired[str],
    "tcString": NotRequired[str],
    "gppString": NotRequired[str],
    "purposes": NotRequired[List[str]],
})

PostReferralsAssociateBody = TypedDict("PostReferralsAssociateBody", {
    "programId": str,
    "customerRef": str,
    "anonId": NotRequired[str],
    "referralToken": NotRequired[str],
    "couponCode": NotRequired[str],
    "emailHash": NotRequired[str],
    "ip": NotRequired[str],
    "ua": NotRequired[str],
    "idempotencyKey": NotRequired[str],
    "occurredAt": NotRequired[str],
    "emailDomain": NotRequired[str],
    "consent": NotRequired["PostReferralsAssociateBodyConsent"],
})

PatchReferralsIdBody = TypedDict("PatchReferralsIdBody", {
    "status": Literal["paused", "active"],
})

PostReferralsIdReassignBody = TypedDict("PostReferralsIdReassignBody", {
    "partnerId": str,
})

PostAttributionReplayBody = TypedDict("PostAttributionReplayBody", {
    "programId": str,
})

PostTrackEventsBodyOption1 = TypedDict("PostTrackEventsBodyOption1", {
    "programId": str,
    "partnerId": str,
    "linkId": NotRequired[str],
    "url": NotRequired[str],
    "anonId": NotRequired[str],
    "ip": NotRequired[str],
    "ua": NotRequired[str],
    "type": Literal["click"],
})

PostTrackEventsBodyOption2 = TypedDict("PostTrackEventsBodyOption2", {
    "programId": str,
    "partnerId": str,
    "linkId": NotRequired[str],
    "url": NotRequired[str],
    "anonId": NotRequired[str],
    "ip": NotRequired[str],
    "ua": NotRequired[str],
    "type": Literal["custom"],
})

PostTrackEventsBodyOption3 = TypedDict("PostTrackEventsBodyOption3", {
    "type": Literal["event"],
    "programId": str,
    "customerRef": str,
    "event": str,
    "occurredAt": NotRequired[str],
    "idempotencyKey": NotRequired[str],
})

PostCommissionRulesBodyConfigBaseOption1 = TypedDict("PostCommissionRulesBodyConfigBaseOption1", {
    "kind": Literal["percent"],
    "bps": int,
})

PostCommissionRulesBodyConfigBaseOption2 = TypedDict("PostCommissionRulesBodyConfigBaseOption2", {
    "kind": Literal["fixed"],
    "amountMinor": int,
    "currency": str,
})

PostCommissionRulesBodyConfigRecurringOption1 = TypedDict("PostCommissionRulesBodyConfigRecurringOption1", {
    "type": Literal["one_time"],
})

PostCommissionRulesBodyConfigRecurringOption2 = TypedDict("PostCommissionRulesBodyConfigRecurringOption2", {
    "type": Literal["lifetime"],
})

PostCommissionRulesBodyConfigRecurringOption3 = TypedDict("PostCommissionRulesBodyConfigRecurringOption3", {
    "type": Literal["months"],
    "months": int,
})

PostCommissionRulesBodyConfigConditionsMetadataItem = TypedDict("PostCommissionRulesBodyConfigConditionsMetadataItem", {
    "key": str,
    "equals": NotRequired[Union[str, float, bool]],
    "in": NotRequired[List[Union[str, float, bool]]],
})

PostCommissionRulesBodyConfigConditions = TypedDict("PostCommissionRulesBodyConfigConditions", {
    "countries": NotRequired[List[str]],
    "excludeCountries": NotRequired[List[str]],
    "metadata": NotRequired[List["PostCommissionRulesBodyConfigConditionsMetadataItem"]],
})

PostCommissionRulesBodyConfigOverridesItemMatchMetadataItem = TypedDict("PostCommissionRulesBodyConfigOverridesItemMatchMetadataItem", {
    "key": str,
    "equals": NotRequired[Union[str, float, bool]],
    "in": NotRequired[List[Union[str, float, bool]]],
})

PostCommissionRulesBodyConfigOverridesItemMatch = TypedDict("PostCommissionRulesBodyConfigOverridesItemMatch", {
    "partnerId": NotRequired[str],
    "linkId": NotRequired[str],
    "productRef": NotRequired[str],
    "countries": NotRequired[List[str]],
    "metadata": NotRequired[List["PostCommissionRulesBodyConfigOverridesItemMatchMetadataItem"]],
})

PostCommissionRulesBodyConfigOverridesItemBaseOption1 = TypedDict("PostCommissionRulesBodyConfigOverridesItemBaseOption1", {
    "kind": Literal["percent"],
    "bps": int,
})

PostCommissionRulesBodyConfigOverridesItemBaseOption2 = TypedDict("PostCommissionRulesBodyConfigOverridesItemBaseOption2", {
    "kind": Literal["fixed"],
    "amountMinor": int,
    "currency": str,
})

PostCommissionRulesBodyConfigOverridesItem = TypedDict("PostCommissionRulesBodyConfigOverridesItem", {
    "match": "PostCommissionRulesBodyConfigOverridesItemMatch",
    "base": Union["PostCommissionRulesBodyConfigOverridesItemBaseOption1", "PostCommissionRulesBodyConfigOverridesItemBaseOption2"],
})

PostCommissionRulesBodyConfigTiersItem = TypedDict("PostCommissionRulesBodyConfigTiersItem", {
    "minCustomers": int,
    "bps": int,
})

PostCommissionRulesBodyConfigBountiesItem = TypedDict("PostCommissionRulesBodyConfigBountiesItem", {
    "event": str,
    "amountMinor": int,
    "currency": str,
})

PostCommissionRulesBodyConfigSubAffiliate = TypedDict("PostCommissionRulesBodyConfigSubAffiliate", {
    "levels": int,
    "ratesBps": List[int],
})

PostCommissionRulesBodyConfigNewVsExpansion = TypedDict("PostCommissionRulesBodyConfigNewVsExpansion", {
    "newBps": int,
    "expansionBps": int,
})

PostCommissionRulesBodyConfig = TypedDict("PostCommissionRulesBodyConfig", {
    "base": Union["PostCommissionRulesBodyConfigBaseOption1", "PostCommissionRulesBodyConfigBaseOption2"],
    "appliesTo": NotRequired[Literal["gross", "net_of_tax", "net_of_fees"]],
    "recurring": NotRequired[Union["PostCommissionRulesBodyConfigRecurringOption1", "PostCommissionRulesBodyConfigRecurringOption2", "PostCommissionRulesBodyConfigRecurringOption3"]],
    "holdDays": NotRequired[int],
    "rounding": NotRequired[Literal["half_even", "floor"]],
    "conditions": NotRequired["PostCommissionRulesBodyConfigConditions"],
    "overrides": NotRequired[List["PostCommissionRulesBodyConfigOverridesItem"]],
    "tiers": NotRequired[List["PostCommissionRulesBodyConfigTiersItem"]],
    "bounties": NotRequired[List["PostCommissionRulesBodyConfigBountiesItem"]],
    "subAffiliate": NotRequired["PostCommissionRulesBodyConfigSubAffiliate"],
    "newVsExpansion": NotRequired["PostCommissionRulesBodyConfigNewVsExpansion"],
})

PostCommissionRulesBody = TypedDict("PostCommissionRulesBody", {
    "programId": str,
    "config": "PostCommissionRulesBodyConfig",
})

PostCommissionsIdAdjustBody = TypedDict("PostCommissionsIdAdjustBody", {
    "amountMinor": int,
    "memo": str,
    "allowNegative": NotRequired[bool],
})

PostCommissionsIdSettleBody = TypedDict("PostCommissionsIdSettleBody", {
    "method": NotRequired[Literal["store_credit"]],
    "reference": str,
    "memo": NotRequired[str],
})

PostBillingConnectionsBodyFilter = TypedDict("PostBillingConnectionsBodyFilter", {
    "metadata": NotRequired[Dict[str, str]],
    "productIds": NotRequired[List[str]],
    "priceIds": NotRequired[List[str]],
    "skus": NotRequired[List[str]],
})

PostBillingConnectionsBody = TypedDict("PostBillingConnectionsBody", {
    "provider": Literal["stripe", "paddle", "lemonsqueezy", "polar", "chargebee", "shopify", "generic", "recurly", "braintree", "woocommerce", "bigcommerce"],
    "name": NotRequired[str],
    "webhookSecret": NotRequired[str],
    "filter": NotRequired["PostBillingConnectionsBodyFilter"],
})

PutBillingConnectionsIdSecretBody = TypedDict("PutBillingConnectionsIdSecretBody", {
    "webhookSecret": str,
})

PutBillingConnectionsIdCredentialsBody = TypedDict("PutBillingConnectionsIdCredentialsBody", {
    "apiKey": NotRequired[str],
    "apiToken": NotRequired[str],
    "storeHash": NotRequired[str],
    "region": NotRequired[Literal["us", "eu"]],
})

PatchBillingConnectionsIdBodyFilterOption1 = TypedDict("PatchBillingConnectionsIdBodyFilterOption1", {
    "metadata": NotRequired[Dict[str, str]],
    "productIds": NotRequired[List[str]],
    "priceIds": NotRequired[List[str]],
    "skus": NotRequired[List[str]],
})

PatchBillingConnectionsIdBody = TypedDict("PatchBillingConnectionsIdBody", {
    "status": NotRequired[Literal["active", "paused"]],
    "name": NotRequired[str],
    "filter": NotRequired[Optional["PatchBillingConnectionsIdBodyFilterOption1"]],
})

PutBillingConnectionsIdValueMappingBody = TypedDict("PutBillingConnectionsIdValueMappingBody", {
    "cash": NotRequired[str],
    "creditApplied": NotRequired[str],
    "discount": NotRequired[str],
    "cost": NotRequired[str],
    "productRef": NotRequired[str],
    "unit": Literal["minor", "major"],
})

PostBillingConnectionsIdValueMappingPreviewBodyMapping = TypedDict("PostBillingConnectionsIdValueMappingPreviewBodyMapping", {
    "cash": NotRequired[str],
    "creditApplied": NotRequired[str],
    "discount": NotRequired[str],
    "cost": NotRequired[str],
    "productRef": NotRequired[str],
    "unit": Literal["minor", "major"],
})

PostBillingConnectionsIdValueMappingPreviewBody = TypedDict("PostBillingConnectionsIdValueMappingPreviewBody", {
    "payload": Any,
    "currency": NotRequired[str],
    "mapping": NotRequired["PostBillingConnectionsIdValueMappingPreviewBodyMapping"],
})

PostBillingInternalCustomersBody = TypedDict("PostBillingInternalCustomersBody", {
    "customerRef": str,
    "note": NotRequired[str],
})

PutPartnersIdPayoutProfileBody = TypedDict("PutPartnersIdPayoutProfileBody", {
    "method": Literal["paypal", "wise", "stripe_connect", "ach", "crypto", "payoneer", "tremendous", "csv"],
    "details": NotRequired[Dict[str, Any]],
    "payoutCurrency": NotRequired[str],
    "minThresholdMinor": NotRequired[int],
})

PatchPartnersIdPayoutProfileBody = TypedDict("PatchPartnersIdPayoutProfileBody", {
    "minThresholdMinor": int,
})

PostPartnersIdTaxFormBody = TypedDict("PostPartnersIdTaxFormBody", {
    "type": Literal["w9", "w8ben", "w8bene"],
    "data": Any,
})

PostFxRatesBody = TypedDict("PostFxRatesBody", {
    "base": str,
    "quote": str,
    "rate": Union[str, float],
    "effectiveAt": NotRequired[str],
})

PutOrgFxFeedBody = TypedDict("PutOrgFxFeedBody", {
    "enabled": bool,
})

PostFxRatesClearOverrideBody = TypedDict("PostFxRatesClearOverrideBody", {
    "base": str,
    "quote": str,
})

PutPayoutConnectionsProviderBodyOption1 = TypedDict("PutPayoutConnectionsProviderBodyOption1", {
    "clientId": str,
    "secret": str,
    "env": NotRequired[Literal["sandbox", "live"]],
})

PutPayoutConnectionsProviderBodyOption2 = TypedDict("PutPayoutConnectionsProviderBodyOption2", {
    "secretKey": str,
    "env": NotRequired[Literal["sandbox", "live"]],
})

PutPayoutConnectionsProviderBodyOption3 = TypedDict("PutPayoutConnectionsProviderBodyOption3", {
    "apiKey": str,
    "walletId": str,
    "defaultChain": NotRequired[str],
    "env": NotRequired[Literal["sandbox", "live"]],
})

PutPayoutConnectionsProviderBodyOption4 = TypedDict("PutPayoutConnectionsProviderBodyOption4", {
    "apiToken": str,
    "profileId": str,
    "env": NotRequired[Literal["sandbox", "live"]],
})

PutPayoutConnectionsProviderBodyOption5 = TypedDict("PutPayoutConnectionsProviderBodyOption5", {
    "clientId": str,
    "secret": str,
    "programId": str,
    "env": NotRequired[Literal["sandbox", "live"]],
})

PutPayoutConnectionsProviderBodyOption6 = TypedDict("PutPayoutConnectionsProviderBodyOption6", {
    "apiKey": str,
    "fundingSourceId": str,
    "campaignId": NotRequired[str],
    "env": NotRequired[Literal["sandbox", "live"]],
})

PostFraudInvalidTrafficScanBody = TypedDict("PostFraudInvalidTrafficScanBody", {
    "windowHours": NotRequired[int],
})

PostFraudCasesIdResolveBody = TypedDict("PostFraudCasesIdResolveBody", {
    "action": Literal["dismiss", "void_referral", "suspend_partner", "ban_partner"],
})

PutProfitabilitySettingsBody = TypedDict("PutProfitabilitySettingsBody", {
    "reportingCurrency": NotRequired[str],
    "defaultMarginBps": NotRequired[Optional[int]],
    "creditCostModel": NotRequired[Literal["face", "margin", "fixed_ratio"]],
    "creditCostRatioBps": NotRequired[int],
    "inference": NotRequired[Literal["fifo_next_payments", "report_only", "on_grant"]],
    "creditDraw": NotRequired[Literal["grants_first", "pro_rata"]],
    "windowDays": NotRequired[int],
    "churnWindowDays": NotRequired[int],
    "countReferrerSpend": NotRequired[bool],
    "costToServeMinorPerMonth": NotRequired[int],
    "taxFeesReduceProfit": NotRequired[bool],
    "valuePatternWeight": NotRequired[float],
    "targetRoiBps": NotRequired[Optional[int]],
    "programId": NotRequired[str],
})

PutProfitabilityProductsProductRefBody = TypedDict("PutProfitabilityProductsProductRefBody", {
    "marginBps": NotRequired[int],
    "unitCostMinor": NotRequired[int],
    "currency": NotRequired[str],
})

PostRoiPatternsPatternReviewBody = TypedDict("PostRoiPatternsPatternReviewBody", {
    "customerRef": NotRequired[str],
    "partnerId": NotRequired[str],
    "programId": NotRequired[str],
})

PostValueEventsBodyEventsItem = TypedDict("PostValueEventsBodyEventsItem", {
    "kind": Literal["payment", "refund", "credit_granted", "credit_redeemed", "credit_expired", "credit_revoked", "cost", "adjustment"],
    "customerRef": NotRequired[str],
    "partnerId": NotRequired[str],
    "partnerExternalRef": NotRequired[str],
    "creditGrantId": NotRequired[str],
    "referralId": NotRequired[str],
    "programId": NotRequired[str],
    "productRef": NotRequired[str],
    "currency": str,
    "cashMinor": NotRequired[int],
    "creditAppliedMinor": NotRequired[int],
    "discountMinor": NotRequired[int],
    "taxMinor": NotRequired[int],
    "feesMinor": NotRequired[int],
    "costMinor": NotRequired[int],
    "faceMinor": NotRequired[int],
    "externalId": str,
    "invoiceRef": NotRequired[str],
    "provider": NotRequired[str],
    "occurredAt": str,
    "role": NotRequired[Literal["referee", "referrer"]],
    "metadata": NotRequired[Dict[str, Any]],
})

# Up to 500 value events; each is validated and recorded on its own, so one bad event is reported in `errors` and the rest are recorded.
PostValueEventsBody = TypedDict("PostValueEventsBody", {
    "events": List["PostValueEventsBodyEventsItem"],
})

# CSV text (up to 10000 rows / 5 MB) plus a column-to-field mapping. "kind" applies to every row unless a column maps to kind. Up to 500 rows are recorded before the response; a larger file answers 202 with a jobId to poll at GET /v1/value/import/{jobId}. A dry run is always immediate.
PostValueImportBody = TypedDict("PostValueImportBody", {
    "csv": str,
    "mapping": Dict[str, Literal["kind", "customerRef", "partnerId", "partnerExternalRef", "creditGrantId", "referralId", "programId", "productRef", "currency", "externalId", "invoiceRef", "provider", "occurredAt", "role", "cashMinor", "creditAppliedMinor", "discountMinor", "taxMinor", "feesMinor", "costMinor", "faceMinor", "cashMajor", "creditAppliedMajor", "discountMajor", "taxMajor", "feesMajor", "costMajor", "faceMajor"]],
    "kind": NotRequired[Literal["payment", "refund", "credit_granted", "credit_redeemed", "credit_expired", "credit_revoked", "cost", "adjustment"]],
    "dryRun": NotRequired[bool],
    "defaultCurrency": NotRequired[str],
})

PostPartnerKycSubmitBody = TypedDict("PostPartnerKycSubmitBody", {
    "legalName": str,
    "country": str,
    "dateOfBirth": NotRequired[str],
    "documentRef": NotRequired[str],
})

PostPartnerLinksBody = TypedDict("PostPartnerLinksBody", {
    "orgId": str,
    "programId": str,
    "destinationUrl": str,
    "assetId": NotRequired[str],
    "code": NotRequired[str],
})

PostPartnerDisputesBody = TypedDict("PostPartnerDisputesBody", {
    "orgId": str,
    "referralId": NotRequired[str],
    "kind": Literal["missing_attribution", "unpaid_commission"],
    "detail": str,
})

PutPartnerOrgsOrgIdPayoutProfileBody = TypedDict("PutPartnerOrgsOrgIdPayoutProfileBody", {
    "method": Literal["paypal", "wise", "stripe_connect", "ach", "crypto", "payoneer", "tremendous", "csv"],
    "details": NotRequired[Dict[str, Any]],
    "payoutCurrency": NotRequired[str],
})

PostPartnerOrgsOrgIdTaxFormBody = TypedDict("PostPartnerOrgsOrgIdTaxFormBody", {
    "type": Literal["w9", "w8ben", "w8bene"],
    "data": Any,
})

PostWebhookEndpointsBody = TypedDict("PostWebhookEndpointsBody", {
    "url": str,
    "topics": NotRequired[List[str]],
    "legacySignature": NotRequired[bool],
    "programIds": NotRequired[Optional[List[str]]],
    "alertContacts": NotRequired[List[str]],
})

PatchWebhookEndpointsIdBody = TypedDict("PatchWebhookEndpointsIdBody", {
    "status": NotRequired[Literal["active", "paused"]],
    "url": NotRequired[str],
    "topics": NotRequired[List[str]],
    "legacySignature": NotRequired[bool],
    "programIds": NotRequired[Optional[List[str]]],
    "alertContacts": NotRequired[List[str]],
})

PostSandboxSimulateBody = TypedDict("PostSandboxSimulateBody", {
    "programId": str,
    "partnerId": str,
    "scenario": NotRequired[Literal["subscription", "refund", "churn"]],
    "priceMinor": NotRequired[int],
    "months": NotRequired[int],
})

PostImportProviderBody = TypedDict("PostImportProviderBody", {
    "csv": str,
})

PutBrandingBody = TypedDict("PutBrandingBody", {
    "logoUrl": NotRequired[str],
    "theme": NotRequired[Dict[str, str]],
    "emailFrom": NotRequired[str],
})

PostBrandingLinkDomainBody = TypedDict("PostBrandingLinkDomainBody", {
    "domain": str,
})

PostBrandingDomainBody = TypedDict("PostBrandingDomainBody", {
    "domain": str,
})

PostEmbedTokensBody = TypedDict("PostEmbedTokensBody", {
    "partnerEmail": str,
})

PostDiscoverySearchBody = TypedDict("PostDiscoverySearchBody", {
    "keywords": List[str],
    "category": NotRequired[str],
})

PostDiscoveryCorpusBodyEntriesItem = TypedDict("PostDiscoveryCorpusBodyEntriesItem", {
    "name": str,
    "url": str,
    "channel": NotRequired[Literal["youtube", "blog", "newsletter", "podcast", "x"]],
    "audienceSize": NotRequired[int],
    "language": NotRequired[str],
    "categories": NotRequired[List[str]],
    "keywords": NotRequired[List[str]],
    "contactEmail": NotRequired[str],
    "html": NotRequired[str],
    "evidenceSnippet": NotRequired[str],
    "evidenceSource": NotRequired[str],
})

PostDiscoveryCorpusBody = TypedDict("PostDiscoveryCorpusBody", {
    "keywords": NotRequired[List[str]],
    "entries": List["PostDiscoveryCorpusBodyEntriesItem"],
})

PostOutreachDraftBody = TypedDict("PostOutreachDraftBody", {
    "prospectId": str,
    "programName": NotRequired[str],
})

PutMarketplaceListingBody = TypedDict("PutMarketplaceListingBody", {
    "programId": str,
    "visibility": NotRequired[Literal["public", "unlisted"]],
    "category": NotRequired[str],
    "headline": NotRequired[str],
    "description": NotRequired[str],
    "sponsored": NotRequired[bool],
})

PostDisputesIdResolveBody = TypedDict("PostDisputesIdResolveBody", {
    "resolution": str,
})

PutPartnerProfileBodyChannelsItem = TypedDict("PutPartnerProfileBodyChannelsItem", {
    "type": Literal["youtube", "blog", "newsletter", "podcast", "x", "tiktok", "instagram", "other"],
    "handle": NotRequired[str],
    "url": NotRequired[str],
    "audience": NotRequired[int],
})

PutPartnerProfileBodyAudienceCountriesItem = TypedDict("PutPartnerProfileBodyAudienceCountriesItem", {
    "code": str,
    "pct": float,
})

PutPartnerProfileBodyAudience = TypedDict("PutPartnerProfileBodyAudience", {
    "countries": NotRequired[List["PutPartnerProfileBodyAudienceCountriesItem"]],
    "age": NotRequired[Dict[str, float]],
    "gender": NotRequired[Dict[str, float]],
})

PutPartnerProfileBody = TypedDict("PutPartnerProfileBody", {
    "published": NotRequired[bool],
    "headline": NotRequired[str],
    "bio": NotRequired[str],
    "categories": NotRequired[List[str]],
    "languages": NotRequired[List[str]],
    "country": NotRequired[str],
    "channels": NotRequired[List["PutPartnerProfileBodyChannelsItem"]],
    "website": NotRequired[str],
    "acceptsInvites": NotRequired[bool],
    "audience": NotRequired["PutPartnerProfileBodyAudience"],
    "engagementBps": NotRequired[int],
})

PostCreatorsAccountIdInviteBody = TypedDict("PostCreatorsAccountIdInviteBody", {
    "programId": str,
    "message": NotRequired[str],
})

PostBillingCheckoutBody = TypedDict("PostBillingCheckoutBody", {
    "plan": Literal["growth", "pro", "scale"],
})

PostBillingActivateBody = TypedDict("PostBillingActivateBody", {
    "plan": Literal["free", "growth", "pro", "scale", "starter"],
})

PutProgramsIdRefereeRewardBody = TypedDict("PutProgramsIdRefereeRewardBody", {
    "enabled": NotRequired[bool],
    "kind": NotRequired[Literal["store_credit", "coupon", "gift_card"]],
    "amountMinor": NotRequired[int],
    "bps": NotRequired[int],
    "capMinor": NotRequired[int],
    "on": NotRequired[Literal["first_commission", "first_payment"]],
    "rounding": NotRequired[Literal["half_even", "floor"]],
    "currency": NotRequired[str],
})

PostRewardsBody = TypedDict("PostRewardsBody", {
    "partnerId": NotRequired[str],
    "partnerExternalRef": NotRequired[str],
    "reason": str,
    "amountMinor": NotRequired[int],
    "currency": NotRequired[str],
    "ruleKey": NotRequired[str],
    "event": NotRequired[str],
    "programId": NotRequired[str],
    "idempotencyKey": str,
})

PostRewardsRedeemByCodeBody = TypedDict("PostRewardsRedeemByCodeBody", {
    "amountMinor": NotRequired[int],
    "billingEventId": NotRequired[str],
    "invoiceRef": NotRequired[str],
    "externalId": NotRequired[str],
    "occurredAt": NotRequired[Any],
    "code": str,
})

PostRewardsIdRedeemBody = TypedDict("PostRewardsIdRedeemBody", {
    "amountMinor": NotRequired[int],
    "billingEventId": NotRequired[str],
    "invoiceRef": NotRequired[str],
    "externalId": NotRequired[str],
    "occurredAt": NotRequired[Any],
})

PutRewardsRulesKeyBody = TypedDict("PutRewardsRulesKeyBody", {
    "event": NotRequired[Optional[str]],
    "programId": NotRequired[Optional[str]],
    "amountMinor": int,
    "currency": NotRequired[str],
    "reason": str,
    "enabled": NotRequired[bool],
})

PostProgramsIdGroupsBodyBaseOption1Option1 = TypedDict("PostProgramsIdGroupsBodyBaseOption1Option1", {
    "kind": Literal["percent"],
    "bps": int,
})

PostProgramsIdGroupsBodyBaseOption1Option2 = TypedDict("PostProgramsIdGroupsBodyBaseOption1Option2", {
    "kind": Literal["fixed"],
    "amountMinor": int,
    "currency": str,
})

PostProgramsIdGroupsBody = TypedDict("PostProgramsIdGroupsBody", {
    "name": str,
    "base": NotRequired[Optional[Union["PostProgramsIdGroupsBodyBaseOption1Option1", "PostProgramsIdGroupsBodyBaseOption1Option2"]]],
    "holdDays": NotRequired[Optional[int]],
    "minThresholdMinor": NotRequired[Optional[int]],
    "payoutCurrency": NotRequired[Optional[str]],
    "onboardingMessage": NotRequired[Optional[str]],
    "onboardingChecklist": NotRequired[List[str]],
})

PatchPartnerGroupsIdBodyBaseOption1Option1 = TypedDict("PatchPartnerGroupsIdBodyBaseOption1Option1", {
    "kind": Literal["percent"],
    "bps": int,
})

PatchPartnerGroupsIdBodyBaseOption1Option2 = TypedDict("PatchPartnerGroupsIdBodyBaseOption1Option2", {
    "kind": Literal["fixed"],
    "amountMinor": int,
    "currency": str,
})

PatchPartnerGroupsIdBody = TypedDict("PatchPartnerGroupsIdBody", {
    "name": NotRequired[str],
    "base": NotRequired[Optional[Union["PatchPartnerGroupsIdBodyBaseOption1Option1", "PatchPartnerGroupsIdBodyBaseOption1Option2"]]],
    "holdDays": NotRequired[Optional[int]],
    "minThresholdMinor": NotRequired[Optional[int]],
    "payoutCurrency": NotRequired[Optional[str]],
    "onboardingMessage": NotRequired[Optional[str]],
    "onboardingChecklist": NotRequired[List[str]],
    "archived": NotRequired[bool],
})

PutProgramsIdPartnersPartnerIdGroupBody = TypedDict("PutProgramsIdPartnersPartnerIdGroupBody", {
    "groupId": Optional[str],
})

PostProgramsIdPromotionsBodyEffectOption1BaseOption1 = TypedDict("PostProgramsIdPromotionsBodyEffectOption1BaseOption1", {
    "kind": Literal["percent"],
    "bps": int,
})

PostProgramsIdPromotionsBodyEffectOption1BaseOption2 = TypedDict("PostProgramsIdPromotionsBodyEffectOption1BaseOption2", {
    "kind": Literal["fixed"],
    "amountMinor": int,
    "currency": str,
})

PostProgramsIdPromotionsBodyEffectOption1 = TypedDict("PostProgramsIdPromotionsBodyEffectOption1", {
    "kind": Literal["replace"],
    "base": Union["PostProgramsIdPromotionsBodyEffectOption1BaseOption1", "PostProgramsIdPromotionsBodyEffectOption1BaseOption2"],
})

PostProgramsIdPromotionsBodyEffectOption2 = TypedDict("PostProgramsIdPromotionsBodyEffectOption2", {
    "kind": Literal["boost"],
    "bps": int,
})

PostProgramsIdPromotionsBody = TypedDict("PostProgramsIdPromotionsBody", {
    "name": str,
    "groupId": NotRequired[Optional[str]],
    "effect": Union["PostProgramsIdPromotionsBodyEffectOption1", "PostProgramsIdPromotionsBodyEffectOption2"],
    "startsAt": str,
    "endsAt": str,
})

PostContractsBodyCompensationOption1 = TypedDict("PostContractsBodyCompensationOption1", {
    "kind": Literal["percent"],
    "bps": int,
})

PostContractsBodyCompensationOption2 = TypedDict("PostContractsBodyCompensationOption2", {
    "kind": Literal["fixed"],
    "amountMinor": int,
    "currency": str,
})

PostContractsBody = TypedDict("PostContractsBody", {
    "programId": str,
    "partnerId": str,
    "title": NotRequired[str],
    "termsMd": NotRequired[str],
    "compensation": Union["PostContractsBodyCompensationOption1", "PostContractsBodyCompensationOption2"],
    "send": NotRequired[bool],
})

PutProgramsIdIncrementalityBody = TypedDict("PutProgramsIdIncrementalityBody", {
    "holdoutBps": int,
})

PutProgramsIdAutopricingBody = TypedDict("PutProgramsIdAutopricingBody", {
    "enabled": NotRequired[bool],
    "targetRoas": NotRequired[float],
    "minBps": NotRequired[int],
    "maxBps": NotRequired[int],
    "objective": NotRequired[Literal["roas", "roi"]],
    "targetRoi": NotRequired[float],
})

PostProgramsIdAutopriceRunBody = TypedDict("PostProgramsIdAutopriceRunBody", {
    "objective": NotRequired[Literal["roas", "roi"]],
})

PostPassportVerifyBody = TypedDict("PostPassportVerifyBody", {
    "passport": Any,
})

PostPartnerAdvanceAcceptBody = TypedDict("PostPartnerAdvanceAcceptBody", {
    "amountMinor": int,
})

PutNetworkSettingsBody = TypedDict("PutNetworkSettingsBody", {
    "enabled": bool,
})

PutProgramsIdNegotiationPolicyBody = TypedDict("PutProgramsIdNegotiationPolicyBody", {
    "enabled": NotRequired[bool],
    "minBps": int,
    "maxBps": int,
    "autoAcceptMaxBps": int,
})

PostAdminOrgsIdSuspendBody = TypedDict("PostAdminOrgsIdSuspendBody", {
    "reason": NotRequired[str],
})

PostAdminOrgsIdPlanBody = TypedDict("PostAdminOrgsIdPlanBody", {
    "plan": Literal["free", "growth", "pro", "scale", "starter"],
})

PostAssetsBody = TypedDict("PostAssetsBody", {
    "programId": str,
    "kind": Literal["banner", "copy", "video", "logo"],
    "title": str,
    "content": NotRequired[str],
    "dimensions": NotRequired[str],
    "groupId": NotRequired[Optional[str]],
})

PostPartnerDealsBody = TypedDict("PostPartnerDealsBody", {
    "orgId": str,
    "programId": str,
    "company": str,
    "contactEmail": str,
    "valueMinor": NotRequired[int],
    "currency": NotRequired[str],
    "notes": NotRequired[str],
})

PostDealsIdApproveBody = TypedDict("PostDealsIdApproveBody", {
    "protectionDays": NotRequired[int],
})

PostDealsIdWonBody = TypedDict("PostDealsIdWonBody", {
    "customerRef": str,
})

PutPartnerOrgsOrgIdPostbackBody = TypedDict("PutPartnerOrgsOrgIdPostbackBody", {
    "url": str,
})

PostPrivacyForgetBody = TypedDict("PostPrivacyForgetBody", {
    "email": NotRequired[str],
    "customerRef": NotRequired[str],
    "partnerId": NotRequired[str],
})

PostPrivacyLookupBody = TypedDict("PostPrivacyLookupBody", {
    "email": str,
})

PostPrivacyRequestsBodySubject = TypedDict("PostPrivacyRequestsBodySubject", {
    "email": NotRequired[str],
    "customerRef": NotRequired[str],
    "partnerId": NotRequired[str],
})

PostPrivacyRequestsBody = TypedDict("PostPrivacyRequestsBody", {
    "subject": "PostPrivacyRequestsBodySubject",
    "type": Literal["access", "erasure"],
})

PutEmailSettingsBody = TypedDict("PutEmailSettingsBody", {
    "provider": NotRequired[Optional[Literal["resend", "brevo", "postmark"]]],
    "apiKey": NotRequired[Optional[str]],
    "fromAddress": NotRequired[Optional[str]],
    "fromName": NotRequired[Optional[str]],
    "replyTo": NotRequired[Optional[str]],
    "defaultLocale": NotRequired[Literal["en", "es", "de", "fr", "pt", "it", "nl", "sv", "ja", "zh"]],
    "logoUrl": NotRequired[Optional[str]],
    "primaryColor": NotRequired[Optional[str]],
})

PutEmailTemplatesEventLocaleBody = TypedDict("PutEmailTemplatesEventLocaleBody", {
    "subject": str,
    "text": str,
    "html": NotRequired[Optional[str]],
})

PostEmailPreviewBodyDraft = TypedDict("PostEmailPreviewBodyDraft", {
    "subject": str,
    "text": str,
    "html": NotRequired[Optional[str]],
})

PostEmailPreviewBody = TypedDict("PostEmailPreviewBody", {
    "event": Literal["payout_sent", "payout_failed", "invitation_received", "partner_approved", "contract_sent", "webhook_endpoint_disabled", "webhook_endpoint_failing", "tax_document_ready"],
    "locale": Literal["en", "es", "de", "fr", "pt", "it", "nl", "sv", "ja", "zh"],
    "draft": NotRequired["PostEmailPreviewBodyDraft"],
})

PostEmailTestBody = TypedDict("PostEmailTestBody", {
    "event": Literal["payout_sent", "payout_failed", "invitation_received", "partner_approved", "contract_sent", "webhook_endpoint_disabled", "webhook_endpoint_failing", "tax_document_ready"],
    "locale": Literal["en", "es", "de", "fr", "pt", "it", "nl", "sv", "ja", "zh"],
    "to": str,
})

PutMeLocaleBody = TypedDict("PutMeLocaleBody", {
    "locale": Literal["en", "es", "de", "fr", "pt", "it", "nl", "sv", "ja", "zh"],
})

PutMeRoiDigestBody = TypedDict("PutMeRoiDigestBody", {
    "enabled": bool,
})

PutPartnerLocaleBody = TypedDict("PutPartnerLocaleBody", {
    "locale": Literal["en", "es", "de", "fr", "pt", "it", "nl", "sv", "ja", "zh"],
})

PutIntegrationsHubspotBody = TypedDict("PutIntegrationsHubspotBody", {
    "token": NotRequired[str],
    "pipeline": NotRequired[Optional[str]],
    "newDealStage": NotRequired[Optional[str]],
    "paidDealStage": NotRequired[Optional[str]],
    "status": NotRequired[Literal["active", "paused"]],
})

PutIntegrationsSegmentBody = TypedDict("PutIntegrationsSegmentBody", {
    "writeKey": NotRequired[str],
    "events": NotRequired[Optional[List[Literal["referral.created", "commission.earned", "commission.reversed", "commission.settled", "payout.sent", "payout.failed", "partner.applied", "partner.enrolled", "partner.approved"]]]],
    "status": NotRequired[Literal["active", "paused"]],
})

PostIntegrationsHubspotTestBody = TypedDict("PostIntegrationsHubspotTestBody", {
    "setupProperties": NotRequired[bool],
})

PostZapierHooksBody = TypedDict("PostZapierHooksBody", {
    "target_url": str,
    "event": Literal["referral.created", "commission.earned", "commission.reversed", "commission.settled", "payout.sent", "payout.failed", "partner.applied", "partner.enrolled", "partner.approved", "deal.submitted", "fraud.case_opened"],
})

PostZapierConversionsBody = TypedDict("PostZapierConversionsBody", {
    "providerEventId": str,
    "type": NotRequired[Literal["invoice_paid", "refund"]],
    "customerRef": str,
    "amountMinor": int,
    "currency": NotRequired[str],
    "invoiceRef": NotRequired[str],
    "occurredAt": NotRequired[str],
    "connectionId": NotRequired[str],
})

PostPartnerSecurityTotpEnableBody = TypedDict("PostPartnerSecurityTotpEnableBody", {
    "code": str,
})

PostPartnerSecurityTotpDisableBody = TypedDict("PostPartnerSecurityTotpDisableBody", {
    "code": str,
})

PostAuthConnectionsBodyKeys = TypedDict("PostAuthConnectionsBodyKeys", {
    "referralToken": NotRequired[str],
    "anonId": NotRequired[str],
    "couponCode": NotRequired[str],
    "programId": NotRequired[str],
    "autoEnroll": NotRequired[str],
})

PostAuthConnectionsBody = TypedDict("PostAuthConnectionsBody", {
    "provider": Literal["atlas", "clerk", "auth0", "supabase", "firebase", "cognito", "stytch", "kinde", "workos", "generic", "custom"],
    "programId": str,
    "instanceId": NotRequired[str],
    "autoEnrollUsers": NotRequired[bool],
    "destinationUrl": NotRequired[str],
    "name": NotRequired[str],
    "secret": NotRequired[str],
    "keys": NotRequired["PostAuthConnectionsBodyKeys"],
})

PutAuthConnectionsIdSecretBody = TypedDict("PutAuthConnectionsIdSecretBody", {
    "secret": str,
})

PatchAuthConnectionsIdBody = TypedDict("PatchAuthConnectionsIdBody", {
    "status": NotRequired[Literal["active", "paused"]],
    "name": NotRequired[str],
    "autoEnrollUsers": NotRequired[bool],
    "destinationUrl": NotRequired[Optional[str]],
    "signatureVersion": NotRequired[Literal["v1+v2", "v2"]],
})

PostAuthConnectionsIdSignupsBodyReferral = TypedDict("PostAuthConnectionsIdSignupsBodyReferral", {
    "code": NotRequired[str],
    "clickId": NotRequired[str],
    "anonId": NotRequired[str],
    "capturedAt": NotRequired[str],
    "consent": NotRequired[Literal["granted", "not_required"]],
})

PostAuthConnectionsIdSignupsBodyRisk = TypedDict("PostAuthConnectionsIdSignupsBodyRisk", {
    "botScore": NotRequired[float],
    "disposableEmail": NotRequired[bool],
    "emailVerified": NotRequired[bool],
    "selfReferral": NotRequired[bool],
    "velocity": NotRequired[int],
    "reasons": NotRequired[List[str]],
    "score": NotRequired[float],
    "level": NotRequired[Literal["low", "medium", "high"]],
    "dropped": NotRequired[bool],
})

PostAuthConnectionsIdSignupsBody = TypedDict("PostAuthConnectionsIdSignupsBody", {
    "customerRef": str,
    "email": NotRequired[str],
    "emailHash": NotRequired[str],
    "name": NotRequired[str],
    "ip": NotRequired[str],
    "ua": NotRequired[str],
    "signedUpAt": str,
    "referral": NotRequired["PostAuthConnectionsIdSignupsBodyReferral"],
    "risk": NotRequired["PostAuthConnectionsIdSignupsBodyRisk"],
    "emailDomain": NotRequired[str],
    "referralCode": NotRequired[str],
    "autoEnroll": NotRequired[bool],
    "test": NotRequired[bool],
})

PostAuthConnectionsIdPartnersBody = TypedDict("PostAuthConnectionsIdPartnersBody", {
    "customerRef": str,
    "email": str,
    "name": NotRequired[str],
    "code": NotRequired[str],
})

PostAuthConnectionsIdEraseBody = TypedDict("PostAuthConnectionsIdEraseBody", {
    "customerRef": str,
})

PostAuthConnectionsIdAliasesBody = TypedDict("PostAuthConnectionsIdAliasesBody", {
    "fromCustomerRef": str,
    "toCustomerRef": str,
})

PostAuthConnectionsIdUsersBody = TypedDict("PostAuthConnectionsIdUsersBody", {
    "customerRef": str,
    "email": NotRequired[str],
    "name": NotRequired[str],
    "status": NotRequired[Literal["active", "suspended", "deleted"]],
})

PostAuthConnectionsIdSignalsBody = TypedDict("PostAuthConnectionsIdSignalsBody", {
    "customerRef": str,
    "signal": Literal["email_verified", "banned", "unbanned", "fraud_confirmed", "self_referral"],
    "at": NotRequired[str],
    "details": NotRequired[Dict[str, Any]],
})

PostAuthConnectionsInstallBody = TypedDict("PostAuthConnectionsInstallBody", {
    "clientId": str,
    "scope": str,
    "redirectUri": str,
    "state": NotRequired[str],
    "codeChallenge": str,
    "instanceId": str,
    "programId": NotRequired[str],
    "decision": Literal["allow", "deny"],
})

PostOauthTokenBody = TypedDict("PostOauthTokenBody", {
    "grant_type": Literal["authorization_code"],
    "code": str,
    "code_verifier": str,
    "client_id": str,
    "redirect_uri": str,
})

PatchOrgSsoBody = TypedDict("PatchOrgSsoBody", {
    "requireSso": NotRequired[bool],
    "roleMapping": NotRequired[Dict[str, Literal["owner", "admin", "finance", "analyst", "support"]]],
})

PostOrgSsoTicketsBody = TypedDict("PostOrgSsoTicketsBody", {
    "expiresInDays": NotRequired[int],
})

PutOrgSsoDirectBodyOption1 = TypedDict("PutOrgSsoDirectBodyOption1", {
    "adapter": Literal["oidc"],
    "issuer": str,
    "clientId": str,
    "clientSecret": NotRequired[str],
    "scopes": NotRequired[str],
    "roleClaim": NotRequired[str],
    "name": NotRequired[str],
    "domains": NotRequired[List[str]],
    "roleMapping": NotRequired[Dict[str, Literal["admin", "finance", "analyst", "support"]]],
    "defaultRole": NotRequired[Optional[Literal["admin", "finance", "analyst", "support"]]],
    "trustEmailVerified": NotRequired[bool],
})

PutOrgSsoDirectBodyOption2 = TypedDict("PutOrgSsoDirectBodyOption2", {
    "adapter": Literal["workos"],
    "clientId": str,
    "apiKey": NotRequired[str],
    "organizationId": str,
    "domains": NotRequired[List[str]],
    "roleMapping": NotRequired[Dict[str, Literal["admin", "finance", "analyst", "support"]]],
    "defaultRole": NotRequired[Optional[Literal["admin", "finance", "analyst", "support"]]],
    "trustEmailVerified": NotRequired[bool],
})

PostPartnerAuthWalletNonceBody = TypedDict("PostPartnerAuthWalletNonceBody", {
    "address": str,
})

PostPartnerAuthWalletVerifyBody = TypedDict("PostPartnerAuthWalletVerifyBody", {
    "address": str,
    "nonce": str,
    "signature": str,
    "name": NotRequired[str],
})

PostOnchainConnectionsBody = TypedDict("PostOnchainConnectionsBody", {
    "programId": str,
    "name": NotRequired[str],
    "secret": NotRequired[str],
    "decimals": NotRequired[Dict[str, int]],
})

PostPublicProgramsHandleJoinBody = TypedDict("PostPublicProgramsHandleJoinBody", {
    "destinationUrl": NotRequired[str],
})

PutSupportAppsAdapterBodyConfig = TypedDict("PutSupportAppsAdapterBodyConfig", {
    "publicKeyPem": NotRequired[str],
    "subdomain": NotRequired[str],
    "cardKey": NotRequired[str],
})

PutSupportAppsAdapterBody = TypedDict("PutSupportAppsAdapterBody", {
    "enabled": NotRequired[bool],
    "secret": NotRequired[str],
    "rotate": NotRequired[bool],
    "config": NotRequired["PutSupportAppsAdapterBodyConfig"],
})

PostSupportAppsAdapterTestBody = TypedDict("PostSupportAppsAdapterTestBody", {
    "email": NotRequired[str],
    "customerRef": NotRequired[str],
    "partnerExternalRef": NotRequired[str],
    "ext": NotRequired[str],
})

PostPrivacyExecutorKeysBodyConfig = TypedDict("PostPrivacyExecutorKeysBodyConfig", {
    "publicKeyPem": NotRequired[str],
    "algorithm": NotRequired[Literal["ES384", "ES256", "RS256"]],
    "sombraUrl": NotRequired[str],
})

PostPrivacyExecutorKeysBody = TypedDict("PostPrivacyExecutorKeysBody", {
    "adapter": Literal["cm-standard-v1", "onetrust", "transcend", "datagrail", "ketch", "osano", "custom"],
    "vendorSecret": NotRequired[str],
    "config": NotRequired["PostPrivacyExecutorKeysBodyConfig"],
    "rotate": NotRequired[bool],
    "enabled": NotRequired[bool],
})

PostAccountCloseBody = TypedDict("PostAccountCloseBody", {
    "confirm": str,
})

PutOrgTrackingConsentBody = TypedDict("PutOrgTrackingConsentBody", {
    "mode": Literal["auto", "none", "pending", "custom", "cookiemunch", "onetrust", "cookiebot", "usercentrics", "didomi", "osano", "termly", "tcf", "gpp", "gcm"],
    "category": NotRequired[str],
    "tcfVendorId": NotRequired[int],
    "gcmSignal": NotRequired[Literal["ad_storage", "analytics_storage"]],
    "noCmp": NotRequired[Literal["persist", "memory"]],
})

PutOrgHostedPagesBodyConsent = TypedDict("PutOrgHostedPagesBodyConsent", {
    "adapter": Literal["none", "builtin", "cookiemunch", "onetrust", "cookiebot", "usercentrics", "didomi", "osano", "termly", "iubenda", "custom"],
    "config": NotRequired[Dict[str, Any]],
})

PutOrgHostedPagesBodyChatOption1 = TypedDict("PutOrgHostedPagesBodyChatOption1", {
    "adapter": Literal["chatly", "intercom", "crisp", "custom"],
    "config": NotRequired[Dict[str, Any]],
})

PutOrgHostedPagesBody = TypedDict("PutOrgHostedPagesBody", {
    "consent": "PutOrgHostedPagesBodyConsent",
    "chat": NotRequired[Optional["PutOrgHostedPagesBodyChatOption1"]],
    "customOrigins": NotRequired[Dict[str, List[str]]],
})

PostGraphqlBody = TypedDict("PostGraphqlBody", {
    "query": str,
    "variables": NotRequired[Dict[str, Any]],
    "operationName": NotRequired[str],
})

