class Lesson:

    def __init__(self, time_period, program_class, room):
        self.time_period = time_period
        self.program_class = program_class
        self.room = room

    def get_teacher(self):
        return self.program_class.teacher

    def get_subject(self):
        return self.program_class.subject

    def get_form(self):
        return self.program_class.form
