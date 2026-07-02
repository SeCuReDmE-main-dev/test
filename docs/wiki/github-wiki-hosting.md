# GitHub Wiki Hosting

This repository uses two public documentation surfaces:

| Surface | URL | Role |
| --- | --- | --- |
| MkDocs site | `https://securedme-main-dev.github.io/test/` | Full structured documentation site. |
| GitHub Wiki | `https://github.com/SeCuReDmE-main-dev/test/wiki` | Fast wiki navigation for test notes and operational summaries. |

## Source Of Truth

The canonical documentation source remains in this repository.

| Source path | Published target |
| --- | --- |
| `docs/` | MkDocs Material site |
| `wiki/` | GitHub Wiki mirror |

## Why Both Exist

MkDocs is the polished public documentation build.

GitHub Wiki is the quick reference layer for:

- test summaries
- personal SecuredMe test notes
- operator procedures
- current cPanel API surface status

## Update Procedure

1. Update Markdown under `docs/` and, when needed, `wiki/`.
2. Build with `python -m mkdocs build --strict`.
3. Commit and push the repo.
4. Push the `wiki/` mirror to `SeCuReDmE-main-dev/test.wiki.git`.

