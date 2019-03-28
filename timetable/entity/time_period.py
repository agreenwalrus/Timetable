class TimePeriod:

    def __init__(self, day_of_week, number, time_duration=""):
        self.day_of_week = day_of_week
        self.number = number
        self.time_duration = time_duration

    def str(self):
        return str(self.day_of_week) + " " + str(self.number) + " " + self.time_duration
