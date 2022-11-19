from collections.abc import Callable


class BaseManager:
    def __init__(self, fn: Callable) -> None:
        self.fn = fn
