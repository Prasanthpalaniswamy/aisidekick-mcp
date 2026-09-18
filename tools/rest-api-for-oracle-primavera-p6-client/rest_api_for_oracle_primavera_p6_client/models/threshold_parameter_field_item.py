from enum import Enum


class ThresholdParameterFieldItem(str, Enum):
    CREATE_DATE = "CREATE_DATE"
    CREATE_USER = "CREATE_USER"
    LAST_UPDATE_DATE = "LAST_UPDATE_DATE"
    LAST_UPDATE_USER = "LAST_UPDATE_USER"
    NAME = "NAME"
    OBJECT_ID = "OBJECT_ID"
    TYPE = "TYPE"

    def __str__(self) -> str:
        return str(self.value)
