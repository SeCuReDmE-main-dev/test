# Test Index

This page tracks executed and planned cPanel operator tests.

## Executed Tests

| ID | Test | Target | Status | Report |
| --- | --- | --- | --- | --- |
| 001 | cPanel subdomain creation | `test.securedme.ca` | Passed | [Report](001-cpanel-subdomain-create.md) |
| 002 | Education scope re-bound | 11 MVP repositories | Passed | [Report](002-education-scope-rebound.md) |
| 003 | CodeProject mesh dry-run | `http://localhost:32168` | Passed | [Report](003-codeproject-mesh-dry-run.md) |

## Planned Tests

| ID | Test | Target | Status |
| --- | --- | --- | --- |
| 004 | DNS zone read | `securedme.ca` | Planned |
| 005 | SSL status read | `test.securedme.ca` | Planned |
| 006 | Email inventory read | `securedme.ca` mailboxes | Planned |
| 007 | Deployment plan | `test.securedme.ca` docroot | Planned |
| 008 | Education suite mismatch report | SecuredMe app domains | Planned |

## Test Lifecycle

| State | Meaning |
| --- | --- |
| Planned | The report shape exists, but the test has not run. |
| Dry-run passed | The operator generated a safe plan, but no live mutation occurred. |
| Passed | Live execution or live readback succeeded with public-safe evidence. |
| Failed | Execution completed but did not meet expected result. |
| Blocked | Execution could not proceed due to missing access, permissions, or unclear authorization. |
