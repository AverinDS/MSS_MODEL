# coding=utf8

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QFileDialog

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
        self.controller = MainWindowController(self)
        self.ui.button_load_dataset.clicked.connect(lambda i: self.choose_file())

    def choose_file(self):
        self.controller = MainWindowController(self)
        file_dialog = QFileDialog(self)
        file_dialog.setAcceptMode(QFileDialog.AcceptOpen)
        if file_dialog.exec_() == QFileDialog.Accepted:
            self.controller.file_chosen(file_dialog.selectedFiles()[0])

    def fill_ts(self, df):
        print(df)
        headers = [str(i) for i in df.columns.values.tolist()]

        # Отображение данных на виджете
        self.ui.tableTS.setRowCount(len(df))
        self.ui.tableTS.setColumnCount(len(headers))
        self.ui.tableTS.setHorizontalHeaderLabels(headers)

        for i_row, row in df.iterrows():
            for i_col in range(len(df.columns)):
                self.ui.tableTS.setItem(i_row, i_col, QTableWidgetItem(str(row[i_col])))

    def show_graphic(self, df):
        x_values = [i for i in range(0, len(df.columns))]
        for i_row, row in df.iterrows():
            self.ui.widgetGraphic.plot(x_values, row.tolist())
