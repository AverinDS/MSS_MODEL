from threading import Thread

from enumeration.fgos import FGOS
from model.model import Model


class MainWindowController:
    window = None
    current_fgos_mode = FGOS.ALWAYS_TRUE
    level = 1
    studentName = ""

    def __init__(self, window):
        self.window = window

    def model_start(self):
        model = Model()
        model.set_args(student_name=self.studentName, level=self.level, fgos=self.current_fgos_mode,
                       main_controller=self)

        model.start()

    def on_selected_fgos(self, mode):
        self.current_fgos_mode = mode

    def on_selected_level(self, level):
        self.level = level

    def on_changed_student_name(self, student_name):
        self.studentName = student_name

    def notify_status(self, status_text):
        self.window.notify_status(status_text)
