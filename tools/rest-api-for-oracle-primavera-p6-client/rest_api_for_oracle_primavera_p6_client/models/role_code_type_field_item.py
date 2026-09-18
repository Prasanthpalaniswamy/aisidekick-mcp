from enum import Enum


class RoleCodeTypeFieldItem(str, Enum):
    CREATEDATE = "CreateDate"
    CREATEUSER = "CreateUser"
    ISSECURECODE = "IsSecureCode"
    LASTUPDATEDATE = "LastUpdateDate"
    LASTUPDATEUSER = "LastUpdateUser"
    LENGTH = "Length"
    NAME = "Name"
    OBJECTID = "ObjectId"
    SEQUENCENUMBER = "SequenceNumber"

    def __str__(self) -> str:
        return str(self.value)
