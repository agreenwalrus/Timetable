from timetable.genetic_algorithm.sequence import Sequence


class UniqEncoder:

    __entity__ = {}

    def __init__(self):
        self.__seq__ = Sequence()

    def encode_all(self, list):
        encoded = {}
        for l in list:
            n = self.encode(l)
            encoded[l] = n
        return encoded

    def encode(self, obj):
        n = self.__seq__.next()
        self.__entity__[n] = obj
        return n

    def decode(self, code):
        return self.__entity__[code] if code in self.__entity__ else None
