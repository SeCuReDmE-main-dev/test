# SeCuReDmE Test Wiki

Welcome to the public GitHub Wiki for the SecuredMe cPanel API Surface Test Lab.

Primary documentation site:

https://securedme-main-dev.github.io/test/

Repository:

https://github.com/SeCuReDmE-main-dev/test

## What This Wiki Hosts

- cPanel API surface test summaries
- public-safe personal SecuredMe test notes
- operator runbooks
- status and roadmap links
- first-result evidence for `test.securedme.ca`

## Start Here

| Page | Purpose |
| --- | --- |
| [Personal SecuredMe Test Docs](Personal-SecuredMe-Test-Docs) | Personal public-safe test documentation index. |
| [Test 001 cPanel Subdomain Creation](Test-001-cPanel-Subdomain-Creation) | First live write test and results. |
| [cPanel API Surface Map](cPanel-API-Surface-Map) | Capability map for the operator. |
| [Live Mutation Gate](Live-Mutation-Gate) | Rules for live cPanel writes. |

## Current Confirmed Result

`test.securedme.ca` exists in cPanel.

Evidence:

- cPanel UI opened the domain management page.
- `DomainInfo/list_domains` found the target.
- document root: `public_html/test.securedme.ca`

## Public Boundary

This wiki must not contain secrets, `.env` data, API tokens, passwords, private keys, mailbox passwords, cPanel session URLs, or raw private cPanel exports.

