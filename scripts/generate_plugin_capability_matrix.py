from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path


TEST_ROOT = Path(r"C:\Users\jeans\Desktop\Case study\test")
MODELE_ROOT = Path(r"C:\Users\jeans\Desktop\Case study\modele")
CONTROLLER_ROOT = Path(r"C:\Users\jeans\plugins\securedme-education-controller")
DRIVE_FOLDER_ID = "1Y5udIpKbRJ-vfXtvHXqM6GSrXrVOI0bm"
DRIVE_FOLDER_URL = f"https://drive.google.com/drive/folders/{DRIVE_FOLDER_ID}"
RUN_ID = "RUN_028_SECUREDME_PLUGIN_CAPABILITY_MATRIX_2026-07-02"


SURFACES = [
    ("Synthia", "synthia.securedme.ca", r"C:\Users\jeans\Desktop\Case study\modele\Synthia\Synthia"),
    ("AlgoQuest", "algoquest.securedme.ca", r"C:\Users\jeans\Desktop\Case study\modele\algoquest-ams-discovry-labs-module-"),
    ("Algorithm Builder", "algorithm-builder.securedme.ca", r"C:\Users\jeans\Desktop\Case study\modele\algorithm-builder-app"),
    ("CeLeBrUm Model Server", "celebrum-model.securedme.ca", r"C:\Users\jeans\Desktop\Case study\modele\celebrum-model-server"),
    ("FfeD QLC MVP", "ffed-qlc.securedme.ca", r"C:\Users\jeans\Desktop\Case study\modele\FfeD-QLC-MVP"),
    ("FNP-QNN MVP", "fnpqnn.securedme.ca", r"C:\Users\jeans\Desktop\Case study\modele\FNP-QNN-MVP\FNP-QNN-MVP"),
    ("Market Guardian RetailGuard", "market-guardian.securedme.ca", r"C:\Users\jeans\Desktop\Case study\modele\market-guardian-retailguard"),
    ("QuaNThoR", "quanthor.securedme.ca", r"C:\Users\jeans\Desktop\Case study\modele\QuaNThoR"),
    ("SecuredMe Scholarium", "scholarium.securedme.ca", r"C:\Users\jeans\Desktop\Case study\modele\securedme-scholarium"),
    ("Tesla Workbench", "tesla-workbench.securedme.ca", r"C:\Users\jeans\Desktop\Case study\modele\tesla-resonance-recovery-workbench"),
    ("V.O.T Guardian", "vot-guardian.securedme.ca", r"C:\Users\jeans\Desktop\Case study\modele\V.O.T-Guardian"),
    ("Visual Algorithm Designer", "visual-algorithm.securedme.ca", r"C:\Users\jeans\Desktop\Case study\modele\VisualAlgorithmDesigner"),
]


