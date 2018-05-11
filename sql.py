import psycopg2
import psycopg2.extras

 
class Sql:
    def __init__(self, controller, connection):
        self.handler = None     # connection
        self.cursor = None
        self.products = None    # [ { <provider_code>: { 'id': 0, 'description': '', price: 0.00 } }, { 'SKF': { 'id': 211, 'description': 'Roscamar 2000', price: 110.40 } }, ]
        self.partners = None    # [ { <parner_name>: <id> },  { 'Mengano': 4324 } ]
        self.controller = controller
        self.connection_string = connection

    def connect(self):
        try:
            return psycopg2.connect(self.connection_string)
        except psycopg2.OperationalError:
            self.controller.showDatabaseNotAvailable()
            return None

    def query(self, sql_code):
        if not self.handler:
            self.handler = self.connect()

        #try:
            # with self.handler.cursor() as cur:
            #     cur.execute(sql_code)
            #     return cur.fetchall()
        self.cursor = self.handler.cursor(cursor_factory=psycopg2.extras.DictCursor)
        self.cursor.execute(sql_code)

        tmp = self.cursor.fetchall()
        # self.handler.commit()
        self.cursor.close()
        return tmp
        #except (psycopg2.ProgrammingError, psycopg2.OperationalError):
        #    self.controller.showDatabaseQueryFailed()
        #    return None

    def commit(self):
        return self.handler.commit()

    def close(self):
        if self.handler:
            self.handler.close()
