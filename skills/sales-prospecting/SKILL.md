---
name: ai-sales-prospecting-outreach
version: 0.1.0
description: Research evidence-based B2B prospects, verify professional contacts, prepare authentic low-volume outbound email, and track replies using native tools first, Composio second, and optional CRM/email discovery providers. Never send or spend without explicit authorization.
---

# Sales prospecting and outreach

## First use

Read `templates/first-use.md`, ask only for missing essentials, and start with
one bounded group of companies. The product or service description supplied
by the user is the source of truth; do not invent features, customers, or ROI.

## Capability routing

Use native authenticated host integrations and vendor MCP/tools first, then
Composio, then provider API or human-approved manual workflow. A free public
web search may identify companies or roles; it must not be represented as a
verified email lookup. Verify actual connection, scopes and provider quotas.
A CRM is optional; CSV files are the minimum durable system.

## Stages

1. **Define:** Product/use case, ICP, geography, exclusions, sending identity,
   jurisdiction, and a small target limit.
2. **Discover companies:** Public primary sources first. Record sources and
   uncertainty; distinguish direct fit, near fit, rejected and unresolved.
3. **Find people:** Select relevant functions. Check existing CRM/suppression
   before enrichments. Use public professional contacts or an approved provider;
   verify work email and current company/role. Never guess addresses.
4. **Prepare records:** Deduplicate by company domain, exact work email, or
   provider ID. Write to a **private** CSV/CRM only when authorized.
5. **Draft:** One specific, true reason for outreach, a relevant problem or
   observation, one modest value statement, one easy question/CTA, and a
   compliant sender signature and opt-out. No invented familiarity.
6. **Review and approve:** Show target, work email verification, sources,
   message, proposed follow-up timing, from-address, suppression check, and
   cost. Sending and sequence enrollment require explicit approval.
7. **Execute:** Create unsent drafts when authorized; never confuse drafts with
   sends. Send only exact approved items via a verified connected mailbox or
   manual human action. Log provider message ID and actual send timestamp.
8. **Monitor:** Reconcile Sent, responses, opt-outs, bounces and meetings.
   Stop follow-ups for any reply, suppression, hard bounce or conflict.
   Derive follow-up dates only from verified sends. Never claim background
   monitoring without a real scheduler/trigger.

## Permission boundaries

- Read-only public research and analysis: generally permitted.
- Reading connected CRM/mailbox: only with account authorization and scope.
- Personal-contact lookup, paid search/enrichment, and export: separate approval
  with exact maximum credits/cost and data scope.
- CRM create/update, draft creation, subscription changes: separate identified
  scope and approval; no silent overwrites or lead creation.
- Sends, sequence enrollment, meeting invitations, auto-follow-ups: explicit
  approval for the exact batch; never implied by 'find leads' or 'write emails'.
- Unsubscribe requests: immediately suppress future sends, maintaining a
  private minimal do-not-contact record as required for compliance.
- Unknown provider result: reconcile before any retry; no duplicate sends.

## Non-negotiable quality

No fabricated contact details or unverified employer roles. No generic bulk
mail merge masquerading as personal correspondence. Never claim exhaustive
coverage of a provider search. No scraping behind access controls, bypassing
CAPTCHAs, buying unauthorized data, or use of personal contact details without
applicable legal basis. No automatic sends by default.

## Outputs

A concise company shortlist (why fit + source + gap), contact eligibility list,
message review packet, private CSV/CRM change proposal, and reconciliation
summary with verified sends, replies, exclusions and next steps. When only
manual tools are available, deliver paste-ready drafts and CSV templates.

Load `references/compliance.md`, `references/contact-discovery.md`, and
`references/outreach.md` before creating or sending any real email.
