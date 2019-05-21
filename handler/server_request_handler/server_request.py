import pickle
from handler.server_request_handler.server_request_handler_interface import *
from timetable.DAO.mysql.mysql_dao import Connection, WorkDayDAO, TeacherDAO, \
    FormDAO, RoomDAO, TimePeriodDAO, SubjectDAO


class SelectAllRequestHandler(RequestHandlerInterface):

    def handle_request(self, socket):
        result = []

        con = Connection('root', 'root', '127.0.0.1', 'schema_test')
        all = WorkDayDAO(con).select_all()
        result.append(all)
        all = TimePeriodDAO(con).select_all()
        result.append(all)
        all = SubjectDAO(con).select_all()
        result.append(all)
        all = RoomDAO(con).select_all()
        result.append(all)
        all = FormDAO(con).select_all()
        result.append(all)
        all = TeacherDAO(con).select_all()
        result.append(all)

        serialized = pickle.dumps(result)
        socket.send(serialized)

        return OK


class TimetableRequestHandler(RequestHandlerInterface):

    def handle_request(self, socket):
        result = []

        con = Connection('root', 'root', '127.0.0.1', 'schema_test')
        all_workday = WorkDayDAO(con).select_all()
        result.append(all)
        all_time = TimePeriodDAO(con).select_all()
        result.append(all)
        all = SubjectDAO(con).select_all()
        result.append(all)
        all = RoomDAO(con).select_all()
        result.append(all)
        all = FormDAO(con).select_all()
        result.append(all)
        all = TeacherDAO(con).select_all()
        result.append(all)

        serialized = pickle.dumps(result)
        socket.send(serialized)

        return OK
