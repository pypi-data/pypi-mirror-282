from argparse import ArgumentParser
from importlib.metadata import distribution

args_parser = ArgumentParser(
    description="Sidera is a tool to manage scenario for system states."
)
args_parser.add_argument(
    "--version", action="version", version=distribution("sidera").version
)
args_parser.add_argument("--config", type=str, help="Configuration file to use.")
args_parser.add_argument(
    nargs="?", type=str, dest="scenario", help="Scenario file to execute."
)
