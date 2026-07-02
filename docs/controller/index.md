# SecuredMe Education Controller

`securedme-education-controller` is the local control plugin for the SecuredMe Education MVP suite.

It coordinates:

- Education mesh registry reads
- cPanel action plans
- GitHub repository and webhook plans
- MkDocs publication plans
- plugin and connector routing
- short-lived local controller sessions

The controller does not replace the existing plugins. It routes to them and keeps live writes gated.

## Current MCP Tools

```text
controller_health
controller_session_start
controller_session_close
controller_plugin_registry
controller_route_plan
controller_github_repo_status
controller_github_webhook_plan
controller_cpanel_github_hook_plan
controller_docs_publish_plan
```

Additional safe read tools expose cPanel domains and Education mesh status.

## Policy

Default mode is dry-run. Live writes require explicit execution intent and an active session.
