import mysql.connector
from timetable.DAO.dao_interface import AbstractDAO
from timetable.entity.entity import Form
from timetable.entity.entity import Room
from timetable.entity.entity import Subject
from timetable.entity.entity import Teacher
from timetable.entity.entity import TimePeriod
from timetable.entity.entity import WorkDay


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

    def commit(self):
        return self.connection.commit()

    def is_connected(self):
        return self.connection.is_connected()

    def rollback(self):
        return self.rollback()


def connection_decorator(method):
    def wrapper(self, *kwargs):
        try:
            self.connection.connect()
            return method(self, *kwargs)
        # except mysql.connector.Error as err:
        #     self.connection.rollback()  # rollback if any exception occured
        #     raise err
        finally:
            if self.connection.is_connected():
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
        l = []
        cursor = self.connection.cursor()
        cursor.execute("SELECT identificator, first_name, last_name, middle_name "
                       "FROM teacher ")
        teach = cursor.fetchall()
        for identificator, first_name, last_name, middle_name in teach:
            cursor.execute(
                "SELECT number, name "
                "FROM impossible_day id "
                "INNER JOIN  Workday wd "
                "ON id.Workday_number = wd.number "
                "WHERE id.Teacher_identificator = '%s'" % identificator)
            result = cursor.fetchall()
            compl = []
            for wd_number, wd_name in result:
                compl.append(WorkDay(number=wd_number, description=wd_name))

            l.append(Teacher(id=identificator, name=first_name, surname=last_name,
                             middle_name=middle_name, impossible_days=compl))
        return l

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
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO time_period(number, description) VALUES(%s, %s)", (object.number, object.description))
        self.connection.commit()

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
        l = []
        cursor = self.connection.cursor()
        cursor.execute("SELECT number, description FROM time_period WHERE number = %s", (id,))
        result = cursor.fetchall()
        for number, description in result:
            l.append(TimePeriod(number=int(number), description=description))
        return l

    @connection_decorator
    def delete(self, iden):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM time_period WHERE number = %s", (iden,))
        self.connection.commit()


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



# con = Connection('root', 'root', '127.0.0.1', 'schema_test')
# r = RoomDAO(con)
# r.select_all()
# r = TimePeriodDAO(con)
# r.select_all()
# r = WorkDayDAO(con)
# r.select_all()
# r = SubjectDAO(con)
# r.select_all()
# r = FormDAO(con)
# r.select_all()
# r = TeacherDAO(con)
# r.select_all()

