import pickle

from handler.client_request_handler.client_request_handler_interface import *
from timetable.DAO.mysql.mysql_dao import Connection, WorkDayDAO, TimePeriodDAO, TeacherDAO, RoomDAO, SubjectDAO, \
    FormDAO


class SelectCommandsRequestHandler(RequestHandlerInterface):

    def handle_request(self, socket):

        result = []

        con = Connection('root', 'root', '127.0.0.1', 'schema_test')
        all = WorkDayDAO(con).select_all()
        lis = list(map(lambda obj: (obj.number, obj.description), all))
        title = [' ', 'Номер', 'Название']
        self.draw(self.tableWidget_day, lis, title)

        con = Connection('root', 'root', '127.0.0.1', 'schema_test')
        all = TimePeriodDAO(con).select_all()
        lis = list(map(lambda obj: (obj.number, obj.description), all))
        title = [' ', 'Номер', 'Название']
        self.draw(self.tableWidget_time, lis, title)

        con = Connection('root', 'root', '127.0.0.1', 'schema_test')
        all = TeacherDAO(con).select_all()
        lis = list(map(lambda obj: (obj.id, obj.surname, obj.name, obj.middle_name), all))
        title = [' ', 'Идентификатор', 'Фамилия', 'Имя', 'Отчество']
        self.draw(self.tableWidget_teacher, lis, title)

        con = Connection('root', 'root', '127.0.0.1', 'schema_test')
        all = RoomDAO(con).select_all()
        lis = list(map(lambda obj: (obj.number, obj.capacity), all))
        title = [' ', 'Номер', 'Вместительность']
        self.draw(self.tableWidget_room, lis, title)

        con = Connection('root', 'root', '127.0.0.1', 'schema_test')
        all = SubjectDAO(con).select_all()
        lis = list(map(lambda obj: (obj.name, obj.short_name), all))
        title = [' ', 'Название', 'Короткое нозвание']
        self.draw(self.tableWidget_subject, lis, title)

        con = Connection('root', 'root', '127.0.0.1', 'schema_test')
        all = FormDAO(con).select_all()
        lis = list(map(lambda obj: (obj.number_letter, obj.people_amount,
                                    obj.max_complexity,
                                    obj.class_start.description), all))
        title = [' ', 'Класс', 'Размер', 'Сложность', 'Начало занятий']
        self.draw(self.tableWidget_form, lis, title)

        con = Connection('root', 'root', '127.0.0.1', 'schema_test')
        all = FormDAO(con).select_all()
        lis = list(map(lambda obj: (obj.number_letter, obj.people_amount,
                                    obj.max_complexity,
                                    obj.class_start.description), all))
        title = [' ', 'Класс', 'Размер', 'Сложность', 'Начало занятий']
        self.draw(self.tableWidget_form, lis, title)

        # con = Connection('root', 'root', '127.0.0.1', 'schema_test')
        # all = ProgramClassDAO(con).select_all()
        # lis = list(map(lambda obj: (obj.number_letter, obj.people_amount,
        #                             obj.max_complexity,
        #                             obj.class_start.description), all))
        # title = [' ', 'Класс', 'Размер', 'Сложность', 'Начало занятий']
        # self.draw(self.tableWidget_form, lis, title)

        a = pickle.dumps(all[0])
        b = pickle.loads(a)
        c = 1
