from enum import Enum


class ParticipantType(str, Enum):
    COLLABORATOR = "COLLABORATOR"
    MEMBER = "MEMBER"
    TEAM = "TEAM"

    def __str__(self) -> str:
        return str(self.value)
