# -*- coding: utf-8 -*-
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QIcon
from ui.ui_loading import Ui_Loading


class LoadingScreen(QDialog, Ui_Loading):
    def __init__(self, parent=None, length=1, app=None):
        """Inicializa ventana."""
        super(LoadingScreen, self).__init__(None, Qt.WindowStaysOnTopHint)
        self.setWindowIcon(QIcon("icons/logo-36.png"))
        self.setupUi(self)
        self.app = app
        self.controller = parent
        self.progress_value = 1
        self.progress_total = length

        self.setWindowTitle("Actualizando precios...")

    def updateProgress(self):
        """Actualizar el progreso de la barra."""
        self.progress_value += 1
        self.progress.setValue((self.progress_value / self.progress_total) * 100)
        self.app.processEvents()

    def closeEvent(self, event):
        """No permite cerrar la ventana."""
        event.ignore()
