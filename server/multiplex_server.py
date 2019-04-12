import socket
import select
from request_handler.multiplex_server_request_handler.request_handler_wrapper import *
from server import ServerInterface


class MultiplexerServer(ServerInterface):
    RUN_SERVER = 1
    STOP_SERVER = 0
    TIMEOUT = 120
    BUFFER_SIZE = 1024

    __running_server__ = STOP_SERVER
    QUEUE_FOR_CONNECTORS_SIZE = 1

    def __init__(self, ipv4_addr, port, socket, request_handler_factory):
        super().__init__(ipv4_addr, port, socket, request_handler_factory)
        # self.socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        self.request_handler_wrappers = {}
        self.write_data = {}
        self.read_list_sockets = []
        self.write_list_sockets = []

    def process_write_list(self, sockets):
        for s in sockets:
            self.request_handler_wrappers[s]
            print("process_write_list ", s, len(self.write_data[s]))
            if len(self.write_data[s]) > 0:
                next_msg = self.write_data[s].pop(0)
                s.send(next_msg)
            else:
                self.write_list_sockets.remove(s)

    def process_read_list(self, sockets):
        for s in sockets:
            if s is self.socket:
                client_socket, client_addr = self.socket.accept()
                print("Connection is established with ", client_addr)
                self.read_list_sockets.append(client_socket)
                self.request_handler_wrappers[client_socket] = RequestHandlerWrapper(self.request_handler_factory)
                self.write_data[client_socket] = []
            else:
                recv_data = s.recv(self.BUFFER_SIZE)
                print("#RECV DATA", recv_data)
                code, data = self.request_handler_wrappers[s].handle_request(recv_data)
                if len(recv_data) == 0 or code == STOP_SERVER:
                    self.process_disconnect(s)
                elif code == OK and data is not None:
                    self.write_data[s].append(data)
                    if socket not in self.write_list_sockets:
                        self.write_list_sockets.append(s)
                else:
                    if socket in self.write_list_sockets:
                        self.write_list_sockets.remove(s)

    def process_disconnect(self, socket):
        self.read_list_sockets.remove(socket)
        del self.request_handler_wrappers[socket]
        del self.write_data[socket]
        if socket in self.write_list_sockets:
            self.write_list_sockets.remove(socket)
        socket.close()

    def process_except_list(self, sockets):
        for s in sockets:
            self.process_disconnect(s)

    def start_server(self):

        self.socket.bind((self.ipv4_addr, self.port))
        self.socket.listen(self.QUEUE_FOR_CONNECTORS_SIZE)
        self.__running_server__ = self.RUN_SERVER

        self.read_list_sockets.append(self.socket)

        while self.__running_server__ == self.RUN_SERVER:
            print("Select start")

            read, write, excpt = select.select(self.read_list_sockets,
                                               self.write_list_sockets,
                                               self.read_list_sockets)
            if (len(read) == 0
                    and len(write) == 0
                    and len(excpt) == 0):
                self.stop_server()

            self.process_except_list(excpt)
            self.process_read_list(read)
            self.process_write_list(write)

        self.__shutdown()

    def __shutdown(self):
        self.socket.shutdown(0)
        self.socket.close()

    def stop_server(self):
        self.__running_server__ = self.STOP_SERVER


