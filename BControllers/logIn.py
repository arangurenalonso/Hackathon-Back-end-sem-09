from DHelpers.menu import Menu
from DHelpers.validacion import validacion
from BControllers.menu_tienda import app
from AModels.Empelado import Empleado


class login_Controllers:
    def __init__(self):
        self.salir = False
        self.validar=validacion()
        self.nombre_modulo="Empleado"
        self.empleado = Empleado()
        

    def menu(self):
        try:
            
            
            while True:
                print('''
                ==================
                    Menu Usuario
                ==================
                ''')
                lista_menu = ["Login", "Olvidaste la contraseña", "Salir"]
                respuesta = Menu(lista_menu).show()

                    
                if respuesta == 1:
                    tipo_empleado=self.Login_usuario()
                    if tipo_empleado:
                        app(tipo_empleado).menu()
                elif respuesta == 2:
                    self.forgot_password()
                else:
                    self.salir = True
                    break
        except Exception as e:
            print(f'{str(e)}')

    def forgot_password(self):
        print('''
                =========================
                Olividaste la contraseña
                ========================
                ''')
        dni_empleado=self.validar.validar_dni("Ingresa el DNI ingresado")
        correo_empleado=self.validar.validar_correo("Ingresar el email válido")

        dniExiste=self.validar.validar_existencia_campo_valor("dni_empleado",dni_empleado,self.empleado)

        if( dniExiste):
            print("hola")
            if( dniExiste["correo_empleado"]== correo_empleado):
                print('CREE UNA NUEVA CONTRASEÑA \n')
                id=self.validar.validar_existencia_campo_valor("dni_empleado",dni_empleado,self.empleado)["_id"]
                pass1=self.validar.validar_pass1('ingresa tu nueva contraseña')
                pass2=self.validar.validar_pass2('Confirma tu contraseña',pass1)
                condition={
                    "_id":id
                }
                change={
                    "pass2":pass2
                }
                self.empleado.update_empleado(condition,change)
                input('La contraseña ha sido actualizado correctamente...')
                input('\nPresiona una tecla para continuar...')
            else:
                print('No coincide el Correo y el DNI')
        else:
            if(not dniExiste):
                print('Has ingresado un DNI invalido')
               
    def Login_usuario(self):
        print('''
                ==================
                  Iniciar Sesion
                ==================
                ''')
        dni=input("Ingresa tu DNI>>")
        pass2=input('ingresa tu contraseña>>')

        dniExiste=self.validar.validar_existencia_campo_valor("dni_empleado",dni,self.empleado)
        if(dni=='12345678' and pass2=="admin"):
            return -1
        if(dniExiste):
            if(dniExiste["pass2"] == pass2):
                nombre=dniExiste["nombre_empleado"]
                apellido=dniExiste["apellido_empleado"]
                print(f'\nBienvenido {nombre} {apellido} gusto tenerte otra vez en nuestra tienda\n')
                input('Presiona una tecla para continuar...')
                return dniExiste
            else:
                print('Credenciales no validas ingrese de nuevo (Contraseña equivocada)')
        else:
            print('DNI no registrado')
           
        