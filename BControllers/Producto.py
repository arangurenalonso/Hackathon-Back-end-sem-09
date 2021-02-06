from AModels.Producto import Producto
from AModels.Categoria import Categoria
from DHelpers.validacion import validacion
from DHelpers.menu import Menu


class ControllerProducto:
    def __init__(self,tipo_empleado):
        self.productos = Producto()
        self.categorias = Categoria()
        self.salir = False
        self.validar = validacion()
        self.tipo_empleado=tipo_empleado
    def menu(self):
        try:
            while True:
                if(self.tipo_empleado==-1):
                    print('''
                    ==================
                       Menu Producto
                    ==================
                    ''')
                    lista_menu = ["Mostrar Producto", "Salir"]
                    respuesta = Menu(lista_menu).show()

                    if respuesta == 1:
                        self.show_producto()
                    else:
                        self.salir = True
                        break
                if(self.tipo_empleado!=-1):
                    print('''
                    ==================
                       Menu Producto
                    ==================
                    ''')
                    lista_menu = ["Crear Producto", "Mostrar Producto", "Buscar Producto", "Salir"]
                    respuesta = Menu(lista_menu).show()

                    if respuesta == 1:
                        self.insert_producto()
                    elif respuesta == 2:
                        self.show_producto()
                    elif respuesta == 3:
                        self.search_producto()
                    else:
                        self.salir = True
                        break
        except Exception as e:
            print(f'{str(e)}')

    def insert_producto(self):
        print('''
            ====================
               CREAR PRODUCTO
            ====================
            ''')
        while True:
            Nombre_producto = self.validar.valiar_ingreso_texto("Ingrese el nombre del producto")
            if self.validar.validar_existencia_campo_valor_producto('nombres_producto',Nombre_producto):
                print('El producto ingresado ya existe, ingrese otro producto')
            else:
                break
            
        categ_id=""
        while True:
            nombre_categoria = self.validar.valiar_ingreso_texto("Ingrese la categoria del producto")
            if self.validar.validar_existencia_campo_valor_categoria('nombres_categoria',nombre_categoria):
                categ_id=self.validar.validar_existencia_campo_valor_categoria('nombres_categoria',nombre_categoria)['_id']
                break
            else:
                print('La categoria ingresada no existe')
        stock = self.validar.valiar_ingreso_integer("Ingrese el stock del producto")
        precio = self.validar.valiar_ingreso_double("Ingrese el precio del producto")  
        data = {
            'nombres_producto': Nombre_producto,
            'stock': stock,
            'precio': precio,
            'categoria_identificador':categ_id,
            'categoria': nombre_categoria
        }
        self.productos.insert_producto(data)
        print('''
        =========================
            Producto Creado
        =========================
        ''')
        producto_creado=self.validar.validar_existencia_campo_valor_producto('nombres_producto',Nombre_producto)
        print(self.validar.print_table(producto_creado, ['ID', 'nombres_producto','stock','precio','categoria_identificador','categoria']))
        input('Presiona una tecla para continuar...')
        
    def show_producto(self):
        try:
            print('''
                =====================
                   MOSTRAR PRODUCTO
                =====================
                ''')
            condicion = {}
            seleccion = {
                '_id' : 1,
                'nombres_producto': 1,
                'stock': 1,
                'precio': 1,
                'categoria_identificador': 1,
                'categoria': 1,

            } 
            prod = self.productos.get_productos(condicion, seleccion)   
            print('''
            =========================
                    Productos
            =========================
            ''')
            print(self.validar.print_table(prod, ['ID', 'nombres_producto','stock','precio','categoria_identificador','categoria']))
            input('Presiona una tecla para continuar...')
            
        except Exception as e:
            print(f'{str(e)}')
    
    def search_producto(self):
        try:
            print('''
                =====================
                    BUSCAR PRODUCTO
                =====================
                ''')
            Nombre_Producto = self.validar.valiar_ingreso_texto("Ingrese el nombre del producto a buscar")
            producto_buscado=self.validar.validar_existencia_campo_valor_producto('nombres_producto',Nombre_Producto)
            if producto_buscado:
                print('''
            =========================
               Producto Encontrado
            =========================
            ''')
                print(self.validar.print_table(producto_buscado, ['ID', 'nombres_producto','stock','precio','categoria_identificador','categoria']))
                if self.validar.question('¿Deseas dar mantenimiento al producto?'):
                    opciones = ['Editar', 'Eliminar', 'Salir']
                    respuesta = Menu(opciones).show()
                    print(respuesta)
                    if respuesta == 1:
                        self.update_producto(producto_buscado["_id"])
                    elif respuesta == 2:
                        self.delete_producto(producto_buscado["_id"])
            
            else:
                print("No existe ninguna categoria ingresada con ese nombre")
        except Exception as e:
            print(f'{str(e)}')


    def delete_producto(self,id_producto):
        print('''
            ======================
              ELIMINAR PRODUCTO
            ======================
            ''')
        data = {
            '_id': id_producto,
        }
        self.productos.delete_producto(data)    
        input('Presiona una tecla para continuar...')


    def update_producto(self,id_producto):
        print('''
                =========================
                    ACTUALIZAR PRODUCTO
                =========================
                ''')
        cambio = {}
        if self.validar.question('¿Deseas cambiar el nombre del producto?'):
            while True:
                Nombre_producto = self.validar.valiar_ingreso_texto("Ingrese el nombre del producto")
                if self.validar.validar_existencia_campo_valor_producto('nombres_producto',Nombre_producto):
                    print('El producto ingresado ya existe, ingrese otro producto')
                else:
                    cambio['nombres_producto']=Nombre_producto
                    break
        if self.validar.question('¿Deseas cambiar la categoria del producto?'):
            while True:
                nombre_categoria = self.validar.valiar_ingreso_texto("Ingrese la categoria del producto")
                if self.validar.validar_existencia_campo_valor_categoria('nombres_categoria',nombre_categoria):
                    cambio['categoria_identificador']=self.validar.validar_existencia_campo_valor_categoria('nombres_categoria',nombre_categoria)['_id']
                    cambio['categoria']=nombre_categoria
                    break
                else:
                    print('La categoria ingresada no existe')
        if self.validar.question('¿Deseas actualizar el stock del producto?'):
            stock= self.validar.valiar_ingreso_integer("Ingrese el stock del producto")
            cambio['stock']=stock
        if self.validar.question('¿Deseas actualizar el precio del producto?'):
            precio = self.validar.valiar_ingreso_double("Ingrese el precio del producto")
            cambio['precio']=precio
        
        condicion = {
        '_id': id_producto
        }
        self.productos.update_producto(condicion,cambio)
        
        print('''
        =========================
          Producto Actualizado
        =========================
        ''')


