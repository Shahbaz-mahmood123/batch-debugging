from enum import Enum


class Visibility(str, Enum):
    PRIVATE = "PRIVATE"
    SHARED = "SHARED"

    def __str__(self) -> str:
        return str(self.value)
