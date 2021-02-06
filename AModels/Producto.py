from Aconnection.conn import Connection



class Producto:
    def __init__(self):
        self.conn = Connection('Farmacia')

    def insert_producto(self, data):
        collection = 'producto'
        self.conn.insert(collection, data)

    def update_producto(self, condition, change):
        collection = 'producto'
        self.conn.update(collection, condition, change)
    
    def get_productos(self, condition, selection):
        collection = 'producto'
        return self.conn.get_all(collection, condition, selection)
        

    def get_producto(self, condition):
        collection = 'producto'
        return self.conn.get_one(collection, condition)

    def delete_producto(self, condition):
        collection = 'producto'
        self.conn.delete(collection, condition)

