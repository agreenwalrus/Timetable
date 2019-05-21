import sys
from PyQt5 import QtWidgets
from matplotlib.backends.backend_qt5 import MainWindow

from gui.mainwindow import TimetableWindow, ConstraintWindow, NoConnectionDialog, InputDialog
from gui.qts.maininfo import Ui_MainWindow


class ExampleApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

        def config_table_widget(tab_widg, title):
            tab_widg.setColumnCount(len(title))
            tab_widg.setHorizontalHeaderLabels(title)

        room_title = [' ', 'Номер', 'Вместительность']
        config_table_widget(self.tableWidget_room, room_title)
        time_title = [' ', 'Номер', 'Название']
        config_table_widget(self.tableWidget_time, time_title)
        teacher_title = [' ', 'Идентификатор', 'Фамилия', 'Имя', 'Отчество']
        config_table_widget(self.tableWidget_teacher, teacher_title)
        subject_title = [' ', 'Название', 'Короткое нозвание']
        config_table_widget(self.tableWidget_subject, subject_title)
        day_title = [' ', 'Номер', 'Название']
        config_table_widget(self.tableWidget_day, day_title)
        form_title = [' ', 'Класс', 'Размер', 'Сложность', 'Начало занятий']
        config_table_widget(self.tableWidget_form, form_title)

    def draw(self, tab_widget, list_data, title):
        row_number = 0
        #tab_widget.clear()
        tab_widget.setRowCount(0)
        for data in list_data:
            tab_widget.insertRow(row_number)
            col_no = 1
            for col in data:
                tab_widget.setItem(row_number, col_no, QtWidgets.QTableWidgetItem(str(col)))
                col_no += 1
            row_number += 1

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = InputDialog()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()
    # app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    # window = TimetableWindow()  # Создаём объект класса ExampleApp
    # window.show()  # Показываем окно
    # app.exec_()
    #main()  # то запускаем функцию main()