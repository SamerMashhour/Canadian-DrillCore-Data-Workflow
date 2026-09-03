from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

TEXT_SUFFIXES = {
    ".md", ".py", ".json", ".csv", ".yml", ".yaml", ".toml",
    ".txt", ".ipynb", ".cff", ".sql", ".svg",
}

# Keep the repository framed as an independent research workflow. Word boundaries
# prevent false positives such as "MERCHANTABILITY" in the MIT license.
FORBIDDEN_PATTERNS = {
    "MERC": re.compile(r"\bMERC\b", re.IGNORECASE),
    "Laurentian": re.compile(r"\bLaurentian\b", re.IGNORECASE),
    "Harquail": re.compile(r"\bHarquail\b", re.IGNORECASE),
    "CDCL": re.compile(r"\bCDCL\b", re.IGNORECASE),
    "Canadian Digital Core Library": re.compile(r"Canadian\s+Digital\s+Core\s+Library", re.IGNORECASE),
    "NRCan": re.compile(r"\bNRCan\b", re.IGNORECASE),
    "Natural Resources Canada": re.compile(r"Natural\s+Resources\s+Canada", re.IGNORECASE),
}

DISALLOWED_PUBLIC_SUFFIXES = {".zip", ".sqlite", ".db", ".xlsx", ".xls"}


def iter_text_files():
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if ".git" in path.parts or ".venv" in path.parts or "__pycache__" in path.parts:
            continue
        if path.suffix.lower() in TEXT_SUFFIXES or path.name in {"LICENSE", "requirements.txt"}:
            yield path


def main() -> int:
    failures: list[str] = []

    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.suffix.lower() in DISALLOWED_PUBLIC_SUFFIXES:
            failures.append(f"disallowed public file type: {path.relative_to(ROOT)}")

    for path in iter_text_files():
        text = path.read_text(encoding="utf-8", errors="ignore")
        for label, pattern in FORBIDDEN_PATTERNS.items():
            if pattern.search(text):
                failures.append(f"institution/program term '{label}' found in {path.relative_to(ROOT)}")

    required = [
        ROOT / "README.md",
        ROOT / "docs" / "WORKFLOW_MERMAID.md",
        ROOT / "docs" / "V0_3_SCIENTIFIC_SYNTHESIS.md",
        ROOT / "docs" / "V0_4_SCIENTIFIC_SYNTHESIS.md",
        ROOT / "releases" / "LINEAGE.md",
        ROOT / "releases" / "RELEASE_NOTES.md",
        ROOT / "data" / "examples" / "synthetic_assays.csv",
        ROOT / "notebooks" / "04_classification_benchmark_demo.ipynb",
    ]
    for path in required:
        if not path.exists():
            failures.append(f"required public-release file missing: {path.relative_to(ROOT)}")

    if failures:
        print("PUBLIC RELEASE VERIFICATION: FAIL")
        for item in failures:
            print(" -", item)
        return 1

    print("PUBLIC RELEASE VERIFICATION: PASS")
    print("Independent-project framing and public-release file checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
