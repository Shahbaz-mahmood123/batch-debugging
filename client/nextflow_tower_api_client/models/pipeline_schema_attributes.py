from enum import Enum


class PipelineSchemaAttributes(str, Enum):
    PARAMS = "params"
    SCHEMA = "schema"

    def __str__(self) -> str:
        return str(self.value)
