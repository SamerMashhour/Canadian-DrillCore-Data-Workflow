from __future__ import annotations
import math


def overlap_length(a0, a1, b0, b1):
    return max(0.0, min(float(a1), float(b1)) - max(float(a0), float(b0)))


def assign_dominant_lithology(sample, intervals, min_fraction=0.80):
    """Assign the lithology with maximum overlap and report boundary confidence."""
    s0, s1 = float(sample["from_m"]), float(sample["to_m"])
    length = s1 - s0
    overlaps = []
    for r in intervals:
        if r["hole_id"] != sample["hole_id"]:
            continue
        ol = overlap_length(s0, s1, r["from_m"], r["to_m"])
        if ol > 0:
            overlaps.append((ol, r["lithology"]))
    if not overlaps or length <= 0:
        return {"lithology": None, "dominant_fraction": 0.0, "confidence_tier": "unassigned"}
    overlaps.sort(reverse=True)
    dom_len, lith = overlaps[0]
    frac = dom_len / length
    if len(overlaps) == 1 and abs(dom_len - length) <= 1e-9:
        tier = "A"
    elif frac >= min_fraction:
        tier = "B"
    else:
        tier = "C"
    return {"lithology": lith, "dominant_fraction": frac, "confidence_tier": tier}


def empirical_percentile(reference_values, x):
    """Mid-rank empirical percentile in [0, 100]."""
    vals = [float(v) for v in reference_values if v is not None and math.isfinite(float(v))]
    if not vals or x is None:
        return None
    x = float(x)
    lt = sum(v < x for v in vals)
    eq = sum(v == x for v in vals)
    return 100.0 * (lt + 0.5 * eq) / len(vals)
