from enum import Enum


class ActionStatus(str, Enum):
    ACTIVE = "ACTIVE"
    CREATING = "CREATING"
    ERROR = "ERROR"
    PAUSED = "PAUSED"

    def __str__(self) -> str:
        return str(self.value)
