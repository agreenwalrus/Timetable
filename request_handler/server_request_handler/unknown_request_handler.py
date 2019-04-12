from request_handler.server_request_handler.server_request_handler_interface import *


class UnknownRequestHandler(RequestHandlerInterface):

    def handle_request(self, socket):
        socket.send("Unknown command!\n".encode(ENCODE))
        return OK

