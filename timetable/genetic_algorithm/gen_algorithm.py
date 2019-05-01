import random
import numpy


def create_individual(program_classes, all_days, all_periods):

    genes = []

    for pr_class in program_classes:
        for _ in range(pr_class.amount_per_week):
            room = random.sample(pr_class.possible_rooms, pr_class.room_amount)
            day = random.choice(all_days)
            t = random.choice(all_periods)
            time = [t - 1, t] if t == max(all_periods) else [t, t + 1] if pr_class.grouped_amount == 2 else [t]
            genes.append((day, time, pr_class, room))

    return genes


def cx_individual(ind1, ind2):
    for i in range(random.choice(range(len(ind1))), len(ind1)):
        ind1[i], ind2[i] = cx_gene(ind1[i], ind2[i])

    return ind1, ind2


def mut_individual(all_day, all_periods, individual):
    i = random.choice(range(len(individual)))

    individual[i] = mut_gene(individual[i], all_day, all_periods)
    return individual,


def cx_gene(gene1, gene2):
    # return (gene2[0], gene1[1], gene1[2]), (gene1[0], gene2[1], gene1[2])
    return (gene2[0], gene2[1], gene1[2], gene2[3]), (gene1[0], gene1[1], gene2[2], gene1[3])


def mut_gene(gene, all_day, all_periods):
    program_class = gene[2]
    room = random.sample(program_class.possible_rooms, program_class.room_amount)
    day = random.choice(all_day)
    t = random.choice(all_periods)
    time = [t - 1, t] if t == max(all_periods) else [t, t + 1] if program_class.grouped_amount == 2 else [t]
    return day, time, program_class, room


def eval_timetable(individual):
    rooms = dict()
    forms = dict()
    teachers = dict()

    DAY_TIME = 0
    SUBJECT = 1

    DAY_POSITION = 0
    TIME_POSITION = 1
    CLASS_POSITION = 2
    ROOM_POSITION = 3

    #time conflict
    t_conflict = 0

    #time conflict
    r_conflict = 0

    #subcject conflict per day
    s_conflict = 0

    #time conflict
    f_conflict = 0
    #over complexity per day
    f_over_complexity = 0
    # amount of windows
    f_window = 0.0
    #first class starts
    f_start = 0

    def additional_form(time_conflict, study_day, program_class):
        subject_conflict = 0
        if program_class.subject in study_day[1]:
            subject_conflict = 1
        else:
            study_day[1].append(program_class.subject)
        study_day[2] += program_class.complexity

        return time_conflict, subject_conflict

    def prepare(obj, all_list, program_class=None, additional=(lambda tc, sd, pr_cl: tc)):

        PERIOD = 0

        conflict = 0

        if obj not in all_list:
            all_list[obj] = {}
        if day not in all_list[obj]:
            all_list[obj][day] = [[], [], 0]
        for wn in window_number:
            if wn in all_list[obj][day][PERIOD]:
                conflict += 1
            else:
                all_list[obj][day][PERIOD].append(wn)
        return additional(conflict, all_list[obj][day], program_class)

    for gene in individual:

        day = gene[DAY_POSITION]
        window_number = gene[TIME_POSITION]
        room = gene[ROOM_POSITION]
        teacher = gene[CLASS_POSITION].teacher
        form = gene[CLASS_POSITION].form

        for r in room:
            r_conflict += prepare(r, rooms)
        f_con, s_con = prepare(form, forms, gene[CLASS_POSITION], additional_form)
        f_conflict += f_con
        s_conflict += s_con
        for t in teacher:
            t_conflict += prepare(t, teachers)

    for form_key in forms.keys():
        for w_day_number, w_day in forms[form_key].items():
            t_period = w_day[0]
            f_over_complexity += sum([com[2] - form_key.daily_complexity[w_day_number]
                                     if com[2] - form_key.daily_complexity[w_day_number] > 0
                                     else 0 for form in forms.values() for com in form.values()])
            f_window += (max(t_period) - min(t_period) + 1) - len(t_period)
            f_start += min(t_period) - form_key.class_start

    return t_conflict + r_conflict + f_conflict + f_window + f_start + f_over_complexity + s_conflict,
