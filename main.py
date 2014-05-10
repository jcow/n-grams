from __future__ import division
from directory_reader import *
from utilities import *
from KFold import *
from ngram import *
from list_window import *

lines = DirectoryReader.get_lines_from_file("files/harry_potter.txt")
words = Utilities.prepare_text(lines)


kfold = KFold(words, step=(len(words)//10))

ngram_size = 2
while kfold.has_next():

    train, test = kfold.get_next()

    if (len(words)//10) <= len(test):

        ng = NGram(train, ngram_size=ngram_size, classification_number=100000)
        ng.generate_counts()
        list_window = ListWindow(test, ngram_size-1)

        counter = 0
        counter_skip = counter+ngram_size-1

        total = 0
        correct = 0
        unseens = 0

        while counter_skip < len(test) and list_window.has_next():
            w_list = list_window.get_next()

            guess_words = ng.classify(w_list)
            actual_word = words[counter_skip]

            if guess_words == False:
                unseens += 1
            else:
                for word, count in guess_words:
                    if word == actual_word:
                        correct += 1
                        break

            counter += 1
            counter_skip += 1
            total += 1

        print correct
        print correct / len(test)
        print unseens
        print '-----'




# ng = NGram(words, ngram_size=ngram_size)
# ng.generate_counts()
# list_window = ListWindow(words, ngram_size-1)
#
# counter = 0
# counter_skip = counter+ngram_size-1
# correct = 0
# while counter_skip < len(words) and list_window.has_next():
#     w_list = list_window.get_next()
#
#     guess_word = ng.classify(w_list)
#     actual_word = words[counter_skip]
#
#     if guess_word == actual_word:
#         correct += 1
#
#     counter += 1
#     counter_skip += 1
#
# print correct
# print correct / len(words)




# while kfold.has_next():
#     train, test = kfold.get_next()
#
#     print train
#
#     ng = NGram(train, ngram_size=ngram_size)
#     ng.generate_counts()
#     list_window = ListWindow(test, ngram_size-1)
#
#     w = list_window.get_next()
#     # print 'foo'
#     # print w
#     ng.classify(w)
#     # break

