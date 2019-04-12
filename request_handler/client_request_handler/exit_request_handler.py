from request_handler.client_request_handler.client_request_handler_interface import *


class ExitRequestHandler(RequestHandlerInterface):

    def handle_request(self, socket):
        socket.send("exit\r\n".encode(ENCODE))
        return STOP_CLIENT, "Good bye!"
