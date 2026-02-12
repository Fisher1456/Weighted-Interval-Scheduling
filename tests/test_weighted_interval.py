from scheduling.io import load_jobs_csv
from scheduling.io import load_bsm_jobs_csv
from scheduling.weighted_interval import solve_weighted_interval, has_overlaps
from scheduling.heuristics import greedy_shortest_processing_time
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# def test_tiny_csv_optimal_is_valid():
#     jobs = load_jobs_csv(PROJECT_ROOT / "data" / "test_tiny.csv")
#     best, selected = solve_weighted_interval(jobs)
#     assert not has_overlaps(selected)
#     assert best == sum(j.weight for j in selected)
#
# def test_tiny_csv_known_optimum():
#     jobs = load_jobs_csv(PROJECT_ROOT / "data" / "test_tiny.csv")
#     best, selected = solve_weighted_interval(jobs)
#     assert best == 16
#     ids = {j.job_id for j in selected}
#     assert ids == {"A", "E"}

# def test_tiny_csv_greedy_earliest_finish():
#     jobs = load_jobs_csv(PROJECT_ROOT / "data" / "test_tiny.csv")
#     best, selected = greedy_earliest_deadline(jobs)
#     assert not has_overlaps(selected)
#     ids = {j.job_id for j in selected}
#     assert ids == {"A", "C", "D", "F"}

# def test_tiny_csv_greedy_earliest_deadline():
#     jobs = load_bsm_jobs_csv(PROJECT_ROOT / "data" / "test_tiny_BSM.csv")
#     l_max = greedy_earliest_deadline(jobs)
#     assert l_max == 3

def test_tiny_csv_greedy_shortest_processing_time():
    jobs = load_bsm_jobs_csv(PROJECT_ROOT / "data" / "test_tiny_BSM.csv")
    f_max = greedy_shortest_processing_time(jobs)
    assert f_max == 56

def test_empty():
    best, selected = solve_weighted_interval([])
    assert best == 0.0
    assert selected == []
