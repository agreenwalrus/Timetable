from timetable.DAO import DAOInterface
from timetable import Subject


class SubjectDAO(DAOInterface):

    __source_file__ = "../source/subject.txt"
    __NAME__ = 0

    def select_all(self):
        subjects = {}

        with open(self.__source_file__, "r") as file_object:
            line = file_object.readline()

            while line:
                line = line.rstrip("\n")
                sl = line.split(" ")
                subject = Subject(sl[self.__NAME__])
                subjects[sl[self.__NAME__]] = subject
                line = file_object.readline()

        return subjects
