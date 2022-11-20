import pytest

from lognament.managers.message_manager import MessageManager
from lognament.messages.base import BaseMessage
from lognament.messages.errors.function_error import FunctionError
from lognament.messages.footers import FunctionEnd
from lognament.messages.headers import FunctionName, FunctionStart
from lognament.utils.errors import MockError


class TestMessage:

    fn_start_expected_msg = "START executing function"
    fn_name_expected_msg = "Function name: do_something"
    fn_end_expected_msg = "FINISH executing function"
    fn_end_runtime_expected_msg = "Function execution time: 1.0000"
    fn_err_expected_msg = (
        "Error occurs while running 'do_something': This is a test error"
    )

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
        "message_class, msg_args, expected_msg, expected_logcount",
        [
            pytest.param(
                FunctionStart, {}, fn_start_expected_msg, 1, id="test_function_start"
            ),
            pytest.param(
                FunctionName, {}, fn_name_expected_msg, 1, id="test_function_name"
            ),
            pytest.param(
                FunctionEnd,
                {"run_time": 1.0},
                fn_end_expected_msg,
                2,
                id="test_function_end",
            ),
        ],
    )
    def test_info_message_class(
        self,
        message_class,
        msg_args,
        expected_msg,
        expected_logcount,
        test_function,
        caplog,
    ):

        # use message in a manager
        def run_manager(fn):
            message = message_class(fn)
            if not msg_args:
                message()
            elif "run_time" in msg_args:
                message(msg_args["run_time"])
            return

        run_manager(fn=test_function)

        assert len(caplog.records) == expected_logcount
        assert caplog.records[0].levelname == "INFO"
        assert caplog.records[0].msg == expected_msg
        assert caplog.records[0].name == "do_something"

    def test_error_message_class(self, test_function, caplog):
        def run_manager(fn):
            try:
                raise MockError("This is a test error")
            except Exception as exc:
                message = FunctionError(fn)
                message(error_msg=exc)

        run_manager(fn=test_function)

        assert len(caplog.records) == 1
        assert caplog.records[0].levelname == "ERROR"
        assert caplog.records[0].msg == self.fn_err_expected_msg
        assert caplog.records[0].name == "do_something"

    def test_message_manager(self, test_function, caplog):
        def run_manager(fn):
            messages = MessageManager(fn)

            messages.function_start()
            messages.function_name()
            messages.function_end(1.0)

            return

        run_manager(fn=test_function)

        assert len(caplog.records) == 4
        for record in caplog.records:
            assert record.levelname == "INFO"
            assert record.name == "do_something"

        assert caplog.records[0].msg == self.fn_start_expected_msg
        assert caplog.records[1].msg == self.fn_name_expected_msg
        assert caplog.records[2].msg == self.fn_end_expected_msg
        assert caplog.records[3].msg == self.fn_end_runtime_expected_msg
