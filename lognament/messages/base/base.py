import logging
from typing import Any


class BaseMessage:
    def __init__(self, fn) -> None:
        self.fn = fn
        self.logger = logging.getLogger(fn.__name__)

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        pass
