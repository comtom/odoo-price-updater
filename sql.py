import psycopg2

 
class Sql:
    def __init__(self, connection):
        self.handler = None     # cursor
        self.products = None    # [ { <provider_code>: { 'id': 0, 'description': '', price: 0.00 } }, { 'SKF': { 'id': 211, 'description': 'Roscamar 2000', price: 110.40 } }, ]
        self.partners = None    # [ { <parner_name>: <id> },  { 'Mengano': 4324 } ]
        self.connection_string = connection

    def connect(self):
        conn = psycopg2.connect(self.connection_string)

        return conn.cursor()

    def query(self, sql_code):
        if not self.handler:
            self.handler = self.connect()

        self.handler.execute(sql_code)
        return self.handler.fetchall()

    def commit(self):
        return self.handler.commit()

    def close(self):
        if self.handler:
            self.handler.close()
