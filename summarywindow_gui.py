# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'summarywindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtWidgets import QSizePolicy, QTableWidgetItem, QTableWidget, QApplication

from addledgerwindow_gui import *
from analyzewindow_gui import Analyze_UI
from editlimitwindow_gui import editLimit_Ui
from editwindow_gui import Edit_Ui
from my_service.check_login import query_data, query_table
from showallwindow_gui import ShowAll_UI


class SummaryUi(object):
    def setupSummaryUi(self, MainWindow, user_data):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.summary_table = QtWidgets.QTableWidget(self.centralwidget)
        self.summary_table.setGeometry(QtCore.QRect(30, 120, 501, 381))
        self.summary_table.setObjectName("summary_table")
        self.Name_label = QtWidgets.QLabel(self.centralwidget)
        self.Name_label.setGeometry(QtCore.QRect(40, 40, 200, 21))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Name_label.setFont(font)
        self.Name_label.setObjectName("Name_label")
        self.income_label = QtWidgets.QLabel(self.centralwidget)
        self.income_label.setGeometry(QtCore.QRect(380, 40, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.income_label.setFont(font)
        self.income_label.setObjectName("income_label")
        self.spend_label = QtWidgets.QLabel(self.centralwidget)
        self.spend_label.setGeometry(QtCore.QRect(650, 40, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.spend_label.setFont(font)
        self.spend_label.setObjectName("spend_label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 40, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(False)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(530, 40, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(40, 80, 711, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.addLedger_btn = QtWidgets.QPushButton(self.centralwidget)
        self.addLedger_btn.setGeometry(QtCore.QRect(590, 150, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.addLedger_btn.setFont(font)
        self.addLedger_btn.setObjectName("addLedger_btn")
        self.editLedger_btn = QtWidgets.QPushButton(self.centralwidget)
        self.editLedger_btn.setGeometry(QtCore.QRect(590, 220, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.editLedger_btn.setFont(font)
        self.editLedger_btn.setObjectName("editLedger_btn")
        self.analyze_btn = QtWidgets.QPushButton(self.centralwidget)
        self.analyze_btn.setGeometry(QtCore.QRect(590, 360, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.analyze_btn.setFont(font)
        self.analyze_btn.setObjectName("analyze_btn")
        self.seeAll_btn = QtWidgets.QPushButton(self.centralwidget)
        self.seeAll_btn.setGeometry(QtCore.QRect(590, 430, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.seeAll_btn.setFont(font)
        self.seeAll_btn.setObjectName("seeAll_btn")
        self.editLimit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.editLimit_btn.setGeometry(QtCore.QRect(590, 290, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.editLimit_btn.setFont(font)
        self.editLimit_btn.setObjectName("editLimit_btn")
        self.update_table_btn = QtWidgets.QPushButton(self.centralwidget)
        self.update_table_btn.setGeometry(QtCore.QRect(30, 510, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.update_table_btn.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/sync-alt-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.update_table_btn.setIcon(icon)
        self.update_table_btn.setObjectName("update_table_btn")
        self.limit_alert_label = QtWidgets.QLabel(self.centralwidget)
        self.limit_alert_label.setGeometry(QtCore.QRect(350, 520, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.limit_alert_label.setFont(font)
        self.limit_alert_label.setScaledContents(False)
        self.limit_alert_label.setObjectName("limit_alert_label")
        self.limit_alert_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.limit_alert_label_2.setGeometry(QtCore.QRect(550, 520, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.limit_alert_label_2.setFont(font)
        self.limit_alert_label_2.setObjectName("limit_alert_label_2")
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
        self.thiswindow = MainWindow  # Set variable to this window

        self.income_label.setStyleSheet('color: green')
        self.spend_label.setStyleSheet('color: red')
        self.limit_alert_label.setStyleSheet('color: orange')

        self.summary_table.setColumnCount(5)
        # self.summary_table.setBackground(QtGui.QColor(255, 0, 0))

        date_col = QtWidgets.QTableWidgetItem('Date')
        date_col.setBackground(QtGui.QColor(255, 222, 191))
        self.summary_table.setHorizontalHeaderItem(0, date_col)

        desc_col = QtWidgets.QTableWidgetItem('Description')
        desc_col.setBackground(QtGui.QColor(255, 222, 191))
        self.summary_table.setHorizontalHeaderItem(1, desc_col)

        income_col = QtWidgets.QTableWidgetItem('Income')
        income_col.setBackground(QtGui.QColor(0, 255, 0))
        self.summary_table.setHorizontalHeaderItem(2, income_col)

        spend_col = QtWidgets.QTableWidgetItem('Spend')
        spend_col.setBackground(QtGui.QColor(255, 0, 0))
        self.summary_table.setHorizontalHeaderItem(3, spend_col)

        type_col = QtWidgets.QTableWidgetItem('Type')
        type_col.setBackground(QtGui.QColor(255, 222, 191))
        self.summary_table.setHorizontalHeaderItem(4, type_col)

        self.user_data = user_data

        #query
        self.loadTable()

        #setText area
        self.Name_label.setText('{} {}'.format(user_data[2],user_data[3]))

        #btn area
        self.addLedger_btn.clicked.connect(self.linktoaddLedger)
        self.editLimit_btn.clicked.connect(self.linktoeditlimit)
        self.analyze_btn.clicked.connect(self.linktoanalyze)
        self.seeAll_btn.clicked.connect(self.linktoshowall)
        self.editLedger_btn.clicked.connect(self.linktoedit)
        self.update_table_btn.clicked.connect(self.loadTable)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Name_label.setText(_translate("MainWindow", "$Name"))
        self.income_label.setText(_translate("MainWindow", "$Income"))
        self.spend_label.setText(_translate("MainWindow", "$Spend"))
        self.label_2.setText(_translate("MainWindow", "รายรับ :"))
        self.label_3.setText(_translate("MainWindow", "รายจ่าย :"))
        self.addLedger_btn.setText(_translate("MainWindow", "เพิ่มรายการ"))
        self.editLedger_btn.setText(_translate("MainWindow", "แก้ไขรายการ"))
        self.analyze_btn.setText(_translate("MainWindow", "วิเคราะห์"))
        self.seeAll_btn.setText(_translate("MainWindow", "ดูรายการทั้งหมด"))
        self.editLimit_btn.setText(_translate("MainWindow", "ควบคุมวงเงิน"))
        self.update_table_btn.setText(_translate("MainWindow", "อัพเดทข้อมูล"))
        self.limit_alert_label.setText(_translate("MainWindow", "เหลือเงินที่ใช้ได้ตามวงเงิน :"))
        self.limit_alert_label_2.setText(_translate("MainWindow", "$current"))

    def linktoaddLedger(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = AddLedgerUi()
        self.ui.AddLedgerSetupUi(self.window, self.user_data, self.thiswindow)
        self.window.show()
        self.thiswindow.hide()

    def linktoeditlimit(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = editLimit_Ui()
        self.ui.editLimit_setupUi(self.window, self.user_data, self.thiswindow)
        self.window.show()
        self.thiswindow.hide()

    def linktoanalyze(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Analyze_UI()
        self.ui.Analyze_setupUI(self.window, self.user_data, self.thiswindow)
        self.window.show()
        self.thiswindow.hide()

    def linktoshowall(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = ShowAll_UI()
        self.ui.ShowAll_setupUi(self.window, self.user_data, self.thiswindow)
        self.window.show()
        self.thiswindow.hide()

    def linktoedit(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Edit_Ui()
        self.ui.Edit_setupUi(self.window, self.user_data, self.thiswindow)
        self.window.show()
        self.thiswindow.hide()

    def loadTable(self):
        self.summary_table.setRowCount(0)
        all_data_table = query_table(self.user_data)
        all_data_table_sorted = sorted(all_data_table, key=lambda k: k['date'])
        print("Prepare to show data on table ==> wait...")
        for row_number,row_data_table in enumerate(all_data_table_sorted):
            self.summary_table.insertRow(row_number)
            self.summary_table.setItem(row_number, 0, QtWidgets.QTableWidgetItem(str("{}".format(row_data_table['date']))))
            self.summary_table.setItem(row_number, 1, QtWidgets.QTableWidgetItem(str("{}".format(row_data_table['desc']))))
            self.summary_table.setItem(row_number, 2, QtWidgets.QTableWidgetItem(str("{} ฿".format(row_data_table['income']))))
            self.summary_table.setItem(row_number, 3, QtWidgets.QTableWidgetItem(str("{} ฿".format(row_data_table['spend']))))
            self.summary_table.setItem(row_number, 4, QtWidgets.QTableWidgetItem(str("{}".format(row_data_table['type']))))
            self.summary_table.item(row_number, 2).setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
            self.summary_table.item(row_number, 3).setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
            if row_data_table['income'] > 0:
                self.summary_table.item(row_number, 2).setBackground(QtGui.QColor(0, 232, 148))
            if row_data_table['spend'] > 0:
                self.summary_table.item(row_number, 3).setBackground(QtGui.QColor(255, 150, 142))

        self.summary_table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers) #set Read only Table

        user_query_data = query_data(self.user_data)
        print(user_query_data)
        self.income_label.setText('{} ฿'.format(str(user_query_data['income_sum'])))
        self.spend_label.setText('{} ฿'.format(str(user_query_data['spend_sum'])))
        cal_limit = user_query_data['limit_value'] - user_query_data['spend_sum']
        self.limit_alert_label_2.setText(str(cal_limit))
        if cal_limit >= 0:
            self.limit_alert_label_2.setStyleSheet('color: green')
        else:
            self.limit_alert_label_2.setStyleSheet('color: red')
        print("Prepare to show data on table ==> success")
        print('-'*30)

class Firstwindow(QtWidgets.QMainWindow, SummaryUi):
    def __init__(self, parent=None):
        super(Firstwindow, self).__init__(parent)
        self.setupSummaryUi(self)
        self.addLedger_btn.clicked.connect(self.hide)


class Secondwindow(QtWidgets.QDialog, AddLedgerUi):
    def __init__(self, parent=None):
        super(Secondwindow, self).__init__(parent)
        self.AddLedgerSetupUi(self)
        self.to_summary_btn.clicked.connect(self.hide)


class Manager:
    def __init__(self):
        self.first = Firstwindow()
        self.second = Secondwindow()

        self.first.addLedger_btn.clicked.connect(self.second.show)
        self.second.to_summary_btn.clicked.connect(self.first.show)

        self.first.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = SummaryUi()
    ui.setupSummaryUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
