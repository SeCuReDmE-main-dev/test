# Test 001: cPanel Subdomain Creation

## Status

Passed.

## Target

`test.securedme.ca`

## Document Root

`public_html/test.securedme.ca`

## What Was Tested

The SecuredMe cPanel operator created a cPanel subdomain through UAPI after explicit live authorization.

## API Surface

| Area | Value |
| --- | --- |
| Plugin | `securedme-cpanel-operator` |
| Tool | `cpanel_create_subdomain` |
| cPanel UAPI write | `SubDomain/addsubdomain` |
| cPanel UAPI readback | `DomainInfo/list_domains` |

## Result

| Check | Result |
| --- | --- |
| Dry-run plan | Passed |
| Live UAPI create | Passed |
| HTTP status | `200` |
| UAPI status | `1` |
| API readback found target | `true` |
| Browser UI confirmation | Passed |

## Important Fix Found During Test

The cPanel URL copied from the browser included a session UI path. Direct API calls against that full URL returned `HTTP 403`.

The plugin was patched to normalize copied cPanel UI URLs to the API origin before calling UAPI.

## What This Proves

- the plugin can perform an approved cPanel UAPI write
- the plugin can create a subdomain under `securedme.ca`
- the plugin can verify the result with a separate API readback

## What This Does Not Prove

- SSL readiness
- DNS global propagation
- production readiness
- public website deployment
- safety review completion

Full report:

https://securedme-main-dev.github.io/test/tests/001-cpanel-subdomain-create/

