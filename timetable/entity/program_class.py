class ProgramClass:

    def __init__(self, teacher, subject, form, amount_per_week, complexity, possible_room):
        self.teacher = teacher
        self.subject = subject
        self.form = form
        self.possible_rooms = possible_room
        self.complexity = complexity
        self.amount_per_week = amount_per_week

    def str(self):
        return self.form.number + " " + \
               self.form.letter + " " + \
               self.subject.name + " " + \
               str(self.amount_per_week) + " " + \
               self.teacher.id + " " + \
               str(self.complexity) + " " + \
               " ".join(str(i.number) for i in self.possible_room)
