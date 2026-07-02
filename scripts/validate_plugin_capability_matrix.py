from __future__ import annotations

import json
import re
import sys
from pathlib import Path


TEST_ROOT = Path(r"C:\Users\jeans\Desktop\Case study\test")
CONTROLLER_ROOT = Path(r"C:\Users\jeans\plugins\securedme-education-controller")
RUN_ID = "RUN_028_SECUREDME_PLUGIN_CAPABILITY_MATRIX_2026-07-02"

FORBIDDEN_PATTERNS = [
    re.compile(pattern, re.IGNORECASE)
    for pattern in [
        r"CPANEL_API_TOKEN\s*=",
        r"DATADOG_API_KEY\s*=",
        r"OPENAI_API_KEY\s*=",
        r"GITHUB_TOKEN\s*=",
        r"password\s*=",
        r"secret\s*=",
        r"private[_-]?key\s*=",
        r"cookie\s*=",
        r"cpsess\d+",
    ]
]


def fail(message: str) -> None:
    print(f"VALIDATION_FAIL: {message}")
    raise SystemExit(1)


def load_json(path: Path) -> object:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # pragma: no cover - command-line guard
        fail(f"{path} is not valid JSON: {exc}")


def validate_registry() -> list[dict[str, object]]:
    registry_path = CONTROLLER_ROOT / "commands" / "plugin_capability_tests.json"
    registry = load_json(registry_path)
    if not isinstance(registry, dict) or registry.get("run_id") != RUN_ID:
        fail("registry run_id mismatch")
    tests = registry.get("tests")
    if not isinstance(tests, list) or len(tests) != 40:
        fail("registry must contain exactly 40 tests")
    ids = [test.get("id") for test in tests if isinstance(test, dict)]
    slugs = [test.get("slug") for test in tests if isinstance(test, dict)]
    if ids != list(range(1, 41)):
        fail("registry ids must be #1-#40")
    if len(set(slugs)) != 40:
        fail("registry slugs must be unique")
    required = {
        "id",
        "slug",
        "name",
        "plugin",
        "target",
        "live_mode",
        "expected_command_or_tool",
        "expected_evidence",
        "pass_criteria",
        "fail_criteria",
        "blocked_criteria",
        "learning_objective",
        "reuse",
        "next_fabrication_step",
        "prompt",
    }
    for test in tests:
        missing = required.difference(test)
        if missing:
            fail(f"test #{test.get('id')} missing fields: {sorted(missing)}")
    return tests


def validate_notebooks(tests: list[dict[str, object]]) -> None:
    nb_dir = TEST_ROOT / "notebooks" / "plugin-capability-matrix"
    files = sorted(nb_dir.glob("*.ipynb"))
    if len(files) != 41:
        fail("expected 40 notebooks plus 000-template.ipynb")
    for path in files:
        data = load_json(path)
        if not isinstance(data, dict) or data.get("nbformat") != 4:
            fail(f"{path} is not a nbformat 4 notebook")
        cells = data.get("cells")
        if not isinstance(cells, list) or len(cells) < 8:
            fail(f"{path} must contain the required educational cells")


def validate_docs(tests: list[dict[str, object]]) -> None:
    docs_dir = TEST_ROOT / "docs" / "plugin-capability-matrix"
    required = [docs_dir / "index.md", docs_dir / "prompt-catalog.md"]
    required += [docs_dir / f"tests-{start:03d}-{start + 4:03d}.md" for start in range(1, 41, 5)]
    for test in tests:
        required.append(docs_dir / f"{int(test['id']):03d}-{test['slug']}.md")
    required += [
        TEST_ROOT / "docs" / "runbooks" / "securedme-education-first-week.md",
        TEST_ROOT / "docs" / "runbooks" / "prompting-and-fabrication-guide.md",
    ]
    missing = [str(path) for path in required if not path.exists()]
    if missing:
        fail(f"missing docs: {missing[:5]}")


def validate_staging() -> None:
    staging = TEST_ROOT / "drive-staging" / RUN_ID
    names = {"manifest.json", "matrix.json", "prompt-catalog.md", "public-summary.md", "runbook.md", "validation-report.md"}
    existing = {path.name for path in staging.glob("*") if path.is_file()}
    if not names.issubset(existing):
        fail(f"drive staging missing files: {sorted(names - existing)}")


def validate_secret_scan() -> None:
    scan_roots = [
        TEST_ROOT / "docs" / "plugin-capability-matrix",
        TEST_ROOT / "docs" / "runbooks",
        TEST_ROOT / "notebooks" / "plugin-capability-matrix",
        TEST_ROOT / "drive-staging" / RUN_ID,
        CONTROLLER_ROOT / "commands",
    ]
    for root in scan_roots:
        for path in root.rglob("*"):
            if path.is_file() and path.suffix.lower() in {".md", ".json", ".ipynb"}:
                text = path.read_text(encoding="utf-8", errors="ignore")
                for pattern in FORBIDDEN_PATTERNS:
                    if pattern.search(text):
                        fail(f"forbidden pattern {pattern.pattern!r} in {path}")


def main() -> int:
    tests = validate_registry()
    validate_notebooks(tests)
    validate_docs(tests)
    validate_staging()
    validate_secret_scan()
    print("VALIDATION_OK: plugin capability matrix")
    return 0


if __name__ == "__main__":
    sys.exit(main())
