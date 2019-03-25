from timetable.DAO.dao_factory_interface import DAOFactoryInterface
from timetable.DAO.file_source.form_dao import FormDAO
from timetable.DAO.file_source.program_class_dao import ProgramClassDAO
from timetable.DAO.file_source.room_dao import RoomDAO
from timetable.DAO.file_source.subject_dao import SubjectDAO
from timetable.DAO.file_source.teacher_dao import TeacherDAO
from timetable.DAO.file_source.time_period_dao import TimePeriodDAO


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
