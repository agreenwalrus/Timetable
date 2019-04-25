from timetable.DAO import DAOInterface
from timetable.entity.teacher import Teacher


class TeacherDAO(DAOInterface):

    __source_file__ = "../source/teacher.txt"

    __ID__ = 0
    __NAME__ = 1
    __SURNAME__ = 2

    def select_all(self):
        teachers = {}

        with open(self.__source_file__, "r") as file_object:
            line = file_object.readline()

            while line:
                line = line.rstrip("\n")
                sl = line.split(" ")
                teacher = Teacher(sl[self.__ID__], sl[self.__NAME__], sl[self.__SURNAME__])
                teachers[sl[self.__ID__]] = teacher
                line = file_object.readline()

        return teachers

