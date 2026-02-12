from typing import Tuple
from .model import Job
from .weighted_interval import has_overlaps

def greedy_earliest_finish(jobs: list[Job]) -> Tuple[float, list[Job]]:
    chosen: list[Job] = []
    total = 0.0
    for job in sorted(jobs, key=lambda j: j.end):
        if not chosen or chosen[-1].end <= job.start:
            chosen.append(job)
            total += job.weight
    return total, chosen

def greedy_highest_weight(jobs: list[Job]) -> Tuple[float, list[Job]]:
    chosen: list[Job] = []
    total = 0.0
    for job in sorted(jobs, key=lambda j: j.weight, reverse=True):
        tentative = chosen + [job]
        if not has_overlaps(tentative):
            chosen.append(job)
            total += job.weight
    chosen.sort(key=lambda j: j.start)
    return total, chosen

def greedy_weight_density(jobs: list[Job]) -> Tuple[float, list[Job]]:
    def density(j: Job) -> float:
        duration = max(1, j.end - j.start)
        return j.weight / duration

    chosen: list[Job] = []
    total = 0.0
    for job in sorted(jobs, key=density, reverse=True):
        tentative = chosen + [job]
        if not has_overlaps(tentative):
            chosen.append(job)
            total += job.weight
    chosen.sort(key=lambda j: j.start)
    return total, chosen
