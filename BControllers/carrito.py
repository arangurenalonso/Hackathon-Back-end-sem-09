from AModels.carrito import carrito
from AModels.factura import factura
from DHelpers.menu import Menu
from DHelpers.validacion import validacion
from AModels.Producto import Producto
from AModels.Empelado import Empleado

class Carrito_Controllers:
    def __init__(self,id_empleado):
        self.id_empleado=id_empleado
        self.carrito = carrito()
        self.salir = False
        self.validar=validacion()
        self.productos=Producto()
        self.factura=factura()
        self.empleado = Empleado()

    def menu(self):
        try:
            registro_carrito=self.carrito.get_all_carrito({
               'id_empleado':self.id_empleado, 
               },{
                '_id':1,
                'id_empleado':1,
                'nombre_empleado':1,
                'producto_seleccionado':1,
                'precio_producto':1,
                'cantidad_comprada':1,
                'monto_total':1
            })
            if registro_carrito:
                
                print('''
                ==================
                    Menu Carrito
                ==================
                ''')
                lista_menu = ["Agregar Productos","Mostrar Carrito", "Editar Carrito", "Finalizar Compra","Salir"]
                respuesta = Menu(lista_menu).show()
                if respuesta == 1:
                    self.agregar_carrito()
                elif respuesta == 2:
                    self.show_carrito()
                    self.menu()
                elif respuesta == 3:
                    self.editar_carrito()
                elif respuesta == 4:
                    self.registrar_factura()
                else:
                    self.salir = True
                    
            else:
                
                print('''
                ==================
                    Menu Carrito
                ==================
                ''')
                lista_menu = ["Agregar Productos","Salir"]
                respuesta = Menu(lista_menu).show()
                if respuesta == 1:
                    self.agregar_carrito()
                else:
                    self.salir = True
                    
                
        except Exception as e:
            print(f'{str(e)}')

    def agregar_carrito(self):
        print('''
            ====================
               Agregar Carrito
            ====================
            ''')
        self.show_producto()
        id_empleado=self.id_empleado
        nombre_empleado=self.validar.validar_existencia_campo_valor("_id",id_empleado,self.empleado)['nombre_empleado']

        while True:
            Nombre_producto = self.validar.valiar_ingreso_texto("Ingrese el nombre del producto")
            if self.validar.validar_existencia_campo_valor_producto('nombres_producto',Nombre_producto):
               precio_producto=self.validar.validar_existencia_campo_valor_producto('nombres_producto',Nombre_producto)['precio']
               break
            else:
               print('No existe el producto deseado')

        
        while True:
            cantidad = self.validar.valiar_ingreso_integer("Ingrese la cantidad deseada")
            if(cantidad > self.validar.validar_existencia_campo_valor_producto('nombres_producto',Nombre_producto)['stock']):
                stock_actual=self.validar.validar_existencia_campo_valor_producto('nombres_producto',Nombre_producto)['stock']
                print(f"No hay en Stock la cantidad Solicitada del producto {Nombre_producto}; en stock hay: {stock_actual} unidades")
                if self.validar.question('¿Deseas aun este producto?'):
                    pass
                else:
                    return
            else:
                break
        
        monto_total = cantidad*precio_producto   
        
        data = {
            'id_empleado': id_empleado,
            'nombre_empleado':nombre_empleado,
            'producto_seleccionado':Nombre_producto,
            'precio_producto':precio_producto,
            'cantidad_comprada':cantidad,
            'monto_total':monto_total,
        }
        self.carrito.insert_carrito(data)
        print('''
        =============================
        Producto agregado al carrito
        =============================
        ''')
        self.menu()
        
    def show_carrito(self):
        try:
            condicion = {}
            seleccion = {
                '_id':0,
                'id_empleado': 1,
                'nombre_empleado': 1,
                'producto_seleccionado': 1,
                'precio_producto': 1,
                'cantidad_comprada':1,
                'monto_total':1,

            } 
            Lista_carrito = self.carrito.get_all_carrito(condicion, seleccion)   
            print('''
            =========================
                Carrito de Compra
            =========================
            ''')
            print(self.validar.print_table(Lista_carrito, ['id_empleado','nombre_empleado','producto_seleccionado','precio_producto','cantidad_comprada','monto_total']))
            input('Presiona una tecla para continuar...')
            
        except Exception as e:
            print(f'{str(e)}')

    def prod_disponibles(self):
        Lista_carrito = self.carrito.get_all_carrito({

        }, {
            '_id':1,
            'id_empleado': 1,
            'nombre_empleado': 1,
            'producto_seleccionado': 1,
            'precio_producto': 1,
            'cantidad_comprada':1,
            'monto_total':1,
        })
          
        Lista_productos = self.productos.get_productos({}, {
            '_id':1,
            'nombres_producto': 1,
            'stock': 1,
            'precio': 1,
            'categoria_identificador':1,
            'categoria': 1,
        })
        
        prod_disponibles=[]
        if  Lista_carrito:
            for producto in Lista_productos: 
                existe=self.carrito.get_all_carrito({
                    'producto_seleccionado':producto['nombres_producto']
                },{})
                if not (existe):
                    prod_disponibles.append(producto)
        else:
            prod_disponibles=Lista_productos
        return prod_disponibles

