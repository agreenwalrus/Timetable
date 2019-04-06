class WorkDay:
    """
    WorkDay is the class for work day of the week
    """

    def __init__(self, number: int, description: str):
        """
        Construct a new 'Foo' object.

        :param number: Day number
        :param description: Name of the day like people use
        :return: returns nothing
        """
        self.number = number
        self.description = description

    def __str__(self) -> str:
        return str(self.number) + " " + self.description

    def __le__(self, other):
        return self.number <= other.number

    def __gt__(self, other):
        return self.number > other.number
