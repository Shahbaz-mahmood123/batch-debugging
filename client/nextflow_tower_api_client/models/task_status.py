from enum import Enum


class TaskStatus(str, Enum):
    ABORTED = "ABORTED"
    CACHED = "CACHED"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    NEW = "NEW"
    RUNNING = "RUNNING"
    SUBMITTED = "SUBMITTED"

    def __str__(self) -> str:
        return str(self.value)
