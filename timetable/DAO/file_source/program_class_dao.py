from timetable.DAO.dao_interface import DAOInterface

from timetable.entity.form import Form
from timetable.entity.program_class import ProgramClass
from timetable.entity.room import Room
from timetable.entity.subject import Subject
from timetable.entity.teacher import Teacher
from timetable.entity.time_period import TimePeriod
from timetable.service.data_bank import DataBank



class ProgramClassDAO(DAOInterface):

    __source_file__ = "../source/program_class.txt"
    __FORM_NUMBER__ = 0
    __FORM_LETTER__ = 1
    __SUBJECT__ = 2
    __AMOUNT_PER_WEEK__ = 3
    __TEACHER_ID__ = 4

    def select_all(self):

        program = {}

        with open(self.__source_file__, "r") as file_object:
            line = file_object.readline()

            while line:
                line = line.rstrip("\n")
                sl = line.split(" ")
                db = DataBank()
                teacher = db.get_data_item("Teacher", sl[self.__TEACHER_ID__])
                subject = db.get_data_item("Subject", sl[self.__SUBJECT__])
                form = db.get_data_item("Form", sl[self.__FORM_NUMBER__] + sl[self.__FORM_LETTER__])
                rooms = []

                for r in sl[self.__TEACHER_ID__ + 1:]:
                    room = db.get_data_item("Room", r)
                    rooms.append(room)

                if len(rooms) == 0:
                    rooms = list(db.get_data("Room").values())

                program_class = ProgramClass(teacher, subject, form, int(sl[self.__AMOUNT_PER_WEEK__]), rooms)

                key = " ".join(str(i) for i in sl[:self.__AMOUNT_PER_WEEK__]) + " " + sl[self.__TEACHER_ID__]
                program[key] = program_class
                line = file_object.readline()

        return program
