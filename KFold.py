
class KFold:

    current = 0
    step = 1
    data = []

    def __init__(self, data, step=1):
        self.step = step
        self.data = data
        self.current = 0

    def has_next(self):
        if self.current < len(self.data):
            return True
        else:
            return False

    def get_next(self):
        data_length = len(self.data)
        step_end = self.current+self.step

        test_d = self.data[self.current:step_end]

        train_d = self.data[0:self.current]
        train_d.extend(self.data[step_end:data_length])

        self.current += self.step
        return train_d, test_d