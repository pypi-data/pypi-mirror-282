from typing import Any, Callable
from logging import getLogger

log = getLogger(__name__)

ValueFunc = Callable[[float, int, list[Any]], float]

DEFAULT_FUNC_NAME = "static"


def static_value(prev: float, time: int, params: list[int | float]):
    """Return static value."""
    assert (
        len(params) > 0
    ), "needs params that contains at least one item, but args is empty."
    return float(params[0])


_value_func_set: dict[str, ValueFunc] = {DEFAULT_FUNC_NAME: static_value}


def add_func(name: str, func: ValueFunc):
    """Add signal function."""
    _value_func_set[name] = func
    log.debug("Add signal function: %s", name)


def get_func(name: str):
    """Get value function."""
    return _value_func_set.get(name)


def func_keys(name: str):
    """Get value function."""
    return _value_func_set.keys()
