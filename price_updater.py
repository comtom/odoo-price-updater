#!env/bin/python
# -*- coding: utf-8 -*-
from sys import argv, exit
from psutil import NoSuchProcess, process_iter
from PyQt5.QtWidgets import QApplication, QMessageBox
from controller import Controller


__timeout_ws__ = 30
__price_updater_version__ = '0.0.1'     # debe tener 4 digitos

config = {
    'host': 'localhost',
    'dbname': 'produccion',
    'user': 'odoo',
    'password': 'odoo',
}

if __name__ == '__main__':
    number_instances = 0
    for proc in process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name'])
        except NoSuchProcess:
            pass
        else:
            if pinfo['name'].split('.')[0] == 'price_updater':
                number_instances += 1

    app = QApplication(argv)

    if number_instances <= 1:
        controller = Controller(app, config, __price_updater_version__)
    else:
        QMessageBox.warning(None, u"Ya se está ejecutando Price Updater", """<b> Hay otra instancia del programa en ejecuci&oacute;n.</b>
            <p>El programa se cerrar&aacute;.""")
        exit(1)

    exit(app.exec_())
