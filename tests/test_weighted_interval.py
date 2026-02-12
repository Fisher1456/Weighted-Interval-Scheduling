from scheduling.io import load_jobs_csv
from scheduling.weighted_interval import solve_weighted_interval, has_overlaps

def test_tiny_csv_optimal_is_valid():
    jobs = load_jobs_csv("data/test_tiny.csv")
    best, selected = solve_weighted_interval(jobs)
    assert not has_overlaps(selected)
    assert best == sum(j.weight for j in selected)

def test_empty():
    best, selected = solve_weighted_interval([])
    assert best == 0.0
    assert selected == []
