# Deployment Planning

Deployment tests are planning-first.

## Current Target

First deployment planning target:

`public_html/test.securedme.ca`

## Planned Checks

- document root exists
- no private files are present
- placeholder artifact path is clear
- rollback path exists
- `.env` files are excluded
- private reports and cPanel exports are excluded

## Deployment Modes

| Mode | Current Status | Notes |
| --- | --- | --- |
| File Manager upload plan | Planned | Generates a safe plan before upload. |
| cPanel Git deployment plan | Planned | Keep checkout outside public docroot unless deploy artifact is filtered. |
| Direct upload execution | Not enabled in public test repo | Requires a separate authorized mission. |

