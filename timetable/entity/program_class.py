class ProgramClass:
    """
    ProgramClass is used for type of class which is in a programm
    """

    def __init__(self, teacher, subject, form, amount_per_week: int, grouped_amount: int, room_amount: int,
                 complexity: int, possible_rooms):
        """

        :param teacher: list of object of Teacher() for this class
        :param subject: object of Subject()
        :param form: object of Form()
        :param amount_per_week: amount of such kind of class per week
        :param grouped_amount: amount of time_period closed together per day
        :param room_amount: room amount
        :param complexity: complexity for class
        :param possible_rooms: list of possible rooms for the class
        """
        self.teacher = teacher
        self.subject = subject
        self.form = form
        self.possible_rooms = possible_rooms
        self.complexity = complexity
        self.amount_per_week = amount_per_week
        self.grouped_amount = grouped_amount
        self.room_amount = room_amount

    def str(self):
        return self.form.number + " " + \
               self.form.letter + " " + \
               self.subject.name + " " + \
               str(self.amount_per_week) + " " + \
               self.teacher.id + " " + \
               str(self.complexity) + " " + \
               " ".join(str(i.number) for i in self.possible_room)
