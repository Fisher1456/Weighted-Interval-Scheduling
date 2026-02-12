import random
import time
from scheduling.model import Job
from scheduling.weighted_interval import solve_weighted_interval
from scheduling.heuristics import (
    greedy_earliest_finish,
    greedy_highest_weight,
    greedy_weight_density,
)

def generate_jobs(n: int, seed: int = 0) -> list[Job]:
    rng = random.Random(seed)
    jobs: list[Job] = []
    for i in range(n):
        start = rng.randint(0, 200)
        length = rng.randint(1, 30)
        end = start + length
        weight = rng.randint(1, 100)
        jobs.append(Job(job_id=f"J{i}", start=start, end=end, weight=weight))
    return jobs

def timed(fn, jobs):
    t0 = time.perf_counter()
    val, sol = fn(jobs)
    t1 = time.perf_counter()
    return val, sol, (t1 - t0)

def main():
    jobs = generate_jobs(200, seed=42)

    opt_val, _, opt_time = timed(solve_weighted_interval, jobs)
    g1_val, _, g1_time = timed(greedy_earliest_finish, jobs)
    g2_val, _, g2_time = timed(greedy_highest_weight, jobs)
    g3_val, _, g3_time = timed(greedy_weight_density, jobs)

    print(f"OPT: value={opt_val:.1f} time={opt_time*1000:.2f}ms")
    print(f"EF : value={g1_val:.1f} ratio={g1_val/opt_val:.3f} time={g1_time*1000:.2f}ms")
    print(f"HV : value={g2_val:.1f} ratio={g2_val/opt_val:.3f} time={g2_time*1000:.2f}ms")
    print(f"VD : value={g3_val:.1f} ratio={g3_val/opt_val:.3f} time={g3_time*1000:.2f}ms")

if __name__ == "__main__":
    main()
