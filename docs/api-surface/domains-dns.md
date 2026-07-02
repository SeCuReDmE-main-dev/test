# Domains And DNS

Domain and DNS tests validate what exists in cPanel and what is publicly resolvable or ready for launch.

## Domain Checks

Current proven domain:

`test.securedme.ca`

Confirmed through:

- cPanel browser UI
- `DomainInfo/list_domains`

## DNS Checks

Planned DNS tests:

- root A record
- `www`
- `mail`
- MX records
- SPF
- DKIM
- DMARC
- Cloudflare and WHC routing notes

## Public Safety Boundary

A DNS record or cPanel domain does not mean the service is public-ready.

Before public launch, each surface needs:

- SSL check
- content review
- auth boundary review when applicable
- noindex or placeholder policy when needed
- rollback plan

