# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from my_service.alert import errorWarShow
from my_service.check_register import check_inputNormal
from registerwindow_gui import RegisterUi

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Register_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Register_btn.setGeometry(QtCore.QRect(420, 250, 75, 23))
        self.Register_btn.setObjectName("Register_btn")
        self.Login_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Login_btn.setGeometry(QtCore.QRect(330, 250, 75, 23))
        self.Login_btn.setObjectName("Login_btn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 70, 501, 81))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.Username_field = QtWidgets.QLineEdit(self.centralwidget)
        self.Username_field.setGeometry(QtCore.QRect(330, 160, 191, 31))
        self.Username_field.setObjectName("Username_field")
        self.Password_field = QtWidgets.QLineEdit(self.centralwidget)
        self.Password_field.setGeometry(QtCore.QRect(330, 200, 191, 31))
        self.Password_field.setObjectName("Password_field")
        self.Password_field.setEchoMode(QtWidgets.QLineEdit.Password)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 160, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(200, 210, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Login_btn.clicked.connect(self.linktologin)
        self.Register_btn.clicked.connect(self.linktoregister) #To register function
        self.thiswindow = MainWindow #Set variable to this window


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Register_btn.setText(_translate("MainWindow", "Register"))
        self.Login_btn.setText(_translate("MainWindow", "Login"))
        self.label.setText(_translate("MainWindow", "โปรแกรมบันทึกรายรับรายจ่าย"))
        self.label_2.setText(_translate("MainWindow", "Username"))
        self.label_3.setText(_translate("MainWindow", "Password"))

    def linktoregister(self): #Function To register page
        self.Username_field.clear()
        self.Password_field.clear()
        self.window = QtWidgets.QMainWindow()
        self.ui = RegisterUi()
        self.ui.setupRegisterUi(self.window)
        self.window.show()
        # self.thiswindow.hide()

    def linktologin(self): #Function To รindex page
        username = self.Username_field.text()
        password = self.Password_field.text()
        list_check = [username, password]  # List for send to check null value function
        if check_inputNormal(list_check):
            print("ok")
        else:
            errorWarShow(self,'Error!!!', 'Please fill Username or Password')
            self.Username_field.clear()
            self.Password_field.clear()
        # self.Username_field.clear()
        # self.Password_field.clear()
        # self.window = QtWidgets.QMainWindow()
        # self.ui = RegisterUi()
        # self.ui.setupRegisterUi(self.window)
        # self.window.show()
        # self.thiswindow.hide()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
