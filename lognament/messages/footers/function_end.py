"""
Log message at the end of function
"""


from typing import Any

from lognament.messages.base.base import BaseMessage


class FunctionEnd(BaseMessage):
    """Class to log message at the end of a function"""

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        self.logger.info("=== End executing function ===")
        return super().__call__(*args, **kwargs)
