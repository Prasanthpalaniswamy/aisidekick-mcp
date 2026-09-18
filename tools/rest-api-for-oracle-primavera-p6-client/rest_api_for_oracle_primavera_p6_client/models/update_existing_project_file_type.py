from enum import Enum


class UpdateExistingProjectFileType(str, Enum):
    GZIP = "GZIP"
    XER = "XER"
    XML = "XML"
    ZIP = "ZIP"

    def __str__(self) -> str:
        return str(self.value)
