from Aconnection.conn import Connection



class Empleado:
    def __init__(self):
        self.conn = Connection('Farmacia')

    def insert_empleado(self, data):
        collection = 'empleado'
        self.conn.insert(collection, data)

    def update_empleado(self, condition, change):
        collection = 'empleado'
        self.conn.update(collection, condition, change)
    
    def get_empleado_condition_selection(self, condition, selection):
        collection = 'empleado'
        return self.conn.get_all(collection, condition, selection)
        

    def get_empleado_condition(self, condition):
        collection = 'empleado'
        return self.conn.get_one(collection, condition)

    def delete_empleado(self, condition):
        collection = 'empleado'
        self.conn.delete(collection, condition)


    def get_all_validacion(self,condition={}):
        return self.conn.get_all_validacion('empleado',condition)
