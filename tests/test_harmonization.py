from drillcore_workflow.harmonization import harmonize_result, safe_ratio


def test_ppm_to_ppb_uncensored():
    r = harmonize_result("0.25", "ppm", "ppb")
    assert r["value"] == 250.0
    assert r["censor"] == ""


def test_ppm_to_ppb_censored_threshold():
    r = harmonize_result("<0.005", "ppm", "ppb")
    assert r["value"] is None
    assert r["limit"] == 5.0
    assert r["censor"] == "<"


def test_safe_ratio():
    assert safe_ratio(10, 2) == 5
    assert safe_ratio(10, 0) is None
