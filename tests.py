from unittest import TestCase
from reader import *
from word_parser import *
from utilities import *
from ngram import *

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



class TestWordParser(TestCase):

    def test_get_individual_words(self):
        w = Word_parser()
        words = w.get_individual_words(["I'm a goose"])
        self.assertListEqual(words, ["I'm", "a", "goose"])


class TestUtilities(TestCase):

    def test_remove_punc_from_ends(self):
        cleaned = Utilities.remove_punc_from_ends("")
        self.assertEquals("", cleaned)

        cleaned = Utilities.remove_punc_from_ends(",")
        self.assertEquals("", cleaned)

        cleaned = Utilities.remove_punc_from_ends("a")
        self.assertEquals("a", cleaned)

        cleaned = Utilities.remove_punc_from_ends("a,")
        self.assertEquals("a", cleaned)

        cleaned = Utilities.remove_punc_from_ends("'a$")
        self.assertEquals("a", cleaned)

        cleaned = Utilities.remove_punc_from_ends("'#")
        self.assertEquals("", cleaned)

        cleaned = Utilities.remove_punc_from_ends("I'm,")
        self.assertEquals("I'm", cleaned)

    def test_remove_empty_words(self):
        no_empty_words = Utilities.remove_empty_words(["I", "", "like", "cake"])
        self.assertListEqual(["I", "like", "cake"], no_empty_words)


class TestNGram(TestCase):

    def test_generate_counts(self):
        words = ["I", "like", "food"]
        ngram = NGram(words)
        ngram.generate_counts()

        self.assertEquals(4, len(ngram.ngrams))
        self.assertEquals(1, ngram.ngrams["||S||"]["I"])
        self.assertEquals(1, ngram.ngrams["I"]["like"])
        self.assertEquals(1, ngram.ngrams["like"]["food"])
        self.assertEquals(1, ngram.ngrams["food"]["||E||"])

        words = ["a", "b", "a", "b"]
        ngram = NGram(words)
        ngram.generate_counts()
        self.assertEquals(3, len(ngram.ngrams))
        self.assertEquals(2, len(ngram.ngrams["b"]))

        self.assertEquals(1, ngram.ngrams["||S||"]["a"])
        self.assertEquals(2, ngram.ngrams["a"]["b"])
        self.assertEquals(1, ngram.ngrams["b"]["a"])
        self.assertEquals(1, ngram.ngrams["b"]["||E||"])