TESTS = [
    ("prompt-governance-envelope", "Prompt-governance envelope", "codex-memory-systeme", "modele governance", "read", "prompt-governance JSON readback"),
    ("live-authorization-boundary", "Live authorization boundary", "securedme-education-controller", "controller safety policy", "read", "live-read, dry-run, and gated-write boundaries stated"),
    ("plugin-manifest-inventory", "Plugin manifest inventory", "securedme-education-controller", "four plugin manifests", "read", "plugin names, versions, and public interfaces listed"),
    ("loaded-tool-surface-comparison", "Loaded tool surface comparison", "codex-memory-systeme", "current Codex tool surface", "read", "callable tools separated from installed-but-not-loaded tools"),
    ("df-hierarchy-preservation", "Hierarchy preservation", "codex-memory-systeme", "prompt hierarchy", "read", "I -> I_system^S -> D_f -> dF -> i_fractal preserved"),
    ("secret-redaction-scan", "Secret redaction scan", "securedme-cpanel-operator", "generated public artifacts", "read", "no token/password/secret/cookie/session URL in public files"),
    ("drive-rag-folder-readback", "Drive RAG folder readback", "codex-memory-systeme", "SECUREDME_RAG_PLAYGROUND", "live-read", "Drive metadata confirms target folder"),
    ("strict-prompt-template-portability", "Strict prompt-template portability", "architecte-zero", "prompt catalog", "read", "template works outside Codex in Colab or Gemini"),
    ("memory-health", "Memory health", "codex-memory-systeme", "local memory MCP", "live-read", "memory_health returns ready=true"),
    ("daily-tool-catalog", "Daily tool catalog", "codex-memory-systeme", "daily operator", "live-read", "catalog lists RAG, Drive, Docs, Architecte-Zero, and strategy groups"),
    ("daily-task-routing", "Daily task routing", "codex-memory-systeme", "daily_route_task", "live-read", "recommended route for Education runbook is RAG-first"),
    ("memory-search-fetch", "Memory search and fetch", "codex-memory-systeme", "SecuredMe context", "live-read", "relevant memory entries found or a blocked reason recorded"),
    ("rag-research-session-start", "RAG research session start", "codex-memory-systeme", "RAG evidence session", "gated-write", "pending session metadata created without publishing secrets"),
    ("pending-redacted-rag-capture", "Pending redacted RAG capture", "codex-memory-systeme", "public-safe evidence", "gated-write", "pending evidence card captured with redacted source"),
    ("rag-publication-export-candidate", "RAG publication export candidate", "codex-memory-systeme", "publication pack", "live-read", "candidate/export plan available or blocked with reason"),
    ("drive-intake-routing", "Drive intake routing", "codex-memory-systeme", "Google Drive workflow", "live-read", "Drive workflow uses folder ID and upload/readback convention"),
    ("cpanel-mcp-smoke", "cPanel MCP smoke", "securedme-cpanel-operator", "cPanel MCP server", "live-read", "initialize, tools/list, and cpanel_health smoke pass"),
    ("cpanel-health", "cPanel health", "securedme-cpanel-operator", "cPanel operator", "live-read", "health report returns env path and redacted readiness"),
    ("cpanel-env-audit", "cPanel env audit", "securedme-cpanel-operator", "modele .env envelope", "live-read", "env audit reports required keys without values"),
    ("cpanel-domain-list-authority", "cPanel domain list authority", "securedme-cpanel-operator", "cPanel PDF/domain list", "live-read", "domain authority source and counts recorded"),
    ("cpanel-domain-inventory", "cPanel domain inventory", "securedme-cpanel-operator", "securedme.ca domains", "live-read", "domain statuses classified with no private details"),
    ("securedme-suite-registry", "12-surface suite registry", "securedme-cpanel-operator", "Education suite registry", "live-read", "12 canonical surfaces listed"),
    ("domain-mismatch-report", "Domain mismatch report", "securedme-cpanel-operator", "README/domain claims", "live-read", "mismatches are report-only unless separately patched"),
    ("dns-zone-read-dry-run", "DNS zone read or dry-run", "securedme-cpanel-operator", "securedme.ca DNS", "dry-run", "zone read plan or live read result is redacted"),
    ("ssl-status-read", "SSL status read", "securedme-cpanel-operator", "test.securedme.ca", "live-read", "SSL status or blocked credential state recorded"),
    ("email-inventory-read", "Email inventory read", "securedme-cpanel-operator", "securedme.ca mailboxes", "live-read", "mailbox names/statuses only; no passwords"),
    ("subdomain-dry-run-readback", "Subdomain dry-run and test-domain readback", "securedme-cpanel-operator", "test.securedme.ca", "dry-run", "create plan plus existing test-domain readback"),
    ("deploy-plan-generation", "Deployment plan generation", "securedme-cpanel-operator", "docroot and Git deploy plans", "dry-run", "upload and Git deploy plans include rollback path"),
    ("education-mesh-doctor", "Education mesh registry and doctor", "securedme-cpanel-operator", "Education mesh", "live-read", "mesh registry and doctor output summarized"),
    ("codeproject-mesh-hook-plan", "CodeProject mesh status and hook plan", "securedme-cpanel-operator", "localhost:32168 mesh", "dry-run", "mesh status or blocked local service reason recorded"),
    ("controller-mcp-smoke", "Controller MCP smoke", "securedme-education-controller", "controller MCP server", "live-read", "initialize, tools/list, and safe calls pass"),
    ("controller-health", "Controller health", "securedme-education-controller", "controller_health", "live-read", "controller health reports local paths and no secrets"),
    ("controller-session-ttl", "Controller session TTL", "securedme-education-controller", "session gate", "gated-write", "session start/close works and expires safely"),
    ("controller-plugin-registry", "Controller plugin registry", "securedme-education-controller", "plugin router", "live-read", "plugin ownership boundaries listed"),
    ("controller-route-plan", "Cross-plugin route plan", "securedme-education-controller", "controller_route_plan", "dry-run", "route plan names owner plugin and next tool"),
    ("github-repo-status-token-gate", "GitHub repo status token gate", "securedme-education-controller", "GitHub route", "live-read", "token-gated status never leaks credentials"),
    ("webhook-dry-run-plans", "GitHub/cPanel webhook dry-run plans", "securedme-education-controller", "webhook bridge", "dry-run", "webhook and cPanel bridge plans return dry_run"),
    ("docs-publish-plan-mkdocs", "Docs publish plan and MkDocs strict build", "securedme-education-controller", "test docs repo", "dry-run", "docs publish plan and mkdocs strict build pass"),
    ("controller-cpanel-mesh-bridge", "Controller cPanel domains and Education mesh bridge", "securedme-education-controller", "controller bridge", "live-read", "controller bridge returns cPanel and mesh summaries"),
    ("architecte-zero-handoff", "Architecte-Zero handoff across 12 surfaces", "architecte-zero", "12 SecuredMe surfaces", "read", "repo-index/task-planner handoff prompt covers all surfaces"),
]


