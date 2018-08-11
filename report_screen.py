# -*- coding: utf-8 -*-
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
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

        self.btn_copy_notmatched.clicked.connect(self.copyAll)
        self.btn_copy_notfound.clicked.connect(self.copyAll)
        self.btn_copy_notupdated.clicked.connect(self.copyAll)

    def copyAll(self):
        if self.sender().objectName() == 'btn_copy_notmatched':
            widget = self.lst_notmatched
        elif self.sender().objectName() == 'btn_copy_notfound':
            widget = self.lst_notfound
        else:
            widget = self.lst_notupdated

        items = ""
        for index in range(widget.count()):
            items += "%s\n" % widget.item(index).text()

        cb = QApplication.clipboard()
        cb.clear(mode=cb.Clipboard)
        cb.setText(items, mode=cb.Clipboard)

    def updateValues(self, updated_list, failed_list, code_not_found_list, description_not_found_list, not_uptated_list):
        for item in code_not_found_list:
            self.lst_notfound.addItem(item)
            # para usar qtablewidget
            # rowPosition = self.lst_notfound.rowCount()
            # self.lst_notfound.setColumnCount(2)
            # self.lst_notfound.insertRow(rowPosition)
            # self.lst_notfound.setItem(rowPosition, 0, QTableWidgetItem(item.split(',')[0]))
            # self.lst_notfound.setItem(rowPosition, 1, QTableWidgetItem(item.split(',')[1]))

        for item in description_not_found_list:
            self.lst_notmatched.addItem(item)

        for item in not_uptated_list:
            self.lst_notupdated.addItem(item)

        updated_qty = len(updated_list)
        failed_qty = len(failed_list) + len(code_not_found_list) + len(description_not_found_list)
        total_qty = len(updated_list) + len(failed_list) + len(code_not_found_list) + len(description_not_found_list)

        self.lbl_updated.setText("%s productos actualizados correctamente. %s productos con errores. Total : %s" % (updated_qty, failed_qty, total_qty))
