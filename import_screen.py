# -*- coding: utf-8 -*-
import os
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon
from ui.ui_import import Ui_Import


class ImportScreen(QDialog, Ui_Import):
    def __init__(self, partners, parent=None):
        """Inicializa ventana."""
        self.controller = parent
        super(ImportScreen, self).__init__(None)
        self.setWindowIcon(QIcon("icons/logo-36.png"))
        self.setupUi(self)

        self.setWindowTitle("Actualizador de precios - Comtom Tech")
        self.buttonBox.button(QDialogButtonBox.Ok).setText("Comenzar")
        self.buttonBox.button(QDialogButtonBox.Cancel).setText("Cancelar")

        self.comboBox.clear()
        self.comboBox.addItem('Seleccione un proveedor')
        self.comboBox.addItems(partners)

        self.pushButton.clicked.connect(self.open)

    def open(self):
        """Muestra un dialogo para abrir un archivo csv y devuelve su ubicacion"""
        file = QFileDialog.getOpenFileName(self, 'Seleccionar archivo a importar', filter='Archivo CSV (*.csv)') or None
        self.lineEdit.setText(file[0])

        return file

    def accept(self):
        """Comienza el proceso de importacion"""
        file = self.lineEdit.text()
        if self.comboBox.currentIndex() == 0:
            QMessageBox.information(self, "No se puede importar", """<b> Debe seleccionar un proveedor.</b>
                <p>Debe seleccionar un proveedor de la lista desplegable para
                poder comenzar el proceso de importacion de precios.""")

        elif not file:
            QMessageBox.information(self, "No se puede importar", """<b> Debe seleccionar un archivo.</b>
                <p>Debe seleccionar un archivo CSV para poder comenzar
                el proceso de importacion de precios.""")

        elif not os.path.isfile(file):
            QMessageBox.information(self, "No se puede importar", """<b> El archivo especificado no existe.</b>
                <p>Debe seleccionar un archivo CSV para poder comenzar
                el proceso de importacion de precios.""")

        else:
            self.controller.beginImport(file)

    def showEmptyFileError(self):
        QMessageBox.information(self, "No se puede importar", """<b> El archivo especificado esta vacio.</b>
            <p>Debe seleccionar un archivo CSV que contenga datos para 
            poder importar datos.""")
