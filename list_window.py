
class ListWindow:

    def __init__(self, data, window_size):
        self.data = data
        self.window_size = window_size
        self.index = 0

    def has_next(self):
        if self.index >= 0 and (self.index+self.window_size <= len(self.data)):
            return True
        else:
            return False

    def get_next(self):
        ret = self.data[self.index:self.index+self.window_size]
        self.index += 1
        return ret