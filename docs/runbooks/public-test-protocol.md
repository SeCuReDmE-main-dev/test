# Public Test Protocol

Use this protocol for every public cPanel operator test.

## Procedure

1. Define one target.
2. Confirm whether the operation is read-only or write.
3. Run health and env audit without printing secrets.
4. Run dry-run for any mutation.
5. Ask for or confirm explicit authorization before a live write.
6. Execute only the approved operation.
7. Verify through a separate readback path.
8. Write a redacted Markdown report.
9. Build docs with `python -m mkdocs build --strict`.
10. Commit and push.

## Minimum Evidence

Every completed test should include:

- target
- tool/API surface
- dry-run result
- live status if executed
- verification method
- public-safe result
- remaining risks

