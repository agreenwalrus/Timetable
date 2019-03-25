from timetable.service.data_bank import DataBank
from timetable.service.term_checker import TermChecker
import random


def generate():
    db = DataBank()

    time_period = list(db.get_data("TimePeriod").values())

    teachers = list(db.get_data("Teacher").values())

    def dep_teacher_time(teacher, time):
        return TermChecker.POSSIBLE

    teacher_checker = TermChecker(teachers, time_period, dep_teacher_time)
    print(teacher_checker.get_conditional_matrix())

    forms = list(db.get_data("Form").values())

    def dep_form_time(form, time):
        return TermChecker.POSSIBLE

    form_checker = TermChecker(forms, time_period, dep_form_time)
    print(form_checker.get_conditional_matrix())

    rooms = list(db.get_data("Room").values())

    def dep_room_time(room, time):
        return TermChecker.POSSIBLE

    room_checker = TermChecker(rooms, time_period, dep_room_time)
    print(room_checker.get_conditional_matrix())

    program_classes = list(db.get_data("ProgramClass").values())

    def dep_room_time(program, room):
        pos_r = program.get_possible_rooms()
        return TermChecker.POSSIBLE if len(pos_r) == 0 or room in pos_r else TermChecker.IMPOSSIBLE

    program_checker = TermChecker(program_classes, rooms, dep_room_time)
    print(program_checker.get_conditional_matrix())

    for pr_c in program_classes:
        print(program_checker.get_possible_states(pr_c))

    z = random.randint()
