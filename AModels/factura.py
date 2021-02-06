from Aconnection.conn import Connection


class factura:
    def __init__(self):
        self.model = Connection('Farmacia')

    def get_all_factura(self,condition={}, select={}):
        return self.model.get_all('factura',condition,select)

    def insert_factura(self, data):
        return self.model.insert('factura',data)

    def update_factura(self, condition, change):
        return self.model.update('factura',condition, change)

