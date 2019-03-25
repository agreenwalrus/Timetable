from timetable.interfaces.singleton import Singleton


class DataBank(metaclass=Singleton):

    __bank__ = {}
    b = {}

    def add_data(self, data_key, data):
        self.__bank__[data_key] = data
        self.b[data_key] = data

    def get_data(self, data_key):
        return self.__bank__[data_key] if data_key in self.__bank__ else None

    def get_data_item(self, data_key, item_key):
        return self.__bank__[data_key][item_key] if data_key in self.__bank__ and item_key in self.__bank__[data_key] \
            else None

    # __forms__ = {}
    # __rooms__ = {}
    # __subjects__ = {}
    # __teachers__ = {}
    # __time_periods__ = {}
    #
    # def get_forms(self):
    #     return self.__forms__.items()
    #
    # def get_rooms(self):
    #     return self.__rooms__.items()
    #
    # def get_subject(self):
    #     return self.__subjects__.items()
    #
    # def get_teachers(self):
    #     return self.__teachers__.items()
    #
    # def get_time_periods(self):
    #     return self.__time_periods__.items()
    #
    #
    # def get_form(self, key):
    #     return self.__forms__[key] if key in self.__forms__ else None
    #
    # def get_rooms(self, key):
    #     return self.__rooms__[key] if key in self.__rooms__ else None
    #
    # def get_subject(self, key):
    #     return self.__subjects__[key] if key in self.__subjects__ else None
    #
    # def get_teachers(self, key):
    #     return self.__teachers__[key] if key in self.__teachers__ else None
    #
    # def get_time_periods(self, key):
    #     return self.__time_periods__[key] if key in self.__time_periods__ else None
    #
