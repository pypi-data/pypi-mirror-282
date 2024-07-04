from __future__ import annotations
from collections.abc import Coroutine
from asyncio import TaskGroup, Task
from logging import getLogger
import asyncio

log = getLogger(__name__)

_coro_list: dict[str, Worker] = {}


def setup_task(coro: Coroutine, name: str):
    """Setup the task."""
    task = Worker(coro, name)
    _coro_list[name] = task
    log.debug("Task [%s] is registered.", name)


def run_all_tasks():
    """Run all tasks."""
    log.info("All workers start.")
    try:
        asyncio.run(Worker.start())

        log.info("All workers finished.")
    except KeyboardInterrupt:
        log.warning("KeyboardInterrupt is received.")


class Worker:
    _task_list: list[Task] = []

    def __init__(self, coro: Coroutine, name: str):
        self.name = name
        self.coro = coro
        self.task: Task | None = None
        if self._task_list:
            raise RuntimeError("Task group is already running.")

    @classmethod
    async def start(cls):
        """Start the task group."""
        async with TaskGroup() as tg:
            for name, worker in _coro_list.items():
                worker.task = tg.create_task(worker.coro, name=name)
                cls._task_list.append(worker.task)
                log.debug("Task [%s] starts.", name)

        cls._task_list.clear()
