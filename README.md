# AI Sales Prospecting & Outreach

Use your AI assistant to find businesses that fit what you sell, identify the right people, and draft a short email with a real reason to reach out. Start with web research, an email account, and a private spreadsheet. Add a customer relationship management system (CRM) if your team uses one.

Say you sell scheduling software to service companies. Give the assistant the kind of business you serve and the claims it can make about the software. Ask it to check a small list of companies, show why each fits, and draft a note for the people whose roles and work addresses it can verify.

## Start With a Small List

Open the [skill](skills/sales-prospecting/SKILL.md) in your assistant, or give it the `skills/sales-prospecting` folder. Paste this request and fill in the details you know.

```text
Read the sales prospecting skill. I offer [product or service] to [type
of business]. Research up to [number] companies in [market]. Show me
why each fits and where you found the evidence. Identify relevant roles
and verify work addresses where you can. Draft a short email for each
eligible contact using [brand notes or sample emails] for the voice.
Bring the drafts back for review. Ask before spending credits, saving
drafts to my mailbox, changing records, or sending anything.
```

The [setup questions](skills/sales-prospecting/templates/first-use.md) help define the search. Start with public sources and use an approved contact provider when you need one. Leave unresolved addresses blank. See the [contact provider guide](skills/sales-prospecting/integrations/free-first.md) for options.

## Review and Track

Use the [review sheet](skills/sales-prospecting/templates/message-review.md) to check the recipient, the source behind the opening line, and the full email. Verify the sender details, opt-out method, and applicable rules before sending. You can send an approved note yourself or authorize a connected mailbox to send it.

Track confirmed sends, replies, and opt-outs in a private spreadsheet or CRM. Base follow-up dates on the confirmed send date. Stop follow-ups when someone replies, opts out, or otherwise becomes ineligible.

## Project Status

The repository includes the workflow and a [fictional campaign](skills/sales-prospecting/examples/fictional-campaign/README.md). Testing so far covers the offline example. For a live campaign, confirm what your [mailbox and CRM tools](skills/sales-prospecting/integrations/native-first.md) can do and review the [outbound email checklist](skills/sales-prospecting/references/compliance.md).
