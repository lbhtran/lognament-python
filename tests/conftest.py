import pytest


@pytest.fixture
def test_function():
    def do_something():
        pass

    return do_something
