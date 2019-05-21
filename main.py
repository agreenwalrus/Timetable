import random

from timetable.genetic_algorithm.gen_algorithm import create_individual, cx_individual, \
                                                        eval_timetable, mut_individual


import numpy
from deap import algorithms
from deap import base
from deap import creator
from deap import tools

from timetable.entity.entity import Form
from timetable.entity.entity import ProgramClass
from timetable.entity.entity import Room
from timetable.entity.entity import Subject
from timetable.entity.entity import Teacher
from timetable.entity.entity import TimePeriod
from timetable.entity.entity import WorkDay
import xlrd, xlsxwriter

toolbox = base.Toolbox()


def init():

    #DataBankFiller.read_data(DAOFactory(), DataBank())

    creator.create("Fitness", base.Fitness, weights=(-1.0,))
    #creator.create("Fitness", base.Fitness, weights=(-1.0, -1.0, -1.0, -1.0, -1.0))
    creator.create("Individual", list, fitness=creator.Fitness)
    program_classes = program_class

    toolbox.register("gene", create_individual, program_classes, [d.number for d in day], [t.number for t in time])
    toolbox.register("individual", tools.initIterate, creator.Individual,
                     toolbox.gene)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    toolbox.register("evaluate", eval_timetable)
    toolbox.register("mate", cx_individual)
    toolbox.register("mutate", mut_individual,  [d.number for d in day], [t.number for t in time])
    toolbox.register("select", tools.selSPEA2)

def create_excel(l, all_day, all_time):
    import xlsxwriter

    wb = xlsxwriter.Workbook('filename.xlsx')
    worksheet = wb.add_worksheet('Timetable')

    worksheet.write(1, 0, 'Класс')
    worksheet.write(1, 1, 'Время')

    for day in range(1, len(all_day) + 1):
        worksheet.merge_range(0, (day * 3) - 1, 0,  (day * 3) - 1 + 2, day)
        worksheet.write(1, (day * 3) - 1, 'Класс')
        worksheet.write(1, (day * 3), 'Преподаватель')
        worksheet.write(1, (day * 3) + 1, 'Аудитория')

    wb.close()

        # timetbl = {}
        #
        # for a in l:
        #     day = a[0]
        #     time = a[1]
        #     form = a[2].form
        #     room = a[3]
        #     if form not in timetbl:
        #         timetbl[form] = [[], [], [], [], [], [], []]
        #     timetbl[form][day].append((time, a[2].subject, room, a[2].teacher))
        #
        # forms = timetbl.keys()
        #
        # for f in forms:
        #     file_object.write("*********************\n")
        #     file_object.write(str(f) + "\n")
        #
        #     for i in range(len(timetbl[f])):
        #         file_object.write(str(i) + ")\n")
        #         for s in timetbl[f][i]:
        #             for tm in s[0]:
        #                 file_object.write(str(tm))
        #                 file_object.write("\n")
        #                 file_object.write(str(s[1]))
        #                 file_object.write("\n")
        #                 for r in s[2]:
        #                     file_object.write(str(r))
        #                     file_object.write("\n")
        #                 for t in s[3]:
        #                     file_object.write(str(t))
        #                     file_object.write("\n")
        #                 file_object.write("----\n")




def write1(l, n):
    with open("../out" + str(n) + ".txt", "w") as file_object:
        timetbl = {}

        for a in l:
            day = a[0]
            time = a[1]
            form = a[2].form
            room = a[3]
            if form not in timetbl:
                timetbl[form] = [[], [], [], [], [], [], []]
            timetbl[form][day].append((time, a[2].subject, room, a[2].teacher))

        forms = timetbl.keys()

        for f in forms:
            file_object.write("*********************\n")
            file_object.write(str(f) + "\n")

            for i in range(len(timetbl[f])):
                file_object.write(str(i) + ")\n")
                for s in timetbl[f][i]:
                    for tm in s[0]:
                        file_object.write(str(tm))
                        file_object.write("\n")
                        file_object.write(str(s[1]))
                        file_object.write("\n")
                        for r in s[2]:
                            file_object.write(str(r))
                            file_object.write("\n")
                        for t in s[3]:
                            file_object.write(str(t))
                            file_object.write("\n")
                        file_object.write("----\n")


