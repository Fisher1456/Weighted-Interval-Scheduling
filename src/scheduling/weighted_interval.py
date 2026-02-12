from bisect import bisect_right
from .model import Job

def _compute_previous_compatible_indices(jobs_sorted_by_end: list[Job]) -> list[int]:
    """
    For each job i, return p[i] = index of the rightmost job j (< i) with end <= start[i].
    If none exists, p[i] = -1.
    """
    ends = [j.end for j in jobs_sorted_by_end]
    p: list[int] = []
    for i, job in enumerate(jobs_sorted_by_end):
        # find rightmost end <= job.start among indices [0...i-1]
        idx = bisect_right(ends, job.start, 0, i) - 1
        p.append(idx)
    return p

def solve_weighted_interval(jobs: list[Job]) -> tuple[float, list[Job]]:
    """
    Returns (best_total_weight, selected_jobs) for the Weighted Interval Scheduling problem.
    """
    if not jobs:
        return 0.0, []

    jobs_sorted = sorted(jobs, key=lambda j: (j.end, j.start))
    p = _compute_previous_compatible_indices(jobs_sorted)

    n = len(jobs_sorted)
    dp = [0.0] * n
    take = [False] * n

    for i in range(n):
        include_weight = jobs_sorted[i].weight + (dp[p[i]] if p[i] != -1 else 0)
        exclude_weight = dp[i - 1] if i > 0 else 0
        if include_weight > exclude_weight:
            dp[i] = include_weight
            take[i] = True
        else:
            dp[i] = exclude_weight
            take[i] = False

    # Reconstruct solution
    selected: list[Job] = []
    i = n - 1
    while i >= 0:
        if take[i]:
            selected.append(jobs_sorted[i])
            i = p[i]
        else:
            i -= 1

    selected.reverse()
    return dp[-1], selected

def has_overlaps(selected_jobs: list[Job]) -> bool:
    """Utility to validate schedule."""
    if not selected_jobs:
        return False
    s = sorted(selected_jobs, key=lambda j: j.start)
    for a, b in zip(s, s[1:]):
        if a.end > b.start:
            return True
    return False
