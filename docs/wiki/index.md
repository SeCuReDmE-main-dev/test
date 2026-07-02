# Wiki Home

This wiki turns the `SeCuReDmE-main-dev/test` repository into a source of truth for cPanel API surface testing.

## Wiki Purpose

The wiki captures:

- what was tested
- which tool or API surface was used
- what evidence was collected
- which actions were live mutations
- what risks or limits remain
- what should be tested next

## Main Pages

| Page | Purpose |
| --- | --- |
| [Navigation Map](navigation-map.md) | Explains the documentation structure. |
| [Documentation Standard](documentation-standard.md) | Defines how each test report should be written. |
| [Test Index](../tests/index.md) | Lists executed and planned tests. |
| [API Surface](../api-surface/index.md) | Maps plugin capability to cPanel API surfaces. |
| [Public Test Protocol](../runbooks/public-test-protocol.md) | Defines the dry-run, execute, verify, report loop. |
| [Redaction Policy](../security/redaction-policy.md) | Defines what can never be published. |

## Source Priority

1. Live cPanel API result, when execution was explicitly authorized.
2. cPanel browser UI confirmation.
3. Local plugin test output.
4. Current cPanel PDF export.
5. Local SecuredMe docs and README files.

## Public Claim Standard

Public documentation should use conservative wording:

- `passed` only when evidence exists
- `planned` when the test is not executed
- `blocked` when a dependency prevents execution
- `not public-ready` when a domain exists but app, auth, SSL, or safety review is incomplete

