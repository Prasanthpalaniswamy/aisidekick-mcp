from enum import Enum


class FundingSourceFieldItem(str, Enum):
    CREATEDATE = "CreateDate"
    CREATEUSER = "CreateUser"
    DESCRIPTION = "Description"
    LASTUPDATEDATE = "LastUpdateDate"
    LASTUPDATEUSER = "LastUpdateUser"
    NAME = "Name"
    OBJECTID = "ObjectId"
    PARENTOBJECTID = "ParentObjectId"
    SEQUENCENUMBER = "SequenceNumber"

    def __str__(self) -> str:
        return str(self.value)
