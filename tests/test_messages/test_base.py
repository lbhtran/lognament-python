from lognament.messages.base import BaseMessage


class TestBaseMessage:
    def test_init(self, test_function, caplog):
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
