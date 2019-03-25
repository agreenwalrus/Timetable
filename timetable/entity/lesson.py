class Lesson:

    def __init__(self, time_period, program_class, room):
        self.__time_period__ = time_period
        self.__program_class__ = program_class
        self.__room__ = room

    def get_teacher(self):
        return self.__program_class__.get_teacher()

    def get_subject(self):
        return self.__program_class__.get_subject()

    def get_form(self):
        return self.__program_class__.get_form()

    def get_time_period(self):
        return self.__time_period__

    def get_program_class(self):
        return self.__program_class__

    def get_room(self):
        return self.__room__
