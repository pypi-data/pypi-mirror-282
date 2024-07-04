from argparse import ArgumentParser
from logging import StreamHandler, getLogger, Formatter
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Literal
from sys import stdout

from pydantic import Field, field_validator

from sidera.config import Config, ConfigModel
from .hook_impl import plugin_hook_impl

log = getLogger(__name__)

# Define log level type
LogLevel = Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL", "NOTSET"]
LOG_LEVELS = LogLevel.__args__

CONSOLE_LOG_FORMAT = "%(message)s"
FILE_LOG_FORMAT = "%(asctime)s [%(levelname)s] %(filename)s %(lineno)s: %(message)s"


@plugin_hook_impl
def setup_config(config: Config):
    """Prepare the plugin configuration."""
    add_args_parser(config.args_parser)
    config.add_config_model("logger", LoggerConfig)


@plugin_hook_impl
def setup_logger(config: Config):
    """Prepare the logger before the initialization."""
    conf: LoggerConfig = config.get_config("logger", LoggerConfig())
    root = getLogger()

    if conf.console.level:
        console_handler = StreamHandler(stream=stdout)
        console_handler.setLevel(conf.console.level)
        console_handler.setFormatter(Formatter(CONSOLE_LOG_FORMAT))
        root.addHandler(console_handler)
        root.setLevel(min(root.level, console_handler.level))

    if conf.file.level and conf.file.path:
        file_handler = RotatingFileHandler(
            filename=conf.file.path,
            maxBytes=conf.file.max_bytes,
            backupCount=conf.file.backup_count,
            encoding="utf-8",
            errors="ignore",
        )
        file_handler.setLevel(conf.file.level)
        file_handler.setFormatter(Formatter(FILE_LOG_FORMAT))
        root.addHandler(file_handler)
        root.setLevel(min(root.level, console_handler.level))
        log.debug("Log to file [%s]: %s", conf.file.level, conf.file.path)


def str_to_upper(cls, v: str):
    """Validator to convert string to uppercase."""
    return v.upper() if isinstance(v, str) else v


class FileLoggerConfig(ConfigModel):
    """Logger configuration for file output."""

    level: LogLevel | None = Field(
        default=None,
        description=f"Log level ({', '.join(LOG_LEVELS)})",
    )
    path: Path | None = Field(alias="file", default=None, description="Log file path.")
    max_bytes: int = Field(
        alias="max-bytes",
        default=1_000_000,
        description="Maximum log file size in bytes.",
    )
    backup_count: int = Field(
        alias="backup-count", default=1, description="Number of backup log files."
    )

    _str_to_upper = field_validator("level", mode="before")(str_to_upper)


class StreamLoggerConfig(ConfigModel):
    """Logger configuration for stream output."""

    level: LogLevel | None = Field(
        default="INFO",
        description=f"Log level ({', '.join(LOG_LEVELS)})",
    )

    _str_to_upper = field_validator("level", mode="before")(str_to_upper)


class LoggerConfig(ConfigModel):
    """Logger configuration."""

    file: FileLoggerConfig = Field(
        default_factory=FileLoggerConfig, description="File logger configuration."
    )
    console: StreamLoggerConfig = Field(
        default_factory=StreamLoggerConfig, description="Stream logger configuration."
    )


def add_args_parser(parser: ArgumentParser):
    """Customize argument parser."""
    # TODO: this argument is for debug.
    parser.add_argument(
        "--logger-version", action="version", version="Simple Logger: v0.1.0"
    )
