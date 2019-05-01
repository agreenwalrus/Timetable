from sockets.tcp_socket import ENCODE, TCPSocket
import socket
from handler.server_request_handler import server_request_handler_interface
from server.server_interface import ServerInterface


class SerialTCPSocketServer(ServerInterface):

    RUN_SERVER = 1
    STOP_SERVER = 0

    __running_server = STOP_SERVER
    QUEUE_FOR_CONNECTORS_SIZE = 1

    def __init__(self, ipv4_addr, port, request_handler_factory):
        super().__init__(ipv4_addr, port, TCPSocket(), request_handler_factory)
        #self.socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        
    def start_server(self):
        self.socket.bind(self.ipv4_addr, self.port)
        self.socket.listen(self.QUEUE_FOR_CONNECTORS_SIZE)
        self.__running_server = self.RUN_SERVER

        while self.__running_server == self.RUN_SERVER:
            client_socket, client_addr = self.socket.accept()
            print("Connection is established with ", client_addr)
            client_socket.send("Welcome!".encode(ENCODE))
            code = server_request_handler_interface.OK
            while code != server_request_handler_interface.STOP_SERVER:
                recieved_data = ''
                while '\n' not in recieved_data:
                    recieved_data += client_socket.recv(2048).decode(ENCODE)
                print(recieved_data)
                request_handler = self.request_handler_factory.get_request_handler(recieved_data)
                code = request_handler.handle_request(client_socket)
                print("Code of operation: ", code)
                # print('rcv :', len(self.socket.recv_buffer), 'sent : ', len(self.socket.sent_buffer))
                # print('rcv : ', self.socket.next_send_pack_number, 'sent :', self.socket.next_rcv_pack_number)

            client_socket.shutdown(socket.SHUT_RDWR)
            client_socket.close()

            ###while 1 client
            self.stop_server()
        self.__shutdown()

    def __shutdown(self):
        self.socket.shutdown(0)
        self.socket.close()

    def stop_server(self):
        self.__running_server = self.STOP_SERVER


