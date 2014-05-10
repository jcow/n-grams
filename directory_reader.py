import os
import codecs

class DirectoryReader:

    def __init__(self, directory):
        self.directory = directory
        self.iterator = 0
        self.files = []
        for file in os.listdir(self.directory):
            self.files.append(file)
        self.dir_length = len(self.files)

    def has_next(self):
        return self.iterator < self.dir_length

    def get_next(self):
        lines = DirectoryReader.get_lines_from_file(self.directory+'/'+self.files[self.iterator])
        self.iterator += 1
        return lines

    @staticmethod
    def get_lines_from_file(path):
        lines = []
        with open(path) as f:
            for line in f:
                lines.append(line.rstrip())
        return lines