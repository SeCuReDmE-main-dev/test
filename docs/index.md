# SeCuReDmE cPanel API Surface Test Lab

This documentation site records public, redacted, repeatable tests for the SecuredMe cPanel operator.

The lab exists to answer one practical question:

> What can the SecuredMe cPanel operator do safely, what evidence proves it, and what remains outside the public automation boundary?

## Current Status

| Area | Status | Notes |
| --- | --- | --- |
| Documentation build | Active | MkDocs Material source is now in this repository. |
| First live cPanel write test | Passed | `test.securedme.ca` was created and verified. |
| Public evidence policy | Active | Reports must use redacted evidence only. |
| DNS read tests | Planned | Next read-only API surface to validate. |
| SSL read tests | Planned | Next readiness check for `test.securedme.ca`. |
| Email inventory tests | Planned | Read-only inventory before any mailbox creation. |

## First Live Result

The first effective cPanel API test created:

`test.securedme.ca`

The result was verified in two ways:

- cPanel browser UI opened the domain management page for `test.securedme.ca`.
- cPanel API `DomainInfo/list_domains` returned `test.securedme.ca` in the live subdomain list.

Full report:

[001: cPanel Subdomain Creation](tests/001-cpanel-subdomain-create.md)

## Documentation Areas

- [Capability Matrix](plugin-capability-matrix/index.md): 40 public plugin capability tests and reusable prompts.
- [Wiki](wiki/index.md): navigation, documentation standards, and source map.
- [Tests](tests/index.md): executed and planned test records.
- [API Surface](api-surface/index.md): cPanel, DNS, SSL, email, deployment, and suite mapping surfaces.
- [Runbooks](runbooks/public-test-protocol.md): repeatable operating procedures.
- [Security](security/redaction-policy.md): redaction and public boundary rules.
- [Status](status/current-state.md): current repository and plugin state.
- [Decisions](decisions/0001-documentation-stack.md): architecture decisions for this documentation system.

## Operating Boundary

This is public documentation. It must not contain credentials, raw `.env` material, cPanel session URLs, private keys, mailbox passwords, private cPanel exports, or deployment archives.

Live cPanel mutations require explicit authorization and must be documented as redacted public evidence.

