from enum import Enum


class JobStatus(Enum):
    finished = "Finished"
    running = "Running"
    uploading = "Uploading"
    canceled = "Canceled"
    failed = "Failed"
