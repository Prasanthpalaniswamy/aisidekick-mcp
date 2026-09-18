from enum import Enum


class ImportProjectsCurrenciesImportInOption(str, Enum):
    BASERATE = "baserate"
    XMLRATE = "xmlrate"

    def __str__(self) -> str:
        return str(self.value)
