from enum import Enum


class ImportProjectsDefaultGlobalImportOption(str, Enum):
    CREATE_NEW = "Create New"
    DO_NOT_IMPORT = "Do Not Import"
    KEEP_EXISTING = "Keep Existing"
    UPDATE_EXISTING = "Update Existing"

    def __str__(self) -> str:
        return str(self.value)
