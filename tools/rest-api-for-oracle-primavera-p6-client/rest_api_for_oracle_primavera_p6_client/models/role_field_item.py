from enum import Enum


class RoleFieldItem(str, Enum):
    CALCULATECOSTFROMUNITS = "CalculateCostFromUnits"
    CREATEDATE = "CreateDate"
    CREATEUSER = "CreateUser"
    ID = "Id"
    LASTUPDATEDATE = "LastUpdateDate"
    LASTUPDATEUSER = "LastUpdateUser"
    NAME = "Name"
    OBJECTID = "ObjectId"
    PARENTOBJECTID = "ParentObjectId"
    RESPONSIBILITIES = "Responsibilities"
    SEQUENCENUMBER = "SequenceNumber"

    def __str__(self) -> str:
        return str(self.value)
