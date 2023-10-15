from enum import Enum


class ForgeConfigType(str, Enum):
    EC2 = "EC2"
    SPOT = "SPOT"

    def __str__(self) -> str:
        return str(self.value)
