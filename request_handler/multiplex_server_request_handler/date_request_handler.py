from request_handler.multiplex_server_request_handler.server_request_handler_interface import *
import datetime


class DateRequestHandler((RequestHandlerInterface)):

    def handle_request(self, data):
        return self.is_alive, OK, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S").encode(ENCODE)


