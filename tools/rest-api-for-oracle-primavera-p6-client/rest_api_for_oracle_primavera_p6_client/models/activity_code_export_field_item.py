from enum import Enum


class ActivityCodeExportFieldItem(str, Enum):
    CODECONCATNAME = "CodeConcatName"
    CODETYPENAME = "CodeTypeName"
    CODETYPEOBJECTID = "CodeTypeObjectId"
    CODETYPESCOPE = "CodeTypeScope"
    CODEVALUE = "CodeValue"
    COLOR = "Color"
    CREATEDATE = "CreateDate"
    CREATEUSER = "CreateUser"
    DESCRIPTION = "Description"
    LASTUPDATEDATE = "LastUpdateDate"
    LASTUPDATEUSER = "LastUpdateUser"
    OBJECTID = "ObjectId"
    PARENTOBJECTID = "ParentObjectId"
    PROJECTOBJECTID = "ProjectObjectId"
    SEQUENCENUMBER = "SequenceNumber"

    def __str__(self) -> str:
        return str(self.value)
