from enum import Enum


class PipelineQueryAttribute(str, Enum):
    COMPUTEENV = "computeEnv"
    LABELS = "labels"
    OPTIMIZED = "optimized"

    def __str__(self) -> str:
        return str(self.value)
