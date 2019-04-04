class Teacher:

    def __init__(self, id: str, name: str, surname: str, impossible_days=[]):
        """

        :param id: Identificator
        :param name: First name
        :param surname: Last name
        :param impossible_days: list with impossible work days
        """
        self.id = id
        self.name = name
        self.surname = surname
        self.impossible_days = impossible_days

    def str(self):
        return self.id + " " + self.name + " " + self.surname
