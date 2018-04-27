# -*- coding: utf-8 -*-
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QDesktopWidget, QWidget
from PyQt5.QtGui import QIcon, QPixmap
from ui.ui_report import Ui_Report


class ReportScreen(QDialog, Ui_Report):
    """Ventana de reporte una vez finalizado el proceso."""

    def __init__(self, parent=None):
        """Inicializa ventana."""
        super(ReportScreen, self).__init__(None, Qt.WindowStaysOnTopHint)
        self.controller = parent
        self.setWindowIcon(QIcon("icons/logo-36.png"))
        self.setupUi(self)

        self.setWindowTitle("Actualizador de precios - Comtom Tech")
