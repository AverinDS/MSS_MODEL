from model.module_current_knowledge import get_mark_of_knowledge


class Model:
    student_name = None
    level = None
    fgos_mode = None
    main_controller = None
    mark_for_student = None

    def set_args(self, student_name, level, fgos, main_controller):
        self.student_name = student_name
        self.level = level
        self.fgos_mode = fgos
        self.main_controller = main_controller

    def start(self):
        self.main_controller.notify_status(
            'Студент {student_name} начинает выполнять тестирование для программы {level}'.format(
                student_name=self.student_name, level=self.level))

        self.main_controller.notify_status(
            "Студент {student_name} выполнил тестирование для программы {level}".format(student_name=self.student_name,
                                                                                        level=self.level))

        self.main_controller.notify_status("Подсчет баллов по проведенному тесту")

        self.mark_for_student = get_mark_of_knowledge()
        self.main_controller.notify_status(
            "Заработано баллов {mark_for_student}".format(mark_for_student=self.mark_for_student))
        self.mark_for_student.notify_status()

    def notify_status(self, status):
        self.main_controller.notify_status(status)
