from enum import Enum


class LabelType(str, Enum):
    ALL = "all"
    RESOURCE = "resource"
    SIMPLE = "simple"

    def __str__(self) -> str:
        return str(self.value)
