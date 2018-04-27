# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/loading.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Loading(object):
    def setupUi(self, Loading):
        Loading.setObjectName("Loading")
        Loading.resize(647, 242)
        self.progress = QtWidgets.QProgressBar(Loading)
        self.progress.setGeometry(QtCore.QRect(140, 160, 361, 23))
        self.progress.setProperty("value", 24)
        self.progress.setObjectName("progress")
        self.lbl_warning = QtWidgets.QLabel(Loading)
        self.lbl_warning.setGeometry(QtCore.QRect(70, 40, 491, 81))
        self.lbl_warning.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_warning.setObjectName("lbl_warning")

        self.retranslateUi(Loading)
        QtCore.QMetaObject.connectSlotsByName(Loading)

    def retranslateUi(self, Loading):
        _translate = QtCore.QCoreApplication.translate
        Loading.setWindowTitle(_translate("Loading", "Dialog"))
        self.lbl_warning.setText(_translate("Loading", "<html><head/><body><p>Advertencia: Cerrar este programa podra causar perdida de informacion.</p><p>Por favor espere a que este proceso finalice.</p></body></html>"))

