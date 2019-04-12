from timetable.DAO import DAOInterface
from timetable.entity.room import Room


class RoomDAO(DAOInterface):

    __source_file__ = "../source/room.txt"

    __NUMBER__ = 0
    __CAPACITY__ = 1

    def select_all(self):
        rooms = {}

        with open(self.__source_file__, "r") as file_object:
            line = file_object.readline()

            while line:
                line = line.rstrip("\n")
                sl = line.split(" ")
                room = Room(sl[self.__NUMBER__], int(sl[self.__CAPACITY__]))
                rooms[sl[self.__NUMBER__]] = room
                line = file_object.readline()

        return rooms
