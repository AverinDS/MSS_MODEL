import random as rd

from enumeration.fgos import FGOS


class ModuleReport:
    fgos_mode = None
    model = None

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
        mean_mark_for_program = self.get_mean_mark_for_program()
        mean_people_for_program = self.get_mean_people_for_program()
        fgos_structure = self.get_fgos_structure()
        fgos_conditions = self.get_fgos_conditions()
        fgos_result = self.get_fgos_result()
