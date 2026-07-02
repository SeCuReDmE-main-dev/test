# Public Boundary

The public boundary separates reusable operational knowledge from private SecuredMe infrastructure.

## Public

- test objectives
- safe test status
- target domain under test
- high-level API surface name
- redacted results
- build docs source
- public runbooks

## Private

- access tokens
- mailbox passwords
- cPanel sessions
- private `.env`
- private PDFs and cPanel exports
- unreleased app internals
- raw operational logs
- private deployment packages

## Domain Readiness Rule

A domain can be confirmed in cPanel without being public-ready.

Public-ready requires separate validation for:

- SSL
- DNS
- content
- authentication
- logging
- rollback
- safety wording