def write(l, n):
    with open("../out" + str(n) + ".txt", "w") as file_object:

        for a in l[n]:
            file_object.write(str(a[0]))
            file_object.write("\n")
            file_object.write(str(a[1].teacher))
            file_object.write("\n")
            file_object.write(str(a[1].form))
            file_object.write("\n")
            file_object.write(str(a[1].subject))
            file_object.write("\n")
            file_object.write(str(a[2]))
            file_object.write("************\n")

def min1(data):
    w = (-1, -1, -1, -1, -1)
    m = list(map(lambda x: (x, sum(x*w)), data))
    return m[min(list(map(lambda x: x[1], m)))]


def main():

    init()

    NGEN = 30
    MU = 50
    LAMBDA = 100
    CXPB = 0.3
    MUTPB = 0.5

    pop = toolbox.population(n=MU)
    hof = tools.HallOfFame(30)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", numpy.mean, axis=0)
    stats.register("std", numpy.std, axis=0)
    stats.register("min", numpy.min, axis=0)
    stats.register("max", numpy.max, axis=0)

    pop, log = algorithms.eaMuPlusLambda(pop, toolbox, MU, LAMBDA, CXPB, MUTPB, NGEN, stats,
                               halloffame=hof)
    hof = hof[0]

    create_excel(hof, day, time)
    write1(hof, 1)

    return pop, stats, hof


