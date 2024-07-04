import json
from pathlib import Path

from .models.scenario import Scenario

DEFAULT_SCENARIO_FILE = "scenario.json"
DEFAULT_SIGNALS_FILE = "signals.json"
DEFAULT_STATES_FILE = "states.json"


class ScenarioFactory:
    """Scenario factory class."""

    def __init__(self, src: Path | str | dict = {}):
        self.path = None
        self.data = {}
        self.root = Scenario()
        match src:
            case dict():
                self.data = src
            case Path():
                self.load(src)
            case str():
                self.data = json.loads(src)
            case _:
                raise ValueError(f"Unsupported type: {type(src)}")

    def load(self, path: Path = Path(DEFAULT_SCENARIO_FILE)):
        """Load scenario data from file or directory."""
        if not isinstance(path, Path) or not path.exists():
            raise FileNotFoundError(f"Scenario path is not found: {path}")

        if path.is_dir():
            file = path / DEFAULT_SCENARIO_FILE
            if not file.exists():
                self.load_dir(path)
                return
            path = file

        self.data = self._load_file(path, "Scenarios")
        self.path = path

        if not self.data.get("signals"):
            self.data["signals"] = self._load_file(
                path.parent / DEFAULT_SIGNALS_FILE, "Signals"
            )
        if not self.data.get("states"):
            self.data["states"] = self._load_file(
                path.parent / DEFAULT_STATES_FILE, "States"
            )

    def load_dir(self, path: Path):
        self.data["signals"] = self._load_file(path / DEFAULT_SIGNALS_FILE, "Signals")
        self.data["states"] = self._load_file(path / DEFAULT_STATES_FILE, "States")

    @staticmethod
    def _load_file(file: Path, typ: str) -> dict:
        if file.exists() and file.is_file():
            text = file.read_text(encoding="utf-8", errors="ignore")
            return json.loads(text)
        else:
            raise FileNotFoundError(f"{typ} file is not found: {file}")

    def create(self):
        """Create scenario."""
        self.root = Scenario(**self.data)
        return self.root
