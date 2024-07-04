from pluggy import HookspecMarker

from sidera.config import Config

plugin_hook_spec = HookspecMarker("sidera")


@plugin_hook_spec(historic=True)
def setup_config(config: Config):
    """Prepare the plugin configuration.
    Args:
        config (Config): Config instance.
    """


@plugin_hook_spec(historic=True)
def setup_logger(config: Config):
    """Prepare the logger before the initialization.
    Args:
        config (Config): Config instance.
    """


@plugin_hook_spec(historic=True)
async def initialize(config: Config):
    """Initialize the plugin.
    Args:
        config (Config): Config instance.
    """
