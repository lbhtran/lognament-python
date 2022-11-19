from typing import Callable, Type, TypeVar

from lognament.managers.base_manager import BaseManager
from lognament.messages.base import BaseMessage
from lognament.messages.footers import FunctionEnd
from lognament.messages.headers import FunctionName, FunctionStart

MessageClassType = TypeVar("MessageClassType", bound=BaseMessage)


class MessageManager(BaseManager):
    def __init__(self, fn: Callable) -> None:
        super().__init__(fn)
        self.function_start = self._load_class(self.fn, FunctionStart)
        self.function_name = self._load_class(self.fn, FunctionName)
        self.function_end = self._load_class(self.fn, FunctionEnd)

    def _load_class(
        self,
        fn: Callable,
        message_class: Type[MessageClassType],
    ) -> Callable:
        message = message_class(fn)
        return message
