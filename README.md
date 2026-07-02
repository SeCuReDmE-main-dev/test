# SeCuReDmE cPanel API Surface Test Lab

Public documentation source for SecuredMe cPanel operator tests.

This repository documents how the `securedme-cpanel-operator` plugin is tested against WHC/cPanel API surfaces, CLI fallback plans, DNS/SSL/email checks, deployment planning, and SecuredMe Education domain governance.

The repository is intentionally located at:

`C:\Users\jeans\Desktop\Case study\test`

It is intentionally outside:

`C:\Users\jeans\Desktop\Case study\modele`

## Documentation System

This repo uses MkDocs Material as the documentation build system.

Published documentation:

https://securedme-main-dev.github.io/test/

Hosted wiki section:

https://securedme-main-dev.github.io/test/wiki/

Primary documentation lives in:

`docs/`

Main entrypoint:

`docs/index.md`

First live test report:

`docs/tests/001-cpanel-subdomain-create.md`

GitHub Wiki source mirror, ready for native Wiki initialization:

`wiki/`

## First Confirmed Test

The first live test created and verified:

`test.securedme.ca`

Result:

- cPanel created the subdomain.
- cPanel browser UI shows the domain.
- cPanel API `DomainInfo/list_domains` readback found the domain.
- Document root is `public_html/test.securedme.ca`.
- API URL normalization was patched and unit-tested in the local plugin.

## Build Locally

Install the docs dependencies:

```powershell
python -m pip install -r requirements-docs.txt
```

Run the local docs server:

```powershell
python -m mkdocs serve
```

Build the static site:

```powershell
python -m mkdocs build --strict
```

## Public Safety

This repository must not contain:

- `.env` files
- API tokens
- passwords
- private keys
- webhook secrets
- mailbox passwords
- cPanel session URLs
- raw private cPanel exports
- private deployment archives

Live write tests require explicit authorization and must be documented with redacted evidence only.
