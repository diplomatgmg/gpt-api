from pydantic_settings import BaseSettings, SettingsConfigDict

from common.logging.enums import LogLevelEnum


__all__ = ["log_config"]


class LogConfig(BaseSettings):
    write_to_file: bool
    level: LogLevelEnum

    model_config = SettingsConfigDict(env_prefix="LOG_")


log_config = LogConfig()
