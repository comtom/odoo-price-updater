import csv
from import_screen import ImportScreen
from loading_screen import LoadingScreen
from report_screen import ReportScreen
from sql import Sql


class Controller(object):
    def __init__(self, app, config, version):
        self.loadingScreen = None
        self.partner_name = None
        self.database = Sql("host='%s' dbname='%s' user='%s' password='%s'" % (
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
        self.database.partners = self.database.query('SELECT * FROM RES_PARTNER WHERE supplier=1')
        return self.database.partners       # ['mock', 'mock2']

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
        self.database.products = self.database.query("SELECT id, description, provider_code, internal_reference, price FROM products_products WHERE supplier=%s" % self.database.partners[partner_name])

        self.importScreen.hide()

        self.loadingScreen = LoadingScreen(self, row_number)
        self.loadingScreen.show()

        self.importExecutor()

    def importExecutor(self):
        for product in self.file:

            self.loadingScreen.updateProgress()
            product_id = self.matchProduct(product['provider_code'], product['description'])

            if product_id:
                self.database.query('UPDATE product_product SET price=%s WHERE id=%s', (product['price'], product_id))

        self.finishImport()

    def finishImport(self):
        self.loadingScreen.hide()
        self.database.commit()
        self.reportScreen.show()

    def exit(self):
        """ sale del programa """
        if self.loadingScreen is None:
            self.importScreen.close()
            self.reportScreen.close()

        exit(0)
