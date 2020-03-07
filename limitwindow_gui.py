# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'limitwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from editlimitwindow_gui import editLimit_Ui
from historylimitwindow_gui import historyLimit_Ui
from my_service.check_limitValue import query_limitValue, query_data
import datetime


class limitmain_Ui(object):
    def limitmain_setupUi(self, MainWindow, user_data, back):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 10, 501, 81))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.monthlimit_label = QtWidgets.QLabel(self.centralwidget)
        self.monthlimit_label.setGeometry(QtCore.QRect(110, 80, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.monthlimit_label.setFont(font)
        self.monthlimit_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.monthlimit_label.setObjectName("monthlimit_label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 150, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(350, 150, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(590, 150, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.limit_value_label = QtWidgets.QLabel(self.centralwidget)
        self.limit_value_label.setGeometry(QtCore.QRect(70, 190, 191, 81))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.limit_value_label.setFont(font)
        self.limit_value_label.setAlignment(QtCore.Qt.AlignCenter)
        self.limit_value_label.setObjectName("limit_value_label")
        self.usedlimit_value_label = QtWidgets.QLabel(self.centralwidget)
        self.usedlimit_value_label.setGeometry(QtCore.QRect(320, 190, 191, 81))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.usedlimit_value_label.setFont(font)
        self.usedlimit_value_label.setAlignment(QtCore.Qt.AlignCenter)
        self.usedlimit_value_label.setObjectName("usedlimit_value_label")
        self.overlimit_value_label = QtWidgets.QLabel(self.centralwidget)
        self.overlimit_value_label.setGeometry(QtCore.QRect(560, 190, 191, 81))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.overlimit_value_label.setFont(font)
        self.overlimit_value_label.setAlignment(QtCore.Qt.AlignCenter)
        self.overlimit_value_label.setObjectName("overlimit_value_label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(280, 120, 20, 161))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(530, 120, 20, 161))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.to_summary_btn = QtWidgets.QPushButton(self.centralwidget)
        self.to_summary_btn.setGeometry(QtCore.QRect(660, 510, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.to_summary_btn.setFont(font)
        self.to_summary_btn.setObjectName("to_summary_btn")
        self.editlimit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.editlimit_btn.setGeometry(QtCore.QRect(40, 300, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.editlimit_btn.setFont(font)
        self.editlimit_btn.setObjectName("editlimit_btn")
        self.historylimit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.historylimit_btn.setGeometry(QtCore.QRect(240, 300, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.historylimit_btn.setFont(font)
        self.historylimit_btn.setObjectName("historylimit_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.thiswindow = MainWindow
        self.back = back
        self.user_data = user_data

        self.to_summary_btn.clicked.connect(self.back_MainWindow)
        self.editlimit_btn.clicked.connect(self.linktoeditlimit)
        self.historylimit_btn.clicked.connect(self.linktohistoryLimit)

        query_result = query_limitValue(user_data)
        print("query ==> {}".format(query_result))
        if query_result[0] == "PASS":
            self.limit_value_label.setText(str(query_result[1]))

        now = datetime.datetime.today().strftime('%b-%Y')

        user_query_data = query_data(self.user_data, now)
        if user_query_data['limit_value'] < user_query_data['spend_sum']:
            cal_limit = user_query_data['limit_value'] - user_query_data['spend_sum']
        else:
            cal_limit = 0
            self.overlimit_value_label.setText(str(cal_limit))
        self.overlimit_value_label.setText(str(cal_limit))
        self.usedlimit_value_label.setText(str(user_query_data['spend_sum']))
        self.monthlimit_label.setText(str(now))

        if cal_limit >= 0:
            self.overlimit_value_label.setStyleSheet('color: green')
        else:
            self.overlimit_value_label.setStyleSheet('color: red')


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "ควบคุมวงเงิน"))
        self.label_2.setText(_translate("MainWindow", "เดือน"))
        self.monthlimit_label.setText(_translate("MainWindow", "N/A"))
        self.label_4.setText(_translate("MainWindow", "วงเงินของคุณ"))
        self.label_5.setText(_translate("MainWindow", "ใช้ไปแล้ว"))
        self.label_6.setText(_translate("MainWindow", "ใช้เกิน"))
        self.limit_value_label.setText(_translate("MainWindow", "N/A"))
        self.usedlimit_value_label.setText(_translate("MainWindow", "N/A"))
        self.overlimit_value_label.setText(_translate("MainWindow", "N/A"))
        self.to_summary_btn.setText(_translate("MainWindow", "กลับไปหน้าหลัก"))
        self.editlimit_btn.setText(_translate("MainWindow", "แก้ไขวงเงิน"))
        self.historylimit_btn.setText(_translate("MainWindow", "ดูประวัติวงเงิน"))

    def back_MainWindow(self):
        self.back.show()
        self.thiswindow.hide()

    def linktoeditlimit(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = editLimit_Ui()
        self.ui.editLimit_setupUi(self.window, self.user_data, self.thiswindow)
        self.window.show()
        self.thiswindow.hide()

    def linktohistoryLimit(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = historyLimit_Ui()
        self.ui.historyLimit_setupUi(self.window, self.user_data, self.thiswindow)
        self.window.show()
        self.thiswindow.hide()