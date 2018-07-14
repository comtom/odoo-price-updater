import csv
import sys
import os
import subprocess
from PyQt5.QtWidgets import QMessageBox
from import_screen import ImportScreen
from loading_screen import LoadingScreen
from report_screen import ReportScreen
from sql import Sql


class Controller(object):
    def __init__(self, app, config, version):
        self.version = version
        self.app = app
        self.loadingScreen = None
        self.partner_name = None
        self._conn = None

        self.updated_list = []
        self.failed_list = []
        self.code_not_found_list = []
        self.description_not_found_list = []

        self.database = Sql(self, 'host=\'%s\' dbname=\'%s\' user=\'%s\' password=\'%s\'' % (
            config['host'],
            config['dbname'],
            config['user'],
            config['password'])
        )

        self.importScreen = ImportScreen(self.loadPartners(), self)
        self.reportScreen = ReportScreen(self)

        self.importScreen.show()

    def loadPartners(self):
        """"Conecta a la DB y devuelve una lista de proveedores."""
        try:
            partners = self.database.query('SELECT id, display_name FROM RES_PARTNER WHERE supplier=True')
        except Exception:
            self.showDatabaseQueryFailed()
            return

        self.database.partners = {partner['display_name']: partner['id'] for partner in partners}
        return self.database.partners

    def ingestFile(self, file):
        self.file = []

        with open(file, newline='') as csvfile:
            csvreader = csv.DictReader(csvfile)

            for row in csvreader:
                self.file.append(
                    {
                        'provider_code': str(row['provider_code']).strip(),
                        'description': str(row['description']).strip(),
                        'price': row['price'],
                    }
                )

    def matchProduct(self, provider_code, product_description):
        try:
            product = self.database.products[provider_code]
        except KeyError:
            self.code_not_found_list.append("%s, %s" % (provider_code, product_description))
            return None
        else:
            if product['description'] == product_description:
                return product['id']
            else:
                self.description_not_found_list.append("%s, %s" % (provider_code, product['description']))

    def beginImport(self, file):
        self.ingestFile(file)

        row_number = len(self.file)

        if row_number < 1:
            self.importScreen.showEmptyFileError()
            return

        partner_name = self.importScreen.comboBox.currentText()

        try:
            products = self.database.query(
                """
                    SELECT t.id, s.product_name, s.product_code, t.description_sale, t.description, t.list_price
                    FROM product_product p
                    JOIN product_template t ON p.product_tmpl_id=t.id
                    JOIN product_supplierinfo s on t.id = s.product_tmpl_id
                    WHERE p.active=true and s.name=%s
                """ % self.database.partners[partner_name]
            )
        except Exception:
            self.showDatabaseQueryFailed()
            return

        self.database.products = {str(product['product_code']).strip(): {'id': product['id'], 'description': str(product['product_name']).strip(), 'price': product['list_price']} for product in products}

        self.importScreen.hide()
        self.loadingScreen = LoadingScreen(self, length=row_number, app=self.app)
        self.loadingScreen.show()

        self.importExecutor()

    def importExecutor(self):
        """Ejectuta cada actualizacion."""
        for product in self.file:
            self.loadingScreen.updateProgress()
            product_id = self.matchProduct(product['provider_code'], product['description'])

            if product_id:
                try:
                    self.database.query("""
                        UPDATE product_template SET list_price=%s, write_date=now() WHERE id=%s""" % (
                            product['price'],
                            product_id
                        )
                    )
                except Exception:
                    self.failed_list.append(
                        {
                            'id': product_id,
                            'provider_code': product['provider_code'],
                            'name_template': product['description'],
                            'list_price': product['price'],
                        }
                    )
                else:
                    self.updated_list.append(
                        {
                            'id': product_id,
                            'provider_code': product['provider_code'],
                            'name_template': product['description'],
                            'list_price': product['price'],
                        }
                    )

        self.finishImport()

    def finishImport(self):
        """Termina la etapa de importacion de datos."""
        self.loadingScreen.hide()

        self.database.commit()
        self.database.close()

        self.reportScreen.updateValues(self.updated_list, self.failed_list, self.code_not_found_list, self.description_not_found_list)
        self.reportScreen.show()

    def showDatabaseNotAvailable(self):
        """Muestra un mensaje de error."""
        QMessageBox.information(None, "Base de datos no disponible", """<b> La base de datos no reponde.</b>
            <p>Verifique la conexion de este equipo y la base de datos. Tenga presente
            que esta aplicacion solo funciona in-situ.""")
        self.exit(1)

    def showDatabaseQueryFailed(self):
        """Muestra un mensaje de error."""
        QMessageBox.information(None, "La consulta a la Base de datos ha fallado", """<b> Ha fallado una consulta a la base de datos.</b>
            <p>Verifique la conexion de este equipo y la base de datos.""")
        self.exit(1)

    def generateFile(self):
        """Genera un template que sirve como guia para cargar los productos"""
        path = os.path.join(os.path.expanduser('~'), 'carga_producto.xls')
        try:
            with open(path, "w") as f:
                f.write('price,description,provider_code\n')
        except FileNotFoundError:
            pass

        try:
            subprocess.call('start ' + path, shell=True)
        except OSError:
            pass

    def exit(self, return_value=0):
        """Sale del programa."""
        if self.database:
            self.database.close()

        if self.loadingScreen is None:
            if hasattr(self, 'importScreen') and self.importScreen:
                self.importScreen.close()

            if hasattr(self, 'reportScreen') and self.reportScreen:
                self.reportScreen.close()

        sys.exit(return_value)
