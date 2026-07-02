# 002: Education Scope Re-Bound

## Summary

The Education workspace was re-bounded to the 11 MVP repositories. The ambiguous internal model folders were moved out of `modele` and preserved at the Case study root.

Status: Passed

## Actions

- `ReaAaS-n` moved from `modele` to `Case study` root.
- `NeuUuR-o` moved from `modele` to `Case study` root.
- Scope exclusion notes were created.
- `education_scope.json` was added to the cPanel operator plugin.
- The gateway is treated as a component of `FNP-QNN-MVP`, not a separate app.

## Redacted Evidence

```text
modele_has_ReaAaS_n: false
modele_has_NeuUuR_o: false
education_repo_count: 11
gateway_counted_as_app: false
```

## Result

The MVP scope is now explicit and testable through the MCP mesh registry.

