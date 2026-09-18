from enum import Enum


class ResourceRoleFieldItem(str, Enum):
    CREATEDATE = "CreateDate"
    CREATEUSER = "CreateUser"
    LASTUPDATEDATE = "LastUpdateDate"
    LASTUPDATEUSER = "LastUpdateUser"
    PROFICIENCY = "Proficiency"
    RESOURCEID = "ResourceId"
    RESOURCENAME = "ResourceName"
    RESOURCEOBJECTID = "ResourceObjectId"
    ROLEID = "RoleId"
    ROLENAME = "RoleName"
    ROLEOBJECTID = "RoleObjectId"

    def __str__(self) -> str:
        return str(self.value)
