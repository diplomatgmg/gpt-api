from enum import StrEnum


__all__ = ["LogLevelEnum"]


class LogLevelEnum(StrEnum):
    debug = "DEBUG"
    info = "INFO"
    warning = "WARNING"
    error = "ERROR"
    critical = "CRITICAL"
