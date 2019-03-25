class Sequence:

    __current__ = 0

    def next(self):
        self.__current__ += 1
        return self.__current__

    def get_current(self):
        return self.__current__
