from enum import Enum


class RiskMatrixThresholdFieldItem(str, Enum):
    CREATEDATE = "CreateDate"
    CREATEUSER = "CreateUser"
    LASTUPDATEDATE = "LastUpdateDate"
    LASTUPDATEUSER = "LastUpdateUser"
    RISKMATRIXNAME = "RiskMatrixName"
    RISKMATRIXOBJECTID = "RiskMatrixObjectId"
    RISKTHRESHOLDNAME = "RiskThresholdName"
    RISKTHRESHOLDOBJECTID = "RiskThresholdObjectId"

    def __str__(self) -> str:
        return str(self.value)
