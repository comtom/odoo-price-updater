#!env/bin/python
# -*- coding: utf-8 -*-
import json
import os
from sys import argv, exit
from psutil import NoSuchProcess, process_iter
from PyQt5.QtWidgets import QApplication, QMessageBox
from controller import Controller


__price_updater_version__ = '1.0.6'     # debe tener 4 digitos

config = dict()

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
        config_path = os.path.join(os.path.join(os.getcwd(), 'config'), 'db.json')
        with open(config_path) as f:
            config = json.load(f)
        
        controller = Controller(app, config, __price_updater_version__)
    else:
        QMessageBox.warning(None, u"Ya se está ejecutando Price Updater", """<b> Hay otra instancia del programa en ejecuci&oacute;n.</b>
            <p>El programa se cerrar&aacute;.""")
        exit(1)

    exit(app.exec_())
