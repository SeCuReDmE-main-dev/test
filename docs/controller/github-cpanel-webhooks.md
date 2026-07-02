# GitHub cPanel Webhooks

The controller can plan a GitHub webhook that sends repository events to a local controller endpoint.

Supported flow:

1. inspect repository metadata
2. prepare a webhook dry-run plan
3. validate HMAC signatures when a webhook secret is configured
4. store webhook event records with redacted payloads
5. route event handling toward cPanel or documentation action plans

## Safety

Webhook creation is dry-run by default. A live webhook create requires an active controller session and explicit execution.

The controller never publishes GitHub tokens, webhook secrets, cPanel API tokens, mailbox passwords, or cPanel session URLs.
