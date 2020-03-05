# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'showallwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from my_service.check_showall import query_table, query_tableByDay


class ShowAll_UI(object):
    def ShowAll_setupUi(self, MainWindow, user_data, back):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(280, 110, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-40, 110, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.startDate_field = QtWidgets.QDateEdit(self.centralwidget)
        self.startDate_field.setGeometry(QtCore.QRect(90, 100, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.startDate_field.setFont(font)
        self.startDate_field.setObjectName("startDate_field")
        self.endstartDate_field = QtWidgets.QDateEdit(self.centralwidget)
        self.endstartDate_field.setGeometry(QtCore.QRect(340, 100, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.endstartDate_field.setFont(font)
        self.endstartDate_field.setObjectName("endstartDate_field")
        self.all_btn = QtWidgets.QPushButton(self.centralwidget)
        self.all_btn.setGeometry(QtCore.QRect(640, 100, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.all_btn.setFont(font)
        self.all_btn.setObjectName("all_btn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 10, 501, 81))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.showall_table = QtWidgets.QTableWidget(self.centralwidget)
        self.showall_table.setGeometry(QtCore.QRect(50, 170, 691, 321))
        self.showall_table.setObjectName("showall_table")
        self.to_summary_btn = QtWidgets.QPushButton(self.centralwidget)
        self.to_summary_btn.setGeometry(QtCore.QRect(660, 510, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.to_summary_btn.setFont(font)
        self.to_summary_btn.setObjectName("to_summary_btn")
        self.find_btn = QtWidgets.QPushButton(self.centralwidget)
        self.find_btn.setGeometry(QtCore.QRect(540, 100, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.find_btn.setFont(font)
        self.find_btn.setObjectName("find_btn")
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

        self.showall_table.setColumnCount(5)
        # self.showall_table.setBackground(QtGui.QColor(255, 0, 0))

        date_col = QtWidgets.QTableWidgetItem('Date')
        date_col.setBackground(QtGui.QColor(255, 222, 191))
        self.showall_table.setHorizontalHeaderItem(0, date_col)

        desc_col = QtWidgets.QTableWidgetItem('Description')
        desc_col.setBackground(QtGui.QColor(255, 222, 191))
        self.showall_table.setHorizontalHeaderItem(1, desc_col)

        income_col = QtWidgets.QTableWidgetItem('Income')
        income_col.setBackground(QtGui.QColor(0, 255, 0))
        self.showall_table.setHorizontalHeaderItem(2, income_col)

        spend_col = QtWidgets.QTableWidgetItem('Spend')
        spend_col.setBackground(QtGui.QColor(255, 0, 0))
        self.showall_table.setHorizontalHeaderItem(3, spend_col)

        type_col = QtWidgets.QTableWidgetItem('Type')
        type_col.setBackground(QtGui.QColor(255, 222, 191))
        self.showall_table.setHorizontalHeaderItem(4, type_col)

        self.user_data = user_data

        self.loadTable()

        self.endstartDate_field.setDateTime(QtCore.QDateTime.currentDateTime())

        self.find_btn.clicked.connect(self.loadTableByDay)
        self.all_btn.clicked.connect(self.loadTable)
        self.to_summary_btn.clicked.connect(self.back_MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "ถึง"))
        self.label_2.setText(_translate("MainWindow", "วันที่ :"))
        self.startDate_field.setDisplayFormat(_translate("MainWindow", "dd-MMM-yyyy"))
        self.endstartDate_field.setDisplayFormat(_translate("MainWindow", "dd-MMM-yyyy"))
        self.all_btn.setText(_translate("MainWindow", "ทั้งหมด"))
        self.label.setText(_translate("MainWindow", "รายการทั้งหมด"))
        self.to_summary_btn.setText(_translate("MainWindow", "กลับไปหน้าหลัก"))
        self.find_btn.setText(_translate("MainWindow", "ค้นหา"))

    def loadTable(self):
        self.showall_table.setRowCount(0)
        self.startDate_field.setDate(QtCore.QDate(2020, 1, 1))
        all_data_table = query_table(self.user_data)
        all_data_table_sorted = sorted(all_data_table, key=lambda k: k['date'])
        print("Prepare to show data on table ==> wait...")
        for row_number,row_data_table in enumerate(all_data_table_sorted):
            self.showall_table.insertRow(row_number)
            self.showall_table.setItem(row_number, 0, QtWidgets.QTableWidgetItem(str("{}".format(row_data_table['date']))))
            self.showall_table.setItem(row_number, 1, QtWidgets.QTableWidgetItem(str("{}".format(row_data_table['desc']))))
            self.showall_table.setItem(row_number, 2, QtWidgets.QTableWidgetItem(str("{} ฿".format(row_data_table['income']))))
            self.showall_table.setItem(row_number, 3, QtWidgets.QTableWidgetItem(str("{} ฿".format(row_data_table['spend']))))
            self.showall_table.setItem(row_number, 4, QtWidgets.QTableWidgetItem(str("{}".format(row_data_table['type']))))
            self.showall_table.item(row_number, 2).setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
            self.showall_table.item(row_number, 3).setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
            if row_data_table['income'] > 0:
                self.showall_table.item(row_number, 2).setBackground(QtGui.QColor(0, 232, 148))
            if row_data_table['spend'] > 0:
                self.showall_table.item(row_number, 3).setBackground(QtGui.QColor(255, 150, 142))

        self.showall_table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers) #set Read only Table
        print("Prepare to show data on table ==> success")
        print('-'*30)

    def loadTableByDay(self):
        self.showall_table.setRowCount(0)
        start_date = self.startDate_field.text()
        end_date = self.endstartDate_field.text()
        all_data_table = query_tableByDay(self.user_data, start_date, end_date)
        all_data_table_sorted = sorted(all_data_table, key=lambda k: k['date'])
        print("Prepare to show data on table ==> wait...")
        for row_number,row_data_table in enumerate(all_data_table_sorted):
            self.showall_table.insertRow(row_number)
            self.showall_table.setItem(row_number, 0, QtWidgets.QTableWidgetItem(str("{}".format(row_data_table['date']))))
            self.showall_table.setItem(row_number, 1, QtWidgets.QTableWidgetItem(str("{}".format(row_data_table['desc']))))
            self.showall_table.setItem(row_number, 2, QtWidgets.QTableWidgetItem(str("{} ฿".format(row_data_table['income']))))
            self.showall_table.setItem(row_number, 3, QtWidgets.QTableWidgetItem(str("{} ฿".format(row_data_table['spend']))))
            self.showall_table.setItem(row_number, 4, QtWidgets.QTableWidgetItem(str("{}".format(row_data_table['type']))))
            self.showall_table.item(row_number, 2).setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
            self.showall_table.item(row_number, 3).setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
            if row_data_table['income'] > 0:
                self.showall_table.item(row_number, 2).setBackground(QtGui.QColor(0, 232, 148))
            if row_data_table['spend'] > 0:
                self.showall_table.item(row_number, 3).setBackground(QtGui.QColor(255, 150, 142))

        self.showall_table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers) #set Read only Table
        print("Prepare to show data on table ==> success")
        print('-'*30)

    def back_MainWindow(self):
        self.back.show()
        self.thiswindow.hide()