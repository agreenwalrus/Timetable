from request_handler.client_request_handler.client_request_handler_interface import *
from sockets.socket_interface import PACKAGE_SIZE


class UnrecognizedCommandsRequestHandler(RequestHandlerInterface):

    def handle_request(self, socket):
        socket.send((self.request + "\r\n").encode(ENCODE))
        return OK, socket.recv(PACKAGE_SIZE).decode(ENCODE)

