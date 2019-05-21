import pickle

from handler.client_request_handler.client_request_handler_interface import *
from sockets.socket_interface import PACKAGE_SIZE
import select


class SelectAllRequestHandler(RequestHandlerInterface):

    def handle_request(self, socket):
        r = ""
        socket.send(("select_all day\r\n").encode(ENCODE))
        readable, writable, exceptional = select.select([socket.socket], [], [])
        r = readable[0].recv(PACKAGE_SIZE)
        while len(readable) != 0:
            r += readable[0].recv(PACKAGE_SIZE)
            readable, writable, exceptional = select.select([socket.socket], [], [], 0)
        result = pickle.loads(r)

        return OK, result

