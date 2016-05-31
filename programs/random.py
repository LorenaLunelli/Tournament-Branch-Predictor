import random


class Rand:
    def __init__(self):
        self._Vector = list()

    def get_number(self, lower=1, upper=1000):
        return random.randint(lower, upper)

    def make_vector(self, size, lower=1, upper=1000):
        for i in range(size):
            self._Vector.append(self.get_number(lower, upper))

    def get_vector(self):
        vec = [x for x in self._Vector]
        return vec
