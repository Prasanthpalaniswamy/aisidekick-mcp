from enum import Enum


class ProjectCodeTypeFieldItem(str, Enum):
    CREATEDATE = "CreateDate"
    CREATEUSER = "CreateUser"
    ISSECURECODE = "IsSecureCode"
    LASTUPDATEDATE = "LastUpdateDate"
    LASTUPDATEUSER = "LastUpdateUser"
    LENGTH = "Length"
    MAXCODEVALUEWEIGHT = "MaxCodeValueWeight"
    NAME = "Name"
    OBJECTID = "ObjectId"
    SEQUENCENUMBER = "SequenceNumber"
    WEIGHT = "Weight"

    def __str__(self) -> str:
        return str(self.value)
