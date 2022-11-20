"""
Log error messages
"""


from typing import Any, Type

from lognament.messages.base.base import BaseMessage


class FunctionError(BaseMessage):
    """Class to log errors inside function"""

    def __call__(self, error_msg: Exception, *args: Any, **kwargs: Any) -> Any:
        self.logger.error(
            f"Error occurs while running {self.fn.__name__!r}: {error_msg}",
            exc_info=True,
        )
        return super().__call__(*args, **kwargs)
