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


# def create_individual(program_classes, all_days, all_periods):
#
#     genes = []
#
#     for pr_class in program_classes:
#         for _ in range(pr_class.amount_per_week):
#             room = random.sample(pr_class.possible_rooms, pr_class.room_amount)
#             day = random.choice(all_days)
#             t = random.choice(all_periods)
#             time = [t - 1, t] if t == max(all_periods) else [t, t + 1] if pr_class.grouped_amount == 2 else [t]
#             genes.append((day, time, pr_class, room))
#
#     return genes


toolbox = base.Toolbox()


# def eval_timetable(individual):
#     rooms = dict()
#     forms = dict()
#     teachers = dict()
#
#     DAY_TIME = 0
#     SUBJECT = 1
#
#     DAY_POSITION = 0
#     TIME_POSITION = 1
#     CLASS_POSITION = 2
#     ROOM_POSITION = 3
#
#     #time conflict
#     t_conflict = 0
#
#     #time conflict
#     r_conflict = 0
#
#     #subcject conflict per day
#     s_conflict = 0
#
#     #time conflict
#     f_conflict = 0
#     #over complexity per day
#     f_over_complexity = 0
#     # amount of windows
#     f_window = 0.0
#     #first class starts
#     f_start = 0
#
#     def additional_form(time_conflict, study_day, program_class):
#         subject_conflict = 0
#         if program_class.subject in study_day[1]:
#             subject_conflict = 1
#         else:
#             study_day[1].append(program_class.subject)
#         study_day[2] += program_class.complexity
#
#         return time_conflict, subject_conflict
#
#     def prepare(obj, all_list, program_class=None, additional=(lambda tc, sd, pr_cl: tc)):
#
#         PERIOD = 0
#
#         conflict = 0
#
#         if obj not in all_list:
#             all_list[obj] = {}
#         if day not in all_list[obj]:
#             all_list[obj][day] = [[], [], 0]
#         for wn in window_number:
#             if wn in all_list[obj][day][PERIOD]:
#                 conflict += 1
#             else:
#                 all_list[obj][day][PERIOD].append(wn)
#         return additional(conflict, all_list[obj][day], program_class)
#
#     for gene in individual:
#
#         day = gene[DAY_POSITION]
#         window_number = gene[TIME_POSITION]
#         room = gene[ROOM_POSITION]
#         teacher = gene[CLASS_POSITION].teacher
#         form = gene[CLASS_POSITION].form
#
#         for r in room:
#             r_conflict += prepare(r, rooms)
#         f_con, s_con = prepare(form, forms, gene[CLASS_POSITION], additional_form)
#         f_conflict += f_con
#         s_conflict += s_con
#         for t in teacher:
#             t_conflict += prepare(t, teachers)
#
#     for form_key in forms.keys():
#         for w_day_number, w_day in forms[form_key].items():
#             t_period = w_day[0]
#             f_over_complexity += sum([com[2] - form_key.daily_complexity[w_day_number]
#                                      if com[2] - form_key.daily_complexity[w_day_number] > 0
#                                      else 0 for form in forms.values() for com in form.values()])
#             f_window += (max(t_period) - min(t_period) + 1) - len(t_period)
#             f_start += min(t_period) - form_key.class_start
#
#     return t_conflict + r_conflict + f_conflict + f_window + f_start + f_over_complexity + s_conflict,


# def cx_individual(ind1, ind2):
#     for i in range(random.choice(range(len(ind1))), len(ind1)):
#         ind1[i], ind2[i] = cx_gene(ind1[i], ind2[i])
#
#     return ind1, ind2
#
#
# def mut_individual(all_day, all_periods, individual):
#     i = random.choice(range(len(individual)))
#
#     individual[i] = mut_gene(individual[i], all_day, all_periods)
#     return individual,
#
# individual

# def cx_individual(ind1, ind2):
#
#     gene_amount = random.choice(range(len(ind1)))
#     gene1 = random.sample(range(len(ind1)), gene_amount)
#     gene2 = random.sample(range(len(ind2)), gene_amount)
#
#     for i in range(gene_amount):
#         ind1[gene1[i]], ind2[gene2[i]] = cx_gene(ind1[gene1[i]], ind2[gene2[i]])
#
#     return ind1, ind2
#
#
# def mut_individual(individual):
#     gene_amount = random.choice(range(len(individual)))
#     gene = random.sample(range(len(individual)), gene_amount)
#
#     for i in range(gene_amount):
#         individual[gene[i]] = mut_gene(individual[gene[i]])
#
#      return individual,

