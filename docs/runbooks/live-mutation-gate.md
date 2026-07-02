# Live Mutation Gate

Live mutations change cPanel state. They require explicit authorization.

## Allowed Without Extra Confirmation

Read-only checks may run when the user asks for live evidence:

- domain list readback
- DNS zone read
- SSL status read
- email inventory read

## Requires Explicit Authorization

These operations require a specific live target:

- create subdomain
- create mailbox
- update DNS
- update redirects
- update document root
- upload files
- deploy public artifacts

## Requires Stronger Confirmation

These operations are destructive or high-risk:

- remove domain
- remove mailbox
- delete DNS record
- overwrite public website files
- expose private/API/model domains publicly

## Current Authorized Mutation Record

| Date | Operation | Target | Status |
| --- | --- | --- | --- |
| 2026-07-01 | Create cPanel subdomain | `test.securedme.ca` | Passed |

