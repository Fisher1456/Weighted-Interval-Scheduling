from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class Job:
    job_id: str
    start: int
    end: int
    weight: int