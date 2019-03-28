class Form:

    def __init__(self, number, letter, people_amount):
        self.number = number
        self.letter = letter
        self.people_amount = people_amount

    def str(self) -> str:
        return str(self.number) + " " + self.letter + " " + str(self.people_amount)






