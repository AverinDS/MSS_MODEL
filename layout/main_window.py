# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(766, 598)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 9, 741, 32))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_load_dataset = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.button_load_dataset.setObjectName("button_load_dataset")
        self.horizontalLayout.addWidget(self.button_load_dataset)
        self.button_analyse = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.button_analyse.setObjectName("button_analyse")
        self.horizontalLayout.addWidget(self.button_analyse)
        self.button_save = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.button_save.setObjectName("button_save")
        self.horizontalLayout.addWidget(self.button_save)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 50, 731, 531))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.tableProperty = QtWidgets.QTableWidget(self.gridLayoutWidget)
        self.tableProperty.setObjectName("tableProperty")
        self.tableProperty.setColumnCount(0)
        self.tableProperty.setRowCount(0)
        self.gridLayout.addWidget(self.tableProperty, 0, 1, 1, 1)
        self.tableTS = QtWidgets.QTableWidget(self.gridLayoutWidget)
        self.tableTS.setObjectName("tableTS")
        self.tableTS.setColumnCount(0)
        self.tableTS.setRowCount(0)
        self.gridLayout.addWidget(self.tableTS, 0, 0, 1, 1)
        self.tableAllProperty = QtWidgets.QTableWidget(self.gridLayoutWidget)
        self.tableAllProperty.setObjectName("tableAllProperty")
        self.tableAllProperty.setColumnCount(0)
        self.tableAllProperty.setRowCount(0)
        self.gridLayout.addWidget(self.tableAllProperty, 1, 1, 1, 1)
        self.widgetGraphic = PlotWidget(self.gridLayoutWidget)
        self.widgetGraphic.setObjectName("widgetGraphic")
        self.gridLayout.addWidget(self.widgetGraphic, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_load_dataset.setText(_translate("MainWindow", "Load dataset"))
        self.button_analyse.setText(_translate("MainWindow", "Analyse"))
        self.button_save.setText(_translate("MainWindow", "Save"))
from pyqtgraph import PlotWidget
