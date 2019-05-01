import pickle
import sys
from PyQt5 import QtWidgets
from gui.maininfo import Ui_MainWindow
from timetable.DAO.mysql.mysql_dao import Connection, WorkDayDAO, TimePeriodDAO, TeacherDAO, RoomDAO, SubjectDAO, \
    FormDAO, ProgramClassDAO


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

        # con = Connection('root', 'root', '127.0.0.1', 'schema_test')
        # all = WorkDayDAO(con).select_all()
        # lis = list(map(lambda obj: (obj.number, obj.description), all))
        # title = [' ', 'Номер', 'Название']
        # self.draw(self.tableWidget_day, lis, title)
        #
        # con = Connection('root', 'root', '127.0.0.1', 'schema_test')
        # all = TimePeriodDAO(con).select_all()
        # lis = list(map(lambda obj: (obj.number, obj.description), all))
        # title = [' ', 'Номер', 'Название']
        # self.draw(self.tableWidget_time, lis, title)
        #
        # con = Connection('root', 'root', '127.0.0.1', 'schema_test')
        # all = TeacherDAO(con).select_all()
        # lis = list(map(lambda obj: (obj.id, obj.surname, obj.name, obj.middle_name), all))
        # title = [' ', 'Идентификатор', 'Фамилия', 'Имя', 'Отчество']
        # self.draw(self.tableWidget_teacher, lis, title)
        #
        # con = Connection('root', 'root', '127.0.0.1', 'schema_test')
        # all = RoomDAO(con).select_all()
        # lis = list(map(lambda obj: (obj.number, obj.capacity), all))
        # title = [' ', 'Номер', 'Вместительность']
        # self.draw(self.tableWidget_room, lis, title)
        #
        # con = Connection('root', 'root', '127.0.0.1', 'schema_test')
        # all = SubjectDAO(con).select_all()
        # lis = list(map(lambda obj: (obj.name, obj.short_name), all))
        # title = [' ', 'Название', 'Короткое нозвание']
        # self.draw(self.tableWidget_subject, lis, title)
        #
        # con = Connection('root', 'root', '127.0.0.1', 'schema_test')
        # all = FormDAO(con).select_all()
        # lis = list(map(lambda obj: (obj.number_letter, obj.people_amount,
        #                             obj.max_complexity,
        #                             obj.class_start.description), all))
        # title = [' ', 'Класс', 'Размер', 'Сложность', 'Начало занятий']
        # self.draw(self.tableWidget_form, lis, title)
        #
        # con = Connection('root', 'root', '127.0.0.1', 'schema_test')
        # all = FormDAO(con).select_all()
        # lis = list(map(lambda obj: (obj.number_letter, obj.people_amount,
        #                             obj.max_complexity,
        #                             obj.class_start.description), all))
        # title = [' ', 'Класс', 'Размер', 'Сложность', 'Начало занятий']
        # self.draw(self.tableWidget_form, lis, title)
        #
        # # con = Connection('root', 'root', '127.0.0.1', 'schema_test')
        # # all = ProgramClassDAO(con).select_all()
        # # lis = list(map(lambda obj: (obj.number_letter, obj.people_amount,
        # #                             obj.max_complexity,
        # #                             obj.class_start.description), all))
        # # title = [' ', 'Класс', 'Размер', 'Сложность', 'Начало занятий']
        # # self.draw(self.tableWidget_form, lis, title)
        #
        # a = pickle.dumps(all[0])
        # b = pickle.loads(a)
        # c = 1


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
    main()  # то запускаем функцию main()