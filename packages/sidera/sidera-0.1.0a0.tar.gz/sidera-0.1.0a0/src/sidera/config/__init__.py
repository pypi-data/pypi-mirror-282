from os import getcwd
from pathlib import Path
from typing import Type
from argparse import ArgumentParser
from tomllib import TOMLDecodeError, loads

from .args_parser import args_parser
from .constants import DEFAULT_CONFIG_FILE
from .models import ArgsModel, ConfigModel, CoreConfigModel, Field


class Config:
    """Configurations manager for the application and all plugins."""

    def __init__(self):
        self._files: list[Path] = []
        self._parser: ArgumentParser = args_parser
        self._config_models: dict[str, Type[ConfigModel]] = {"": CoreConfigModel}
        self._args_models: dict[str, Type[ConfigModel]] = {"core": ArgsModel}
        self._configs: dict[str, ConfigModel] = {}
        self._args: dict[str, ConfigModel] = {}

    def parse_args(self):
        """Parse the arguments"""
        args = self._parser.parse_args()
        for key, model in self._args_models.items():
            self._args[key] = model(**vars(args))

        # Add specified configuration file with args.
        if self.args.config:
            self.add_file(self.args.config)
        else:
            self.add_file(Path(getcwd()) / DEFAULT_CONFIG_FILE)

    def print_usage_args(self):
        """Print the usage of the arguments."""
        self._parser.print_usage()

    def add_file(self, file: Path) -> bool:
        """Add a configuration file to the list.
        Returns:
            bool: True if the file was added, False otherwise.
        """
        if file.exists() and file.is_file():
            self._files.append(file.expanduser())

    def load(self):
        """Load the configuration from the file."""
        for file in self._files:
            if not file.exists() or not file.is_file():
                continue

            text = file.read_text(encoding="utf-8", errors="ignore")
            try:
                conf_dict = loads(text)
                sidera_dict: dict = conf_dict.get("sidera", {})
            except TOMLDecodeError as e:
                raise TOMLDecodeError(f"Error decoding {file}: {e}") from e

            for key, model in self._config_models.items():
                if key == "":
                    update_items = sidera_dict
                else:
                    update_items = sidera_dict.get(key, {})
                origin = self._configs.get(key)
                if origin is None:
                    self._configs[key] = model(**update_items)
                else:
                    self._configs[key] = origin.update(**update_items)

    def save(self, file: Path = [Path(getcwd()) / DEFAULT_CONFIG_FILE]):
        """Save the configuration to the file."""
        # TODO: Implement the save method.
        pass

    def add_config_model(self, key: str, model: Type[ConfigModel]):
        """Add a configuration model to the manager."""
        self._config_models[key] = model

    def get_config(
        self, key: str, default: ConfigModel | None = None
    ) -> ConfigModel | None:
        """Get the configuration for each model."""
        return self._configs.get(key, default)

    @property
    def core(self) -> CoreConfigModel:
        """Return the core configuration."""
        return self._configs.get("core", CoreConfigModel())

    @property
    def args(self) -> ArgsModel:
        """Return the core arguments."""
        return self._args.get("core", ArgsModel())

    @property
    def args_parser(self) -> ArgumentParser:
        """Return the argument parser."""
        return self._parser

    @property
    def files(self) -> list[Path]:
        """Return the list of configuration files."""
        return self._files


__all__ = ["Config", "ConfigModel", "Field"]
