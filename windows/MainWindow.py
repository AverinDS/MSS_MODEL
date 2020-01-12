# coding=utf8

from PyQt5 import QtWidgets

from enumeration.fgos import FGOS
from layout.main_window import Ui_MainWindow
from windows.MainWindowController import MainWindowController

ROUTE_TAG = 'MainWindow'


class MainWindow(QtWidgets.QMainWindow):
    controller = None

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.controller = MainWindowController(self)
        self.ui.lineEditStudentName.textChanged.connect(self.controller.on_changed_student_name)
        self.ui.lineEditStudentLevel.textChanged.connect(self.controller.on_selected_level)
        self.ui.rbFgosFalse.clicked.connect(lambda i: self.controller.on_selected_fgos(FGOS.ALWAYS_FALSE))
        self.ui.rbFgosTrue.clicked.connect(lambda i: self.controller.on_selected_fgos(FGOS.ALWAYS_TRUE))
        self.ui.rbFgosRandom.clicked.connect(lambda i: self.controller.on_selected_fgos(FGOS.RANDOM))
        self.ui.buttonStartModel.clicked.connect(self.controller.model_start)

    def notify_status(self, status_text):
        status = self.ui.plainTextStatus.toPlainText() + status_text + '\n'
        self.ui.plainTextStatus.setPlainText(status)
        self.ui.plainTextStatus.repaint()

    def clear_text_status(self):
        self.ui.plainTextStatus.setPlainText("")
        self.ui.plainTextStatus.repaint()
