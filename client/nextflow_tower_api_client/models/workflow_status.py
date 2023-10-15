from enum import Enum


class WorkflowStatus(str, Enum):
    CANCELLED = "CANCELLED"
    FAILED = "FAILED"
    RUNNING = "RUNNING"
    SUBMITTED = "SUBMITTED"
    SUCCEEDED = "SUCCEEDED"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
