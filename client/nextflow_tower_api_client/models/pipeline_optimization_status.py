from enum import Enum


class PipelineOptimizationStatus(str, Enum):
    OPTIMIZABLE = "OPTIMIZABLE"
    OPTIMIZED = "OPTIMIZED"
    UNAVAILABLE = "UNAVAILABLE"

    def __str__(self) -> str:
        return str(self.value)
