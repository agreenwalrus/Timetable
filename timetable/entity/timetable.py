class Timetable:

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

