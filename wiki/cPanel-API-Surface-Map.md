# cPanel API Surface Map

This map summarizes the current operator surface.

## Confirmed

| Surface | Status |
| --- | --- |
| cPanel authentication through token | Confirmed after API URL normalization |
| Subdomain creation | Confirmed with `test.securedme.ca` |
| Domain readback | Confirmed with `DomainInfo/list_domains` |
| Documentation publication | Confirmed through GitHub Pages |

## Planned

| Surface | Next Test |
| --- | --- |
| DNS zone read | `cpanel_parse_zone` |
| SSL status | `cpanel_ssl_status` |
| Email inventory | `cpanel_email_inventory` |
| Email creation | `cpanel_create_email` with env-backed password key |
| Deployment planning | `cpanel_file_upload_plan` and `cpanel_git_deploy_plan` |

## Safety Boundary

Write tools stay dry-run unless a specific live target is approved.

Destructive operations require stronger confirmation and a rollback plan.

