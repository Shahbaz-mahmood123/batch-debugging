from enum import Enum


class JobCleanupPolicy(str, Enum):
    ALWAYS = "always"
    NEVER = "never"
    ON_SUCCESS = "on_success"

    def __str__(self) -> str:
        return str(self.value)
