"""
Log message at the start of function
"""

from typing import Any

from lognament.messages.base import BaseMessage


class FunctionStart(BaseMessage):
    """Class to log message at the start of a function"""

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        self.logger.info("=== Start executing function ===")
        return super().__call__(*args, **kwargs)