# def cx_gene(gene1, gene2):
#     # return (gene2[0], gene1[1], gene1[2]), (gene1[0], gene2[1], gene1[2])
#     return (gene2[0], gene2[1], gene1[2], gene2[3]), (gene1[0], gene1[1], gene2[2], gene1[3])
#
# def mut_gene(gene, all_day, all_periods):
#     program_class = gene[2]
#     room = random.sample(program_class.possible_rooms, program_class.room_amount)
#     day = random.choice(all_day)
#     t = random.choice(all_periods)
#     time = [t - 1, t] if t == max(all_periods) else [t, t + 1] if program_class.grouped_amount == 2 else [t]
#     return day, time, program_class, room


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

    NGEN = 100
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

    write1(hof, 1)

    return pop, stats, hof


if __name__ == '__main__':

    subject = [Subject(name='Math', short_name='Math'), Subject(name='Phycology', short_name='Phyc'),
               Subject(name='Russian', short_name='Rus'), Subject(name='History', short_name='Hist'),
               Subject(name='Phisics', short_name='Phi'), Subject(name='Music', short_name='Music')]

    teacher = [Teacher(id='123', surname='Runova', impossible_days=[], name='Yuliya'),
               Teacher(id='234', surname='One', impossible_days=[], name='Yuliya'),
               Teacher(id='345', surname='Two', impossible_days=[], name='Yuliya'),
               Teacher(id='456', surname='Three', impossible_days=[], name='Yuliya'),
               Teacher(id='567', surname='Four', impossible_days=[], name='Yuliya'),
               Teacher(id='678', surname='Five', impossible_days=[], name='Yuliya')]

    room = [Room(number='1', capacity=22), Room(number='2', capacity=22),
            Room(number='3', capacity=22), Room(number='4', capacity=22),
            Room(number='5', capacity=22), Room(number='6', capacity=22),
            Room(number='7', capacity=22), Room(number='8', capacity=22),
            Room(number='9', capacity=22), Room(number='10', capacity=22)]

    day = [WorkDay(number=1, description='Monday'), WorkDay(number=2, description='Monday'),
           WorkDay(number=3, description='Monday'), WorkDay(number=4, description='Monday'),
           WorkDay(number=5, description='Monday'), WorkDay(number=6, description='Monday')]

    daily_complexity = {1: 4,
                        2: 8,
                        3: 9,
                        4: 9,
                        5: 5,
                        6: 0}

    form = [Form(class_start=1, people_amount=20, number=5, letter='a', daily_complexity=daily_complexity, max_complexity=3),
            Form(class_start=1, people_amount=20, number=6, letter='a', daily_complexity=daily_complexity, max_complexity=3),
            Form(class_start=1, people_amount=20, number=7, letter='a', daily_complexity=daily_complexity, max_complexity=3),
            Form(class_start=1, people_amount=20, number=8, letter='a', daily_complexity=daily_complexity, max_complexity=3)]

    time = [TimePeriod(number=1, description='08:00 - 8:45'), TimePeriod(number=2, description='08:00 - 8:45'),
            TimePeriod(number=3, description='08:00 - 8:45'), TimePeriod(number=4, description='08:00 - 8:45'),
            TimePeriod(number=5, description='08:00 - 8:45'), TimePeriod(number=6, description='08:00 - 8:45'),
            TimePeriod(number=7, description='08:00 - 8:45'), TimePeriod(number=8, description='08:00 - 8:45'),
            TimePeriod(number=9, description='08:00 - 8:45'), TimePeriod(number=10, description='08:00 - 8:45'),
            TimePeriod(number=11, description='08:00 - 8:45'), TimePeriod(number=12, description='08:00 - 8:45')]

    program_class = [ProgramClass(subject=subject[0], teacher=[teacher[0], teacher[1]], possible_rooms=room, room_amount=2,
                                  amount_per_week=1, grouped_amount=1, complexity=2, form=form[0]),
                     ProgramClass(subject=subject[1], teacher=[teacher[0]], possible_rooms=room, room_amount=1,
                                  amount_per_week=1, grouped_amount=2, complexity=2, form=form[0]),
                     ProgramClass(subject=subject[2], teacher=[teacher[0]], possible_rooms=room, room_amount=1,
                                  amount_per_week=1, grouped_amount=1, complexity=2, form=form[0])]
    main()


