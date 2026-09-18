from enum import Enum


class RoleRateFieldItem(str, Enum):
    CREATEDATE = "CreateDate"
    CREATEUSER = "CreateUser"
    EFFECTIVEDATE = "EffectiveDate"
    LASTUPDATEDATE = "LastUpdateDate"
    LASTUPDATEUSER = "LastUpdateUser"
    MAXUNITSPERTIME = "MaxUnitsPerTime"
    OBJECTID = "ObjectId"
    PRICEPERUNIT = "PricePerUnit"
    PRICEPERUNIT2 = "PricePerUnit2"
    PRICEPERUNIT3 = "PricePerUnit3"
    PRICEPERUNIT4 = "PricePerUnit4"
    PRICEPERUNIT5 = "PricePerUnit5"
    ROLEID = "RoleId"
    ROLENAME = "RoleName"
    ROLEOBJECTID = "RoleObjectId"

    def __str__(self) -> str:
        return str(self.value)
