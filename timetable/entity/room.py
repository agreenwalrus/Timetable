
class Room:

    def __init__(self, number, capacity):
        self.__number__ = number
        self.__capacity__ = capacity

    def __str__(self):
        return str(self.__number__) + " " + str(self.__capacity__)

    def get_number(self):
        return self.__number__

    def get_capacity(self):
        return self.__capacity__
