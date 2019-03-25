class Form:

    def __init__(self, number, letter, people_amount):
        self.__number__ = number
        self.__letter__ = letter
        self.__people_amount__ = people_amount

    def get_number(self):
        return self.__number__

    def get_letter(self):
        return self.__letter__

    def get_people_amount(self):
        return self.__people_amount__

    def __str__(self) -> str:
        return str(self.__number__) + " " + self.__letter__ + " " + str(self.__people_amount__)






