from enum import Enum


class ResourceCodeFieldItem(str, Enum):
    CODECONCATNAME = "CodeConcatName"
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

    def __str__(self) -> str:
        return str(self.value)
