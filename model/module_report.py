import random as rd

from enumeration.fgos import FGOS

THRESHOLD_PROBLEM = 0.6


class ModuleReport:
    fgos_mode = None
    model = None
    mean_mark_for_program = None
    mean_people_for_program = None
    fgos_structure = None
    fgos_conditions = None
    fgos_result = None
    quality = None
    count_of_problem = 0

    def __init__(self, fgos_mode, model):
        self.fgos_mode = fgos_mode
        self.model = model

    def get_mean_mark_for_program(self):
        return rd.randint(40, 100)

    def get_mean_people_for_program(self):
        return rd.randint(50, 100)

    def get_fgos_structure(self):
        return self.get_fgos()

    def get_fgos_conditions(self):
        return self.get_fgos()

    def get_fgos_result(self):
        return self.get_fgos()

    def get_fgos(self):
        if self.fgos_mode == FGOS.ALWAYS_TRUE:
            return 1
        elif self.fgos_mode == FGOS.ALWAYS_FALSE:
            return 0
        else:
            return rd.randint(0, 1)

    def get_quality(self):
        self.mean_mark_for_program = self.get_mean_mark_for_program()
        self.model.notify_status("Средняя оценка по программе: {mean_mark_for_program}".format(
            mean_mark_for_program=self.mean_mark_for_program))

        self.mean_people_for_program = self.get_mean_people_for_program()
        self.model.notify_status("Средний % людей, успешно сдавших программу: {mean_people_for_program} ".format(
            mean_people_for_program=self.mean_people_for_program))

        self.fgos_structure = self.get_fgos_structure()
        self.model.notify_status(
            "Соответствие ФГОС по структуре: {fgos_structure}".format(fgos_structure=self.fgos_structure))

        self.fgos_conditions = self.get_fgos_conditions()
        self.model.notify_status(
            "Соответствие ФГОС по условиям: {fgos_conditions}".format(fgos_conditions=self.fgos_conditions))

        self.fgos_result = self.get_fgos_result()
        self.model.notify_status(
            "Соответствие ФГОС по результатам: {fgos_result}".format(fgos_result=self.fgos_result))

        self.quality = (self.mean_mark_for_program + self.mean_people_for_program) \
                       * self.fgos_structure \
                       * self.fgos_conditions \
                       * self.fgos_result \
                       / 200
        return self.quality

    def make_diagnostic(self):
        if self.quality <= THRESHOLD_PROBLEM:
            self.model.notify_status("Обнаружена проблема")
            self.find_problem()
        else:
            self.model.notify_status("Проблем не обнаружено")

    def find_problem(self):
        self.model.notify_status("Ищем источник проблем")
        if self.fgos_result == 0:
            self.show_problem("Соответствие требованиям к результатам освоения основных образовательных программ")
        if self.fgos_conditions == 0:
            self.show_problem("Соответствие требованиям к условиям реализации")
        if self.fgos_structure == 0:
            self.show_problem("Соответствие требованиям к структуре основных образовательных программ")

        if self.fgos_result * self.fgos_conditions * self.fgos_structure != 0:
            if self.mean_mark_for_program < self.mean_people_for_program:
                self.show_problem("Cредний балл по программе")
            else:
                self.show_problem("Количество людей % освоивших программу")

    def show_problem(self, problem):
        self.count_of_problem = self.count_of_problem + 1
        self.model.notify_status(
            "Проблема № {number}: {problem}".format(
                number=self.count_of_problem, problem=problem))
