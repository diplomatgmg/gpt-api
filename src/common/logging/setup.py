import logging
from logging import LogRecord
import multiprocessing
from pathlib import Path
import sys

from loguru import logger

from common.environment.config import env_config
from common.logging.config import log_config


__all__ = ["setup_module_logging"]


PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent
LOG_DIR = PROJECT_ROOT / "logs"


class InterceptHandler(logging.Handler):
    """Хендлер для перенаправления логов из logging в loguru."""

    def emit(self, record: LogRecord) -> None:  # noqa: PLR6301
        level = logger.level(record.levelname).name
        logger.opt(depth=6, exception=record.exc_info).log(level, record.getMessage())


def setup_module_logging(module_name: str) -> None:
    """Инициализирует logger для модуля"""
    logger.remove()
    logger.add(
        sys.stdout,
        level=log_config.level,
        colorize=True,
    )

    process_name = multiprocessing.current_process().name
    if process_name == "MainProcess":
        logger.info(f'Initializing logger for module "{module_name}"')
        logger.info(f"Env mode: {env_config.mode}, log level: {log_config.level}")

    # Перехватывает логи из logging в loguru
    logging.basicConfig(handlers=[InterceptHandler()], level=logging.NOTSET)

    if log_config.write_to_file:

        def make_log_path(m: str) -> Path:
            return LOG_DIR / m / f"{m}.log"

        module_logger = logger.bind(name=module_name)

        module_logger.add(
            make_log_path(module_name),
            rotation="1 MB",
            retention="7 days",
            compression="zip",
            level=log_config.level,
        )
