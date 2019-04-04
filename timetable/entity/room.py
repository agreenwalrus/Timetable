
class Room:
    """
    Room is used for room entities
    """

    def __init__(self, number: str, capacity: int):
        """
        Constructor

        :param number: Description number of the room
        :param capacity: Max amount of students possible to study in it the same time
        """
        self.number = number
        self.capacity = capacity

    def str(self):
        return str(self.number) + " " + str(self.capacity)
