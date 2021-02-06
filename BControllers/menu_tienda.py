
from BControllers.carrito import Carrito_Controllers
from BControllers.Categoria import ControllerCategoria
from BControllers.Producto import ControllerProducto
from BControllers.carrito import Carrito_Controllers
from BControllers.Empleado import EmpleadoController
from DHelpers.validacion import validacion
from AModels.carrito import carrito
from DHelpers.menu import Menu
class app():
    def __init__(self, obj_empleado):
        if(obj_empleado!=-1):
            self.tipo_empleado = obj_empleado["tipo_empleado"]
            self.id_empleado=obj_empleado["_id"]
        else:
            self.tipo_empleado=-1

        self.carrito=carrito()
        self.validar=validacion() 
    def menu(self):

        try:
            if (self.tipo_empleado==-1):
                print('''
                ==========================
                    MENU ADMINISTRADOR
                ==========================
                ''')
                menu_principal = ["Empleado","Productos", "Salir"]
                menu=Menu(menu_principal)
                respuesta = menu.show()
                if respuesta == 1:
                    empleado = EmpleadoController()
                    empleado.menu()
                    if empleado.salir:
                        self.menu()
                elif respuesta == 2:
                    producto = ControllerProducto(self.tipo_empleado)
                    producto.menu()
                    if producto.salir:
                        self.menu()
            if (self.tipo_empleado==1):
                print('''
                ==========================
                    MENU ALMACENERO
                ==========================
                ''')
                menu_principal = ["Categoria", "Producto","Salir"]
                menu=Menu(menu_principal)
                respuesta = menu.show()
                if respuesta == 1:
                    categoria = ControllerCategoria()
                    categoria.menu()
                    if categoria.salir:
                        self.menu()
                elif respuesta == 2:
                    producto = ControllerProducto(self.tipo_empleado)
                    producto.menu()
                    if producto.salir:
                        self.menu()
            if (self.tipo_empleado==2):
                print('''
                ==========================
                    MENU VENDEDOR
                ==========================
                ''')
                registro_carrito=self.carrito.get_all_carrito({
                   'id_empleado':self.id_empleado, 
                   },{
                    '_id':1,
                    'id_empleado':1,
                    'nombre_cliente':1,
                    'producto_seleccionado':1,
                    'precio_producto':1,
                    'cantidad_comprada':1,
                    'monto_total':1
                })
                if registro_carrito:
                    if self.validar.question('¿Deseas Mantener el registro existente de los productos en el carrito de compra?'):
                        pass
                    else:
                        self.carrito.delete_carrito_all({
                            'cliente_id':self.id_empleado, 
                        })

                menu_principal = ["Carrito de compra", "Salir"]
                menu=Menu(menu_principal)
                respuesta = menu.show()
                if respuesta == 1:
                    carrito = Carrito_Controllers(self.id_empleado)
                    carrito.menu()
                    if producto.salir:
                        self.menu()
            
            
            

            print("\n Gracias por utilizar el sistema \n")
        except KeyboardInterrupt:
            print('\n Se interrumpio la aplicación')
        except Exception as e:
            print(f'{str(e)}')
