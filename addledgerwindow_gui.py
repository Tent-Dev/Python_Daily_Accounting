# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addledgerwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate

from my_service.alert import errorWarShow
from my_service.check_addledger import checkAddLedger
#from summarywindow_gui import SummaryUi
from my_service.check_register import check_inputNormal
from summarywindow_gui import *


class AddLedgerUi(object):
    def AddLedgerSetupUi(self, MainWindow, user_data, back):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 20, 501, 81))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.date_field = QtWidgets.QDateEdit(self.centralwidget)
        self.date_field.setGeometry(QtCore.QRect(140, 90, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.date_field.setFont(font)
        self.date_field.setObjectName("date_field")
        self.date_field.setDateTime(QtCore.QDateTime.currentDateTime()) #Set current date
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 150, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.desc_field = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.desc_field.setGeometry(QtCore.QRect(140, 150, 221, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.desc_field.setFont(font)
        self.desc_field.setObjectName("desc_field")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 240, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 310, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.income_field = QtWidgets.QLineEdit(self.centralwidget)
        self.income_field.setGeometry(QtCore.QRect(140, 300, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.income_field.setFont(font)
        self.income_field.setObjectName("income_field")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 370, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.spend_field = QtWidgets.QLineEdit(self.centralwidget)
        self.spend_field.setGeometry(QtCore.QRect(140, 360, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.spend_field.setFont(font)
        self.spend_field.setObjectName("spend_field")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(370, 310, 21, 20))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(370, 370, 21, 20))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.add_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_btn.setGeometry(QtCore.QRect(140, 420, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.add_btn.setFont(font)
        self.add_btn.setObjectName("add_btn")
        self.reset_btn = QtWidgets.QPushButton(self.centralwidget)
        self.reset_btn.setGeometry(QtCore.QRect(280, 420, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.reset_btn.setFont(font)
        self.reset_btn.setObjectName("reset_btn")
        self.to_summary_btn = QtWidgets.QPushButton(self.centralwidget)
        self.to_summary_btn.setGeometry(QtCore.QRect(660, 510, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.to_summary_btn.setFont(font)
        self.to_summary_btn.setObjectName("to_summary_btn")
        self.type_field = QtWidgets.QComboBox(self.centralwidget)
        self.type_field.setGeometry(QtCore.QRect(140, 240, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.type_field.setFont(font)
        self.type_field.setObjectName("type_field")
        self.type_field.addItem("")
        self.type_field.addItem("")
        self.type_field.addItem("")
        self.type_field.addItem("")
        self.type_field.addItem("")
        self.type_field.addItem("")
        self.type_field.addItem("")
        self.type_field.addItem("")
        self.type_field.setItemText(7, "")
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
        self.thiswindow = MainWindow
        self.back = back

        self.user_data = user_data
        self.income_field.setText("0")
        self.spend_field.setText("0")

        self.add_btn.clicked.connect(self.linktoAdd_Process)
        self.reset_btn.clicked.connect(self.reset_form_btn)
        self.to_summary_btn.clicked.connect(self.back_MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "เพิ่มรายการ"))
        self.label_2.setText(_translate("MainWindow", "วันที่ :"))
        self.date_field.setDisplayFormat(_translate("MainWindow", "dd-MMM-yyyy"))
        self.label_3.setText(_translate("MainWindow", "รายละเอียด :"))
        self.label_4.setText(_translate("MainWindow", "ประเภท :"))
        self.label_5.setText(_translate("MainWindow", "รายรับ :"))
        self.label_6.setText(_translate("MainWindow", "รายจ่าย :"))
        self.label_7.setText(_translate("MainWindow", "฿"))
        self.label_8.setText(_translate("MainWindow", "฿"))
        self.add_btn.setText(_translate("MainWindow", "บันทึก"))
        self.reset_btn.setText(_translate("MainWindow", "ยกเลิก"))
        self.to_summary_btn.setText(_translate("MainWindow", "กลับไปหน้าหลัก"))
        self.type_field.setItemText(0, _translate("MainWindow", "ค่าเดินทาง"))
        self.type_field.setItemText(1, _translate("MainWindow", "ค่าอาหาร"))
        self.type_field.setItemText(2, _translate("MainWindow", "ค่าใช้จ่ายทั่วไป"))
        self.type_field.setItemText(3, _translate("MainWindow", "ค่าใช้จ่ายออนไลน์"))
        self.type_field.setItemText(4, _translate("MainWindow", "ค่าใช้จ่ายของใช้ที่จำเป็น"))
        self.type_field.setItemText(5, _translate("MainWindow", "รายรับทั่วไป"))
        self.type_field.setItemText(6, _translate("MainWindow", "รายรับเงินเดือน"))

    def linktoAdd_Process(self):
        print("adding new data ==> start...")

        date_Transaction = self.date_field.text()
        desc_Transaction = self.desc_field.toPlainText()
        income_Transaction = self.income_field.text()
        income_Transaction_float = float(income_Transaction)
        spend_Transaction = self.spend_field.text()
        spend_Transaction_float = float(spend_Transaction)
        type_Transaction = self.type_field.currentText()

        if income_Transaction :
            income_Transaction_float = 0
        if spend_Transaction == '':
            spend_Transaction_float = 0

        list_check = [date_Transaction, desc_Transaction, type_Transaction]  # List for send to check null value function
        if check_inputNormal(list_check):
            if income_Transaction_float != '' or spend_Transaction_float != '':
                datatoinput = {"username": self.user_data[1],
                               "date": date_Transaction,
                               "desc": desc_Transaction,
                               "income": income_Transaction_float,
                               "spend": spend_Transaction_float,
                               "type": type_Transaction
                               }

                dataLogin = checkAddLedger(datatoinput)
                if(dataLogin):
                    self.desc_field.clear()
                    self.income_field.setText("0")
                    self.spend_field.setText("0")
                    self.type_field.currentText()
                    self.date_field.setDateTime(QtCore.QDateTime.currentDateTime())
            else:
                errorWarShow(self, 'Error!!!', 'Please fill income or spend value')
        else:
            errorWarShow(self, 'Error!!!', 'Please fill description')

    def reset_form_btn(self):
        self.desc_field.clear()
        self.income_field.setText("0")
        self.spend_field.setText("0")
        self.type_field.currentText()
        self.date_field.setDateTime(QtCore.QDateTime.currentDateTime())

    def back_MainWindow(self):
        self.back.show()
        self.thiswindow.hide()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = AddLedgerUi()
    ui.AddLedgerSetupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
