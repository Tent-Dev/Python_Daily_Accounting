from PyQt5 import QtCore, QtGui, QtWidgets

def errorWarShow(self, title, message):
    WarBox = QtWidgets.QMessageBox()
    WarBox.setIcon(QtWidgets.QMessageBox.Warning)
    WarBox.setWindowTitle(title)
    WarBox.setText(message)
    WarBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
    WarBox.exec_()


def sucessShow(self, title, message):
    SucBox = QtWidgets.QMessageBox()
    SucBox.setIcon(QtWidgets.QMessageBox.Information)
    SucBox.setWindowTitle(title)
    SucBox.setText(message)
    SucBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
    SucBox.exec_()


def errorCriShow(self, title, message):
    CriBox = QtWidgets.QMessageBox()
    CriBox.setIcon(QtWidgets.QMessageBox.Critical)
    CriBox.setWindowTitle(title)
    CriBox.setText(message)
    CriBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
    CriBox.exec_()