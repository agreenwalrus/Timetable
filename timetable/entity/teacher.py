class Teacher:

    def __init__(self, id, name, surname):
        self.id = id
        self.name = name
        self.surname = surname

    def str(self):
        return self.id + " " + self.name + " " + self.surname
