from typing import Callable, Type, TypeVar

from lognament.managers.base_manager import BaseManager
from lognament.messages.base import BaseMessage
from lognament.messages.footers import FunctionEnd
from lognament.messages.headers import FunctionName, FunctionStart

MessageClassType = TypeVar("MessageClassType", bound=BaseMessage)


class MessageManager(BaseManager):
    def __init__(self, fn: Callable) -> None:
        super().__init__(fn)

    def _load_class(
        self,
        message_class: Type[MessageClassType],
    ) -> Callable:
        message = message_class(self.fn)
        return message

    @property
    def function_start(self):
        return self._load_class(FunctionStart)

    @property
    def function_name(self):
        return self._load_class(FunctionName)

    @property
    def function_end(self):
        return self._load_class(FunctionEnd)
