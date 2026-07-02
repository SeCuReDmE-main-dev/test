# Validation Report

Run: `RUN_028_SECUREDME_PLUGIN_CAPABILITY_MATRIX_2026-07-02`

## Results

| Check | Command | Result |
| --- | --- | --- |
| Matrix schema, notebooks, docs, staging, and redaction scan | `python scripts\validate_plugin_capability_matrix.py` | Passed: `VALIDATION_OK: plugin capability matrix` |
| MkDocs strict build | `python -m mkdocs build --strict` | Passed |
| Education Controller plugin tests | `python -m pytest tests -q` | Passed: 17 tests |
| cPanel Operator plugin tests | `python -m pytest tests -q` | Passed: 15 tests |
| Plugin manifest validation | `python ...\plugin-creator\scripts\validate_plugin.py C:\Users\jeans\plugins\securedme-education-controller` | Passed |
| Plugin cache reinstall | `codex plugin add securedme-education-controller@local-codex-plugins` | Passed: installed `0.1.0+codex.20260702035132` |
| Installed-cache registry smoke | JSON parse of installed `commands\plugin_capability_tests.json` | Passed: 40 tests, first slug `prompt-governance-envelope`, last slug `architecte-zero-handoff` |
| Drive readback | Google Drive folder listing | Passed: root package 10 items, notebooks 41, docs 3, command registry 5 |

## Notes

- MkDocs reported that the 40 individual test detail pages are linked from the matrix index but not listed individually in navigation. This is intentional: the public nav exposes the matrix overview, prompt catalog, and eight grouped pages to keep onboarding readable.
- The generated public artifact scan looks for token, password, secret, private key, cookie, and cPanel session URL patterns.
- Destructive cPanel and GitHub mutations are outside this run.
- Drive package: https://drive.google.com/drive/folders/1p582FA0n0IKvoPpidbCuVXfVg9TqxfR0
