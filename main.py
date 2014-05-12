from __future__ import division
from directory_reader import *
from utilities import *
from KFold import *
from ngram import *
from list_window import *
from random import shuffle


lines = DirectoryReader.get_lines_from_file("files/shakespeare.txt")
words = Utilities.prepare_text(lines)

ngram_csv = []
unseens_csv = []



for class_number in [1,5,10,20]:
    for ngram_size in [2,3,4,5]:

        fold_step = len(words)//10
        kfold = KFold(words, step=fold_step)

        total_correct = 0
        total_tested = 0
        total_unseen = 0
        while kfold.has_next():

            train, test = kfold.get_next()

            if fold_step <= len(test):

                ng = NGram(train, ngram_size=ngram_size, classification_number = class_number)
                ng.generate_counts()

                counter = 0
                counter_skip = counter+ngram_size-1

                total = 0
                correct = 0
                unseens = 0

                while counter_skip < len(test):

                    w_list = test[counter:counter_skip]

                    guess_words = ng.classify(w_list)
                    actual_word = test[counter_skip]

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

                total_correct += correct
                total_tested += total
                total_unseen += unseens

        ngram_csv.append(str(ngram_size)+","+str(class_number)+","+str(round(total_correct / total_tested, 3)))
        unseens_csv.append(str(round(total_unseen / total_tested, 3)))

for i in ngram_csv:
    print i

for i in unseens_csv:
    print i