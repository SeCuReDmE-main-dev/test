# 003: CodeProject Mesh Dry Run

## Summary

The cPanel operator plugin now includes Education mesh tools that can prepare CodeProject.AI Server probes without mutating the server or importing internal runtimes.

Status: Passed

## Target

Default CodeProject.AI URL:

`http://localhost:32168`

## Tools Added

- `education_codeproject_status`
- `education_codeproject_mesh_status`
- `education_mesh_hook_plan`

## Redacted Evidence

```text
status_probe_mode: dry_run
planned_status_endpoint: http://localhost:32168/v1/server/status
mesh_probe_mode: dry_run
tcp_probe_port: 32168
mutates_codeproject_config: false
```

## Result

The mesh contract is now represented by MCP tools. Live CodeProject.AI reads remain explicit and gated.