MICRO_ACTIONS = [
    "Confirm the public test repository exists.",
    "Confirm the SecuredMe modele suite root exists.",
    "Confirm the Education Controller plugin source exists.",
    "Confirm the cPanel Operator plugin source exists.",
    "Confirm the Codex Memory Systeme plugin source exists.",
    "Confirm the Architecte-Zero installed cache is readable.",
    "Read the live prompt-governance envelope.",
    "Record governance constraints in the public runbook.",
    "Confirm the Drive RAG folder ID.",
    "Verify Drive folder metadata readback.",
    "Create the public runbook folder in the test repo.",
    "Create the public notebook folder in the test repo.",
    "Create the staging folder for Drive uploads.",
    "Create the generated-artifacts manifest.",
    "Define the 12 SecuredMe surfaces as canonical.",
    "Mark the 11-repo controller registry as an implementation subset.",
    "Define evidence labels.",
    "Define live modes.",
    "Define redaction rules.",
    "Define public and private artifact boundaries.",
    "Extract the 40 test IDs into JSON.",
    "Add action slugs for all tests.",
    "Add plugin owner for each test.",
    "Add target repo or surface for each test.",
    "Add expected command or tool for each test.",
    "Add expected evidence for each test.",
    "Add pass, fail, and blocked criteria.",
    "Add user-facing learning objective.",
    "Add reusable user prompt field.",
    "Add next fabrication step field.",
    "Write the strict prompt template header.",
    "Add mission correction section.",
    "Add absolute CWD section.",
    "Add allowed scope section.",
    "Add anti-drift section.",
    "Add evidence standard section.",
    "Add live authorization section.",
    "Add redaction section.",
    "Add expected deliverables section.",
    "Add final answer contract section.",
]
MICRO_ACTIONS += [f"Generate prompt #{i}." for i in range(1, 41)]
MICRO_ACTIONS += [
    "Create MkDocs index page for the matrix.",
    "Create MkDocs page for tests #1-#5.",
    "Create MkDocs page for tests #6-#10.",
    "Create MkDocs page for tests #11-#15.",
    "Create MkDocs page for tests #16-#20.",
    "Create MkDocs page for tests #21-#25.",
    "Create MkDocs page for tests #26-#30.",
    "Create MkDocs page for tests #31-#35.",
    "Create MkDocs page for tests #36-#40.",
    "Add navigation entries to mkdocs.yml.",
    "Create notebook template.",
    "Add intro markdown cell.",
    "Add prompt cell.",
    "Add expected evidence cell.",
    "Add execution checklist cell.",
    "Add result capture cell.",
    "Add redaction reminder cell.",
    "Add user learning cell.",
    "Add next fabrication cell.",
    "Validate notebook template as JSON.",
]
MICRO_ACTIONS += [f"Generate notebook #{i}." for i in range(1, 41)]
MICRO_ACTIONS += [
    "Add public first-week onboarding page.",
    "Add Day 1: know the tools.",
    "Add Day 2: run safe reads.",
    "Add Day 3: run dry-runs.",
    "Add Day 4: read evidence.",
    "Add Day 5: adapt prompts.",
    "Add Day 6: build your first workflow.",
    "Add Day 7: publish your own runbook.",
    "Add visible progress checklist.",
    "Add user confidence milestones.",
    "Add public how to prompt Codex guide.",
    "Add public how to prompt Gemini/Colab guide.",
    "Add public how to read result evidence guide.",
    "Add public how to avoid secret leaks guide.",
    "Add public how to fork a prompt guide.",
    "Add public how to make your own test guide.",
    "Add public how to graduate from user to builder guide.",
    "Add glossary for plugins.",
    "Add glossary for RAG.",
    "Add glossary for dry-run/live-read/gated-write.",
    "Add commands/test.md to Education Controller.",
    "Add commands/test-matrix.md.",
    "Add commands/onboard.md.",
    "Add command convention notes.",
    "Add command registry JSON.",
    "Link commands to test IDs.",
    "Link commands to action slugs.",
    "Link commands to prompt bodies.",
    "Update plugin manifest default prompts.",
    "Preserve plugin safety wording.",
    "Run Education Controller tests.",
    "Run cPanel Operator tests.",
    "Run MkDocs strict build.",
    "Validate all notebooks parse.",
    "Run generated-link check.",
    "Run no-secret scan.",
    "Run Drive staging manifest check.",
    "Run plugin command file lint.",
    "Run registry schema validation.",
    "Run slash command lookup smoke.",
    "Create Drive folder for the run.",
    "Upload matrix JSON.",
    "Upload runbook Markdown.",
    "Upload prompt catalog.",
    "Upload all notebooks.",
    "Upload public summary.",
    "Upload validation report.",
    "Read back Drive folder listing.",
    "Read back key file metadata.",
    "Record Drive URLs locally.",
    "Update local dorsal memory summary.",
    "Add public-safe RAG evidence capture.",
    "Keep sensitive evidence pending/private.",
    "Commit test repo changes.",
    "Push test repo changes.",
    "Commit modele memory-backup changes.",
    "Push modele memory-backup changes.",
    "Commit Education Controller plugin changes.",
    "Run plugin cachebuster/reinstall flow.",
    "Produce final public handoff.",
]


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")


