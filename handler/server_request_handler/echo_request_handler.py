from handler.server_request_handler.server_request_handler_interface import *


class EchoRequestHandler(RequestHandlerInterface):

    def handle_request(self, socket):
        from timetable.DAO.mysql.mysql_dao import Connection
        con = Connection('root', 'root', '127.0.0.1', 'schema_test')
        from timetable.DAO.mysql.mysql_dao import WorkDayDAO
        all = WorkDayDAO(con).select_all()
        lis = list(map(lambda obj: (obj.number, obj.description), all))
        title = [' ', 'Номер', 'Название']
        import pickle
        dump = pickle.dumps((title, lis))
        socket.send(dump)
        # if '\r\n' in self.params_and_data:
        #     params, data = self.parse_params_and_data()
        #     data_for_sending = params
        # else:
        #     data_for_sending = '\r\n'
        # socket.send(data_for_sending.encode(ENCODE))
        return OK
