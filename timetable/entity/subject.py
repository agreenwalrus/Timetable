class Subject:

    def __init__(self, name):
        self.__name__ = name

    def get_name(self):
        return self.__name__

    def __str__(self):
        return self.__name__