def slug_file(test: dict[str, object]) -> str:
    return f"{test['id']:03d}-{test['slug']}"


def test_prompt(test: dict[str, object]) -> str:
    return f"""STRICT PATH CHECK REQUIRED

## Mission Correction
This run validates SecuredMe Education capability test #{test['id']}: {test['name']}.

## Absolute Working Rule
Work from:
`C:\\Users\\jeans\\Desktop\\Case study\\test`

Use the suite root only as an evidence source:
`C:\\Users\\jeans\\Desktop\\Case study\\modele`

## Allowed Scope
- Plugin owner: `{test['plugin']}`
- Target: `{test['target']}`
- Live mode: `{test['live_mode']}`
- Expected evidence: {test['expected_evidence']}

## Anti-Drift Rule
Do not search unrelated workspaces. If the target path or tool is unavailable, mark the result as `blocked` and explain the exact missing dependency.

## Evidence Standard
Label each claim as one of:
- `confirmed by local code`
- `confirmed by live read`
- `confirmed by dry-run`
- `blocked`
- `inferred from docs`

## Redaction Rule
Never print tokens, passwords, private keys, cookies, mailbox passwords, raw `.env` values, cPanel session URLs, or full private exports.

## Expected Deliverables
1. status: `passed`, `failed`, or `blocked`
2. evidence summary
3. redaction confirmation
4. what a new user learned
5. next fabrication step

## Final Answer Contract
End with a compact result table and do not claim public-ready status unless the evidence proves it."""


def enrich_tests() -> list[dict[str, object]]:
    items: list[dict[str, object]] = []
    for index, (slug, name, plugin, target, live_mode, expected) in enumerate(TESTS, 1):
        prompt = test_prompt(
            {
                "id": index,
                "slug": slug,
                "name": name,
                "plugin": plugin,
                "target": target,
                "live_mode": live_mode,
                "expected_evidence": expected,
            }
        )
        items.append(
            {
                "id": index,
                "slug": slug,
                "name": name,
                "plugin": plugin,
                "target": target,
                "live_mode": live_mode,
                "expected_command_or_tool": expected_command_for(slug),
                "expected_evidence": expected,
                "pass_criteria": "The expected evidence is produced, redacted, and tied to the named target.",
                "fail_criteria": "The tool or artifact runs but contradicts the expected evidence or leaks unsafe material.",
                "blocked_criteria": "The target, credential, local service, or connector is unavailable and the exact blocker is recorded.",
                "learning_objective": learning_for(plugin, live_mode),
                "reuse": f"Copy the prompt for #{index} and replace the target with your own repo, domain, or plugin surface.",
                "next_fabrication_step": fabrication_for(plugin),
                "prompt": prompt,
            }
        )
    return items


def expected_command_for(slug: str) -> str:
    mapping = {
        "memory-health": "mcp__codex_memory_systeme.memory_health",
        "daily-tool-catalog": "mcp__codex_memory_systeme.daily_tool_catalog",
        "daily-task-routing": "mcp__codex_memory_systeme.daily_route_task",
        "drive-rag-folder-readback": "Google Drive metadata/readback",
        "cpanel-mcp-smoke": "python -m pytest tests/test_mcp_smoke.py -q",
        "controller-mcp-smoke": "python -m pytest tests/test_controller_mcp.py -q",
        "docs-publish-plan-mkdocs": "python -m mkdocs build --strict",
    }
    return mapping.get(slug, f"/securedme-education-controller:test {slug}")


def learning_for(plugin: str, live_mode: str) -> str:
    if plugin == "architecte-zero":
        return "Learn how a broad request becomes a bounded implementation or handoff prompt."
    if plugin == "codex-memory-systeme":
        return "Learn how RAG-first routing preserves context without over-trusting stale memory."
    if plugin == "securedme-cpanel-operator":
        return f"Learn how cPanel work is checked in {live_mode} mode without exposing credentials."
    return f"Learn how the Education Controller routes plugin work in {live_mode} mode."


