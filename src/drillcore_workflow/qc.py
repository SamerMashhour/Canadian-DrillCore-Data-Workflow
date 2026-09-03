from __future__ import annotations
import math
import re

_CENSOR_RE = re.compile(r"^\s*([<>])\s*([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?)\s*$")


def parse_censored_value(raw):
    """Parse numeric or qualified analytical results without inventing a measured value."""
    if raw is None or (isinstance(raw, float) and math.isnan(raw)):
        return {"raw": raw, "value": None, "limit": None, "censor": ""}
    text = str(raw).strip()
    if not text:
        return {"raw": raw, "value": None, "limit": None, "censor": ""}
    m = _CENSOR_RE.match(text)
    if m:
        return {"raw": raw, "value": None, "limit": float(m.group(2)), "censor": m.group(1)}
    try:
        return {"raw": raw, "value": float(text), "limit": None, "censor": ""}
    except ValueError:
        return {"raw": raw, "value": None, "limit": None, "censor": "unparsed"}


def validate_intervals(rows, hole_col="hole_id", from_col="from_m", to_col="to_m", tolerance=1e-9):
    """Validate ordering and within-hole gaps/overlaps for interval records."""
    grouped = {}
    for r in rows:
        grouped.setdefault(r[hole_col], []).append(r)
    issues = []
    for hole, items in grouped.items():
        clean = sorted(items, key=lambda r: float(r[from_col]))
        for r in clean:
            a, b = float(r[from_col]), float(r[to_col])
            if not (a >= 0 and b > a):
                issues.append({"hole_id": hole, "issue": "invalid_bounds", "from_m": a, "to_m": b})
        for prev, cur in zip(clean, clean[1:]):
            pto, cfrom = float(prev[to_col]), float(cur[from_col])
            delta = cfrom - pto
            if delta > tolerance:
                issues.append({"hole_id": hole, "issue": "gap", "from_m": pto, "to_m": cfrom, "magnitude_m": delta})
            elif delta < -tolerance:
                issues.append({"hole_id": hole, "issue": "overlap", "from_m": cfrom, "to_m": pto, "magnitude_m": -delta})
    return issues
