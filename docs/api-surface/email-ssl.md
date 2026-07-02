# Email And SSL

Email and SSL tests are read-first surfaces.

## SSL

Planned checks:

- SSL installed-host status
- AutoSSL readiness
- certificate coverage for `test.securedme.ca`
- WHC origin SSL status
- Cloudflare mode assumptions

Recommendation policy:

- do not recommend Flexible SSL as the target mode
- prefer valid origin SSL and Full or Full Strict when Cloudflare is involved

## Email

Planned checks:

- mailbox inventory
- routing state
- MX records
- SPF
- DKIM
- DMARC

Mailbox creation rule:

- use password values from `.env` only
- never pass a literal password in chat
- never commit mailbox credentials

