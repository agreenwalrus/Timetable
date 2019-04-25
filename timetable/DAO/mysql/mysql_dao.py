import mysql.connector
from timetable.DAO.dao_interface import AbstractDAO
from timetable.entity.form import Form
from timetable.entity.room import Room
from timetable.entity.subject import Subject
from timetable.entity.time_period import TimePeriod
from timetable.entity.work_day import WorkDay


class Connection:

    connection = None

    def __init__(self, user, password, host, database):
        self.user = user
        self.password = password
        self.host = host
        self.database = database

    def connect(self):

        self.connection = mysql.connector.connect(user=self.user,
                                                  password=self.password,
                                                  host=self.host,
                                                  database=self.database)
        return self.connection

    def close(self):
        self.connection.close()

    def cursor(self):
        return self.connection.cursor()


def connection_decorator(method):
    def wrapper(self, **kwargs):
        try:
            self.connection.connect()
            method(self, **kwargs)
        finally:
            self.connection.close()

    return wrapper


class SubjectDAO(AbstractDAO):

    connection = None

    def __init__(self, connection):
        self.connection = connection

    @connection_decorator
    def save(self, object):
        raise NotImplementedError

    @connection_decorator
    def select_all(self):
        l = []
        cursor = self.connection.cursor()
        cursor.execute("SELECT full_name, short_name FROM subject")
        result = cursor.fetchall()
        for full_name, short_name in result:
            l.append(Subject(name=full_name, short_name=short_name))
        return l

    @connection_decorator
    def select(self, id):
        raise NotImplementedError

    @connection_decorator
    def delete(self, id):
        raise NotImplementedError


class FormDAO(AbstractDAO):

    connection = None

    def __init__(self, connection):
        self.connection = connection

    @connection_decorator
    def save(self, object):
        raise NotImplementedError

    @connection_decorator
    def select_all(self):
        l = []
        cursor = self.connection.cursor()
        cursor.execute("SELECT f.number_letter, f.student_quantity, f.max_amt_of_cls_daily, "
                       "f.max_cmplxt_for_cls, cls_start, tp.description "
                       "FROM form f "
                       "INNER JOIN time_period tp "
                       "ON tp.number = f.cls_start")
        form = cursor.fetchall()
        for number_letter, student_quantity, max_amt_of_cls_daily, max_cmplxt_for_cls, tp_number, tp_description in form:
            cursor.execute(
                "SELECT wd.number, wd.name, cpd.complexity "
                "FROM Complexity_per_day cpd "
                "INNER JOIN  Workday wd "
                "ON cpd.Workday_number = wd.number "
                "WHERE cpd.Form_number_letter = '%s'" % number_letter)
            result = cursor.fetchall()
            compl = {}
            for wd_number, wd_name, cpd_complexity in result:
                compl[WorkDay(number=wd_number, description=wd_name)] = cpd_complexity

            time = TimePeriod(number=tp_number, description=tp_description)

            l.append(Form(number_letter=number_letter,
                          people_amount=student_quantity,
                          max_complexity=max_cmplxt_for_cls,
                          daily_complexity=compl,
                          class_start=time))
        return l

    @connection_decorator
    def select(self, id):
        raise NotImplementedError

    @connection_decorator
    def delete(self, id):
        raise NotImplementedError


class RoomDAO(AbstractDAO):

    connection = None

    def __init__(self, connection):
        self.connection = connection

    @connection_decorator
    def save(self, object):
        raise NotImplementedError

    @connection_decorator
    def select_all(self):
        l = []
        cursor = self.connection.cursor()
        cursor.execute("SELECT number, capacity FROM room")
        result = cursor.fetchall()
        for number, capacity in result:
            l.append(Room(number=number, capacity=int(capacity)))
        return l

    @connection_decorator
    def select(self, id):
        raise NotImplementedError

    @connection_decorator
    def delete(self, id):
        raise NotImplementedError


class ProgramClassDAO(AbstractDAO):

    connection = None

    def __init__(self, connection):
        self.connection = connection

    @connection_decorator
    def save(self, object):
        raise NotImplementedError

    @connection_decorator
    def select_all(self):
        raise NotImplementedError

    @connection_decorator
    def select(self, id):
        raise NotImplementedError

    @connection_decorator
    def delete(self, id):
        raise NotImplementedError


class TeacherDAO(AbstractDAO):

    connection = None

    def __init__(self, connection):
        self.connection = connection

    @connection_decorator
    def save(self, object):
        raise NotImplementedError

    @connection_decorator
    def select_all(self):
        raise NotImplementedError

    @connection_decorator
    def select(self, id):
        raise NotImplementedError

    @connection_decorator
    def delete(self, id):
        raise NotImplementedError


class TimePeriodDAO(AbstractDAO):

    connection = None

    def __init__(self, connection):
        self.connection = connection

    @connection_decorator
    def save(self, object):
        raise NotImplementedError

    @connection_decorator
    def select_all(self):
        l = []
        cursor = self.connection.cursor()
        cursor.execute("SELECT number, description FROM time_period")
        result = cursor.fetchall()
        for number, description in result:
            l.append(TimePeriod(number=int(number), description=description))
        return l

    @connection_decorator
    def select(self, id):
        raise NotImplementedError

    @connection_decorator
    def delete(self, id):
        raise NotImplementedError


class TimetableDAO(AbstractDAO):

    connection = None

    def __init__(self, connection):
        self.connection = connection

    @connection_decorator
    def save(self, object):
        raise NotImplementedError

    @connection_decorator
    def select_all(self):
        raise NotImplementedError

    @connection_decorator
    def select(self, id):
        raise NotImplementedError

    @connection_decorator
    def delete(self, id):
        raise NotImplementedError


class WorkDayDAO(AbstractDAO):
    connection = None

    def __init__(self, connection):
        self.connection = connection

    @connection_decorator
    def save(self, object):
        raise NotImplementedError

    @connection_decorator
    def select_all(self):
        l = []
        cursor = self.connection.cursor()
        cursor.execute("SELECT number, name FROM workday")
        result = cursor.fetchall()
        for number, name in result:
            l.append(WorkDay(number=int(number), description=name))
        return l

    @connection_decorator
    def select(self, id):
        raise NotImplementedError

    @connection_decorator
    def delete(self, id):
        raise NotImplementedError



con = Connection('root', 'root', '127.0.0.1', 'schema_test')
r = RoomDAO(con)
r.select_all()
r = TimePeriodDAO(con)
r.select_all()
r = WorkDayDAO(con)
r.select_all()
r = SubjectDAO(con)
r.select_all()
r=FormDAO(con)
r.select_all()