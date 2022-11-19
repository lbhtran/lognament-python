"""
Base message module
"""

import logging
from typing import Any, Callable


class BaseMessage:
    """BaseMessage class

    Base class to create message components

    Attributes
    ----------
    fn : Callable
        Function to set the log messages. This allow the message components
        to access details of the function like name

    logger : logging.Logger
        Logger to set log messages
    """

    def __init__(self, fn: Callable) -> None:
        self.fn: Callable = fn
        self.logger: logging.Logger = logging.getLogger(fn.__name__)

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        pass