def fabrication_for(plugin: str) -> str:
    if plugin == "architecte-zero":
        return "Turn this capability check into a repo-index or task-planner handoff for one app."
    if plugin == "codex-memory-systeme":
        return "Capture a redacted evidence card and decide whether it should stay pending or become public."
    if plugin == "securedme-cpanel-operator":
        return "Convert the result into a domain, DNS, SSL, email, or deploy runbook step."
    return "Convert the route plan into a safe controller command or dry-run automation."


def markdown_table(tests: list[dict[str, object]]) -> str:
    rows = ["| ID | Action | Plugin | Mode | Target |", "| --- | --- | --- | --- | --- |"]
    for test in tests:
        rows.append(
            f"| #{test['id']} | [{test['name']}]({slug_file(test)}.md) | `{test['plugin']}` | `{test['live_mode']}` | {test['target']} |"
        )
    return "\n".join(rows)


def write_matrix_docs(tests: list[dict[str, object]]) -> None:
    docs_dir = TEST_ROOT / "docs" / "plugin-capability-matrix"
    write(
        docs_dir / "index.md",
        f"""# SecuredMe Education Plugin Capability Matrix

This public matrix teaches users how to validate the SecuredMe Education plugin stack without guessing, leaking secrets, or drifting across unrelated workspaces.

## Canonical Surfaces

| Surface | Domain | Local path |
| --- | --- | --- |
{chr(10).join(f"| {name} | `{domain}` | `{path}` |" for name, domain, path in SURFACES)}

## Test Matrix

{markdown_table(tests)}

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
""",
    )
    for start in range(1, 41, 5):
        group = tests[start - 1 : start + 4]
        write(
            docs_dir / f"tests-{start:03d}-{start + 4:03d}.md",
            "# Capability Tests #{0}-#{1}\n\n".format(start, start + 4)
            + "\n\n".join(test_card(test, include_prompt=False) for test in group),
        )
    for test in tests:
        write(docs_dir / f"{slug_file(test)}.md", test_card(test, include_prompt=True))
    write(docs_dir / "prompt-catalog.md", prompt_catalog(tests))
    write(docs_dir / "generated-artifacts.json", json.dumps(manifest(tests), indent=2))


def test_card(test: dict[str, object], include_prompt: bool) -> str:
    prompt = ""
    if include_prompt:
        prompt = f"""
## Copy-Paste Prompt

```text
{test['prompt']}
```
"""
    return f"""# #{test['id']}: {test['name']}

## Purpose

{test['learning_objective']}

## Capability

| Field | Value |
| --- | --- |
| Plugin owner | `{test['plugin']}` |
| Target | {test['target']} |
| Live mode | `{test['live_mode']}` |
| Expected command or tool | `{test['expected_command_or_tool']}` |
| Expected evidence | {test['expected_evidence']} |

## Acceptance

- Pass: {test['pass_criteria']}
- Fail: {test['fail_criteria']}
- Blocked: {test['blocked_criteria']}

## Reuse

{test['reuse']}

## Next Fabrication Step

{test['next_fabrication_step']}
{prompt}
"""


def prompt_catalog(tests: list[dict[str, object]]) -> str:
    return "# Prompt Catalog\n\n" + "\n\n".join(
        f"## #{test['id']}: {test['name']}\n\n```text\n{test['prompt']}\n```" for test in tests
    )


def write_runbooks_and_guides(tests: list[dict[str, object]]) -> None:
    runbook = TEST_ROOT / "docs" / "runbooks" / "securedme-education-first-week.md"
    guide = TEST_ROOT / "docs" / "runbooks" / "prompting-and-fabrication-guide.md"
    write(runbook, first_week_runbook())
    write(guide, prompting_guide())
    index = TEST_ROOT / "docs" / "index.md"
    text = index.read_text(encoding="utf-8")
    marker = "- [Capability Matrix](plugin-capability-matrix/index.md): 40 public plugin capability tests and reusable prompts."
    if marker not in text:
        text = text.replace("## Documentation Areas\n\n", f"## Documentation Areas\n\n{marker}\n")
        index.write_text(text, encoding="utf-8", newline="\n")


