from drillcore_workflow.qc import parse_censored_value, validate_intervals


def test_censored_value_is_not_imputed():
    r = parse_censored_value("<5")
    assert r["value"] is None
    assert r["limit"] == 5.0
    assert r["censor"] == "<"


def test_interval_gap_detection():
    rows = [
        {"hole_id":"H1","from_m":0,"to_m":10},
        {"hole_id":"H1","from_m":12,"to_m":20},
    ]
    issues = validate_intervals(rows)
    assert any(x["issue"] == "gap" and x["magnitude_m"] == 2 for x in issues)
