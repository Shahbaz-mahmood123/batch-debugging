from enum import Enum


class CloudPriceModel(str, Enum):
    SPOT = "spot"
    STANDARD = "standard"

    def __str__(self) -> str:
        return str(self.value)
