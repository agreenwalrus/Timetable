from handler.client_request_handler.client_request_handler_interface import *
from sockets.socket_interface import PACKAGE_SIZE



class SelectCommandsRequestHandler(RequestHandlerInterface):

    def handle_request(self, socket):
        socket.send(("select_all day\r\n").encode(ENCODE))
        r = socket.recv(PACKAGE_SIZE)

        from PyQt5 import QtWidgets
        from gui.maininfo import Ui_MainWindow
        class ExampleApp(QtWidgets.QMainWindow, Ui_MainWindow):
            def __init__(self):
                super().__init__()
                self.setupUi(self)  # Это нужно для инициализации нашего дизайна

                import pickle
                b = pickle.loads(r)
                self.draw(self.tableWidget_room, b[1], b[0])


            def draw(self, tab_widget, list_data, title):
                row_number = 0
                tab_widget.clear()
                tab_widget.setRowCount(0)
                tab_widget.setColumnCount(len(title))
                tab_widget.setHorizontalHeaderLabels(title)
                for data in list_data:
                    tab_widget.insertRow(row_number)
                    col_no = 1
                    for col in data:
                        tab_widget.setItem(row_number, col_no, QtWidgets.QTableWidgetItem(str(col)))
                        col_no += 1
                    row_number += 1

        import sys
        app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
        window = ExampleApp()  # Создаём объект класса ExampleApp
        window.show()  # Показываем окно
        app.exec_()  # и запускаем приложение



        return OK, 'LOL'

