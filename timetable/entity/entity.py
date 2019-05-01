class Drawable:
    def draw(self):
        raise NotImplementedError


class Form(Drawable):
    """
    Form is entity for form in school.
    """

    def __init__(self, number_letter: str, people_amount: int, max_complexity: int, daily_complexity, class_start):
        """
        Construct a new 'Form' object.

        :param number: The number of the form
        :param letter: Letter of the form
        :param people_amount: Amount of the students in class
        :param max_complexity: Max complexity for the first and the last class per day
        :param daily_complexity: dictionary {work_day: complexity} with max complexity for each day
        :param class_start: Fist time period number when classes start per day

        """
        self.number_letter = number_letter
        self.people_amount = people_amount
        # for first and last class per day
        self.max_complexity = max_complexity
        self.class_start = class_start
        self.daily_complexity = daily_complexity

    def str(self) -> str:
        return self.number_letter + " " + str(self.people_amount) + " " + str(self.max_complexity) \
               + " " + str(self.class_start)

    def draw(self):
        return self.number_letter, self.people_amount, self.max_complexity, self.class_start.description


class ProgramClass(Drawable):
    """
    ProgramClass is used for type of class which is in a program
    """

    def __init__(self, teacher, subject, form, amount_per_week: int, grouped_amount: int, room_amount: int,
                 complexity: int, possible_rooms):
        """

        :param teacher: list of object of Teacher() for this class
        :param subject: object of Subject()
        :param form: object of Form()
        :param amount_per_week: amount of such kind of class per week
        :param grouped_amount: amount of time_period closed together per day
        :param room_amount: room amount
        :param complexity: complexity for class
        :param possible_rooms: list of possible rooms for the class
        """
        self.teacher = teacher
        self.subject = subject
        self.form = form
        self.possible_rooms = possible_rooms
        self.complexity = complexity
        self.amount_per_week = amount_per_week
        self.grouped_amount = grouped_amount
        self.room_amount = room_amount

    def str(self):
        return self.form.number + " " + \
               self.form.letter + " " + \
               self.subject.name + " " + \
               str(self.amount_per_week) + " " + \
               self.teacher.id + " " + \
               str(self.complexity) + " " + \
               " ".join(str(i.number) for i in self.possible_room)


class Room(Drawable):
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

    def draw(self):
        return self.number, self.capacity


class Subject(Drawable):

    def __init__(self, name: str, short_name: str):
        """

        :param name: Full name of the subject
        :param short_name: Short name of the subject
        """
        self.name = name
        self.short_name = short_name

    def str(self):
        return self.name + " " + self.short_name

    def draw(self):
        return self.name, self.short_name


class Teacher(Drawable):

    def __init__(self, id: str, name: str, surname: str, middle_name: str, impossible_days=[]):
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
        self.middle_name = middle_name

    def str(self):
        return self.id + " " + self.name + " " + self.surname

    def draw(self):
        return self.id, self.name, self.surname, self.middle_name


class TimePeriod(Drawable):

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
        self.next = None
        self.prev = None

    def str(self):
        return str(self.number) + " " + self.description

    def __le__(self, other):
        return self.number <= other.number

    def __gt__(self, other):
        return self.number > other.number

    def draw(self):
        return self.number, self.description


class Timetable(Drawable):

    def __init__(self):
        self.__lessons__ = []

    def add_lesson(self, lesson):
        self.__lessons__.append(lesson)

    def get_lessons(self):
        return self.__lessons__

    def __get_grouped_by__(self, get_grouping_obj):

        grouped = {}

        for les in self.__lessons__:
            obj = get_grouping_obj(les)
            if obj not in grouped:
                grouped[obj] = []
            grouped[obj].append(les)
        return grouped

    def get_timetable_grouped_by_teacher(self):
        return self.__get_grouped_by__(lambda x: x.teacher)

    def get_timetable_grouped_by_room(self):
        return self.__get_grouped_by__(lambda x: x.room)

    def get_timetable_grouped_by_form(self):
        return self.__get_grouped_by__(lambda x: x.form)


class WorkDay(Drawable):
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

    def draw(self):
        return self.number, self.description
