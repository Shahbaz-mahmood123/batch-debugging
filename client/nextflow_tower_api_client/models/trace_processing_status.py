from enum import Enum


class TraceProcessingStatus(str, Enum):
    KO = "KO"
    OK = "OK"

    def __str__(self) -> str:
        return str(self.value)
