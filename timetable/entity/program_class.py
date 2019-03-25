class ProgramClass:

    def __init__(self, teacher, subject, form, amount_per_week, possible_room):
        self.__teacher__ = teacher
        self.__subject__ = subject
        self.__form__ = form
        self.__possible_room__ = possible_room
        self.__amount_per_week__ = amount_per_week

    def __str__(self):
        return self.__form__.get_number() + " " + \
               self.__form__.get_letter() + " " + \
               self.__subject__.get_name() + " " + \
               str(self.__amount_per_week__) + " " + \
               self.__teacher__.get_id() + " " + \
               " ".join(str(i.get_number()) for i in self.__possible_room__)

    def get_teacher(self):
        return self.__teacher__

    def get_subject(self):
        return self.__subject__

    def get_form(self):
        return self.__form__

    def get_possible_rooms(self):
        return self.__possible_room__

    def get_amount_per_week(self):
        return self.__amount_per_week__
