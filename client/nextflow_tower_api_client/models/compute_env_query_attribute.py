from enum import Enum


class ComputeEnvQueryAttribute(str, Enum):
    LABELS = "labels"

    def __str__(self) -> str:
        return str(self.value)
