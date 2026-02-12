from bisect import insort, bisect_left
from .model import Job
from .model import BSMJob
from .weighted_interval import has_overlaps

def greedy_earliest_finish(jobs: list[Job]) -> tuple[float, list[Job]]:
    """
    Earliest Finish (EF): maximizes number of jobs

    :param jobs: list of jobs
    :return: tuple of [total weight, list of chosen jobs]
    """
    chosen: list[Job] = []
    total = 0.0
    for job in sorted(jobs, key=lambda j: j.end):
        if not chosen or chosen[-1].end <= job.start:
            chosen.append(job)
            total += job.weight
    return total, chosen

def greedy_earliest_deadline(jobs: list[BSMJob]) -> int:
    """
    Earliest Due Date (EDD): minimizes max lateness in a Basic Single Machine Model

    :param jobs: list of jobs
    :return: max lateness
    """

    max_lateness = 0
    job_lateness = 0
    current_time = 0

    sorted_jobs = sorted(jobs, key=lambda j: j.dead)

    for job in sorted_jobs:
        print(job.job_id)
        current_time += job.proc
        job_lateness += current_time - job.dead if current_time - job.dead > 0 else 0
        if job_lateness > max_lateness:
            max_lateness = job_lateness

    return max_lateness

def greedy_shortest_processing_time(jobs: list[BSMJob]) -> int:
    """
        Shortest Processing Time (SPT): minimizes sum of Flow times, or
        minimizes average number of jobs in the system.
        Basic Single Machine model

        :param jobs: list of jobs
        :return: Total Flow
        """

    total_flow = 0
    current_time = 0

    for job in sorted(jobs, key=lambda j: j.proc):
        current_time += job.proc
        total_flow += current_time
    return total_flow

def greedy_weighted_shortest_processing_time(jobs: list[BSMJob]) -> int:
    """
        Weighted Shortest Processing Time (WSPT): minimizes weighted total Flow times
        Basic Single Machine model

        Must have only one of processing time or weight with zero values

        :param jobs: list of jobs
        :return: Total Weighted Flow
        """

    proc_value_zero, weight_value_zero = False
    proc_job_zero, weight_job_zero = "Z"
    for job in jobs:
        if job.proc == 0:
            proc_value_zero = True
            proc_job_zero = job.job_id
        if job.weight == 0:
            weight_value_zero = True
            weight_job_zero = job.job_id
    if proc_value_zero and weight_value_zero:
        raise ValueError(f"Jobs have incompatible values: "
                         f"Job {proc_job_zero} has processing time 0 and "
                         f"Job {weight_job_zero} has weight 0. "
                         f"Make sure that only one of processing time or weight has zero values")

    total_flow = 0
    current_time = 0

    if proc_value_zero:
        for job in sorted(jobs, key=lambda j: (j.proc/j.weight)):
            current_time += job.proc
            total_flow += current_time
        return total_flow
    else:
        for job in sorted(jobs, key=lambda j: (j.weight/j.proc), reverse=True):
            current_time += job.proc
            total_flow += current_time
        return total_flow


def greedy_highest_weight(jobs: list[Job]) -> tuple[float, list[Job]]:
    chosen: list[Job] = []
    total = 0.0

    for job in sorted(jobs, key=lambda j: j.weight, reverse=True):
        pos = bisect_left([c.start for c in chosen], job.start)

        if pos > 0 and chosen[pos - 1].end > job.start:
            continue

        if pos < len(chosen) and job.end > chosen[pos].start:
            continue

        chosen.insert(pos, job)
        total += job.weight

    return total, chosen

def greedy_weight_density(jobs: list[Job]) -> tuple[float, list[Job]]:
    def density(j: Job) -> float:
        duration = max(1, j.end - j.start)
        return j.weight / duration

    chosen: list[Job] = []
    total = 0.0

    for job in sorted(jobs, key=density, reverse=True):
        pos = bisect_left([c.start for c in chosen], job.start)

        if pos > 0 and chosen[pos - 1].end > job.start:
            continue

        if pos < len(chosen) and job.end > chosen[pos].start:
            continue

        chosen.insert(pos, job)
        total += job.weight

    return total, chosen
