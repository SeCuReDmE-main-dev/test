# cPanel Operator Lab Notes

## Current Lab Objective

Build a public-safe evidence trail for the SecuredMe cPanel operator.

The operator should be able to:

- audit access readiness
- create approved test domains
- verify cPanel readback
- inspect DNS and SSL state
- prepare email and deployment operations
- preserve a strict redaction boundary

## First Effective Test

The first effective live test created:

`test.securedme.ca`

Result:

- cPanel UAPI write succeeded.
- cPanel UI showed the new domain.
- API readback found the domain.
- document root was assigned.

Full report:

[001: cPanel Subdomain Creation](../tests/001-cpanel-subdomain-create.md)

## Current Capability Confidence

| Capability | Confidence | Reason |
| --- | --- | --- |
| cPanel token authentication | High | Live UAPI calls returned `HTTP 200` after URL normalization. |
| Create subdomain | High for approved test domains | `test.securedme.ca` was created. |
| Domain inventory readback | High | `DomainInfo/list_domains` verified the target. |
| DNS parsing | Not yet proven in public docs | Planned next test. |
| SSL status | Not yet proven in public docs | Planned next test. |
| Email inventory | Not yet proven in public docs | Planned next test. |
| Deployment planning | Medium | Planning tools exist; no public deployment test has run yet. |

## Personal Operating Notes

- Use dry-run first for every write tool.
- Execute only one approved mutation at a time.
- Verify through a separate read operation.
- Write results into `docs/tests/`.
- Mirror short summaries into the GitHub Wiki.

