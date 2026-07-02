# 0001: Documentation Stack

## Decision

Use MkDocs Material as the documentation build system for this repository.

## Context

The repository needs to become a public documentation source for cPanel API surface tests. The documentation should be clean enough for SecuredMe website quality expectations, but simple enough to remain a mostly-Markdown evidence system.

## Reasons

MkDocs Material was selected because:

- documentation content stays in Markdown
- navigation is explicit
- GitHub Pages deployment is straightforward
- local builds are fast
- the theme is professional without requiring a custom frontend app
- search and code-copy features are available

## Consequences

The repository needs a few non-Markdown support files:

- `mkdocs.yml`
- `requirements-docs.txt`
- `.github/workflows/docs.yml`
- a small SVG mark

All substantive documentation remains Markdown under `docs/`.

