from enum import Enum


class OrgRole(str, Enum):
    COLLABORATOR = "collaborator"
    MEMBER = "member"
    OWNER = "owner"

    def __str__(self) -> str:
        return str(self.value)
