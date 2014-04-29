

class NGram:

    def __init__(self, words, ngram_size=2,start_word="||S||",end_word="||E||"):

        self.words = words
        self.ngram_size = ngram_size
        self.ngrams = {}
        self.start_word = start_word
        self.end_word = end_word

    def generate_counts(self):
        counts = {}
        window = range(-self.ngram_size+1, 1)

        words_length = len(self.words)
        window_length = len(window)

        go = True
        while go:
            if window[0] >= words_length:
                go = False
            else:

                reference = self.ngrams
                for i in xrange(0, window_length):

                    if window[i] < 0:
                        word = self.start_word
                    elif window[i] >= words_length:
                        word = self.end_word
                    else:
                        word = self.words[window[i]]

                    if i != (window_length-1):
                        if word not in reference:
                            reference[word] = {}
                        reference = reference[word]
                    else:
                        if word not in reference:
                            reference[word] = 0
                        reference[word] += 1

                    window[i] += 1