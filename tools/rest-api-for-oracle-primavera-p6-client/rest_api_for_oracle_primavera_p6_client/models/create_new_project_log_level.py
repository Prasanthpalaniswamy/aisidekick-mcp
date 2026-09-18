from enum import Enum


class CreateNewProjectLogLevel(str, Enum):
    CONFIG = "CONFIG"
    FINE = "FINE"
    FINER = "FINER"
    FINEST = "FINEST"
    INFO = "INFO"
    SEVERE = "SEVERE"
    WARNING = "WARNING"

    def __str__(self) -> str:
        return str(self.value)
