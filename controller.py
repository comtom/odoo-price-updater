import csv
import sys
from PyQt5.QtWidgets import QMessageBox
from import_screen import ImportScreen
from loading_screen import LoadingScreen
from report_screen import ReportScreen
from sql import Sql


class Controller(object):
    def __init__(self, app, config, version):
        self.loadingScreen = None
        self.partner_name = None
        self._conn = None
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
        """"Conecta a la DB y devuelve una lista de proveedores"""
        partners = self.database.query('SELECT id, display_name FROM RES_PARTNER WHERE supplier=True')
        self.database.partners = {partner['display_name']: partner['id'] for partner in partners}

        return self.database.partners

    def ingestFile(self, file):
        self.file = []

        with open(file, newline='') as csvfile:
            csvreader = csv.DictReader(csvfile)

            for row in csvreader:
                self.file.append(
                    {
                        'provider_code': row['provider_code'],
                        'description': row['description']
                    }
                )

    def matchProduct(self, provider_code, product_description):
        product = self.database.products[provider_code]

        if product and product.description == product_description:
            return product.id

    def beginImport(self, file):
        self.ingestFile(file)

        row_number = len(self.file)

        if row_number < 1:
            self.importScreen.showEmptyFileError()
            return

        partner_name = self.importScreen.comboBox.currentText()

        self.database.products = self.database.query("""
            SELECT t.id, p.name_template, p.default_code, t.description_sale, t.description, t.name, t.list_price
            FROM product_product p
            JOIN product_template t ON p.product_tmpl_id=t.id
            JOIN product_supplierinfo s on p.id = s.product_id
            WHERE p.active=true and s.name=%s
            """ % self.database.partners[partner_name]
        )
        # FIXME: revisar cual de p.name_template, t.description_sale, t.description, t.name es el necesario

        self.importScreen.hide()

        self.loadingScreen = LoadingScreen(self, row_number)
        self.loadingScreen.show()

        self.importExecutor()

    def importExecutor(self):
        """Ejectuta cada actualizacion."""
        for product in self.file:
            self.loadingScreen.updateProgress()
            product_id = self.matchProduct(product['provider_code'], product['description'])

            if product_id:
                self.database.query('UPDATE product_template SET list_price=%s, write_date=now() WHERE id=%s', (product['price'], product_id))

        self.finishImport()

    def finishImport(self):
        """Termina la etapa de importacion de datos."""
        self.loadingScreen.hide()
        self.database.commit()
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
            <p>Verifique la conexion de este equipo y la base de datos. Tenga presente
            que esta aplicacion solo funciona in-situ.""")
        self.exit(1)

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
