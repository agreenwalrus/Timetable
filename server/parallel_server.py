from sockets import ENCODE
from request_handler.server_request_handler import server_request_handler_interface
from threading import Lock
from server.pool import ThreadsPool


class ParallelServer:
    RUN_SERVER = 1
    STOP_SERVER = 0
    CLIENT_TIMEOUT = 10

    __running_server = STOP_SERVER
    QUEUE_FOR_CONNECTORS_SIZE = 10
    socket_thread_pool = {}

    def process_client(self, client_socket, client_addr):
        try:
            code = server_request_handler_interface.OK
            while code != server_request_handler_interface.STOP_SERVER:
                recieved_data = ''
                while '\n' not in recieved_data:
                    data = client_socket.recv(2048).decode("cp1252")
                    print(data)
                    print(recieved_data)
                    if data is None or data == '':
                        raise ConnectionAbortedError
                    recieved_data += data
                print(client_addr, ": ", recieved_data)
                request_handler = self.request_handler_factory.get_request_handler(recieved_data)
                code = request_handler.handle_request(client_socket)
                print(client_addr, ": ", "Code of operation: ", code)
        except ConnectionAbortedError:
            pass
        finally:
            print(client_addr, " client has disconnected")
            client_socket.close()
            self.__change_current_amount_of_clients__(-1)

    def __init__(self, ipv4_addr, port, socket, request_handler_factory, max_amount_of_clients):
        self.ipv4_addr = ipv4_addr
        self.port = port
        self.socket = socket
        self.request_handler_factory = request_handler_factory
        self.max_amount_of_clients = max_amount_of_clients
        self.current_amount_of_clients = 0
        self.pool = ThreadsPool(max_amount_of_clients)
        self.lock = Lock()
        # self.socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

    def __change_current_amount_of_clients__(self, delta):
        self.lock.acquire()
        self.current_amount_of_clients += delta
        self.lock.release()

    def start_server(self):
        self.socket.bind((self.ipv4_addr, self.port))
        self.socket.listen(self.QUEUE_FOR_CONNECTORS_SIZE)
        self.__running_server = self.RUN_SERVER

        while self.__running_server == self.RUN_SERVER:
            client_socket, client_addr = self.socket.accept()
            print("Here is a client ", client_addr)
            if self.current_amount_of_clients < self.max_amount_of_clients:
                client_socket.send("Welcome!".encode(ENCODE))
                print("Connection is established with ", client_addr)
                self.socket_thread_pool[client_socket] = self.pool.execute(self.process_client, client_socket, client_addr)
                self.__change_current_amount_of_clients__(1)
            else:
                print("No more resources!")
                client_socket.close()
        self.pool.shutdown(self.CLIENT_TIMEOUT)
        self.__shutdown()

    def __shutdown(self):
        self.socket.shutdown(0)
        self.socket.close()

    def stop_server(self):
        self.__running_server = self.STOP_SERVER


