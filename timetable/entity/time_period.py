class TimePeriod:

    """
    TimePeriod is used for possible time of studying periods per work day
    """

    def __init__(self, number: int, description: str):
        """

        :param number: Number of time period in a work day
        :param description: Time period like people understand it
        """
        self.number = number
        self.description = description

    def str(self):
        return str(self.number) + " " + self.description
