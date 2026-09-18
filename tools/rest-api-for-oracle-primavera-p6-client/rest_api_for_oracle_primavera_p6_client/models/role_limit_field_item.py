from enum import Enum


class RoleLimitFieldItem(str, Enum):
    CREATEDATE = "CreateDate"
    CREATEUSER = "CreateUser"
    EFFECTIVEDATE = "EffectiveDate"
    LASTUPDATEDATE = "LastUpdateDate"
    LASTUPDATEUSER = "LastUpdateUser"
    MAXUNITSPERTIME = "MaxUnitsPerTime"
    OBJECTID = "ObjectId"
    ROLEOBJECTID = "RoleObjectId"

    def __str__(self) -> str:
        return str(self.value)
