# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 20, 501, 81))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.to_summary_btn = QtWidgets.QPushButton(self.centralwidget)
        self.to_summary_btn.setGeometry(QtCore.QRect(1030, 570, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.to_summary_btn.setFont(font)
        self.to_summary_btn.setObjectName("to_summary_btn")
        self.date_field = QtWidgets.QDateEdit(self.centralwidget)
        self.date_field.setGeometry(QtCore.QRect(190, 90, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.date_field.setFont(font)
        self.date_field.setObjectName("date_field")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 100, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.to_summary_btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.to_summary_btn_2.setGeometry(QtCore.QRect(660, 510, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.to_summary_btn_2.setFont(font)
        self.to_summary_btn_2.setObjectName("to_summary_btn_2")
        self.query_table = QtWidgets.QTableView(self.centralwidget)
        self.query_table.setGeometry(QtCore.QRect(140, 160, 521, 331))
        self.query_table.setObjectName("query_table")
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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "แก้ไขรายการ"))
        self.to_summary_btn.setText(_translate("MainWindow", "กลับไปหน้าหลัก"))
        self.date_field.setDisplayFormat(_translate("MainWindow", "dd-MMM-yyyy"))
        self.label_2.setText(_translate("MainWindow", "วันที่ :"))
        self.to_summary_btn_2.setText(_translate("MainWindow", "กลับไปหน้าหลัก"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())