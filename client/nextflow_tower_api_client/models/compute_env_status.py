from enum import Enum


class ComputeEnvStatus(str, Enum):
    AVAILABLE = "AVAILABLE"
    CREATING = "CREATING"
    ERRORED = "ERRORED"
    INVALID = "INVALID"

    def __str__(self) -> str:
        return str(self.value)
