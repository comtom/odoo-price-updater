# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/report.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Report(object):
    def setupUi(self, Report):
        Report.setObjectName("Report")
        Report.resize(693, 650)
        self.buttonBox = QtWidgets.QDialogButtonBox(Report)
        self.buttonBox.setGeometry(QtCore.QRect(340, 610, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.lbl_updated = QtWidgets.QLabel(Report)
        self.lbl_updated.setGeometry(QtCore.QRect(10, 80, 621, 20))
        self.lbl_updated.setObjectName("lbl_updated")
        self.lbl_title = QtWidgets.QLabel(Report)
        self.lbl_title.setGeometry(QtCore.QRect(10, 20, 351, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_title.setFont(font)
        self.lbl_title.setObjectName("lbl_title")
        self.lbl_notfound = QtWidgets.QLabel(Report)
        self.lbl_notfound.setGeometry(QtCore.QRect(10, 370, 451, 20))
        self.lbl_notfound.setObjectName("lbl_notfound")
        self.lbl_notmatched = QtWidgets.QLabel(Report)
        self.lbl_notmatched.setGeometry(QtCore.QRect(10, 120, 541, 20))
        self.lbl_notmatched.setObjectName("lbl_notmatched")
        self.lst_notmatched = QtWidgets.QListWidget(Report)
        self.lst_notmatched.setGeometry(QtCore.QRect(10, 150, 671, 192))
        self.lst_notmatched.setObjectName("lst_notmatched")
        self.lst_notfound = QtWidgets.QListWidget(Report)
        self.lst_notfound.setGeometry(QtCore.QRect(10, 400, 671, 192))
        self.lst_notfound.setObjectName("lst_notfound")

        self.retranslateUi(Report)
        self.buttonBox.accepted.connect(Report.accept)
        self.buttonBox.rejected.connect(Report.reject)
        QtCore.QMetaObject.connectSlotsByName(Report)

    def retranslateUi(self, Report):
        _translate = QtCore.QCoreApplication.translate
        Report.setWindowTitle(_translate("Report", "Dialog"))
        self.lbl_updated.setText(_translate("Report", "XXXX productos actualizados"))
        self.lbl_title.setText(_translate("Report", "Actualizacion completada"))
        self.lbl_notfound.setText(_translate("Report", "Los siguientes productos no han encontrado (codigo inexistente)"))
        self.lbl_notmatched.setText(_translate("Report", "Los siguientes productos no coinciden con la descripcion (codigo dado de alta)"))

