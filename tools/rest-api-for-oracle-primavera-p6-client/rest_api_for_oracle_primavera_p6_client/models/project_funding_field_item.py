from enum import Enum


class ProjectFundingFieldItem(str, Enum):
    AMOUNT = "Amount"
    CREATEDATE = "CreateDate"
    CREATEUSER = "CreateUser"
    FUNDINGSOURCENAME = "FundingSourceName"
    FUNDINGSOURCEOBJECTID = "FundingSourceObjectId"
    FUNDSHARE = "FundShare"
    ISBASELINE = "IsBaseline"
    ISTEMPLATE = "IsTemplate"
    LASTUPDATEDATE = "LastUpdateDate"
    LASTUPDATEUSER = "LastUpdateUser"
    OBJECTID = "ObjectId"
    PROJECTID = "ProjectId"
    PROJECTOBJECTID = "ProjectObjectId"

    def __str__(self) -> str:
        return str(self.value)
