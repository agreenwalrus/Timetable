import numpy as np

from timetable.interfaces.singleton import Singleton


class TermChecker:

    POSSIBLE = 0
    IMPOSSIBLE = 1

    def __init__(self, all_dependent, all_conditions, get_possibility):
        self.__dependent__ = all_dependent
        self.__conditions__ = all_conditions
        self.__constraint_matrix__ = np.zeros((len(self.__dependent__), len(self.__conditions__)))
        for dep in all_dependent:
            for cond in all_conditions:
                self.__constraint_matrix__[self.__dependent__.index(dep)][self.__conditions__.index(cond)] = \
                    get_possibility(dep, cond)

    def get_dependent(self):
        return self.__dependent__

    def get_conditions(self):
        return self.__conditions__

    def get_conditional_matrix(self):
        return self.__constraint_matrix__

    def is_possible_pair(self, dependent, condition):
        return self.__constraint_matrix__[self.__dependent__.index(dependent)][self.__conditions__.index(condition)] \
               == TermChecker.POSSIBLE

    def set_impossible(self, dependent, condition):
        self.__constraint_matrix__[self.__dependent__.index(dependent)][self.__conditions__.index(condition)] = \
            self.IMPOSSIBLE

    def set_possible(self, dependent, condition):
        self.__constraint_matrix__[self.__dependent__.index(dependent)][self.__conditions__.index(condition)] = \
            self.POSSIBLE

    def get_possible_states(self, obj):
        possible = []
        obj_ind = self.__dependent__.index(obj)

        for i in range(self.__constraint_matrix__[obj_ind].shape[0]):
            if self.__constraint_matrix__[obj_ind][i] == self.POSSIBLE:
                possible.append(self.__conditions__[i])

        return possible
