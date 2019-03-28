import random
from operator import attrgetter

import numpy
from deap import algorithms
from deap import base
from deap import creator
from deap import tools

from timetable.DAO.file_source.dao_factory import DAOFactory
from timetable.entity.program_class import ProgramClass
from timetable.service.data_bank import DataBank
from timetable.service.data_bank_filler import DataBankFiller

def create_individual(program_classes):

    individual = []

    for gen in program_classes:
        for _ in range(gen.amount_per_week):
            room = random.choice(gen.possible_rooms)
            t = list(DataBank().get_data("TimePeriod").values())
            time = random.choice(t)
            individual.append((time, gen, room))

    return individual


toolbox = base.Toolbox()


def eval_timetable(individual):

    teachers = {}
    rooms = {}
    forms = {}

    t_conflict = 0
    f_conflict = 0
    r_conflict = 0

    f_window = 0.0

    f_start = 0

    complexity = 0
    COMPLEXITY_STAND = 5

    def prepare(obj, all_list):
        conflict = 0

        if obj not in all_list:
            all_list[obj] = {}
        if day not in all_list[obj]:
            all_list[obj][day] = []
        if window_number in all_list[obj][day]:
            conflict = 1
        else:
            all_list[obj][day].append(window_number)
        return conflict

    for gene in individual:
        time = gene[0]
        room = gene[2]
        teacher = gene[1].teacher
        form = gene[1].form
        day = time.day_of_week
        window_number = time.number

        r_conflict += prepare(room, rooms)
        f_conflict += prepare(form, forms)
        t_conflict += prepare(teacher, teachers)

    for form in forms.values():
        for day in form.values():
            f_window += (max(day) - min(day) + 1) - len(day)
            f_start += min(day) - 1

    return t_conflict + r_conflict + f_conflict + f_window + f_start,
    #return t_conflict, r_conflict, f_conflict, f_window, f_start


def cx_individual(ind1, ind2):

    i = random.choice(range(len(ind1)))
    #b = i
    b = random.choice(range(len(ind1)))

    ind1[i], ind2[b] = cx_gene(ind1[i], ind2[b])

    return ind1, ind2


def mut_individual(individual):
    i = random.choice(range(len(individual)))

    individual[i] = mut_gene(individual[i])
    return individual,
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

def cx_gene(gene1, gene2):
    # return (gene2[0], gene1[1], gene1[2]), (gene1[0], gene2[1], gene1[2])
    return (gene2[0], gene1[1], gene1[2]), (gene1[0], gene2[1], gene2[2])

def mut_gene(gene):
    program_class = gene[1]
    room = random.choice(program_class.possible_rooms)
    t = list(DataBank().get_data("TimePeriod").values())
    time = random.choice(t)
    return time, gene[1], room


def init():

    DataBankFiller.read_data(DAOFactory(), DataBank())

    creator.create("Fitness", base.Fitness, weights=(-1.0,))
    #creator.create("Fitness", base.Fitness, weights=(-1.0, -1.0, -1.0, -1.0, -1.0))
    creator.create("Individual", list, fitness=creator.Fitness)
    db = DataBank()
    program_classes = db.get_data("ProgramClass").values()

    toolbox.register("gene", create_individual, program_classes)
    toolbox.register("individual", tools.initIterate, creator.Individual,
                     toolbox.gene)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    toolbox.register("evaluate", eval_timetable)
    toolbox.register("mate", cx_individual)
    toolbox.register("mutate", mut_individual)
    toolbox.register("select", tools.selSPEA2)


def write1(l, n):
    with open("../out" + str(n) + ".txt", "w") as file_object:
        t = {}

        for a in l:
            time = a[0]
            form = a[1].form
            room = a[2]
            if form not in t:
                t[form] = [[], [], [], [], [], []]
            t[form][time.day_of_week].append((time.number, a[1].subject, room, a[1].teacher))

        forms = t.keys()

        for f in forms:
            file_object.write("*********************\n")
            file_object.write(str(f) + "\n")

            for i in range(len(t[f])):
                file_object.write(str(i) + ")\n")
                for s in t[f][i]:
                    file_object.write(str(s[0]))
                    file_object.write("\n")
                    file_object.write(str(s[1]))
                    file_object.write("\n")
                    file_object.write(str(s[2]))
                    file_object.write("\n")
                    file_object.write(str(s[3]))
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
    m  = list(map(lambda x: (x, sum(x*w)), data))
    return m[min(list(map(lambda x: x[1], m)))]


def main():
    init()

    NGEN = 3000
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
    main()



