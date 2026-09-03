from __future__ import annotations
import math
from .qc import parse_censored_value


def convert_concentration(value, from_unit: str, to_unit: str):
    """Convert between ppm and ppb for numeric concentrations."""
    if value is None:
        return None
    f, t = from_unit.lower(), to_unit.lower()
    if f == t:
        return float(value)
    if f == "ppm" and t == "ppb":
        return float(value) * 1000.0
    if f == "ppb" and t == "ppm":
        return float(value) / 1000.0
    raise ValueError(f"Unsupported conversion: {from_unit} -> {to_unit}")


def harmonize_result(raw, from_unit: str, to_unit: str):
    """Harmonize a result while preserving censor semantics."""
    parsed = parse_censored_value(raw)
    value = convert_concentration(parsed["value"], from_unit, to_unit)
    limit = convert_concentration(parsed["limit"], from_unit, to_unit)
    return {**parsed, "value": value, "limit": limit, "unit": to_unit}


def safe_ratio(a, b):
    if a is None or b is None or b == 0:
        return None
    return float(a) / float(b)


def log10_positive(x):
    if x is None or x <= 0:
        return None
    return math.log10(float(x))
