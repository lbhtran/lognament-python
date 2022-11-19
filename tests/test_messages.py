import pytest

from lognament.managers.message_manager import MessageManager
from lognament.messages.base import BaseMessage
from lognament.messages.footers import FunctionEnd
from lognament.messages.headers import FunctionName, FunctionStart


class TestMessage:

    function_start_expected_msg = "=== Start executing function ==="
    function_name_expected_msg = "Function name: do_something"
    function_end_expected_msg = "=== End executing function ==="

    def test_base(self, test_function, caplog):
        message = BaseMessage(fn=test_function)

        # Set log messages
        message.logger.info(f"Logged by BaseMessage")
        message.logger.info(f"Function name: {message.fn.__name__}")

        assert message.fn.__name__ == "do_something"
        for record in caplog.records:
            assert record.levelname == "INFO"
            assert record.name == "do_something"

        assert caplog.records[0].msg == "Logged by BaseMessage"
        assert caplog.records[1].msg == "Function name: do_something"

    @pytest.mark.parametrize(
        "message_class, expected_msg",
        [
            pytest.param(
                FunctionStart, function_start_expected_msg, id="test_function_start"
            ),
            pytest.param(
                FunctionName, function_name_expected_msg, id="test_function_name"
            ),
            pytest.param(
                FunctionEnd, function_end_expected_msg, id="test_function_end"
            ),
        ],
    )
    def test_single_message_class(
        self, message_class, expected_msg, test_function, caplog
    ):
        # use message in a manager
        def run_manager(fn):
            message = message_class(fn)
            message()
            return

        run_manager(fn=test_function)

        assert len(caplog.records) == 1
        assert caplog.records[0].levelname == "INFO"
        assert caplog.records[0].msg == expected_msg
        assert caplog.records[0].name == "do_something"

    def test_message_manager(self, test_function, caplog):
        def run_manager(fn):
            messages = MessageManager(fn)

            messages.function_start()
            messages.function_name()
            messages.function_end()

            return

        run_manager(fn=test_function)

        assert len(caplog.records) == 3
        for record in caplog.records:
            assert record.levelname == "INFO"
            assert record.name == "do_something"

        assert caplog.records[0].msg == self.function_start_expected_msg
        assert caplog.records[1].msg == self.function_name_expected_msg
        assert caplog.records[2].msg == self.function_end_expected_msg
