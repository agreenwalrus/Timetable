
from peewee import *
import mysql.connector
import pymysql

from timetable.DAO.mysql.mysql_dao import ProgramClassDAO, Connection
#
# dbhandle = MySQLDatabase("mydb", host="127.0.0.1", port=3306,
#                          user="root", passwd="root")
#
#
# class BaseModel(Model):
#
#     class Meta:
#         database = dbhandle
#
#
# class Room(BaseModel):
#
#     number = CharField(max_length=20, primary_key=True)
#     capacity = IntegerField()
#
#     class Meta:
#         db_table = "room"
#
#
# class Teacher(BaseModel):
#
#     identificator = CharField(max_length=100, primary_key=True)
#     first_name = CharField(max_length=45)
#     middle_name = CharField(max_length=45)
#     last_name = CharField(max_length=45)
#
#     class Meta:
#         db_table = "teacher"
#
#
# class TimePeriod(BaseModel):
#
#     number = IntegerField(primary_key=True)
#     description = CharField(max_length=45)
#
#     class Meta:
#         db_table = "time_period"
#
#
# class Workday(BaseModel):
#
#     number = IntegerField(primary_key=True)
#     name = CharField(max_length=45)
#
#     class Meta:
#         db_table = "workday"
#
#
# class Form(BaseModel):
#
#     number_letter = CharField(max_length=45, primary_key=True)
#     max_complexity = IntegerField()
#     people_amount = IntegerField()
#     people_amount = IntegerField()
#     #daily_complexity =
#
#     class Meta:
#         db_table = "program_class"
#
# class ProgramClass(BaseModel):
#
#     number = IntegerField(primary_key=True)
#     name = CharField(max_length=45)
#
#     class Meta:
#         db_table = "workday"
#
# dbhandle.connect()
# for r in Room.select():
#     print(r)


if __name__ == '__main__':
    con = Connection('root', 'root', '127.0.0.1', 'schema_test')
    dao = ProgramClassDAO(con)
    result = dao.select_all()
    print(result)
    exit