# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\bakalavr\diplom\mycloud\auth_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
import register_form
import database
import funcs as f
import cloud_storage_form
from s3 import S3

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(333, 278)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.login_txt = QtWidgets.QLineEdit(self.centralwidget)
        self.login_txt.setGeometry(QtCore.QRect(30, 90, 281, 20))
        self.login_txt.setObjectName("login_txt")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 10, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 120, 47, 13))
        self.label_3.setObjectName("label_3")
        self.pass_txt = QtWidgets.QLineEdit(self.centralwidget)
        self.pass_txt.setGeometry(QtCore.QRect(30, 150, 281, 20))
        self.pass_txt.setObjectName("pass_txt")
        self.pass_txt.setEchoMode(QLineEdit.Password)
        self.login_btn = QtWidgets.QPushButton(self.centralwidget)
        self.login_btn.setGeometry(QtCore.QRect(90, 220, 151, 41))
        self.login_btn.setObjectName("login_btn")
        self.register_link = QtWidgets.QPushButton(self.centralwidget)
        self.register_link.setGeometry(QtCore.QRect(240, 180, 75, 23))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.register_link.setFont(font)
        self.register_link.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.register_link.setStyleSheet("color: rgb(0, 0, 255);")
        self.register_link.setObjectName("register_link")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Авторизация"))
        self.label_2.setText(_translate("MainWindow", "Логин"))
        self.label_3.setText(_translate("MainWindow", "Пароль"))
        self.login_btn.setText(_translate("MainWindow", "Вход"))
        self.register_link.setToolTip(_translate("MainWindow", "зарегайся"))
        self.register_link.setText(_translate("MainWindow", "Регистрация"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
