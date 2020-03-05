from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from my_service.check_editledger import checkDeleteLedger


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

def questionDialog(self, title, message, id):
    CriBox = QtWidgets.QMessageBox()
    CriBox.setIcon(QtWidgets.QMessageBox.Question)
    CriBox.setWindowTitle(title)
    CriBox.setText("{}\n{}".format(message, id))
    CriBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    CriBox.accepted.connect(lambda: checkDeleteLedger(id))
    CriBox.exec_()