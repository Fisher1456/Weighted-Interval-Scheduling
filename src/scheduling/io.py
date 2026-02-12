import csv
from pathlib import Path
# from typing import List
from .model import Job

def load_jobs_csv(path: str | Path) -> list[Job]:
    path = Path(path)
    jobs: list[Job] = []
    with path.open("r", newline = "", encoding = "utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            jobs.append(
                Job(
                    job_id = row["id"],
                    start = int(row["start"]),
                    end = int(row["end"]),
                    weight = int(row["weight"]),
                )
            )
    return jobs
