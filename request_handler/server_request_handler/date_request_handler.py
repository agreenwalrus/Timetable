from request_handler.server_request_handler.server_request_handler_interface import *
import datetime


class DateRequestHandler((RequestHandlerInterface)):

    def handle_request(self, socket):
        socket.send(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S").encode(ENCODE))
        return OK

