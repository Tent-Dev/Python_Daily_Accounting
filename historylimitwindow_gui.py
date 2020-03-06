# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'historylimitwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from my_service.check_limitValue import query_alllimit


class historyLimit_Ui(object):
    def historyLimit_setupUi(self, MainWindow, user_data, back):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 20, 501, 81))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.historylimit_table = QtWidgets.QTableWidget(self.centralwidget)
        self.historylimit_table.setGeometry(QtCore.QRect(50, 100, 691, 361))
        self.historylimit_table.setObjectName("historylimit_table")
        self.to_summary_btn = QtWidgets.QPushButton(self.centralwidget)
        self.to_summary_btn.setGeometry(QtCore.QRect(660, 510, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.to_summary_btn.setFont(font)
        self.to_summary_btn.setObjectName("to_summary_btn")
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

        self.historylimit_table.setColumnCount(3)
        # self.historylimit_table.setBackground(QtGui.QColor(255, 0, 0))

        date_col = QtWidgets.QTableWidgetItem('Date')
        date_col.setBackground(QtGui.QColor(255, 222, 191))
        self.historylimit_table.setHorizontalHeaderItem(0, date_col)

        limit_col = QtWidgets.QTableWidgetItem('Limit')
        limit_col.setBackground(QtGui.QColor(255, 222, 191))
        self.historylimit_table.setHorizontalHeaderItem(1, limit_col)

        used_col = QtWidgets.QTableWidgetItem('Usable')
        used_col.setBackground(QtGui.QColor(255, 222, 191))
        self.historylimit_table.setHorizontalHeaderItem(2, used_col)

        self.loadTable()

        self.to_summary_btn.clicked.connect(self.back_MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "ประวัติวงเงิน"))
        self.to_summary_btn.setText(_translate("MainWindow", "กลับไปหน้าหลัก"))
        
    def loadTable(self):
        self.historylimit_table.setRowCount(0)
        all_data_table = query_alllimit(self.user_data)
        all_data_table_sorted = sorted(all_data_table, key=lambda k: k['date_create'])
        print("Prepare to show data on table ==> wait...")
        print(all_data_table_sorted)
        for row_number,row_data_table in enumerate(all_data_table_sorted):
            self.historylimit_table.insertRow(row_number)
            self.historylimit_table.setItem(row_number, 0, QtWidgets.QTableWidgetItem(str("{}".format(row_data_table['date_create']))))
            self.historylimit_table.setItem(row_number, 1, QtWidgets.QTableWidgetItem(str("{}".format(row_data_table['limit_value']))))
            self.historylimit_table.setItem(row_number, 2, QtWidgets.QTableWidgetItem(str("{} ฿".format(row_data_table['used']))))

            if row_data_table['used'] < 0:
                self.historylimit_table.item(row_number, 2).setBackground(QtGui.QColor(255, 150, 142))
            else:
                self.historylimit_table.item(row_number, 2).setBackground(QtGui.QColor(0, 232, 148))

        self.historylimit_table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers) #set Read only Table
        print("Prepare to show data on table ==> success")
        print('-'*30)

    def back_MainWindow(self):
        self.back.show()
        self.thiswindow.hide()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = historyLimit_Ui()
    ui.historyLimit_setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
