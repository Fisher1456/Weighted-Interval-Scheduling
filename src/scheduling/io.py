import csv
from pathlib import Path
from .model import Job
from .model import BSMJob

def load_jobs_csv(path: str | Path) -> list[Job]:
    path = Path(path)
    jobs: list[Job] = []
    with path.open("r", newline = "", encoding = "utf-8") as f:
        reader = csv.DictReader(f)

        required = {"id", "start", "end", "weight"}
        if not required.issubset(reader.fieldnames or []):
            missing = required - set(reader.fieldnames or [])
            raise ValueError(f"CSV is missing columns: {missing}")

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

def load_bsm_jobs_csv(path: str | Path) -> list[BSMJob]:
    path = Path(path)
    jobs: list[BSMJob] = []
    with path.open("r", newline = "", encoding = "utf-8") as f:
        reader = csv.DictReader(f)

        required = {"id", "proc", "dead", "weight"}
        if not required.issubset(reader.fieldnames or []):
            missing = required - set(reader.fieldnames or [])
            raise ValueError(f"CSV is missing columns: {missing}")

        for row in reader:
            jobs.append(
                BSMJob(
                    job_id = row["id"],
                    proc = int(row["proc"]),
                    dead = int(row["dead"]),
                    weight = int(row["weight"]),
                )
            )
    return jobs
