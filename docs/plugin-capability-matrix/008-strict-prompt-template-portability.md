# #8: Strict prompt-template portability

## Purpose

Learn how a broad request becomes a bounded implementation or handoff prompt.

## Capability

| Field | Value |
| --- | --- |
| Plugin owner | `architecte-zero` |
| Target | prompt catalog |
| Live mode | `read` |
| Expected command or tool | `/securedme-education-controller:test strict-prompt-template-portability` |
| Expected evidence | template works outside Codex in Colab or Gemini |

## Acceptance

- Pass: The expected evidence is produced, redacted, and tied to the named target.
- Fail: The tool or artifact runs but contradicts the expected evidence or leaks unsafe material.
- Blocked: The target, credential, local service, or connector is unavailable and the exact blocker is recorded.

## Reuse

Copy the prompt for #8 and replace the target with your own repo, domain, or plugin surface.

## Next Fabrication Step

Turn this capability check into a repo-index or task-planner handoff for one app.

## Copy-Paste Prompt

```text
STRICT PATH CHECK REQUIRED

## Mission Correction
This run validates SecuredMe Education capability test #8: Strict prompt-template portability.

## Absolute Working Rule
Work from:
`C:\Users\jeans\Desktop\Case study\test`

Use the suite root only as an evidence source:
`C:\Users\jeans\Desktop\Case study\modele`

## Allowed Scope
- Plugin owner: `architecte-zero`
- Target: `prompt catalog`
- Live mode: `read`
- Expected evidence: template works outside Codex in Colab or Gemini

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
End with a compact result table and do not claim public-ready status unless the evidence proves it.
```

