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
