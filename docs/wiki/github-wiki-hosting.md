# GitHub Wiki Hosting

This repository uses a primary public documentation surface and keeps a GitHub Wiki mirror source ready.

| Surface | URL | Role |
| --- | --- | --- |
| MkDocs site | `https://securedme-main-dev.github.io/test/` | Full structured documentation site. |
| Hosted wiki section | `https://securedme-main-dev.github.io/test/wiki/` | Fast wiki navigation for test notes and operational summaries. |
| Native GitHub Wiki source mirror | `wiki/` | Markdown source ready to publish to `test.wiki.git` after GitHub initializes the native wiki repository. |

## Source Of Truth

The canonical documentation source remains in this repository.

| Source path | Published target |
| --- | --- |
| `docs/` | MkDocs Material site |
| `docs/wiki/` | Hosted wiki section inside the MkDocs site |
| `wiki/` | Native GitHub Wiki mirror source |

## Why Both Exist

MkDocs is the polished public documentation build.

The hosted wiki section is the quick reference layer for:

- test summaries
- personal SecuredMe test notes
- operator procedures
- current cPanel API surface status

## Native GitHub Wiki Status

The repository setting `has_wiki` is enabled, but GitHub has not initialized the separate `test.wiki.git` repository yet. Attempts to push the first page directly to `https://github.com/SeCuReDmE-main-dev/test.wiki.git` returned `Repository not found`.

Until the native Wiki is initialized from GitHub's web UI, the active public wiki is the hosted MkDocs section:

`https://securedme-main-dev.github.io/test/wiki/`

## Update Procedure

1. Update Markdown under `docs/` and, when needed, `wiki/`.
2. Build with `python -m mkdocs build --strict`.
3. Commit and push the repo.
4. After native GitHub Wiki initialization, push the `wiki/` mirror to `SeCuReDmE-main-dev/test.wiki.git`.
