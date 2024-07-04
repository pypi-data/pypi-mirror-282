from asyncio import sleep
from importlib.metadata import distribution
from logging import getLogger

from sidera.config import Config
from sidera.plugin import PluginHooks
from sidera.scenario import ScenarioFactory
from sidera.task import run_all_tasks, setup_task

log = getLogger(__name__)


def main():
    config = Config()
    plugin_hooks = PluginHooks(config)
    plugin_hooks.initialize()

    async def _main_entry():
        log.info("===== starting Sidera v%s =====", distribution("sidera").version)
        plugins = plugin_hooks.get_plugins()
        if config.files:
            log.info(
                "Loaded config file: %s", ", ".join(str(file) for file in config.files)
            )
        else:
            log.info("No config file loaded.")
        log.info("Plug-in[%d]: %s", len(plugins), ", ".join(plugins))

        factory = ScenarioFactory()
        if config.args.scenario:
            factory.load(config.args.scenario)
            factory.create()

        await sleep(1)

    setup_task(_main_entry(), "main")
    run_all_tasks()


if __name__ == "__main__":
    main()
