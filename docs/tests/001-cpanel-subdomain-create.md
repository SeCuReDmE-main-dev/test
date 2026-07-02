# 001: cPanel Subdomain Creation

## Summary

The first live cPanel API write test created `test.securedme.ca` and verified that cPanel recognizes it as an active subdomain.

Status: Passed

Evidence class:

- confirmed by live cPanel API
- confirmed by cPanel UI
- confirmed by local plugin test

## Objective

Validate that the SecuredMe cPanel operator can create a new subdomain through cPanel UAPI when a user explicitly authorizes a live mutation.

## Scope

Target domain:

`test.securedme.ca`

Root domain:

`securedme.ca`

Document root:

`public_html/test.securedme.ca`

Repository documenting the test:

`SeCuReDmE-main-dev/test`

Local public documentation root:

`C:\Users\jeans\Desktop\Case study\test`

## Authorization Mode

The user explicitly requested creation of:

`test.securedme.ca`

This changed the operation from dry-run only to authorized live mutation for this one domain.

No broad permission was granted for unrelated domain, DNS, email, SSL, deployment, or deletion operations.

## Tool And API Surface

Plugin:

`securedme-cpanel-operator`

Relevant tool:

`cpanel_create_subdomain`

Underlying cPanel UAPI function:

`SubDomain/addsubdomain`

Verification UAPI function:

`DomainInfo/list_domains`

## Preflight

The plugin first attempted to use the cPanel base URL from the local access envelope.

Initial issue:

- the cPanel URL was copied from the browser UI
- it contained a `cpsess.../frontend/jupiter/...` path
- direct UAPI calls against that full UI URL returned `HTTP 403`

Correction:

- the plugin was patched to normalize cPanel UI URLs to the API origin
- the effective API origin became the cPanel service root on port `2083`
- secret values were not printed

## Dry-Run Result

Dry-run generated this public-safe plan:

| Field | Value |
| --- | --- |
| Operation | Create subdomain |
| Subdomain label | `test` |
| Root domain | `securedme.ca` |
| Full domain | `test.securedme.ca` |
| Document root | `public_html/test.securedme.ca` |
| Auth display | redacted |

Dry-run status: Passed

## Live Execution Result

The authorized live cPanel UAPI call returned:

| Field | Result |
| --- | --- |
| HTTP status | `200` |
| cPanel response status | `1` |
| cPanel errors | none |
| cPanel warnings | none |

Live execution status: Passed

## Verification Result

The domain was verified through `DomainInfo/list_domains`.

Public-safe verification result:

| Field | Result |
| --- | --- |
| HTTP status | `200` |
| UAPI status | `1` |
| Target found | `true` |
| Subdomain count after readback | `51` |
| Target domain | `test.securedme.ca` |

Browser UI confirmation:

- cPanel opened the management page for `test.securedme.ca`
- cPanel displayed the document root `public_html/test.securedme.ca`
- cPanel displayed the domain as not redirected

## Redacted Evidence

Public-safe evidence:

```text
target: test.securedme.ca
docroot: public_html/test.securedme.ca
create_http_status: 200
create_uapi_status: 1
verify_http_status: 200
verify_uapi_status: 1
verify_target_found: true
verify_subdomain_count: 51
```

Excluded evidence:

- API token
- cPanel username
- cPanel password
- SSH password
- full `.env` contents
- cPanel session URL
- raw DNS zone payload
- raw private cPanel export

## Result Interpretation

This test proves:

- the plugin can perform an authorized cPanel UAPI write
- the plugin can create a subdomain under `securedme.ca`
- the plugin can verify the result through cPanel API readback
- the plugin can support a public evidence workflow without printing secrets

This test does not prove:

- the domain is production-ready
- SSL is valid for the new domain
- DNS has propagated globally
- a public website has been deployed
- the domain has passed public-safety review
- any other cPanel write operation is safe by default

## Follow-Up Tests

Recommended next tests:

1. Read DNS zone state for `securedme.ca`.
2. Check SSL status for `test.securedme.ca`.
3. Prepare a placeholder deployment plan for `public_html/test.securedme.ca`.
4. Verify no private files exist in the public document root.
5. Document removal procedure separately before any deletion test.

## Final Status

Passed.

`test.securedme.ca` exists in cPanel and is suitable as the first controlled test domain for future read-only DNS, SSL, and deployment-plan tests.

