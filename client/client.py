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


            def my_exception_hook(exctype, value, traceback):
                # Print the error and traceback
                print(exctype, value, traceback)
                # Call the normal Exception hook after
                sys._excepthook(exctype, value, traceback)
                sys.exit(1)

            sys._excepthook = sys.excepthook
            # Set the exception hook to our wrapping function
            sys.excepthook = my_exception_hook
            app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
            window = MainUi(self.socket)  # Создаём объект класса ExampleApp
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