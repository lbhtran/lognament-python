from typing import Any

from lognament.messages.base import BaseMessage


class FunctionName(BaseMessage):
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        self.logger.info(f"Function name: {self.fn.__name__}")
        return super().__call__(*args, **kwds)
