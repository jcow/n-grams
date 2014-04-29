import re


class Word_parser:

    def get_individual_words(self, lines):
        words = []
        for line in lines:
            words.extend(line.split())
        return words