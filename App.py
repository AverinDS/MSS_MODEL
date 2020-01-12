# coding=utf8

import sys

from PyQt5 import QtWidgets

from router import Router
from windows.MainWindow import ROUTE_TAG as MAIN_WINDOW_TAG


class App:
    current_window = None

    def __init__(self):
        app = QtWidgets.QApplication([])
        self.current_window = Router().go_to_window(MAIN_WINDOW_TAG)
        sys.exit(app.exec())


App()
