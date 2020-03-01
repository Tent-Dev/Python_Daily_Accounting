# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from my_service.check_editledger import query_table


class Edit_Ui(object):
    def Edit_setupUi(self, MainWindow, user_data):
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
        self.query_table = QtWidgets.QTableWidget(self.centralwidget)
        self.query_table.setGeometry(QtCore.QRect(30, 160, 731, 331))
        self.query_table.setObjectName("query_table")
        self.find_btn = QtWidgets.QPushButton(self.centralwidget)
        self.find_btn.setGeometry(QtCore.QRect(440, 90, 91, 41))
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
        self.date_field.setDateTime(QtCore.QDateTime.currentDateTime())

        self.query_table.setColumnCount(7)
        # self.query_table.setBackground(QtGui.QColor(255, 0, 0))

        date_col = QtWidgets.QTableWidgetItem('Date')
        date_col.setBackground(QtGui.QColor(255, 222, 191))
        self.query_table.setHorizontalHeaderItem(0, date_col)

        desc_col = QtWidgets.QTableWidgetItem('Description')
        desc_col.setBackground(QtGui.QColor(255, 222, 191))
        self.query_table.setHorizontalHeaderItem(1, desc_col)

        income_col = QtWidgets.QTableWidgetItem('Income')
        income_col.setBackground(QtGui.QColor(0, 255, 0))
        self.query_table.setHorizontalHeaderItem(2, income_col)

        spend_col = QtWidgets.QTableWidgetItem('Spend')
        spend_col.setBackground(QtGui.QColor(255, 0, 0))
        self.query_table.setHorizontalHeaderItem(3, spend_col)

        type_col = QtWidgets.QTableWidgetItem('Type')
        type_col.setBackground(QtGui.QColor(255, 222, 191))
        self.query_table.setHorizontalHeaderItem(4, type_col)

        edit_col = QtWidgets.QTableWidgetItem('Action')
        edit_col.setBackground(QtGui.QColor(255, 222, 191))
        self.query_table.setHorizontalHeaderItem(5, edit_col)

        delete_col = QtWidgets.QTableWidgetItem('Delete')
        delete_col.setBackground(QtGui.QColor(255, 222, 191))
        self.query_table.setHorizontalHeaderItem(6, delete_col)
        
        self.user_data = user_data

        self.loadTable()

        self.find_btn.clicked.connect(self.loadTable)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "แก้ไขรายการ"))
        self.to_summary_btn.setText(_translate("MainWindow", "กลับไปหน้าหลัก"))
        self.date_field.setDisplayFormat(_translate("MainWindow", "dd-MMM-yyyy"))
        self.label_2.setText(_translate("MainWindow", "วันที่ :"))
        self.to_summary_btn_2.setText(_translate("MainWindow", "กลับไปหน้าหลัก"))
        self.find_btn.setText(_translate("MainWindow", "ค้นหา"))
        
    def loadTable(self):
        all_data_table = query_table(self.user_data,self.date_field.text())
        print("Prepare to show data on table ==> wait...")
        for row_number,row_data_table in enumerate(all_data_table):
            self.query_table.insertRow(row_number)
            self.query_table.setItem(row_number, 0, QtWidgets.QTableWidgetItem(str("{}".format(row_data_table['date']))))
            self.query_table.setItem(row_number, 1, QtWidgets.QTableWidgetItem(str("{}".format(row_data_table['desc']))))
            self.query_table.setItem(row_number, 2, QtWidgets.QTableWidgetItem(str("{} ฿".format(row_data_table['income']))))
            self.query_table.setItem(row_number, 3, QtWidgets.QTableWidgetItem(str("{} ฿".format(row_data_table['spend']))))
            self.query_table.setItem(row_number, 4, QtWidgets.QTableWidgetItem(str("{}".format(row_data_table['type']))))
            self.btn_edit = QtWidgets.QPushButton('Edit')
            # self.btn_edit.clicked.connect(self.handleButtonClicked)
            self.query_table.setCellWidget(row_number, 5, self.btn_edit)

            self.btn_delete = QtWidgets.QPushButton('Delete')
            # self.btn_edit.clicked.connect(self.handleButtonClicked)
            self.query_table.setCellWidget(row_number, 6, self.btn_delete)

            self.query_table.item(row_number, 2).setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
            self.query_table.item(row_number, 3).setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
            if row_data_table['income'] > 0:
                self.query_table.item(row_number, 2).setBackground(QtGui.QColor(0, 232, 148))
            if row_data_table['spend'] > 0:
                self.query_table.item(row_number, 3).setBackground(QtGui.QColor(255, 150, 142))

        self.query_table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers) #set Read only Table
        print("Prepare to show data on table ==> success")
        print('-' * 30)
