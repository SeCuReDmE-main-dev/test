# API Surface Overview

This section maps the SecuredMe cPanel operator capability surface.

## Capability Groups

| Group | Purpose | Current Public Status |
| --- | --- | --- |
| Health and environment audit | Confirm access readiness without printing secrets. | Active |
| Domain inventory | Compare cPanel, PDF, and planned domains. | Active |
| Subdomain creation | Create authorized test subdomains. | Live-tested |
| DNS reads | Inspect cPanel zone records. | Planned |
| SSL reads | Inspect SSL and AutoSSL status. | Planned |
| Email reads | Inventory cPanel mailboxes. | Planned |
| Email creation | Create mailboxes using password values from `.env`. | Planned |
| Deployment planning | Plan File Manager or Git deployment routes. | Active as planning only |
| Education suite mapping | Compare app domains and readiness claims. | Active as documentation logic |
| SSH fallback planning | Prepare server-side UAPI commands without executing them. | Planning only |

## Default Execution Rule

Write operations must remain dry-run unless the user explicitly authorizes a live mutation for a specific target.

Read-only checks can be executed when the mission asks for live evidence, but outputs must still be redacted before publication.

