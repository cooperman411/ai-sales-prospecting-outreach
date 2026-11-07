# Outbound email compliance and deliverability

**This is an operational checklist, not legal advice.** Rules vary by recipient
location, entity type, channel, and data source. If consent/lawful basis is
uncertain, stop at research or draft review. A tool's ability to send does not
establish legal permission.

## United States

The FTC CAN-SPAM Act applies to **commercial business-to-business email** too.
Use accurate sender/header information and non-deceptive subjects, a valid
physical postal address, a clear working opt-out, and prompt opt-out handling
(within 10 business days under the FTC rule). Treat any opt-out as immediate
suppression for this workflow. Check the official FTC guide and current law.

## UK/EU and elsewhere

Different consent and privacy rules apply. UK PECR treats corporate subscribers
differently from sole traders and certain partnerships; processing personal
business-contact data can still engage UK GDPR. For EU and other countries,
confirm applicable laws before contacting; don't generalize US rules globally.
Do not use collected data from a public page without considering privacy laws.
Retain evidence of the applicable basis and objection/suppression handling.

## Sender requirements

Before sending to Gmail destinations, follow Google's sender guidelines:
SPF or DKIM authentication for all senders, TLS, valid DNS, and low spam
complaint rates. Google recommends SPF, DKIM **and** DMARC; bulk sender rules
have additional strict requirements including one-click unsubscribe for certain
marketing/subscription messages. Do not claim that a mailbox's daily send quota
is a safe cold outreach volume. Increase legitimate volume gradually. Do not
advise rotating domains/inboxes to evade spam or rate limits.

## Quality and metrics

- Prefer opt-in or highly relevant, lawful B2B contact over a large purchased
  or scraped list. Manually review a small first batch, then improve targeting.
- Verify work email before sending. Track bounce, negative reply/complaint,
  positive reply, conversations, meetings, and opt-outs. Treat open tracking as
  unreliable and potentially privacy-sensitive; it is not a definitive read.
- Plain, concise copy is generally easier to evaluate. Do not embed deceptive
  links, tracking pixels without an appropriate basis, or misleading subject
  lines. Respect stated prospect preferences and quiet periods.
- A repeat reply by the recipient ends automated follow-up eligibility even
  when the reply is a polite refusal. Always honor unsubscribe requests.
- Daily summaries should distinguish actual sends from drafts and uncertain
  mail-delivery outcomes. Reconcile Gmail Sent and CRM activity instead of
  guessing.

Official references:
- US FTC: https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business
- Google: https://support.google.com/mail/answer/81126
- UK ICO: https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/business-to-business-marketing/
