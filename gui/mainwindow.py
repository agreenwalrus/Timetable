import sys
from PyQt5 import QtWidgets, QtGui

from gui.qts.constraint_window import Ui_ConstraintWindow
from gui.qts.dialog_wday import Ui_DialogWorkday
from gui.qts.maininfo import Ui_MainWindow
from gui.qts.mainui import Ui_MainUi
from gui.qts.no_connection import Ui_DialogNoConnection
from gui.qts.timetable_window import Ui_TimetableWindow


class MainUi(QtWidgets.QMainWindow, Ui_MainUi):

    def init_slots(self):
        self.button_next.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.pushButton_back.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.button_next_2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.pushButton_back_2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))


    def __init__(self, data):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)

        self.init_slots()

        def config_table_widget(tab_widg, title):
            tab_widg.setColumnCount(len(title))
            tab_widg.setHorizontalHeaderLabels(title)

        room_title = ['Номер', 'Вместительность']
        config_table_widget(self.tableWidget_room, room_title)
        time_title = ['Номер', 'Название']
        config_table_widget(self.tableWidget_time, time_title)
        teacher_title = ['Идентификатор', 'Фамилия', 'Имя', 'Отчество']
        config_table_widget(self.tableWidget_teacher, teacher_title)
        subject_title = ['Название', 'Короткое нозвание']
        config_table_widget(self.tableWidget_subject, subject_title)
        day_title = ['Номер', 'Название']
        config_table_widget(self.tableWidget_day, day_title)
        form_title = ['Класс', 'Размер', 'Сложность', 'Начало занятий']
        config_table_widget(self.tableWidget_form, form_title)

        self.draw(self.tableWidget_day, data[0])
        self.draw(self.tableWidget_time, data[1])
        self.draw(self.tableWidget_subject, data[2])
        self.draw(self.tableWidget_room, data[3])
        self.draw(self.tableWidget_form, data[4])
        self.draw(self.tableWidget_teacher, data[5])

    def draw(self, tab_widget, list_data):
        row_number = 0
        # tab_widget.clear()
        tab_widget.setRowCount(0)
        for data in list_data:
            tab_widget.insertRow(row_number)
            col_no = 0
            drawable = data.draw()
            for col in drawable:
                tab_widget.setItem(row_number, col_no, QtWidgets.QTableWidgetItem(str(col)))
                col_no += 1
            row_number += 1


class ExampleApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, data):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

        def config_table_widget(tab_widg, title):
            tab_widg.setColumnCount(len(title))
            tab_widg.setHorizontalHeaderLabels(title)

        room_title = ['Номер', 'Вместительность']
        config_table_widget(self.tableWidget_room, room_title)
        time_title = ['Номер', 'Название']
        config_table_widget(self.tableWidget_time, time_title)
        teacher_title = ['Идентификатор', 'Фамилия', 'Имя', 'Отчество']
        config_table_widget(self.tableWidget_teacher, teacher_title)
        subject_title = ['Название', 'Короткое нозвание']
        config_table_widget(self.tableWidget_subject, subject_title)
        day_title = ['Номер', 'Название']
        config_table_widget(self.tableWidget_day, day_title)
        form_title = ['Класс', 'Размер', 'Сложность', 'Начало занятий']
        config_table_widget(self.tableWidget_form, form_title)

        self.draw(self.tableWidget_day, data[0])
        self.draw(self.tableWidget_time, data[1])
        self.draw(self.tableWidget_subject, data[2])
        self.draw(self.tableWidget_room, data[3])
        self.draw(self.tableWidget_form, data[4])
        self.draw(self.tableWidget_teacher, data[5])

    def draw(self, tab_widget, list_data):
        row_number = 0
        #tab_widget.clear()
        tab_widget.setRowCount(0)
        for data in list_data:
            tab_widget.insertRow(row_number)
            col_no = 0
            drawable = data.draw()
            for col in drawable:
                tab_widget.setItem(row_number, col_no, QtWidgets.QTableWidgetItem(str(col)))
                col_no += 1
            row_number += 1


class TimetableWindow(QtWidgets.QMainWindow, Ui_TimetableWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна


class ConstraintWindow(QtWidgets.QMainWindow, Ui_ConstraintWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.label.setPixmap(QtGui.QPixmap("D:/diploma/python_project/gui/resource/error.png"))


class NoConnectionDialog(QtWidgets.QMainWindow, Ui_DialogNoConnection):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна


class InputDialog(QtWidgets.QMainWindow, Ui_DialogWorkday):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайн



