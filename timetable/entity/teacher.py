class Teacher:

    def __init__(self, id, name, surname):
        self.__id__ = id
        self.__name__ = name
        self.__surname__ = surname

    def __str__(self):
        return self.__id__ + " " + self.__name__ + " " + self.__surname__

    def get_id(self):
        return self.__id__

    def get_name(self):
        return self.__name__

    def get_surname(self):
        return self.__surname__