def first_week_runbook() -> str:
    actions = "\n".join(f"{idx}. {action}" for idx, action in enumerate(MICRO_ACTIONS, 1))
    return f"""# SecuredMe Education First Week Runbook

This runbook is public by design. It is not hidden internal machinery. Its job is to help a new user see useful progress in the first week, understand the tools, and start making their own repeatable workflows.

## Week One Path

| Day | Focus | User-visible progress |
| --- | --- | --- |
| 1 | Know the tools | The user can name the four plugin surfaces and the 12 Education surfaces. |
| 2 | Run safe reads | The user can run read-only checks and understand evidence labels. |
| 3 | Run dry-runs | The user can produce cPanel, controller, GitHub, and docs plans without mutation. |
| 4 | Read evidence | The user can decide whether a result passed, failed, or was blocked. |
| 5 | Adapt prompts | The user can copy one strict prompt and retarget it safely. |
| 6 | Build a workflow | The user can combine two or three tests into a small personal workflow. |
| 7 | Publish a runbook | The user can produce a public-safe notebook and MkDocs page for their own task. |

## Progress Checklist

- [ ] I can explain `read`, `live-read`, `dry-run`, and `gated-write`.
- [ ] I can run one test from `#1-#40`.
- [ ] I can find the expected evidence.
- [ ] I can redact unsafe material.
- [ ] I can adapt one prompt to my own task.
- [ ] I can create a new notebook page from the template.
- [ ] I can publish a public-safe result.

## 200 Micro-Actions

{actions}
"""


def prompting_guide() -> str:
    return """# Prompting And Fabrication Guide

## How To Prompt Codex

Start with the exact workspace, the target plugin, the live mode, and the expected evidence. Ask Codex to mark every claim as confirmed, inferred, or blocked.

## How To Prompt Gemini Or Colab

Open the notebook, copy the strict prompt cell, and paste it into the AI environment. Keep the path and redaction rules visible so the assistant does not drift.

## How To Read Evidence

A result is useful only when it states where the evidence came from, what it proves, and what it does not prove yet.

## How To Avoid Secret Leaks

Never paste `.env` values, tokens, passwords, private keys, cookies, cPanel session URLs, mailbox passwords, or raw private exports. Use status fields and redacted summaries.

## How To Fork A Prompt

Change only the target surface, expected evidence, and final deliverable. Keep the absolute CWD, anti-drift rule, evidence standard, and redaction rule.

## How To Make Your Own Test

Pick one capability, define one target, choose one live mode, and write one pass criterion. If you cannot write the pass criterion, the test is not ready.

## How To Graduate From User To Builder

After you can run tests, combine them into a small workflow: read current state, generate a dry-run plan, capture evidence, publish a redacted notebook, then add a command for reuse.

## Glossary

- Plugin: a Codex capability bundle with skills, commands, and possibly MCP tools.
- RAG: retrieval-augmented context used to preserve evidence and reuse prior knowledge.
- Dry-run: a mutation-shaped plan with execution disabled.
- Live-read: a current state read without mutation.
- Gated-write: a bounded write that is explicitly authorized by a plan and validated afterward.
"""


def notebook(test: dict[str, object]) -> dict[str, object]:
    cells = [
        md(f"# #{test['id']}: {test['name']}\n\nPortable SecuredMe Education capability notebook."),
        md(f"## Prompt\n\n```text\n{test['prompt']}\n```"),
        md(f"## Expected Evidence\n\n{test['expected_evidence']}"),
        md(
            "## Execution Checklist\n\n"
            "- [ ] Confirm target path or tool.\n"
            "- [ ] Run only the allowed live mode.\n"
            "- [ ] Capture evidence label.\n"
            "- [ ] Redact unsafe material.\n"
            "- [ ] Record pass, fail, or blocked."
        ),
        md("## Result Capture\n\nStatus:\n\nEvidence label:\n\nEvidence summary:\n\nBlocked reason, if any:"),
        md("## Redaction Reminder\n\nDo not paste tokens, passwords, raw `.env` values, private keys, cookies, or cPanel session URLs."),
        md(f"## What The User Learns\n\n{test['learning_objective']}"),
        md(f"## Next Fabrication Step\n\n{test['next_fabrication_step']}"),
    ]
    return {
        "cells": cells,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "pygments_lexer": "ipython3"},
            "securedme": {"test_id": test["id"], "slug": test["slug"], "plugin": test["plugin"]},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def md(source: str) -> dict[str, object]:
    return {"cell_type": "markdown", "metadata": {}, "source": source.splitlines(keepends=True)}


def write_notebooks(tests: list[dict[str, object]]) -> None:
    nb_dir = TEST_ROOT / "notebooks" / "plugin-capability-matrix"
    for test in tests:
        write(nb_dir / f"{slug_file(test)}.ipynb", json.dumps(notebook(test), indent=2))
    template = tests[0].copy()
    template.update({"id": 0, "slug": "template", "name": "Reusable Capability Test Template"})
    write(nb_dir / "000-template.ipynb", json.dumps(notebook(template), indent=2))


