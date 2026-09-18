from enum import Enum


class ActivityNoteFieldItem(str, Enum):
    ACTIVITYID = "ActivityId"
    ACTIVITYNAME = "ActivityName"
    ACTIVITYOBJECTID = "ActivityObjectId"
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
    WBSOBJECTID = "WBSObjectId"

    def __str__(self) -> str:
        return str(self.value)
