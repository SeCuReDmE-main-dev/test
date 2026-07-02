# Navigation Map

This repository is organized as a documentation product, not as an app repository.

## Repository Root

| Path | Role |
| --- | --- |
| `README.md` | GitHub landing page and quick build instructions. |
| `mkdocs.yml` | Documentation navigation, theme, and build configuration. |
| `requirements-docs.txt` | Python dependency pin for the docs builder. |
| `.github/workflows/docs.yml` | GitHub Pages build and deploy workflow. |
| `.gitignore` | Blocks local secrets and generated artifacts. |
| `docs/` | Markdown documentation source. |

## Documentation Tree

| Path | Role |
| --- | --- |
| `docs/index.md` | Site home. |
| `docs/wiki/` | Wiki pages and documentation standards. |
| `docs/tests/` | Test reports and test index. |
| `docs/api-surface/` | cPanel API capability map. |
| `docs/runbooks/` | Repeatable operating procedures. |
| `docs/security/` | Public boundary and redaction rules. |
| `docs/status/` | Current state and roadmap. |
| `docs/decisions/` | Architecture decisions. |

## How To Add A Test

1. Add a test report under `docs/tests/`.
2. Add a row to `docs/tests/index.md`.
3. Link the test from `docs/status/current-state.md` if it changes current capability.
4. Build the docs with `python -m mkdocs build --strict`.
5. Commit and push.

