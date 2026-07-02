# SeCuReDmE cPanel API Surface Test Lab

This public repository is a safe test harness for documenting and validating what the SecuredMe cPanel operator can do through WHC/cPanel APIs, local CLI fallbacks, and GitHub-reviewed procedures.

It does not contain secrets, tokens, exported `.env` files, cPanel session URLs, private PDFs, mailbox passwords, SSH keys, or production deployment artifacts.

## Purpose

The goal is to document repeatable tests for the `securedme-cpanel-operator` plugin and to separate public operational learning from private SecuredMe implementation files.

This repository lives at the root of the local study-case workspace:

`C:\Users\jeans\Desktop\Case study\test`

It is intentionally outside:

`C:\Users\jeans\Desktop\Case study\modele`

## Confirmed Starting Evidence

- A live cPanel subdomain creation test was executed for `test.securedme.ca`.
- cPanel confirmed the domain in the browser UI.
- The cPanel API confirmed the same domain through `DomainInfo/list_domains`.
- The document root shown by cPanel is `public_html/test.securedme.ca`.
- The plugin was corrected to normalize copied cPanel UI session URLs to the API origin before UAPI calls.

## Safety Rules

- Never commit `.env` files.
- Never commit API tokens, passwords, private keys, webhook secrets, mailbox passwords, cPanel session URLs, or raw credential exports.
- Live write tests require explicit authorization before execution.
- Default mode for cPanel mutation tools should remain dry-run.
- Public test reports should include only redacted evidence.
- Private/API/model domains must not be treated as public-ready just because they exist in DNS or cPanel.

## cPanel API Surface To Test

### 1. Health And Environment Audit

Objective: verify the plugin can see its local configuration without exposing secrets.

Planned checks:

- `cpanel_health`
- `cpanel_env_audit`
- required cPanel keys present
- `.env` path resolved correctly
- secret values redacted
- SSH fields detected but not printed

Expected result:

- API access is reported as available.
- No secret values appear in output.

### 2. Domain Inventory

Objective: compare cPanel domain authority with planned SecuredMe web architecture.

Planned checks:

- `cpanel_list_domains`
- `cpanel_domain_inventory`
- live `DomainInfo/list_domains`
- classify domains as root identity, app surface, ops/support, FFeD cluster, private/API, or WHC technical host

Expected result:

- `securedme.ca` is the root identity.
- `test.securedme.ca` appears after the live creation test.
- known app domains are categorized without changing website docs.

### 3. Subdomain Creation

Objective: verify controlled creation of cPanel subdomains.

Planned checks:

- dry-run `cpanel_create_subdomain`
- authorized live `cpanel_create_subdomain`
- verify through cPanel browser UI
- verify through `DomainInfo/list_domains`
- verify document root assignment

Current known successful case:

- `test.securedme.ca`
- document root: `public_html/test.securedme.ca`

Expected result:

- cPanel creates the subdomain.
- API readback confirms it.
- no credentials are logged.

### 4. DNS Zone Read Tests

Objective: inspect DNS data safely without exposing unnecessary infrastructure details in public reports.

Planned checks:

- dry-run `cpanel_parse_zone`
- authorized live read `cpanel_parse_zone`
- root A/AAAA/CNAME state
- `www`
- `mail`
- MX
- SPF
- DKIM
- DMARC

Expected result:

- records can be read.
- public report summarizes readiness without dumping sensitive operational noise.

### 5. SSL And AutoSSL Checks

Objective: verify whether cPanel reports usable SSL state for a domain.

Planned checks:

- `cpanel_ssl_status`
- SSL installed-host inventory
- AutoSSL readiness
- Cloudflare/WHC routing notes

Expected result:

- SSL status can be checked for root and subdomains.
- recommendations avoid Flexible SSL as the preferred launch mode.

### 6. Email Inventory

Objective: audit SecuredMe mailbox state without exposing passwords.

Planned checks:

- dry-run `cpanel_email_inventory`
- authorized live read `cpanel_email_inventory`
- mailbox list
- quota and status fields if available
- routing assumptions

Expected result:

- mailbox names and statuses can be reported.
- passwords and reset data never appear.

### 7. Email Creation

Objective: validate safe mailbox creation using password values stored only in the local `.env`.

Planned checks:

- confirm target mailbox policy
- confirm password env key exists
- dry-run `cpanel_create_email`
- authorized live `cpanel_create_email`
- readback inventory

Expected result:

- mailbox can be created without passing a literal password in chat.
- report includes mailbox name and status only.

### 8. Generic UAPI Calls

Objective: test controlled escape hatch access to cPanel UAPI.

Planned checks:

- `cpanel_uapi_call` with dry-run
- read-only UAPI calls with explicit execution
- write UAPI calls only after explicit authorization

Expected result:

- the plugin can reach cPanel UAPI directly.
- dangerous operations remain gated.

### 9. SSH Fallback Planning

Objective: document how a server-side `uapi` fallback would be constructed without exposing secrets.

Planned checks:

- `cpanel_ssh_uapi_plan`
- SSH host/user/port presence audit
- command preview with secret redaction

Expected result:

- fallback plan is available.
- plugin does not execute SSH mutations automatically in this test repo.

### 10. Deployment Planning

Objective: prepare safe deployment routes for cPanel document roots.

Planned checks:

- `cpanel_file_upload_plan`
- `cpanel_git_deploy_plan`
- document root validation
- rollback notes
- ensure `.env` and private materials are excluded

Expected result:

- deployment plans are generated without uploading files automatically.
- public artifacts are separated from private operations data.

### 11. SecuredMe Education Suite Mapping

Objective: verify public web architecture mapping without overclaiming readiness.

Planned checks:

- `securedme_suite_registry`
- `securedme_domain_mismatch_report`
- compare planned app domains against cPanel domains
- keep Tesla canonical target as `tesla-workbench.securedme.ca`
- note current cPanel state when different

Expected result:

- app-to-domain map is explicit.
- stale README/domain mismatches can be reported.
- Education suite remains labeled `pre-alpha` unless app-specific validation proves otherwise.

## What This Repository Should Not Do

- It should not host production secrets.
- It should not replace the private SecuredMe website workspace.
- It should not publish raw cPanel exports.
- It should not expose private/API/model surfaces as public-ready.
- It should not automatically remove domains, mailboxes, DNS records, or SSL records.
- It should not change `_ops\suite-ecoles-readiness` report files.

## First Test Status

| Test | Target | Status | Evidence |
| --- | --- | --- | --- |
| Create subdomain | `test.securedme.ca` | Passed | Browser cPanel UI and `DomainInfo/list_domains` readback |
| Document root assignment | `public_html/test.securedme.ca` | Passed | cPanel domain management page |
| API URL normalization | cPanel UI URL to API origin | Passed | Plugin patched and unit-tested |

## Next Test Queue

1. Run a live read-only DNS zone parse for `securedme.ca`.
2. Check SSL status for `test.securedme.ca`.
3. Audit cPanel email inventory without printing passwords.
4. Prepare a placeholder deployment plan for `test.securedme.ca`.
5. Record mismatch findings for SecuredMe Education domains.

## Public Reporting Standard

Every public test note should use this format:

- Objective
- Tool or API surface
- Dry-run result
- Live execution status, if authorized
- Redacted evidence
- Risk or limitation
- Next action

