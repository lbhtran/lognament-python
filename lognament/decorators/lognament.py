import functools
import time
from typing import Any, Callable

from lognament.managers.message_manager import MessageManager


class Lognament:
    def __init__(self, fn: Callable) -> None:
        functools.update_wrapper(self, fn)
        self.fn = fn
        self.msg_manager = MessageManager(self.fn)

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        self.msg_manager.function_start()
        self.msg_manager.function_name()
        try:
            result = self.fn(*args, **kwargs)

            return result
        finally:
            end_time = time.perf_counter()
            run_time = end_time - start_time
            self.msg_manager.function_end(run_time)
