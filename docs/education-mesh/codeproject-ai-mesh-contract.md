# CodeProject.AI Mesh Contract

CodeProject.AI Server is treated as an HTTP backend and optional mesh target.

Default URL:

`http://localhost:32168`

## Contract

- Do not copy CodeProject.AI Server into any app.
- Do not import CodeProject.AI Server code.
- Do not edit CodeProject.AI `appsettings.json` from the MCP v1.
- Probe by URL only.
- Treat mesh as backend transport, not account authentication.

## MCP Tools

- `education_codeproject_status`
- `education_codeproject_mesh_status`
- `education_mesh_hook_plan`

All are dry-run by default unless an explicit `execute=true` read probe is requested.

