from enum import Enum


class ProjectNoteFieldItem(str, Enum):
    AVAILABLEFORACTIVITY = "AvailableForActivity"
    AVAILABLEFOREPS = "AvailableForEPS"
    AVAILABLEFORPROJECT = "AvailableForProject"
    AVAILABLEFORWBS = "AvailableForWBS"
    CREATEDATE = "CreateDate"
    CREATEUSER = "CreateUser"
    ISBASELINE = "IsBaseline"
    ISTEMPLATE = "IsTemplate"
    LASTUPDATEDATE = "LastUpdateDate"
    LASTUPDATEUSER = "LastUpdateUser"
    NOTE = "Note"
    NOTEBOOKTOPICNAME = "NotebookTopicName"
    NOTEBOOKTOPICOBJECTID = "NotebookTopicObjectId"
    OBJECTID = "ObjectId"
    PROJECTID = "ProjectId"
    PROJECTOBJECTID = "ProjectObjectId"
    RAWTEXTNOTE = "RawTextNote"
    WBSCODE = "WBSCode"
    WBSNAME = "WBSName"
    WBSOBJECTID = "WBSObjectId"

    def __str__(self) -> str:
        return str(self.value)
