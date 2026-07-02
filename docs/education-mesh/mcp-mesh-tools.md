# MCP Mesh Tools

The SecuredMe cPanel Operator now exposes Education mesh tools.

| Tool | Purpose |
| --- | --- |
| `education_mesh_registry` | Return the bounded 11-repo Education registry. |
| `education_mesh_doctor` | Check scope, exclusions, and mesh readiness. |
| `education_repo_mesh_readiness` | Inspect one or all repos for CodeProject mesh markers. |
| `education_codeproject_status` | Dry-run or execute read-only CodeProject.AI status probes. |
| `education_codeproject_mesh_status` | Dry-run or execute mesh transport diagnostics. |
| `education_mesh_hook_plan` | Generate an app-to-CodeProject hook plan without mutation. |

These tools do not import the true internal runtime stack.

