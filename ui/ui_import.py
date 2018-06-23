# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/import.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Import(object):
    def setupUi(self, Import):
        Import.setObjectName("Import")
        Import.resize(532, 259)
        self.buttonBox = QtWidgets.QDialogButtonBox(Import)
        self.buttonBox.setGeometry(QtCore.QRect(410, 170, 101, 71))
        self.buttonBox.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Argentina))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.pushButton = QtWidgets.QPushButton(Import)
        self.pushButton.setGeometry(QtCore.QRect(320, 200, 41, 28))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Import)
        self.lineEdit.setGeometry(QtCore.QRect(90, 200, 221, 28))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Import)
        self.label.setGeometry(QtCore.QRect(10, 20, 421, 101))
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(Import)
        self.comboBox.setGeometry(QtCore.QRect(90, 140, 221, 28))
        self.comboBox.setObjectName("comboBox")
        self.lbl_provider = QtWidgets.QLabel(Import)
        self.lbl_provider.setGeometry(QtCore.QRect(10, 140, 81, 20))
        self.lbl_provider.setObjectName("lbl_provider")
        self.lbl_file = QtWidgets.QLabel(Import)
        self.lbl_file.setGeometry(QtCore.QRect(10, 200, 81, 20))
        self.lbl_file.setObjectName("lbl_file")
        self.genFile = QtWidgets.QPushButton(Import)
        self.genFile.setGeometry(QtCore.QRect(390, 20, 131, 31))
        self.genFile.setObjectName("genFile")

        self.retranslateUi(Import)
        self.buttonBox.accepted.connect(Import.accept)
        self.buttonBox.rejected.connect(Import.reject)
        QtCore.QMetaObject.connectSlotsByName(Import)

    def retranslateUi(self, Import):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate("Import", "..."))
        self.label.setText(_translate("Import", "<html><head/><body><p><span style=\" font-size:10pt;\">Esta aplicacion actualiza masivamente los precios de productos. </span></p><p><span style=\" font-size:10pt;\">Para comenzar, presione &quot;Generar Archivo&quot; y luego cargue en el todos los productos para un proveedor determinado.</span></p><p><span style=\" font-size:10pt;\">A continuacion, seleccione el proveedor, el archivo y presione &quot;OK&quot;.</span></p></body></html>"))
        self.lbl_provider.setText(_translate("Import", "Proveedor"))
        self.lbl_file.setText(_translate("Import", "Archivo"))
        self.genFile.setText(_translate("Import", "Generar archivo"))

