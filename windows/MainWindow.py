# coding=utf8

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QFileDialog, QMessageBox

from controller.MainWindowController import MainWindowController
from layout.main_window import Ui_MainWindow
from model.model_analysis import fields, propertiesDicIndex

ROUTE_TAG = 'MainWindow'


class MainWindow(QtWidgets.QMainWindow):
    controller = None

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.controller = MainWindowController(self)
        self.ui.button_load_dataset.clicked.connect(lambda i: self.choose_file())
        self.ui.button_analyse.clicked.connect(self.start_analysis)

    def start_analysis(self):
        self.controller.make_analysis()

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

    def show_properties(self, list_model_analysis):
        if len(list_model_analysis) == 0:
            return

        self.ui.tableProperty.setRowCount(len(list_model_analysis))
        self.ui.tableProperty.setColumnCount(len(fields))
        self.ui.tableProperty.setHorizontalHeaderLabels(fields)

        for index_model in range(len(list_model_analysis)):
            column = 0
            for key in propertiesDicIndex.keys():
                self.ui.tableProperty.setItem(index_model, column, QTableWidgetItem(
                    list_model_analysis[index_model].get_property(propertiesDicIndex[key])))
                column += 1
        self.ui.tableProperty.resizeColumnsToContents()

    def show_taus(self, tau_list):
        self.ui.tableAllProperty.setRowCount(1)
        self.ui.tableAllProperty.setColumnCount(len(fields))
        self.ui.tableAllProperty.setHorizontalHeaderLabels(fields)
        for i in range(len(tau_list)):
            self.ui.tableAllProperty.setItem(0, i, QTableWidgetItem(
                tau_list[i]))
        self.ui.tableAllProperty.resizeColumnsToContents()

    def show_error(self, err):
        dialog = QMessageBox()
        dialog.setIcon(QMessageBox.Critical)
        dialog.setText(err)
        dialog.addButton(QMessageBox.Ok)
        dialog.exec()
