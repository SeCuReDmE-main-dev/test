# Live Mutation Gate

Live cPanel mutations are gated.

## Read-Only Checks

Allowed when live evidence is requested:

- domain inventory readback
- DNS zone read
- SSL status read
- email inventory read

## Standard Write Gate

Requires explicit target authorization:

- create subdomain
- create mailbox
- update document root
- upload public files
- deploy a public artifact

## High-Risk Gate

Requires stronger confirmation and rollback plan:

- delete domain
- delete mailbox
- delete or overwrite DNS record
- remove SSL state
- overwrite public website files

## Existing Authorized Mutation

| Date | Operation | Target | Result |
| --- | --- | --- | --- |
| 2026-07-01 | Create cPanel subdomain | `test.securedme.ca` | Passed |