def write_drive_staging(tests: list[dict[str, object]]) -> None:
    staging = TEST_ROOT / "drive-staging" / RUN_ID
    write(staging / "matrix.json", json.dumps({"run_id": RUN_ID, "tests": tests}, indent=2))
    write(staging / "prompt-catalog.md", prompt_catalog(tests))
    write(staging / "public-summary.md", public_summary(tests))
    write(staging / "validation-report.md", "# Validation Report\n\nGenerated before validation. Final command results are appended after checks run.\n")
    write(staging / "runbook.md", first_week_runbook())
    write(staging / "manifest.json", json.dumps(manifest(tests), indent=2))


def public_summary(tests: list[dict[str, object]]) -> str:
    return f"""# {RUN_ID}

This package contains a public SecuredMe Education capability matrix:

- 40 reusable tests
- 40 strict prompts
- 40 portable notebooks
- public MkDocs pages
- Education Controller command registry

Root Drive folder: {DRIVE_FOLDER_URL}

No secrets are intentionally included. All generated artifacts are public-safe training material.

## Plugin Counts

| Plugin | Tests |
| --- | --- |
{chr(10).join(f"| `{plugin}` | {sum(1 for t in tests if t['plugin'] == plugin)} |" for plugin in sorted({t['plugin'] for t in tests}))}
"""


def manifest(tests: list[dict[str, object]]) -> dict[str, object]:
    return {
        "run_id": RUN_ID,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "test_repo": str(TEST_ROOT),
        "modele_root": str(MODELE_ROOT),
        "controller_plugin": str(CONTROLLER_ROOT),
        "drive_folder_id": DRIVE_FOLDER_ID,
        "canonical_surface_count": len(SURFACES),
        "test_count": len(tests),
        "commands": [
            "/securedme-education-controller:test #1",
            "/securedme-education-controller:test cpanel-health",
            "/securedme-education-controller:test-matrix",
            "/securedme-education-controller:onboard",
        ],
        "tests": [{"id": t["id"], "slug": t["slug"], "name": t["name"], "plugin": t["plugin"]} for t in tests],
    }


def update_mkdocs() -> None:
    path = TEST_ROOT / "mkdocs.yml"
    text = path.read_text(encoding="utf-8")
    matrix_nav = """  - Capability Matrix:
      - Overview: plugin-capability-matrix/index.md
      - Prompt Catalog: plugin-capability-matrix/prompt-catalog.md
      - "Tests 001-005": plugin-capability-matrix/tests-001-005.md
      - "Tests 006-010": plugin-capability-matrix/tests-006-010.md
      - "Tests 011-015": plugin-capability-matrix/tests-011-015.md
      - "Tests 016-020": plugin-capability-matrix/tests-016-020.md
      - "Tests 021-025": plugin-capability-matrix/tests-021-025.md
      - "Tests 026-030": plugin-capability-matrix/tests-026-030.md
      - "Tests 031-035": plugin-capability-matrix/tests-031-035.md
      - "Tests 036-040": plugin-capability-matrix/tests-036-040.md
"""
    if "plugin-capability-matrix/index.md" not in text:
        text = text.replace("  - Personal Test Docs:\n", matrix_nav + "  - Personal Test Docs:\n")
    if "securedme-education-first-week.md" not in text:
        text = text.replace(
            "  - Runbooks:\n",
            "  - Runbooks:\n      - SecuredMe Education First Week: runbooks/securedme-education-first-week.md\n      - Prompting And Fabrication Guide: runbooks/prompting-and-fabrication-guide.md\n",
        )
    path.write_text(text, encoding="utf-8", newline="\n")


def write_plugin_commands(tests: list[dict[str, object]]) -> None:
    commands = CONTROLLER_ROOT / "commands"
    write(commands / "_conventions.md", command_conventions())
    write(commands / "test.md", command_test())
    write(commands / "test-matrix.md", command_matrix())
    write(commands / "onboard.md", command_onboard())
    write(commands / "plugin_capability_tests.json", json.dumps({"run_id": RUN_ID, "tests": tests}, indent=2))
    manifest_path = CONTROLLER_ROOT / ".codex-plugin" / "plugin.json"
    manifest_data = json.loads(manifest_path.read_text(encoding="utf-8"))
    prompts = manifest_data["interface"].setdefault("defaultPrompt", [])
    additions = [
        "/securedme-education-controller:test #1",
        "/securedme-education-controller:test cpanel-health",
        "/securedme-education-controller:test-matrix",
        "/securedme-education-controller:onboard",
    ]
    for item in additions:
        if item not in prompts:
            prompts.append(item)
    manifest_path.write_text(json.dumps(manifest_data, indent=2) + "\n", encoding="utf-8")


