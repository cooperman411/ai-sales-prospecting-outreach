# Second option: Composio

Use Composio only when host-native or vendor-native tools do not provide the
needed authorized action, or the user prefers it.

Possible categories: CRM (HubSpot/Zoho/Salesforce), Gmail or email account,
contact intelligence (Apollo/Hunter), and other data sources. Availability
is tool- and account-specific, not guaranteed by a toolkit listing.

1. List toolkits and account connections; check the exact advertised action.
2. Verify user-selected sending mailbox, recipient lookup permissions, CRM
   identity, OAuth scopes, and any billable operations.
3. Perform read-only lookups first. Propose a bounded paid-data batch with
   maximum credits/cost before using it.
4. Obtain separate approval for CRM create/update, draft, actual send, or
   sequence enrollment. Never use 'complete workflow' to infer send approval.
5. Verify results and persist remote message/contact IDs privately.

Composio has a free tool-call allowance, but underlying provider fees, auth
and API restrictions remain. Do not report 'free contacts' simply because the
connector's invocation is free.

Sources: https://composio.dev/pricing and https://docs.composio.dev/toolkits
