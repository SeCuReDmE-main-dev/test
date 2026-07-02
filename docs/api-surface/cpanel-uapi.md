# cPanel UAPI

The plugin uses cPanel UAPI for controlled operations.

## Confirmed Working Pattern

The effective API URL must be the cPanel service origin, not a browser session path.

Good shape:

```text
https://<cpanel-host>:2083/execute/<Module>/<function>
```

Bad shape for API calls:

```text
https://<cpanel-host>:2083/cpsess.../frontend/jupiter/...
```

The plugin now normalizes copied UI URLs to the API origin before calling UAPI.

## Known Working Calls

| Module | Function | Purpose | Status |
| --- | --- | --- | --- |
| `SubDomain` | `addsubdomain` | Create subdomain | Passed for `test.securedme.ca` |
| `DomainInfo` | `list_domains` | Verify domain inventory | Passed |

## Planned Calls

| Module | Function | Purpose |
| --- | --- | --- |
| `DNS` | `parse_zone` | Read DNS zone state |
| SSL-related module | installed host status | Check SSL and AutoSSL state |
| Email-related module | list mailboxes | Read mailbox inventory |
| Email-related module | add mailbox | Create mailbox from env-backed password |

## Public Output Rule

Do not publish full raw UAPI payloads when they include internal paths, operational details, or excessive DNS record data. Summarize the relevant status fields instead.

