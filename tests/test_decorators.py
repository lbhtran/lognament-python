import logging

from lognament.decorators.lognament import Lognament

logger = logging.getLogger(__name__)


class TestDecorators:
    def test_lognament_no_args(self, caplog):
        @Lognament
        def do_anything():
            logger.debug("<function_content>")
            return 1

        do_anything()

        assert len(caplog.records) == 5
        for record in caplog.records:
            if record.name != "tests.test_decorators":
                assert record.levelname == "INFO"
                assert record.name == "do_anything"
            else:
                assert record.levelname == "DEBUG"
                assert record.name == "tests.test_decorators"
                assert record.msg == "<function_content>"
