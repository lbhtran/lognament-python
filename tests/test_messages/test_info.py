from lognament.messages.info import FunctionName


class TestInfoMessage:
    def test_function_detail(self, test_function, caplog):
        # use message in a manager
        def run_manager(fn):
            message = FunctionName(fn)
            message()
            return

        run_manager(fn=test_function)

        assert len(caplog.records) == 1
        assert caplog.records[0].levelname == "INFO"
        assert caplog.records[0].msg == "Function name: do_something"
        assert caplog.records[0].name == "do_something"
