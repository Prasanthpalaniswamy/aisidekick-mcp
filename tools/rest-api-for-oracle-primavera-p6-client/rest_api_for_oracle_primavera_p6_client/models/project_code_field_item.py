from enum import Enum


class ProjectCodeFieldItem(str, Enum):
    CODETYPENAME = "CodeTypeName"
    CODETYPEOBJECTID = "CodeTypeObjectId"
    CODEVALUE = "CodeValue"
    CREATEDATE = "CreateDate"
    CREATEUSER = "CreateUser"
    DESCRIPTION = "Description"
    LASTUPDATEDATE = "LastUpdateDate"
    LASTUPDATEUSER = "LastUpdateUser"
    OBJECTID = "ObjectId"
    PARENTOBJECTID = "ParentObjectId"
    SEQUENCENUMBER = "SequenceNumber"
    WEIGHT = "Weight"

    def __str__(self) -> str:
        return str(self.value)
