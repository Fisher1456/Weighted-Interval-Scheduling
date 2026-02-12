from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class Job:
    job_id: str
    start: int
    end: int
    weight: int

    def __post_init__(self):
        # frozen=true blocks normal assignment
        # use object.__setattr__ to validate at construction
        if self.end <= self.start:
            raise ValueError(
                f"Job {self.job_id}: end {self.end} must be > start {self.start}"
            )
        if self.weight <= 0:
            raise ValueError(
                f"Job {self.job_id}: weight {self.weight} must be > 0"
            )

@dataclass(frozen=True, slots=True)
class BSMJob:
    """
    Basic Single Machine model:
        independent single operations
        available for processing simultaneously at time t=0
        setup times are included in the processing times
        jobs are deterministic, known in advance
        non-delay schedule
        no pre-emption
    """
    job_id: str
    proc: int
    dead: int
    weight: int

    def __post_init__(self):
        if self.weight < 0:
            raise ValueError(
                f"Job {self.job_id}: weight {self.weight} must be >= 0"
            )

        if self.proc < 0:
            raise ValueError(
                f"Job {self.job_id}: processing time {self.proc} must be >= 0"
            )

        if self.dead < 0:
            raise ValueError(
                f"Job {self.job_id}: deadline {self.dead} must be >= 0"
            )
