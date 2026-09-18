from enum import Enum


class ProjectDocumentFieldItem(str, Enum):
    ACTIVITYID = "ActivityId"
    ACTIVITYNAME = "ActivityName"
    ACTIVITYOBJECTID = "ActivityObjectId"
    CREATEDATE = "CreateDate"
    CREATEUSER = "CreateUser"
    DOCUMENTCATEGORYNAME = "DocumentCategoryName"
    DOCUMENTOBJECTID = "DocumentObjectId"
    DOCUMENTSTATUSNAME = "DocumentStatusName"
    DOCUMENTTITLE = "DocumentTitle"
    ISBASELINE = "IsBaseline"
    ISTEMPLATE = "IsTemplate"
    ISWORKPRODUCT = "IsWorkProduct"
    LASTUPDATEDATE = "LastUpdateDate"
    LASTUPDATEUSER = "LastUpdateUser"
    OBJECTID = "ObjectId"
    PARENTWBSOBJECTID = "ParentWBSObjectId"
    PROJECTID = "ProjectId"
    PROJECTOBJECTID = "ProjectObjectId"
    WBSCODE = "WBSCode"
    WBSNAME = "WBSName"
    WBSOBJECTID = "WBSObjectId"

    def __str__(self) -> str:
        return str(self.value)
