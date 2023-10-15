from enum import Enum


class State(str, Enum):
    CANCELED = "CANCELED"
    CANCELING = "CANCELING"
    COMPLETE = "COMPLETE"
    EXECUTOR_ERROR = "EXECUTOR_ERROR"
    INITIALIZING = "INITIALIZING"
    PAUSED = "PAUSED"
    QUEUED = "QUEUED"
    RUNNING = "RUNNING"
    SYSTEM_ERROR = "SYSTEM_ERROR"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
