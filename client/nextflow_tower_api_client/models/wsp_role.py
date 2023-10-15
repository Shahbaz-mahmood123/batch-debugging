from enum import Enum


class WspRole(str, Enum):
    ADMIN = "admin"
    LAUNCH = "launch"
    MAINTAIN = "maintain"
    OWNER = "owner"
    VIEW = "view"

    def __str__(self) -> str:
        return str(self.value)