if __name__ == '__main__':
    subject = [Subject(name='Math', short_name='Math'), Subject(name='Phycology', short_name='Phyc'),
               Subject(name='Russian', short_name='Rus')]

    teacher = [Teacher(id='123', surname='Runova', impossible_days=[], name='Yuliya', middle_name=''),
               Teacher(id='234', surname='One', impossible_days=[], name='Yuliya', middle_name=''),
               Teacher(id='345', surname='Two', impossible_days=[], name='Yuliya', middle_name=''),
               Teacher(id='678', surname='Three', impossible_days=[], name='Yuliya', middle_name='')]

    room = [Room(number='1', capacity=22), Room(number='2', capacity=22),
            Room(number='3', capacity=22), Room(number='4', capacity=22),
            Room(number='5', capacity=22)]

    day = [WorkDay(number=1, description='Monday'), WorkDay(number=2, description='Tuesday')]

    daily_complexity = {1: 6,
                        2: 8}

    form = [
        Form(class_start=1, people_amount=20, number_letter='5_a', daily_complexity=daily_complexity, max_complexity=3),
        Form(class_start=1, people_amount=20, number_letter='6_a', daily_complexity=daily_complexity, max_complexity=3),
        Form(class_start=1, people_amount=20, number_letter='7_a', daily_complexity=daily_complexity, max_complexity=3)]

    time = [TimePeriod(number=1, description='08:00 - 8:45'), TimePeriod(number=2, description='08:00 - 8:45'),
            TimePeriod(number=3, description='08:00 - 8:45'), TimePeriod(number=4, description='08:00 - 8:45')]

    program_class = [
        ProgramClass(subject=subject[0], teacher=[teacher[0], teacher[1]], possible_rooms=room, room_amount=2,
                     amount_per_week=1, grouped_amount=1, complexity=2, form=form[0]),
        ProgramClass(subject=subject[0], teacher=[teacher[0], teacher[1]], possible_rooms=room, room_amount=2,
                     amount_per_week=1, grouped_amount=1, complexity=2, form=form[1]),
        ProgramClass(subject=subject[0], teacher=[teacher[0], teacher[1]], possible_rooms=room, room_amount=2,
                     amount_per_week=1, grouped_amount=1, complexity=2, form=form[2]),

        ProgramClass(subject=subject[1], teacher=[teacher[2]], possible_rooms=room, room_amount=1,
                     amount_per_week=1, grouped_amount=2, complexity=2, form=form[0]),
        ProgramClass(subject=subject[1], teacher=[teacher[2]], possible_rooms=room, room_amount=1,
                     amount_per_week=1, grouped_amount=2, complexity=2, form=form[1]),
        ProgramClass(subject=subject[1], teacher=[teacher[2]], possible_rooms=room, room_amount=1,
                     amount_per_week=1, grouped_amount=2, complexity=2, form=form[2]),

        ProgramClass(subject=subject[2], teacher=[teacher[3]], possible_rooms=room, room_amount=1,
                     amount_per_week=2, grouped_amount=1, complexity=2, form=form[0]),
        ProgramClass(subject=subject[2], teacher=[teacher[3]], possible_rooms=room, room_amount=1,
                     amount_per_week=2, grouped_amount=1, complexity=2, form=form[1]),
        ProgramClass(subject=subject[2], teacher=[teacher[3]], possible_rooms=room, room_amount=1,
                     amount_per_week=2, grouped_amount=1, complexity=2, form=form[2])
    ]

    # subject = [Subject(name='Math', short_name='Math'), Subject(name='Phycology', short_name='Phyc'),
    #            Subject(name='Russian', short_name='Rus'), Subject(name='History', short_name='Hist'),
    #            Subject(name='Phisics', short_name='Phi'), Subject(name='Music', short_name='Music')]
    #
    # teacher = [Teacher(id='123', surname='Runova', impossible_days=[], name='Yuliya', middle_name=''),
    #            Teacher(id='234', surname='One', impossible_days=[], name='Yuliya', middle_name=''),
    #            Teacher(id='345', surname='Two', impossible_days=[], name='Yuliya', middle_name=''),
    #            Teacher(id='456', surname='Three', impossible_days=[], name='Yuliya', middle_name=''),
    #            Teacher(id='567', surname='Four', impossible_days=[], name='Yuliya', middle_name=''),
    #            Teacher(id='678', surname='Five', impossible_days=[], name='Yuliya', middle_name='')]
    #
    # room = [Room(number='1', capacity=22), Room(number='2', capacity=22),
    #         Room(number='3', capacity=22), Room(number='4', capacity=22),
    #         Room(number='5', capacity=22), Room(number='6', capacity=22),
    #         Room(number='7', capacity=22), Room(number='8', capacity=22),
    #         Room(number='9', capacity=22), Room(number='10', capacity=22)]
    #
    # day = [WorkDay(number=1, description='Monday'), WorkDay(number=2, description='Monday'),
    #        WorkDay(number=3, description='Monday'), WorkDay(number=4, description='Monday'),
    #        WorkDay(number=5, description='Monday'), WorkDay(number=6, description='Monday')]
    #
    # daily_complexity = {1: 4,
    #                     2: 8,
    #                     3: 9,
    #                     4: 9,
    #                     5: 5,
    #                     6: 0}
    #
    # form = [Form(class_start=1, people_amount=20, number_letter='a', daily_complexity=daily_complexity, max_complexity=3),
    #         Form(class_start=1, people_amount=20, number_letter='a', daily_complexity=daily_complexity, max_complexity=3),
    #         Form(class_start=1, people_amount=20, number_letter='a', daily_complexity=daily_complexity, max_complexity=3),
    #         Form(class_start=1, people_amount=20, number_letter='a', daily_complexity=daily_complexity, max_complexity=3)]
    #
    # time = [TimePeriod(number=1, description='08:00 - 8:45'), TimePeriod(number=2, description='08:00 - 8:45'),
    #         TimePeriod(number=3, description='08:00 - 8:45'), TimePeriod(number=4, description='08:00 - 8:45'),
    #         TimePeriod(number=5, description='08:00 - 8:45'), TimePeriod(number=6, description='08:00 - 8:45'),
    #         TimePeriod(number=7, description='08:00 - 8:45'), TimePeriod(number=8, description='08:00 - 8:45'),
    #         TimePeriod(number=9, description='08:00 - 8:45'), TimePeriod(number=10, description='08:00 - 8:45'),
    #         TimePeriod(number=11, description='08:00 - 8:45'), TimePeriod(number=12, description='08:00 - 8:45')]
    #
    # program_class = [ProgramClass(subject=subject[0], teacher=[teacher[0], teacher[1]], possible_rooms=room, room_amount=2,
    #                               amount_per_week=1, grouped_amount=1, complexity=2, form=form[0]),
    #                  ProgramClass(subject=subject[1], teacher=[teacher[0]], possible_rooms=room, room_amount=1,
    #                               amount_per_week=1, grouped_amount=2, complexity=2, form=form[0]),
    #                  ProgramClass(subject=subject[2], teacher=[teacher[0]], possible_rooms=room, room_amount=1,
    #                               amount_per_week=1, grouped_amount=1, complexity=2, form=form[0])]
    main()


