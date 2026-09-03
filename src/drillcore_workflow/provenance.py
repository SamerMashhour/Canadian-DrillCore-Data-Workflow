from __future__ import annotations
from pathlib import Path
import hashlib
import csv


def sha256_file(path: str | Path) -> str:
    """Return a SHA-256 digest for a file."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def build_file_manifest(root: str | Path, relative_to: str | Path | None = None):
    """Return a publication-friendly file manifest for all files under *root*."""
    root = Path(root)
    base = Path(relative_to) if relative_to else root
    rows = []
    for p in sorted(x for x in root.rglob("*") if x.is_file()):
        rows.append({
            "path": str(p.relative_to(base)),
            "bytes": p.stat().st_size,
            "sha256": sha256_file(p),
        })
    return rows


def read_source_registry(path: str | Path):
    with open(path, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def registry_missing_identifiers(rows):
    """Return rows missing both an identifier and an authoritative URL."""
    return [r for r in rows if not (r.get("identifier") or r.get("official_url"))]
