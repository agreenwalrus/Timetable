from timetable.DAO.mysql.mysql_dao import *


class MySQLDAOFactory():

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
