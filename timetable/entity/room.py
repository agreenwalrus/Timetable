
class Room:

    def __init__(self, number, capacity):
        self.number = number
        self.capacity = capacity

    def str(self):
        return str(self.number) + " " + str(self.capacity)
