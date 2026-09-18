from enum import Enum


class RiskImpactFieldItem(str, Enum):
    CREATEDATE = "CreateDate"
    CREATEUSER = "CreateUser"
    ISBASELINE = "IsBaseline"
    ISTEMPLATE = "IsTemplate"
    LASTUPDATEDATE = "LastUpdateDate"
    LASTUPDATEUSER = "LastUpdateUser"
    PROJECTID = "ProjectId"
    PROJECTNAME = "ProjectName"
    PROJECTOBJECTID = "ProjectObjectId"
    RISKID = "RiskId"
    RISKNAME = "RiskName"
    RISKOBJECTID = "RiskObjectId"
    RISKTHRESHOLDLEVELCODE = "RiskThresholdLevelCode"
    RISKTHRESHOLDLEVELNAME = "RiskThresholdLevelName"
    RISKTHRESHOLDLEVELOBJECTID = "RiskThresholdLevelObjectId"
    RISKTHRESHOLDNAME = "RiskThresholdName"
    RISKTHRESHOLDOBJECTID = "RiskThresholdObjectId"

    def __str__(self) -> str:
        return str(self.value)
