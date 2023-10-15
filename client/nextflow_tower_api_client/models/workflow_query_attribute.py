from enum import Enum


class WorkflowQueryAttribute(str, Enum):
    LABELS = "labels"
    MINIMAL = "minimal"
    OPTIMIZED = "optimized"

    def __str__(self) -> str:
        return str(self.value)
