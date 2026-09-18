from enum import Enum


class DocumentStatusCodeFieldItem(str, Enum):
    CREATEDATE = "CreateDate"
    CREATEUSER = "CreateUser"
    LASTUPDATEDATE = "LastUpdateDate"
    LASTUPDATEUSER = "LastUpdateUser"
    NAME = "Name"
    OBJECTID = "ObjectId"
    SEQUENCENUMBER = "SequenceNumber"

    def __str__(self) -> str:
        return str(self.value)
