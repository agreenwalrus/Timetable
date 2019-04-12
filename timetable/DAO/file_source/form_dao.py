from timetable.DAO import DAOInterface
from timetable.entity.form import Form


class FormDAO(DAOInterface):

    __source_file__ = "../source/form.txt"

    __NUMBER__ = 0
    __LETTER__ = 1
    __PEOPLE_AMOUNT__ = 2

    def select_all(self):
        forms = {}

        with open(self.__source_file__, "r") as file_object:
            line = file_object.readline()

            while line:
                line = line.rstrip("\n")
                sl = line.split(" ")
                form = Form(sl[self.__NUMBER__], sl[self.__LETTER__], int(sl[self.__PEOPLE_AMOUNT__]))
                forms[sl[self.__NUMBER__] + sl[self.__LETTER__]] = form
                line = file_object.readline()

        return forms
