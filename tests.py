from unittest import TestCase
from reader import Reader


TEST_FILES_LOCATION = "files/test"


class TestReader(TestCase):

    def test_has_next(self):
        reader = Reader(TEST_FILES_LOCATION)

        self.assertEquals(True, reader.has_next())
        reader.get_next()
        self.assertEquals(True, reader.has_next())
        reader.get_next()
        self.assertEquals(False, reader.has_next())

    def test_get_next(self):
        a = 1
        reader = Reader(TEST_FILES_LOCATION)

        lines = reader.get_next()
        self.assertListEqual(["file", "one"], lines)
        lines2 = reader.get_next()
        self.assertListEqual((["file", "two"]), lines2)
