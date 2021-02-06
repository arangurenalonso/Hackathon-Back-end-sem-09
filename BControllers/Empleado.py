from AModels.Empelado import Empleado
from DHelpers.validacion import validacion
from DHelpers.menu import Menu

class EmpleadoController:
    def __init__(self):
        self.empleado = Empleado()
        self.salir = False
        self.validar = validacion()
        self.nombre_modulo="Empleado"
    
    def menu(self): 
        try:
            while True:
                print(f'''
                 =====================
                Menu {self.nombre_modulo}
                =====================
                ''')
                lista_menu = ["Crear Empleado", "Mostrar Empleado","Mantenimiento Empleado", "Salir"]
                respuesta = Menu(lista_menu).show()

                if respuesta == 1:
                    self.insert_empleado()
                elif respuesta == 2:
                    self.show_empleado()
                elif respuesta == 3:
                    self.mantenimiento_empleado()
                else:
                    self.salir = True
                    break
        except Exception as e:
            print(f'{str(e)}')

    def insert_empleado(self):
        print(f'''
                =====================
                   Crear {self.nombre_modulo}
                =====================
            ''')
        nombre_empleado = self.validar.valiar_ingreso_texto("Ingrese el nombre del nuevo Empleado")
        apellido_empleado=self.validar.valiar_ingreso_texto("Ingrese tu apellidos")
        dni_empleado=self.validar.validar_dni("Ingresar el DNI del nuevo empleado")
        if self.validar.validar_existencia_campo_valor('dni_empleado',dni_empleado,self.empleado):
            input('Este DNI ya ha sido ingresado anteriormente...')
            return
        correo_empleado = self.validar.validar_correo("Ingresar un email válido")
        pass1=self.validar.validar_pass1('Crea tu contraseña')
        pass2=self.validar.validar_pass2('Confirma tu contraseña',pass1)
        Lista_tipo_empleado = ["Almacenero", "Cajero/Vendedor", "Salir"]
        tipo_empleado = Menu(Lista_tipo_empleado).show()
        data = {
            'nombre_empleado': nombre_empleado,
            'apellido_empleado':apellido_empleado,
            'dni_empleado':dni_empleado,
            'correo_empleado':correo_empleado,
            'pass2':pass2,
            'tipo_empleado':tipo_empleado

        }
        
        self.empleado.insert_empleado(data)
        
        print(f'''
        =====================
        {self.nombre_modulo}  creado
        =====================
        ''')
        
        empleado_registrado=self.validar.validar_existencia_campo_valor('nombre_empleado',nombre_empleado,self.empleado)

        print(self.validar.print_table(empleado_registrado, ['ID', 'nombre_empleado','apellido_empleado','dni_empleado','correo_empleado','pass2','tipo_empleado']))
        input('Presiona una tecla para continuar...')

    def show_empleado(self):
        try:
            print(f'''
                =====================
                   MOSTRAR {self.nombre_modulo}
                =====================
                ''')
            condicion = {}
            seleccion = {
                '_id' : 0,
                'nombre_empleado': 1,
                'dni_empleado':1,
                'correo_empleado':1,
                'tipo_empleado':1


            }    
            lista_empleados = self.empleado.get_empleado_condition_selection(condicion, seleccion)
            
            
            print(f'''
            =====================
             {self.nombre_modulo}
            =====================
            ''')
            print(self.validar.print_table(lista_empleados, ['nombre_empleado', 'dni_empleado','correo_empleado', 'tipo_empleado']))
            input('Presiona una tecla para continuar...')

        except Exception as e:
            print(f'{str(e)}')
    
    def mantenimiento_empleado(self):
        try:
            print(f'''
                =====================
                   Buscar {self.nombre_modulo}
                =====================
                ''')
            dni_empleado=self.validar.validar_dni("Ingresar el DNI del Empleado a buscar")
            empleado_registrado=self.validar.validar_existencia_campo_valor('dni_empleado',dni_empleado,self.empleado)

            if empleado_registrado:
                print(f'''
                =====================
                {self.nombre_modulo} encontrado
                =====================
            ''')
                print(self.validar.print_table(empleado_registrado, ['ID', 'nombre_empleado','apellido_empleado','dni_empleado','correo_empleado','pass2','tipo_empleado']))
                if self.validar.question('¿Deseas dar mantenimiento a la categorias?'):
                    opciones = ['Editar', 'Eliminar', 'Salir']
                    respuesta = Menu(opciones).show()
                    print(respuesta)
                    if respuesta == 1:
                        self.update_empleado(empleado_registrado["_id"])
                    elif respuesta == 2:
                        self.delete_empleado(empleado_registrado["_id"])
            else:
                print("No existe ninguna categoria ingresada con ese nombre")
            
        except Exception as e:
            print(f'{str(e)}')
        input('Presiona una tecla para continuar...')
    
    def delete_empleado(self,id):
        
        data = {
            '_id': id
        }
        self.empleado.delete_empleado(data)
        print(f'''
        =========================
          {self.nombre_modulo} Eliminado
        =========================
        ''')




    def update_empleado(self, id):   
    
        print(f'''
        =========================
        Actualizar {self.nombre_modulo}
        =========================
        ''')
        cambio = {}
        if self.validar.question('¿Deseas actualizar el nombre del empleado?'):
            nombre_empleado = self.validar.valiar_ingreso_texto("Ingrese el nombre del nuevo Empleado")
            cambio['nombre_empleado']=nombre_empleado
        if self.validar.question('¿Deseas actualizar el apellido del empleado?'):
            apellido_empleado=self.validar.valiar_ingreso_texto("Ingrese tu apellidos")
            cambio['apellido_empleado']=apellido_empleado
        if self.validar.question('¿Deseas actualizar el DNI del empleado?'):
            dni_empleado=self.validar.validar_dni("Ingresar el DNI del nuevo empleado")
            cambio['dni_empleado']=dni_empleado
        if self.validar.question('¿Deseas actualizar el correo  electrónico del empleado?'):
            correo_empleado = self.validar.validar_correo("Ingresar un email válido")
            cambio['correo_empleado']=correo_empleado
        if self.validar.question('¿Deseas actualizar el rol del empleado?'):
            Lista_tipo_empleado = ["Almacenero", "Cajero/Vendedor", "Salir"]
            tipo_empleado = Menu(Lista_tipo_empleado).show()
            cambio['tipo_empleado']=tipo_empleado
        condicion = {
            '_id': id
        }
        self.empleado.update_empleado(condicion,cambio)
        


        print(f'''
        =========================
          {self.nombre_modulo} Actualizada
        =========================
        ''')

