class TimePeriod:

    def __init__(self, day_of_week, number, time_duration=""):
        self.__day_of_week__ = day_of_week
        self.__number__ = number
        self.__time_duration__ = time_duration

    def __str__(self):
        return str(self.__day_of_week__) + " " + str(self.__number__) + " " + self.__time_duration__

    def get_day_of_week(self):
        return self.__day_of_week__

    def get_number(self):
        return self.__number__
