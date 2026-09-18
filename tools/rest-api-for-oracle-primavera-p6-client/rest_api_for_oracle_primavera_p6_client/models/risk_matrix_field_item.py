from enum import Enum


class RiskMatrixFieldItem(str, Enum):
    CREATEDATE = "CreateDate"
    CREATEUSER = "CreateUser"
    DESCRIPTION = "Description"
    IMPACTTHRESHOLDLEVEL = "ImpactThresholdLevel"
    LASTUPDATEDATE = "LastUpdateDate"
    LASTUPDATEUSER = "LastUpdateUser"
    NAME = "Name"
    OBJECTID = "ObjectId"
    PROBABILITYTHRESHOLDLEVEL = "ProbabilityThresholdLevel"
    RISKSCORINGMETHOD = "RiskScoringMethod"

    def __str__(self) -> str:
        return str(self.value)
