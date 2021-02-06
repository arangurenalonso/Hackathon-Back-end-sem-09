from Aconnection.conn import Connection



class Categoria:
    def __init__(self):
        self.conn = Connection('Farmacia')

    def insert_categorias(self, data):
        collection = 'categoria'
        self.conn.insert(collection, data)

    def update_categoria(self, condition, change):
        collection = 'categoria'
        self.conn.update(collection, condition, change)
    
    def get_categorias(self, condition, selection):
        collection = 'categoria'
        return self.conn.get_all(collection, condition, selection)
        

    def get_categoria(self, condition):
        collection = 'categoria'
        return self.conn.get_one(collection, condition)

    def delete_categoria(self, condition):
        collection = 'categoria'
        self.conn.delete(collection, condition)