#Esta bien            
    def show_producto(self):
        try:
            productos_disponibles=self.prod_disponibles()

            print('''
            =========================
                Productos Disponibles
            =========================
            ''')
            
            print(self.validar.print_table(productos_disponibles, ['ID', 'nombres_producto','stock','precio','categoria_identificador','categoria']))
            input('Presiona una tecla para continuar...')
        except Exception as e:
            print(f'{str(e)}')

    def editar_carrito(self):
        self.show_carrito()
        try:
            print('''
                ======================
                    EDITAR CARRITO
                ======================
                ''')
            Nombre_Producto = self.validar.valiar_ingreso_texto("Ingrese el nombre del producto a buscar")

            registro_carrito=self.carrito.get_all_carrito({
               'id_empleado':self.id_empleado, 
               'producto_seleccionado':Nombre_Producto
            },{
                '_id':1,
                'id_empleado':1,
                'nombre_empleado':1,
                'producto_seleccionado':1,
                'precio_producto':1,
                'cantidad_comprada':1,
                'monto_total':1
            })[0]
            if registro_carrito:
                print('''
            =========================
               Registro Encontrado
            =========================
            ''')
                print(self.validar.print_table(registro_carrito, ['ID', 'id_empleado','nombre_empleado','producto_seleccionado','precio_producto','cantidad_comprada','monto_total']))
                if self.validar.question('¿Deseas dar mantenimiento al producto?'):
                    opciones = ['Editar la cantidad comprada', 'Eliminar producto carrito', 'Salir']
                    respuesta = Menu(opciones).show()
                    print(respuesta)
                    if respuesta == 1:
                        self.actualizar_cantidad_comprada(registro_carrito["_id"],registro_carrito)
                    elif respuesta == 2:
                        self.delete_registro_carrito(registro_carrito["_id"])
            
            else:
                print("No existe ninguna categoria ingresada con ese nombre")
                self.menu()
        except Exception as e:
            print(f'{str(e)}')

    def delete_registro_carrito(self,registro_carrito):
        print('''
            ======================
              ELIMINAR PRODUCTO DE CARRITO
            ======================
            ''')
        data = {
            '_id': registro_carrito,
        }
        self.carrito.delete_carrito(data)    
        input('Presiona una tecla para continuar...')
        self.menu()

    def actualizar_cantidad_comprada(self,registro_carrito,objeto_carrito):
        print('''
                ==================================
                    ACTUALIZAR CANTIDAD COMPRADA
                ==================================
                ''')
        cambio = {}
        
        if self.validar.question('¿Deseas actualizar la cantidad comprada?'):
            cantidad_comrpada= self.validar.valiar_ingreso_integer("Ingresar la nueva cantidad comrpada")
            cambio['cantidad_comprada']=cantidad_comrpada
            cambio['monto_total']=cantidad_comrpada*objeto_carrito['precio_producto']
            print(objeto_carrito)
            print(objeto_carrito['precio_producto'])
            print(cambio)        
        condicion = {
        '_id': registro_carrito
        }
        self.carrito.update_carrito(condicion,cambio)
        
        print('''
        =========================
          Producto Actualizado
        =========================
        ''')
        self.menu()

    def registrar_factura(self):
        condicion = {}
        seleccion = {
                '_id':0,
                'id_empleado': 1,
                'nombre_empleado': 1,
                'producto_seleccionado': 1,
                'precio_producto': 1,
                'cantidad_comprada':1,
                'monto_total':1,

            } 
        Lista_carrito = self.carrito.get_all_carrito(condicion, seleccion)  
        listado_productos_comrpados=[]
        total_pagar=0
        id_empleado=""
        nombre_empleado=""
        for carr in Lista_carrito:
            total_pagar+=carr['monto_total']
            producto_comprado={
                'nombre':carr['producto_seleccionado'],
                'cantidad':carr['cantidad_comprada'],
                'precio_unitario':carr['precio_producto']
            }
            listado_productos_comrpados.append(producto_comprado)
            id_empleado=carr['id_empleado']
            nombre_empleado=carr['nombre_empleado']
        data={
            'id_empleado':id_empleado,
            'nombre_empleado':nombre_empleado,
            'listado_productos_comrpados':listado_productos_comrpados,
            'total_pagar':total_pagar

        }
        print(data)
        self.factura.insert_factura(data)
        print('''
        =========================
          Factura creada
        =========================
        ''')
        self.carrito.delete_carrito_all({
                        'id_empleado':id_empleado, 
                    })







