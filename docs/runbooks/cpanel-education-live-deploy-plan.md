# cPanel Education Live Deploy Plan

This runbook records the public-safe deployment path for publishing the SecuredMe Education GitHub Pages build under `securedme.ca/education/`.

## Current Gate

| Gate | Status | Evidence |
| --- | --- | --- |
| GitHub Pages source build | ready | `python -m mkdocs build --strict` passes locally. |
| Public-safe asset boundary | ready | Only MkDocs output, Education PNG assets, CSS, and public docs are included. |
| Domain authority read | ready | cPanel domain PDF authority read returned 52 domains, including `securedme.ca`. |
| Controller live-write session | blocked | No active Education Controller session was present during this run. |
| Live cPanel execution | blocked | Execution is allowed only with an active controller session and explicit gated approval. |

## Target

| Item | Value |
| --- | --- |
| Public URL | `https://securedme.ca/education/` |
| Preferred source | `https://github.com/SeCuReDmE-main-dev/test.git` |
| Preferred branch | `gh-pages` |
| cPanel docroot target | `securedme.ca/education` |
| Local build source | `C:\Users\jeans\Desktop\Case study\test\site` |

## Deployment Options

### Option A: cPanel Git Version Control

1. Create or reuse a repo-specific SSH deploy key in cPanel.
2. Add the public key to GitHub as a read-only deploy key.
3. Register `https://github.com/SeCuReDmE-main-dev/test.git` in cPanel Git Version Control.
4. Use branch `gh-pages`.
5. Deploy only the static public site output to `securedme.ca/education`.
6. Verify `https://securedme.ca/education/` returns HTTP 200.

### Option B: Fileman Upload

1. Use local source `C:\Users\jeans\Desktop\Case study\test\site`.
2. Upload only the contents of `site/` into `securedme.ca/education`.
3. Do not upload `.env`, private PDFs, raw cPanel exports, mailbox credentials, private keys, ops archives, or local caches.
4. Verify `https://securedme.ca/education/` returns HTTP 200.

## Rollback

Before live deployment, record the current `securedme.ca/education` file/source location. Rollback is restoring that previous source or removing the new deployment directory if it did not previously exist.

## Live Execution Rule

Live cPanel deployment remains blocked until all of these are true:

- Education Controller session is active.
- The operator explicitly sets `execute=true` for the approved deployment action.
- The cPanel Operator confirms the target domain and public-safe file boundary.
- The final readback confirms `https://securedme.ca/education/` without exposing cPanel session URLs or credentials.
