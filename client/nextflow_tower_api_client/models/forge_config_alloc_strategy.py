from enum import Enum


class ForgeConfigAllocStrategy(str, Enum):
    BEST_FIT = "BEST_FIT"
    BEST_FIT_PROGRESSIVE = "BEST_FIT_PROGRESSIVE"
    SPOT_CAPACITY_OPTIMIZED = "SPOT_CAPACITY_OPTIMIZED"
    SPOT_PRICE_CAPACITY_OPTIMIZED = "SPOT_PRICE_CAPACITY_OPTIMIZED"

    def __str__(self) -> str:
        return str(self.value)
