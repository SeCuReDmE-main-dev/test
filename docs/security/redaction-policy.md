# Redaction Policy

This public repository must never expose operational secrets.

## Never Publish

- `.env` files
- API tokens
- passwords
- private keys
- SSH keys
- webhook secrets
- mailbox passwords
- cPanel session URLs
- raw credential exports
- raw private cPanel PDFs
- deployment archives
- private support or billing data

## Safe To Publish

When needed, these can be published:

- domain names intentionally under test
- redacted status fields
- HTTP status codes
- UAPI status codes
- count summaries
- non-secret document root names
- test IDs
- public repository links

## Redaction Standard

Use placeholders:

```text
<redacted>
<private>
<not published>
```

Do not publish hashes of secrets unless there is a specific reason. A hash can still become operationally sensitive when used as a fingerprint.

