from enum import StrEnum


__all__ = ["EnvironmentEnum"]


class EnvironmentEnum(StrEnum):
    DEVELOPMENT = "development"
    PRODUCTION = "production"
