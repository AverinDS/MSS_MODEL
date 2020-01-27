# coding=utf8

import numpy
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QFileDialog, QMessageBox
from pyqtgraph import mkPen, QtCore

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
        # self.ui.widgetGraphic.setBackground([0, 7, 3, 1])

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
            column_i = 0
            for i_col in df.columns:
                self.ui.tableTS.setItem(i_row, column_i, QTableWidgetItem(str(row[i_col])))
                column_i += 1
        self.ui.tableTS.resizeColumnsToContents()

    def show_graphic(self, df):
        for i_row, row in df.iterrows():
            y_values = [i for i in row.tolist() if not numpy.isnan(i)]
            x_values = [i for i in range(len(y_values))]
            pen = mkPen('y', width=8, style=QtCore.Qt.SolidLine)
            self.ui.widgetGraphic.plot(x_values, y_values, pen=pen)
            # self.ui.widgetGraphic.viewRange([min(x_values), max(x_values), min(y_values), max(y_values)])

            self.ui.widgetGraphic.setXRange(0, max(x_values))
            self.ui.widgetGraphic.setYRange(0, max(y_values))

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

    def show_taus(self, taus, ling):
        self.ui.tableAllProperty.setRowCount(2)
        self.ui.tableAllProperty.setColumnCount(len(taus))
        self.ui.tableAllProperty.setHorizontalHeaderLabels(fields)
        for i in range(len(taus)):
            self.ui.tableAllProperty.setItem(0, i, QTableWidgetItem(
                taus[i]))

        for i in range(len(ling)):
            self.ui.tableAllProperty.setItem(1, i, QTableWidgetItem(
                ling[i]))

        self.ui.tableAllProperty.resizeColumnsToContents()

    def show_error(self, err):
        dialog = QMessageBox()
        dialog.setIcon(QMessageBox.Critical)
        dialog.setText(err)
        dialog.addButton(QMessageBox.Ok)
        dialog.exec()
