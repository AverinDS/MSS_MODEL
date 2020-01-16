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
        MainWindow.resize(823, 637)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 40, 121, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 241, 16))
        self.label_2.setObjectName("label_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 120, 341, 121))
        self.groupBox.setObjectName("groupBox")
        self.rbFgosTrue = QtWidgets.QRadioButton(self.groupBox)
        self.rbFgosTrue.setGeometry(QtCore.QRect(10, 20, 291, 20))
        self.rbFgosTrue.setChecked(True)
        self.rbFgosTrue.setObjectName("rbFgosTrue")
        self.rbFgosFalse = QtWidgets.QRadioButton(self.groupBox)
        self.rbFgosFalse.setGeometry(QtCore.QRect(10, 50, 231, 20))
        self.rbFgosFalse.setObjectName("rbFgosFalse")
        self.rbFgosRandom = QtWidgets.QRadioButton(self.groupBox)
        self.rbFgosRandom.setGeometry(QtCore.QRect(10, 80, 241, 20))
        self.rbFgosRandom.setObjectName("rbFgosRandom")
        self.buttonStartModel = QtWidgets.QPushButton(self.centralwidget)
        self.buttonStartModel.setGeometry(QtCore.QRect(130, 270, 131, 32))
        self.buttonStartModel.setObjectName("buttonStartModel")
        self.lineEditStudentName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditStudentName.setGeometry(QtCore.QRect(122, 40, 241, 21))
        self.lineEditStudentName.setObjectName("lineEditStudentName")
        self.lineEditStudentLevel = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditStudentLevel.setGeometry(QtCore.QRect(260, 90, 101, 21))
        self.lineEditStudentLevel.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.lineEditStudentLevel.setObjectName("lineEditStudentLevel")
        self.plainTextStatus = QtWidgets.QTextEdit(self.centralwidget)
        self.plainTextStatus.setGeometry(QtCore.QRect(390, 20, 391, 551))
        self.plainTextStatus.setObjectName("plainTextStatus")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 361, 16))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Электронный учитель"))
        self.label.setText(_translate("MainWindow", "ФИО ученика"))
        self.label_2.setText(_translate("MainWindow", "Уровень до которого нужно обучить"))
        self.groupBox.setTitle(_translate("MainWindow", "ФГОС стандарты"))
        self.rbFgosTrue.setText(_translate("MainWindow", "ФГОС (всегда соответствует)"))
        self.rbFgosFalse.setText(_translate("MainWindow", "ФГОС (всегда не соответствует)"))
        self.rbFgosRandom.setText(_translate("MainWindow", "ФГОС (случайное соответствие)"))
        self.buttonStartModel.setText(_translate("MainWindow", "Запуск модели"))
        self.label_3.setText(_translate("MainWindow", "Добро пожаловать в программу \"Электронный учитель\""))
