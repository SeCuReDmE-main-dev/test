# Documentation Standard

Every public test report must be written so another operator can understand what happened without seeing private credentials.

## Required Sections

Each test report should include:

- objective
- scope
- tool or API surface
- authorization mode
- preflight checks
- dry-run result
- live execution result, if authorized
- verification result
- redacted evidence
- risk notes
- next action

## Evidence Labels

Use these labels consistently:

| Label | Meaning |
| --- | --- |
| `confirmed by live cPanel API` | The result came from a live cPanel read or write response. |
| `confirmed by cPanel UI` | The result was visible in the browser cPanel interface. |
| `confirmed by local plugin test` | The result came from local plugin tests or unit tests. |
| `planned` | The test is documented but not executed. |
| `blocked` | Execution could not proceed. |

## Public Wording

Avoid overclaiming. Domain existence does not mean production readiness.

Use:

- `domain exists`
- `API readback confirmed`
- `document root assigned`
- `SSL not yet reviewed`
- `public readiness not established`

Do not use:

- `production-ready`
- `student-data-ready`
- `secure by default`
- `certified`
- `fully deployed`

