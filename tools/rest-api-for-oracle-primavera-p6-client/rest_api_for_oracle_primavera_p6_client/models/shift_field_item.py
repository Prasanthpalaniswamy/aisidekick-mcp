from enum import Enum


class ShiftFieldItem(str, Enum):
    CREATEDATE = "CreateDate"
    CREATEUSER = "CreateUser"
    LASTUPDATEDATE = "LastUpdateDate"
    LASTUPDATEUSER = "LastUpdateUser"
    NAME = "Name"
    OBJECTID = "ObjectId"

    def __str__(self) -> str:
        return str(self.value)
