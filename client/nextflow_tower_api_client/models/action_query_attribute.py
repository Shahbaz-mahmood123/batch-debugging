from enum import Enum


class ActionQueryAttribute(str, Enum):
    LABELS = "labels"

    def __str__(self) -> str:
        return str(self.value)
