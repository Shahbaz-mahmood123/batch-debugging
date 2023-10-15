from enum import Enum


class ActionSource(str, Enum):
    GITHUB = "github"
    TOWER = "tower"

    def __str__(self) -> str:
        return str(self.value)
