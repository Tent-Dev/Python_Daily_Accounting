# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'summarywindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QSizePolicy

from addledgerwindow_gui import AddLedgerUi
from editlimitwindow_gui import editLimit_Ui


class SummaryUi(object):
    def setupSummaryUi(self, MainWindow, user_data):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.summary_table = QtWidgets.QTableView(self.centralwidget)
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

        self.user_data = user_data

        #setText area
        self.Name_label.setText('{} {}'.format(user_data[2],user_data[3]))

        #btn area
        self.addLedger_btn.clicked.connect(self.linktoaddLedger)
        self.editLimit_btn.clicked.connect(self.linktoeditlimit)


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

    def linktoaddLedger(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = AddLedgerUi()
        self.ui.AddLedgerSetupUi(self.window, self.user_data)
        self.window.show()

    def linktoeditlimit(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = editLimit_Ui()
        self.ui.editLimit_setupUi(self.window, self.user_data)
        self.window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = SummaryUi()
    ui.setupSummaryUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
