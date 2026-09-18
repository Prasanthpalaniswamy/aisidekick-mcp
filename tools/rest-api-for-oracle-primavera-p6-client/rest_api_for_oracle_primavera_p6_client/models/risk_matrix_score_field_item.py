from enum import Enum


class RiskMatrixScoreFieldItem(str, Enum):
    CREATEDATE = "CreateDate"
    CREATEUSER = "CreateUser"
    LASTUPDATEDATE = "LastUpdateDate"
    LASTUPDATEUSER = "LastUpdateUser"
    OBJECTID = "ObjectId"
    PROBABILITYTHRESHOLDLEVEL = "ProbabilityThresholdLevel"
    RISKMATRIXNAME = "RiskMatrixName"
    RISKMATRIXOBJECTID = "RiskMatrixObjectId"
    SEVERITY1 = "Severity1"
    SEVERITY1LABEL = "Severity1Label"
    SEVERITY2 = "Severity2"
    SEVERITY2LABEL = "Severity2Label"
    SEVERITY3 = "Severity3"
    SEVERITY3LABEL = "Severity3Label"
    SEVERITY4 = "Severity4"
    SEVERITY4LABEL = "Severity4Label"
    SEVERITY5 = "Severity5"
    SEVERITY5LABEL = "Severity5Label"
    SEVERITY6 = "Severity6"
    SEVERITY6LABEL = "Severity6Label"
    SEVERITY7 = "Severity7"
    SEVERITY7LABEL = "Severity7Label"
    SEVERITY8 = "Severity8"
    SEVERITY8LABEL = "Severity8Label"
    SEVERITY9 = "Severity9"
    SEVERITY9LABEL = "Severity9Label"

    def __str__(self) -> str:
        return str(self.value)
