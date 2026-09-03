from drillcore_workflow.integration import assign_dominant_lithology, empirical_percentile


def test_dominant_lithology_tier_a():
    sample = {"hole_id":"H1","from_m":2,"to_m":4}
    intervals = [{"hole_id":"H1","from_m":0,"to_m":10,"lithology":"gabbro"}]
    r = assign_dominant_lithology(sample, intervals)
    assert r["lithology"] == "gabbro"
    assert r["confidence_tier"] == "A"


def test_empirical_percentile_midrank():
    p = empirical_percentile([1,2,3,4], 3)
    assert p == 62.5