def command_conventions() -> str:
    return """# SecuredMe Education Controller Command Conventions

Command files live in `commands/` and end with `.md`. Files prefixed with `_` are documentation and are not exposed as slash commands.

Every public command must include:

- YAML frontmatter with `description`
- Preflight
- Plan
- Commands
- Verification
- Summary
- Next Steps

Commands must preserve the controller safety model: read first, dry-run before mutation, active session for gated writes, and no copied connector secrets.
"""


def command_test() -> str:
    return """---
description: Run or explain one SecuredMe Education capability test by ID or action slug.
argument-hint: [#1-#40-or-action-slug]
allowed-tools: [Read, Glob, Grep, Bash]
---

# /securedme-education-controller:test

Use `skills/securedme-education-controller/SKILL.md` and `commands/plugin_capability_tests.json`.

The user invoked this command with: $ARGUMENTS

## Preflight

Resolve `$ARGUMENTS` as either `#1` through `#40` or an action slug. If no argument is supplied, show the available IDs and ask for one target.

## Plan

Load the matching registry entry, preserve its live mode, and run only the bounded evidence procedure described in the prompt.

## Commands

Return the strict prompt, expected evidence, local target, live mode, and exact result-capture shape.

## Verification

Mark the result as `passed`, `failed`, or `blocked`. Confirm redaction before returning any evidence.

## Summary

Explain what a new user learned and what they can fabricate next.

## Next Steps

Suggest the next adjacent test from the matrix.
"""


def command_matrix() -> str:
    return """---
description: Show the complete SecuredMe Education plugin capability matrix.
argument-hint: [optional-plugin-or-mode-filter]
allowed-tools: [Read, Glob, Grep]
---

# /securedme-education-controller:test-matrix

Use `commands/plugin_capability_tests.json`.

The user invoked this command with: $ARGUMENTS

## Preflight

Load the matrix and apply any plugin or live-mode filter supplied by the user.

## Plan

Group tests by plugin owner and mode so users can see the learning path.

## Commands

Print the table with ID, slug, plugin, target, mode, and expected evidence.

## Verification

Confirm all IDs #1-#40 and slugs resolve uniquely.

## Summary

Return the shortest useful next action for a new user.

## Next Steps

Recommend `/securedme-education-controller:onboard` for first-week learning.
"""


def command_onboard() -> str:
    return """---
description: Start the public first-week SecuredMe Education onboarding path.
argument-hint: [optional-day-1-to-7]
allowed-tools: [Read, Glob, Grep]
---

# /securedme-education-controller:onboard

Use the public runbook at `C:\\Users\\jeans\\Desktop\\Case study\\test\\docs\\runbooks\\securedme-education-first-week.md`.

The user invoked this command with: $ARGUMENTS

## Preflight

Resolve the requested day. If none is supplied, start at Day 1.

## Plan

Show the day objective, the visible progress signal, and the tests that support that day.

## Commands

Provide the exact test commands or prompts to copy.

## Verification

Confirm the user can identify one evidence label and one next fabrication step.

## Summary

Keep the onboarding result public-safe and beginner-readable.

## Next Steps

Move to the next day or first blocked test.
"""


def write_dorsal_summary(tests: list[dict[str, object]]) -> None:
    path = MODELE_ROOT / "Short term memory modele" / "Dorsal pocket" / "securedme_plugin_capability_matrix_dorsal.md"
    write(
        path,
        f"""# SecuredMe Plugin Capability Matrix Dorsal Note

Run: `{RUN_ID}`

This note records the public runbook and notebook package for the 40-test SecuredMe Education plugin capability matrix.

## Public Locations

- Test repo docs: `C:\\Users\\jeans\\Desktop\\Case study\\test\\docs\\plugin-capability-matrix`
- Test repo notebooks: `C:\\Users\\jeans\\Desktop\\Case study\\test\\notebooks\\plugin-capability-matrix`
- Drive target folder: `{DRIVE_FOLDER_URL}`
- Controller plugin source: `C:\\Users\\jeans\\plugins\\securedme-education-controller`

## Boundaries

- Public artifacts contain prompts, expected evidence, and redacted guidance only.
- Real secret-bearing values remain local-only in the modele root `.env`.
- Destructive cPanel and GitHub mutations are outside this runbook.

## Counts

- Canonical Education surfaces: {len(SURFACES)}
- Capability tests: {len(tests)}
- Micro-actions: {len(MICRO_ACTIONS)}
""",
    )


def main() -> int:
    tests = enrich_tests()
    write_matrix_docs(tests)
    write_runbooks_and_guides(tests)
    write_notebooks(tests)
    write_drive_staging(tests)
    update_mkdocs()
    write_plugin_commands(tests)
    write_dorsal_summary(tests)
    print(json.dumps({"generated_tests": len(tests), "micro_actions": len(MICRO_ACTIONS), "run_id": RUN_ID}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
