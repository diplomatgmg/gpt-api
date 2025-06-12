from typing import Annotated

from fastapi import Header, HTTPException, status
from loguru import logger

from app.core.config import app_config
from common.environment.config import env_config


def verify_api_key(api_key: Annotated[str | None, Header(..., alias="X-API-Key")] = None) -> None:
    """Проверка API-ключа для доступа к эндпоинтам"""
    if env_config.debug:
        return

    if api_key != app_config.api_key.get_secret_value():
        logger.warning(f"Invalid API key attempt: {api_key}")
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid API Key")
