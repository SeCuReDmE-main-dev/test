# SecuredMe Education Plugin Capability Matrix

This public matrix teaches users how to validate the SecuredMe Education plugin stack without guessing, leaking secrets, or drifting across unrelated workspaces.

## Canonical Surfaces

| Surface | Domain | Local path |
| --- | --- | --- |
| Synthia | `synthia.securedme.ca` | `C:\Users\jeans\Desktop\Case study\modele\Synthia\Synthia` |
| AlgoQuest | `algoquest.securedme.ca` | `C:\Users\jeans\Desktop\Case study\modele\algoquest-ams-discovry-labs-module-` |
| Algorithm Builder | `algorithm-builder.securedme.ca` | `C:\Users\jeans\Desktop\Case study\modele\algorithm-builder-app` |
| CeLeBrUm Model Server | `celebrum-model.securedme.ca` | `C:\Users\jeans\Desktop\Case study\modele\celebrum-model-server` |
| FfeD QLC MVP | `ffed-qlc.securedme.ca` | `C:\Users\jeans\Desktop\Case study\modele\FfeD-QLC-MVP` |
| FNP-QNN MVP | `fnpqnn.securedme.ca` | `C:\Users\jeans\Desktop\Case study\modele\FNP-QNN-MVP\FNP-QNN-MVP` |
| Market Guardian RetailGuard | `market-guardian.securedme.ca` | `C:\Users\jeans\Desktop\Case study\modele\market-guardian-retailguard` |
| QuaNThoR | `quanthor.securedme.ca` | `C:\Users\jeans\Desktop\Case study\modele\QuaNThoR` |
| SecuredMe Scholarium | `scholarium.securedme.ca` | `C:\Users\jeans\Desktop\Case study\modele\securedme-scholarium` |
| Tesla Workbench | `tesla-workbench.securedme.ca` | `C:\Users\jeans\Desktop\Case study\modele\tesla-resonance-recovery-workbench` |
| V.O.T Guardian | `vot-guardian.securedme.ca` | `C:\Users\jeans\Desktop\Case study\modele\V.O.T-Guardian` |
| Visual Algorithm Designer | `visual-algorithm.securedme.ca` | `C:\Users\jeans\Desktop\Case study\modele\VisualAlgorithmDesigner` |

## Test Matrix

