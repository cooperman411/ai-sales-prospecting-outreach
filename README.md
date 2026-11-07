# AI Sales Prospecting & Outreach

A simple, vendor-neutral AI skill: **find suitable businesses, locate verified
professional contacts, write useful individual emails, track replies, and
prepare sensible follow-ups.** Start with web research and an email account.
A CRM and paid prospecting service are optional, not prerequisites.

**Status: initial skill package.** Documentation and fictional, offline-tested
examples only. No live mail or CRM actions have been tested. No actual sending
code or scheduler is bundled.

## The simplest version

1. Describe the customer you want to reach and the problem you solve.
2. Research a small, bounded set of promising businesses using public sources.
3. Identify relevant business roles and find **verified work addresses** using
   a connected native tool, a free-tier provider, or authorized public sources.
4. Let the AI write a concise, specific email with one reason for contacting
   the recipient. Review each draft or a bounded batch.
5. Send manually from your mailbox, or explicitly authorize a supported
   connector to send the exact approved messages.
6. Track what was **actually sent**, replies, opt-outs and follow-up dates in
   CSV. Use HubSpot, Zoho, Salesforce, or another CRM if desired.

## First-use copy prompt

```text
Help me use the AI Sales Prospecting & Outreach skill in this folder.
Read README.md, skills/sales-prospecting/SKILL.md and the referenced files.
Keep setup short. Begin with public company research and verified work
contacts, then prepare a small set of emails for my review. Use native
integrations first, Composio second, then other suitable tools. No paid data
usage, CRM writes, email sends, enrollment, or scheduling without my explicit
authorization. Never invent contact information.
```

## What you need

- **Required:** company/product facts, an ICP or target description, an approved
  sending identity, and a way to review outputs.
- **Optional:** prospecting service (Hunter, Prospeo, Apollo, etc.), CRM,
  connected Gmail or Microsoft 365, agent tools/MCP, private file storage.
- **No integration:** Use manual public research, optional human-verified
  business contacts, email drafts ready to paste, and private CSV files.

## Structure

- `skills/sales-prospecting/SKILL.md` — control flow and approval boundaries.
- `references/` — targeting, contact discovery, email writing, compliance, monitoring.
- `integrations/` — native-first, Composio, and free-first provider guidance.
- `templates/` — short setup, CSV columns, message review, and opt-out checklist.
- `examples/` — fully fictional, non-contactable campaign records.
- `tests/` — offline example checks.
- `SOURCES.md` — dated official pricing and compliance references.

Run `python3 -m unittest discover -s tests -v` to validate the examples.

## Security and compliance

This is not an autonomous mass mailer. Unsolicited commercial email is legally
regulated, even business-to-business email. Before any send, verify jurisdiction,
legal basis/consent as applicable, verified sender identity, required address
and opt-out method, suppression state, and message accuracy. The FTC's CAN-SPAM
rules apply to US B2B commercial emails. See `references/compliance.md`.

Never store real leads, messages, personal data or tokens in this public repo.
Publishing this skill grants nobody permission to prospect, spend provider
credits, change CRM records, or send email. MIT-licensed without warranty.
