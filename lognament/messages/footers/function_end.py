"""
Log message at the end of function
"""


from typing import Any

from lognament.messages.base.base import BaseMessage


class FunctionEnd(BaseMessage):
    """Class to log message at the end of a function"""

    def __call__(self, run_time: float, *args: Any, **kwargs: Any) -> Any:
        self.logger.info("FINISH executing function")
        self.logger.info(f"Function execution time: {run_time:.4f}")
        return super().__call__(*args, **kwargs)
