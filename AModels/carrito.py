from Aconnection.conn import Connection


class carrito:
    def __init__(self):
        self.model = Connection('Farmacia')
 
    def get_all_carrito(self,condition={}, select={}):
        return self.model.get_all('carrito',condition,select)
    def get_one_carrito(self, condition,select):
        return self.model.get_one('carrito', condition,select)

    def insert_carrito(self, data):
        return self.model.insert('carrito',data)

    def update_carrito(self, condition, change):
        return self.model.update('carrito',condition, change)
#
    def delete_carrito(self, condition):
        return self.model.delete('carrito',condition)
    def delete_carrito_all(self, condition):
        return self.model.delete_many('carrito',condition)
