from unittest import TestCase
from directory_reader import *
from word_parser import *
from utilities import *
from ngram import *
from list_window import *
from KFold import *

TEST_FILES_LOCATION = "files/test"


class TestReader(TestCase):

    def test_has_next(self):
        reader = DirectoryReader(TEST_FILES_LOCATION)

        self.assertEquals(True, reader.has_next())
        reader.get_next()
        self.assertEquals(True, reader.has_next())
        reader.get_next()
        self.assertEquals(False, reader.has_next())

    def test_get_next(self):
        reader = DirectoryReader(TEST_FILES_LOCATION)

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

    def test_lines_to_words(self):
        lines = ["I like apples", ",but not potatoes"]
        words = Utilities.lines_to_words(lines)
        self.assertListEqual(["I", "like", "apples", ",but", "not", "potatoes"], words)

    def test_prepare_text(self):
        lines = ["\"I like people", ",but I don't like their smell\" !!!"]
        words = Utilities.prepare_text(lines)
        self.assertEquals(["i", "like", "people", "but", "i", "don't", "like", "their", "smell"], words)

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

        words = ["I", "am", "a", "taco"]
        ngram = NGram(words, ngram_size=3)
        ngram.generate_counts()
        self.assertEquals(5, len(ngram.ngrams))

    def test_generate_dict_from_list(self):
        self.assertEquals(4, len(NGram.generate_dict_from_list(['a', 'a', 'b', 'b', 'c', 'b', 'd'])))

    def test_sort_dictionary(self):
        dict = {'a':1, 'b':2, 'c':10, 'd':4}
        sorted = NGram.sort_dictionary(dict)
        self.assertListEqual([('c', 10), ('d', 4), ('b', 2), ('a', 1)], sorted)

    def test_classify(self):
        ngram = NGram(['i', 'like', 'potatoes', 'like', 'potatoes', 'like', 'a', 'boss'], ngram_size=2)
        ngram.generate_counts()
        self.assertListEqual([('potatoes', 2)], ngram.classify(['like']))

class TestListWindow(TestCase):

    def test_has_next(self):
        lwind = ListWindow(["a", "b", "c", "d", "e"], 2)
        self.assertEquals(True, lwind.has_next())
        lwind.get_next()
        self.assertEquals(True, lwind.has_next())
        lwind.get_next()
        self.assertEquals(True, lwind.has_next())
        lwind.get_next()
        self.assertEquals(True, lwind.has_next())
        lwind.get_next()
        self.assertEquals(False, lwind.has_next())

    def test_get_next(self):
        lwind = ListWindow(["a", "b", "c", "d", "e"], 2)
        self.assertListEqual(["a", "b"], lwind.get_next())
        self.assertListEqual(["b", "c"], lwind.get_next())
        self.assertListEqual(["c", "d"], lwind.get_next())
        self.assertListEqual(["d", "e"], lwind.get_next())


def test_get_next(self):
        data = [1,2,3,4,5,6,7,8,9,10]
        classes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

        counter = 0
        kfold = KFold(2, data, classes)
        while kfold.has_next():
            train_d1, test_d1 = kfold.get_next()

            self.assertEquals(8, len(train_d1))
            self.assertEquals(2, len(test_d1))
            counter += 1

        self.assertEquals(5, counter)

        kfold = KFold(2, data, classes)

        train_d1, train_c1, test_d1, test_c1 = kfold.get_next()
        self.assertListEqual(train_d1, [3,4,5,6,7,8,9,10])
        self.assertListEqual(test_d1, [1,2])

        train_d1, test_d1= kfold.get_next()
        self.assertListEqual(train_d1, [1,2,5,6,7,8,9,10])
        self.assertEquals(test_d1, [3,4])

        kfold.get_next()
        kfold.get_next()
        kfold.get_next()

        self.assertListEqual(train_d1, [1,2,3,4,5,6,7,8])
        self.assertListEqual(test_d1, [9,10])