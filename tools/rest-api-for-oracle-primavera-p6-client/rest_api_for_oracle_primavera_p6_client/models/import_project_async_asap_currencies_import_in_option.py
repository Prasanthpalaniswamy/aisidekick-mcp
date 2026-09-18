from enum import Enum


class ImportProjectAsyncASAPCurrenciesImportInOption(str, Enum):
    BASERATE = "baserate"
    XMLRATE = "xmlrate"

    def __str__(self) -> str:
        return str(self.value)