| ID | Action | Plugin | Mode | Target |
| --- | --- | --- | --- | --- |
| #1 | [Prompt-governance envelope](001-prompt-governance-envelope.md) | `codex-memory-systeme` | `read` | modele governance |
| #2 | [Live authorization boundary](002-live-authorization-boundary.md) | `securedme-education-controller` | `read` | controller safety policy |
| #3 | [Plugin manifest inventory](003-plugin-manifest-inventory.md) | `securedme-education-controller` | `read` | four plugin manifests |
| #4 | [Loaded tool surface comparison](004-loaded-tool-surface-comparison.md) | `codex-memory-systeme` | `read` | current Codex tool surface |
| #5 | [Hierarchy preservation](005-df-hierarchy-preservation.md) | `codex-memory-systeme` | `read` | prompt hierarchy |
| #6 | [Secret redaction scan](006-secret-redaction-scan.md) | `securedme-cpanel-operator` | `read` | generated public artifacts |
| #7 | [Drive RAG folder readback](007-drive-rag-folder-readback.md) | `codex-memory-systeme` | `live-read` | SECUREDME_RAG_PLAYGROUND |
| #8 | [Strict prompt-template portability](008-strict-prompt-template-portability.md) | `architecte-zero` | `read` | prompt catalog |
| #9 | [Memory health](009-memory-health.md) | `codex-memory-systeme` | `live-read` | local memory MCP |
| #10 | [Daily tool catalog](010-daily-tool-catalog.md) | `codex-memory-systeme` | `live-read` | daily operator |
| #11 | [Daily task routing](011-daily-task-routing.md) | `codex-memory-systeme` | `live-read` | daily_route_task |
| #12 | [Memory search and fetch](012-memory-search-fetch.md) | `codex-memory-systeme` | `live-read` | SecuredMe context |
| #13 | [RAG research session start](013-rag-research-session-start.md) | `codex-memory-systeme` | `gated-write` | RAG evidence session |
| #14 | [Pending redacted RAG capture](014-pending-redacted-rag-capture.md) | `codex-memory-systeme` | `gated-write` | public-safe evidence |
| #15 | [RAG publication export candidate](015-rag-publication-export-candidate.md) | `codex-memory-systeme` | `live-read` | publication pack |
| #16 | [Drive intake routing](016-drive-intake-routing.md) | `codex-memory-systeme` | `live-read` | Google Drive workflow |
| #17 | [cPanel MCP smoke](017-cpanel-mcp-smoke.md) | `securedme-cpanel-operator` | `live-read` | cPanel MCP server |
| #18 | [cPanel health](018-cpanel-health.md) | `securedme-cpanel-operator` | `live-read` | cPanel operator |
| #19 | [cPanel env audit](019-cpanel-env-audit.md) | `securedme-cpanel-operator` | `live-read` | modele .env envelope |
| #20 | [cPanel domain list authority](020-cpanel-domain-list-authority.md) | `securedme-cpanel-operator` | `live-read` | cPanel PDF/domain list |
| #21 | [cPanel domain inventory](021-cpanel-domain-inventory.md) | `securedme-cpanel-operator` | `live-read` | securedme.ca domains |
| #22 | [12-surface suite registry](022-securedme-suite-registry.md) | `securedme-cpanel-operator` | `live-read` | Education suite registry |
| #23 | [Domain mismatch report](023-domain-mismatch-report.md) | `securedme-cpanel-operator` | `live-read` | README/domain claims |
| #24 | [DNS zone read or dry-run](024-dns-zone-read-dry-run.md) | `securedme-cpanel-operator` | `dry-run` | securedme.ca DNS |
| #25 | [SSL status read](025-ssl-status-read.md) | `securedme-cpanel-operator` | `live-read` | test.securedme.ca |
| #26 | [Email inventory read](026-email-inventory-read.md) | `securedme-cpanel-operator` | `live-read` | securedme.ca mailboxes |
| #27 | [Subdomain dry-run and test-domain readback](027-subdomain-dry-run-readback.md) | `securedme-cpanel-operator` | `dry-run` | test.securedme.ca |
| #28 | [Deployment plan generation](028-deploy-plan-generation.md) | `securedme-cpanel-operator` | `dry-run` | docroot and Git deploy plans |
| #29 | [Education mesh registry and doctor](029-education-mesh-doctor.md) | `securedme-cpanel-operator` | `live-read` | Education mesh |
| #30 | [CodeProject mesh status and hook plan](030-codeproject-mesh-hook-plan.md) | `securedme-cpanel-operator` | `dry-run` | localhost:32168 mesh |
| #31 | [Controller MCP smoke](031-controller-mcp-smoke.md) | `securedme-education-controller` | `live-read` | controller MCP server |
| #32 | [Controller health](032-controller-health.md) | `securedme-education-controller` | `live-read` | controller_health |
| #33 | [Controller session TTL](033-controller-session-ttl.md) | `securedme-education-controller` | `gated-write` | session gate |
| #34 | [Controller plugin registry](034-controller-plugin-registry.md) | `securedme-education-controller` | `live-read` | plugin router |
| #35 | [Cross-plugin route plan](035-controller-route-plan.md) | `securedme-education-controller` | `dry-run` | controller_route_plan |
| #36 | [GitHub repo status token gate](036-github-repo-status-token-gate.md) | `securedme-education-controller` | `live-read` | GitHub route |
| #37 | [GitHub/cPanel webhook dry-run plans](037-webhook-dry-run-plans.md) | `securedme-education-controller` | `dry-run` | webhook bridge |
| #38 | [Docs publish plan and MkDocs strict build](038-docs-publish-plan-mkdocs.md) | `securedme-education-controller` | `dry-run` | test docs repo |
| #39 | [Controller cPanel domains and Education mesh bridge](039-controller-cpanel-mesh-bridge.md) | `securedme-education-controller` | `live-read` | controller bridge |
| #40 | [Architecte-Zero handoff across 12 surfaces](040-architecte-zero-handoff.md) | `architecte-zero` | `read` | 12 SecuredMe surfaces |

## Evidence Labels

- `confirmed by local code`: local repository or plugin files prove the claim.
- `confirmed by live read`: a connector or MCP read returned current state.
- `confirmed by dry-run`: a tool generated the plan without mutation.
- `blocked`: a dependency was missing and the exact blocker is recorded.
- `inferred from docs`: documentation supports the claim but live proof is not available yet.

## Live Modes

- `read`: local file inspection only.
- `live-read`: current external or MCP state is read without writes.
- `dry-run`: mutation-shaped plan is generated with execution disabled.
- `gated-write`: write is allowed only because this runbook explicitly authorizes the bounded action.
