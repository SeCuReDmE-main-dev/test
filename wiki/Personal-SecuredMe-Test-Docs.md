# Personal SecuredMe Test Docs

This page indexes personal SecuredMe test documentation that is safe to publish.

Personal means the notes are tailored to the SecuredMe operator workflow. It does not mean private data can be published.

## Active Threads

| Thread | Status | Link |
| --- | --- | --- |
| cPanel operator lab | Active | [cPanel API Surface Map](cPanel-API-Surface-Map) |
| First subdomain write | Passed | [Test 001](Test-001-cPanel-Subdomain-Creation) |
| DNS readback | Planned | Main docs roadmap |
| SSL readback | Planned | Main docs roadmap |
| Email inventory | Planned | Main docs roadmap |

## Public-Safe Rule

Allowed:

- target domains
- redacted status fields
- HTTP/UAPI status codes
- summarized test results
- non-secret document root names

Not allowed:

- tokens
- passwords
- `.env`
- cPanel session URLs
- raw private exports
- raw operational logs

