from timetable.DAO.dao_interface import DAOInterface
from timetable.entity.time_period import TimePeriod


class TimePeriodDAO(DAOInterface):

    __source_file__ = "../source/time_period.txt"

    __DAY_OF_WEEK__ = 0
    __NUMBER__ = 1

    def select_all(self):
        periods = {}

        with open(self.__source_file__, "r") as file_object:
            line = file_object.readline()

            while line:
                line = line.rstrip("\n")
                sl = line.split(" ")
                period = TimePeriod(int(sl[self.__DAY_OF_WEEK__]), int(sl[self.__NUMBER__]))
                key = line
                periods[key] = period
                line = file_object.readline()

        return periods
