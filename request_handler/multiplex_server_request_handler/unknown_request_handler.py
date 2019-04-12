from request_handler.multiplex_server_request_handler.server_request_handler_interface import *


class UnknownRequestHandler(RequestHandlerInterface):

    def handle_request(self, socket):
        return self.is_alive, OK, "Unknown command!\n".encode(ENCODE)

