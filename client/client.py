import sys

from PyQt5 import QtWidgets

from client.client_interface import ClientInterface
import handler.client_request_handler.client_request_handler_interface as rh
import handler.client_request_handler.client_request as cr
from gui.mainwindow import ExampleApp, MainUi
from sockets.tcp_socket import TCPSocket


class SerialTCPSocketClient(ClientInterface):

    TIMEOUT = 500

    def __init__(self,  ipv4_addr, port, request_handler_factory):
        super().__init__(ipv4_addr, port, TCPSocket(), request_handler_factory)
        #self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start_client(self):
        self.socket.connect(self.ipv4_addr, self.port)
        try:
            data = self.socket.recv(2048)
            if len(data) == 0:
                raise ConnectionAbortedError
            print("Connection with ", self.ipv4_addr, ":", self.port, " is established.")
            code = rh.OK

            app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
            request_handler = self.request_handler_factory.get_request_handler(self.request_handler_factory.SELECT_ALL)
            code, result = request_handler.handle_request(self.socket)
            window = MainUi(result)  # Создаём объект класса ExampleApp
            window.show()  # Показываем окно
            app.exec_()

        except ConnectionAbortedError:
            print("Connection is aborted by server!")
        finally:
            self.stop_client()

    def __shutdown(self):
        self.socket.shutdown(0)
        self.socket.close()

    def stop_client(self):
        self.__shutdown()