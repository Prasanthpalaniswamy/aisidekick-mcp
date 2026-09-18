from enum import Enum


class ResourceRateFieldItem(str, Enum):
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
    RESOURCEID = "ResourceId"
    RESOURCENAME = "ResourceName"
    RESOURCEOBJECTID = "ResourceObjectId"
    SHIFTPERIODOBJECTID = "ShiftPeriodObjectId"

    def __str__(self) -> str:
        return str(self.value)
