from pluggy import PluginManager
from sys import exit, stderr
from pydantic import ValidationError

from sidera.config import Config

from . import hook_specs
from .plugin_registry import PLUGIN_REGISTRY_LIST


class PluginHooks:
    """Plugin hooks provider."""

    def __init__(self, config: Config):
        self.config = config
        self.plugin_manager = self.get_plugin_manager()

    @staticmethod
    def get_plugin_manager() -> PluginManager:
        """Get plugin manager."""
        pm = PluginManager("sidera")
        pm.add_hookspecs(hook_specs)
        pm.load_setuptools_entrypoints("sidera")
        # resister default plugins
        for plugin in PLUGIN_REGISTRY_LIST:
            pm.register(plugin)
        return pm

    def initialize(self):
        """Initialize the plugins."""
        try:
            self.setup_config()
        except ValidationError as e:
            print(f"error: parsing configurations: {e}", file=stderr)
            exit(1)
        self.init_logger()
        self.init_plugin()

    def setup_config(self):
        """Setup the configuration customized by plugin."""
        self.plugin_manager.hook.setup_config.call_historic(
            kwargs=dict(
                config=self.config,
            )
        )
        try:
            self.config.parse_args()
        except ValidationError as e:
            self.config.print_usage_args()
            print(f"error: parsing arguments: {e}", file=stderr)
            exit(1)
        try:
            self.config.load()
        except ValidationError as e:
            print(f"error: parsing configurations: {e}", file=stderr)
            exit(1)

    def init_logger(self):
        """Setup the logger before the initialization."""
        self.plugin_manager.hook.setup_logger.call_historic(
            kwargs=dict(
                config=self.config,
            )
        )

    def init_plugin(self):
        """Initialize the plugins."""
        self.plugin_manager.hook.initialize.call_historic(
            kwargs=dict(
                config=self.config,
            )
        )

    def get_plugins(self) -> list[str]:
        """Get the list of plugin names."""
        return [name for name, _ in self.plugin_manager.list_name_plugin()]
