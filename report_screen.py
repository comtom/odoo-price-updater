# -*- coding: utf-8 -*-
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QIcon
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

    def updateValues(self, updated_list, failed_list, code_not_found_list, description_not_found_list):
        for item in code_not_found_list:
            self.lst_notfound.addItem(item)

        for item in description_not_found_list:
            self.lst_notmatched.addItem(item)

        updated_qty = len(updated_list)
        failed_qty = len(failed_list) + len(code_not_found_list) + len(description_not_found_list)
        total_qty = len(updated_list) + len(failed_list) + len(code_not_found_list) + len(description_not_found_list)
        self.lbl_updated.setText("%s productos actualizados correctamente. %s Productos con errores. Total : %s" % (updated_qty, failed_qty, total_qty))
