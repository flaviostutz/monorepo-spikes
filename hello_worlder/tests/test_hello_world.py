import unittest

from hello_worlder.hello_world import hello


class TestSimple(unittest.TestCase):
    def test_add_one(self) -> None:
        assert hello() == "Hello world!"
