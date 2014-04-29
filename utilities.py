import string


class Utilities:

    @staticmethod
    def remove_punc_from_ends(word):
        word_length = len(word)
        if word_length == 0:
            return word

        elif word_length == 1 and word[0] in string.punctuation:
            return ""

        else:

            # go forward from end and remove punctuation
            counter = 0
            for char in word:
                if (char in string.punctuation) == False:
                    break
                counter += 1
            word = word[counter:word_length]

            # length might have changed from the forward removal
            word_length = len(word)

            counter = word_length
            for char in reversed(word):
                if (char in string.punctuation) == False:
                   break
                counter -= 1
            word = word[0:counter]

            return word

            #
            #
            #
            # if word[0] in string.punctuation:
            #     word = word[1:]
            #
            # new_word_length = len(word)
            #
            # if word[new_word_length-1] in string.punctuation:
            #     word = word[:new_word_length-1]
            #
            # return word

    @staticmethod
    def remove_empty_words(word_list):
        return [x for x in word_list if x != ""]