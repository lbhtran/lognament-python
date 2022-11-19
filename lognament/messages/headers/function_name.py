"""
Function name module
"""

from typing import Any

from lognament.messages.base import BaseMessage


class FunctionName(BaseMessage):
    """Class to log function name"""

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        self.logger.info(f"Function name: {self.fn.__name__}")
        return super().__call__(*args, **kwargs)
