class Form:
    """
    Form is entity for form in school.
    """

    def __init__(self, number: int, letter: str, people_amount: int, max_complexity: int, daily_complexity, class_start=1):
        """
        Construct a new 'Form' object.

        :param number: The number of the form
        :param letter: Letter of the form
        :param people_amount: Amount of the students in class
        :param max_complexity: Max complexity for the first and the last class per day
        :param daily_complexity: dictionary {work_day: complexity} with max complexity for each day
        :param class_start: Fist time period number when classes start per day

        """
        self.number = number
        self.letter = letter
        self.people_amount = people_amount
        # for first and last class per day
        self.max_complexity = max_complexity
        self.class_start = class_start

    def str(self) -> str:
        return str(self.number) + " " + self.letter + " " + str(self.people_amount) + " " + str(self.max_complexity) \
               + " " + str(self.class_start)






