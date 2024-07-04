from subprocess import run
from re import Pattern, search
from pathlib import Path
from tempfile import NamedTemporaryFile

LOGOUT_CONFIG = """
[sidera.logger.console]
level = "debug"
"""


def check_execution(args: str, pattern: Pattern[str] = r".*", return_code: int = 0):
    """Execute with the arguments and check the output and return code."""
    co = run(
        ["python", "src/sidera", *args.split()],
        capture_output=True,
        text=True,
        errors="ignore",
        encoding="utf-8",
    )
    assert co.returncode == return_code
    assert search(pattern, co.stdout)


def test_arg_version():
    """Test --version argument."""
    check_execution(args="--version", pattern=r"\d+\.\d+\.\d+\W*")


def test_arg_help():
    """Test --help argument."""
    check_execution(args="--help", pattern=r"usage: sidera")


def test_arg_config():
    """Test --config argument."""
    with NamedTemporaryFile(suffix=".toml") as fd:
        tmp_file = Path(fd.name)
        tmp_file.write_text(LOGOUT_CONFIG)
        check_execution(
            args=f"--config {tmp_file}",
            pattern=rf"Loaded config file: {tmp_file}",
        )
    check_execution(args=f"--config {tmp_file}", return_code=1)
