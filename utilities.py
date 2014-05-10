import string


class Utilities:

    @staticmethod
    def prepare_text(lines):
        words = Utilities.lines_to_words(lines)
        words = [Utilities.remove_punc_from_ends(x) for x in words]
        words = Utilities.remove_empty_words(words)
        words = [x.lower() for x in words]
        return words

    @staticmethod
    def lines_to_words(lines):
        words = []
        for line in lines:
            words.extend(line.split())
        return words

    @staticmethod
    def list_lines_to_lower(l):
        for i in xrange(0, len(l)):
            l[i] = l[i].lower()
        return l

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