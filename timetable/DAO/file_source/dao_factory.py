from timetable.DAO import DAOFactoryInterface
from timetable.DAO import FormDAO
from timetable.DAO import ProgramClassDAO
from timetable.DAO import RoomDAO
from timetable.DAO import SubjectDAO
from timetable.DAO import TeacherDAO
from timetable.DAO import TimePeriodDAO


class DAOFactory(DAOFactoryInterface):

    def get_form_dao(self):
        return FormDAO()

    def get_program_class_dao(self):
        return ProgramClassDAO()

    def get_room_dao(self):
        return RoomDAO()

    def get_subject_dao(self):
        return SubjectDAO()

    def get_teacher_dao(self):
        return TeacherDAO()

    def get_time_period_dao(self):
        return TimePeriodDAO()
