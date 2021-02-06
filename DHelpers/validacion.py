import re
from prettytable import PrettyTable
from AModels.carrito import carrito
from AModels.Categoria import Categoria
from AModels.Producto import Producto

class validacion:
    def __init__(self):
        self.categoria=Categoria()
        self.producto=Producto()
        self.carrito=carrito()
    
    def validar_existencia_campo_valor(self,campo,valor,objeto):
        lista=objeto.get_all_validacion({})
        encontro_coincidencia=False
        for unidad in lista:
            if(unidad[f"{campo}"]==valor):
                encontro_coincidencia=unidad
        return encontro_coincidencia   

    def validar_existencia_campo_valor_producto(self,campo,valor):
        lista_producto=self.producto.get_productos({
                
            },{
                '_id':1,
                'nombres_producto':1,
                'stock':1,
                'precio':1,
                'categoria_identificador':1,
                'categoria':1
            })
        encontro_coincidencia=False
        for prod in lista_producto:
            if(prod[f"{campo}"]==valor):
                encontro_coincidencia=prod
        return encontro_coincidencia   


    def validar_existencia_campo_valor_categoria(self,campo,valor):
        lista_categoria=self.categoria.get_categorias({
                
            },{
                '_id':1,
                'nombres_categoria':1,
            })
        encontro_coincidencia=False
        for categ in lista_categoria:
            if(categ[f"{campo}"]==valor):
                encontro_coincidencia=categ
        return encontro_coincidencia   

    #def validar_existencia_campo_valor(self,campo,valor):
    #    lista_usuarios=self.usuario.get_all_usuarios({
    #            
    #        },{
    #            '_id':1,
    #            'nombres':1,
    #            'apellido':1,
    #            'dni':1,
    #            'correo':1,
    #            'password':1
    #        })
    #    encontro_coincidencia=False
    #    for usuario in lista_usuarios:
    #        if(usuario[f"{campo}"]==valor):
    #            encontro_coincidencia=usuario
    #    return encontro_coincidencia   
###############################################################################
    @staticmethod
    def valiar_ingreso_texto(Comentario):
        expresion_regular="^[A-Za-záéíóúñ ]*$"
        while True:
            texto=input(f"{Comentario}>>").strip()
            if re.match(expresion_regular,texto):
                return texto
            else:
                print("Error-El texto ingresado contiene caracteres no alfabeticos") 
    @classmethod
    def validar_tipo_empleado(cls,Comentario):
        dni=""
        while True:
            dni=input(f"{Comentario}:\n").strip()
            if len(dni)==8 and cls.validar_caracter_numero(dni):
                return dni
            else:
                if not(len(dni)==8):
                    print('''Error: El DNI tiene ingresado no tiene 8 caracteres''')
                if not(cls.validar_caracter_numero(dni)):
                    print('''Error: El DNI ingresado tiene caracteres alfabeticos''')
       
    @classmethod
    def validar_dni(cls,Comentario):
        dni=""
        while True:
            dni=input(f"{Comentario}:\n").strip()
            if len(dni)==8 and cls.validar_caracter_numero(dni):
                return dni
            else:
                if not(len(dni)==8):
                    print('''Error: El DNI tiene ingresado no tiene 8 caracteres''')
                if not(cls.validar_caracter_numero(dni)):
                    print('''Error: El DNI ingresado tiene caracteres alfabeticos''')
    @staticmethod
    def validar_pass1(Comentario):
        while True:
            pass1=input(f"{Comentario}:\n").strip()
            expresion_regular ='^(?=\w*\d)(?=\w*[A-Z])(?=\w*[a-z])\S{8,16}$'
            if re.match(expresion_regular,pass1) :
                return pass1
            else:
                print('La contraseña debe tener al entre 8 y 16 caracteres, al menos un dígito, al menos una minúscula y al menos una mayúscula')
    @staticmethod
    def validar_pass2(Comentario, pass1):
        while True:
            pass2=input(f"{Comentario}:\n").strip()
            if pass1==pass2 :
                return pass2
            else:
                print('La contraseña ingresada no coincide con la anterior')
                                    
    @staticmethod
    def validar_caracter_numero(texto):
        valor_de_Verdad=True
        for caracter in texto:
            try: 
                caracter_int=int(caracter)
            except ValueError:
                valor_de_Verdad=False
        return valor_de_Verdad

    @staticmethod
    def validar_edad(Comentario):
        edad=''
        while True:
            try:
                while True:
                    edad=int(input(f"{Comentario}:\n"))
                    if edad>=0 and edad<=100:
                        return edad
                    else:
                        print("Error-Ingrese una edad entre 0 a 100")
                break
            
            except ValueError:
                print(f'Error-Ingrese un numero valido')
    @staticmethod
    def validar_correo(Comentario):
        correo=''
        while True:
            correo=input(f"{Comentario}:\n")
            expresion_regular = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
    
            if re.match(expresion_regular,correo.lower()):
                return correo
            else:
                print("Error-Correo ingresado no válido")

    
    @staticmethod
    def valiar_ingreso_integer(Comentario):
        
        while True:
            try:
                num=int(input(f"{Comentario}>>").strip())
                if num>=0:
                    return num
                else:
                    print("Debe ingresar un valor entero mayor a 0")
            except:
                print("Error-El valor ingresado no es un entero")
    @staticmethod
    def valiar_ingreso_double(Comentario):
        
        while True:
            try:
                num=float(input(f"{Comentario}>>").strip())
                if num>=0:
                    return num
                else:
                    print("Debe ingresar un valor entero mayor a 0")
            except:
                print("Error-El valor ingresado no es un entero")

    def print_table(self,data, header=[]):
        tabla = 'Algo ocurrio mal'
        if not data:
            raise ValueError("No hay ningún dato para mostrar")
        
        if isinstance(data, list):
            if isinstance(data[0], dict):
                header = list(data[0].keys())
                tabla = PrettyTable(header)
                for row in data:
                    tabla.add_row(list(row.values()))
            elif isinstance(data[0], tuple):
                header = self.table_header(data[0], header)
                tabla = PrettyTable(header)
                for row in data:
                    tabla.add_row(list(row))
        elif isinstance(data, dict):
            header = list(data.keys())
            tabla = PrettyTable(header)
            tabla.add_row(list(data.values()))
        elif isinstance(data, tuple):
            header = self.table_header(data, header)
            tabla = PrettyTable(header)
            tabla.add_row(list(data))
        return tabla


    def table_header(self,data, head):

        if not head:
            head = list(range(1, len(data) + 1))
        if len(head) < len(data):
        # extend --> Modificar una lista agregandole una iteracion como
        #           lista tupla o diccionario
        # 
        # syntax ---> list1.extend(iterable)
        # 
        # the extend() method takes an iterable such as list, tuple, string etc.
        # and modifies the original list.
        # --------------------------------------------------------------------
        # EXAMPLE      
        # languages list
        #   languages = ['French', 'English']
        # another list of language
        #   languages1 = ['Spanish', 'Portuguese']
        # appending language1 elements to language
        #   languages.extend(languages1)
        #output Languages List: ['French', 'English', 'Spanish', 'Portuguese']   
        #  

            head.extend(list(range(len(head) + 1, len(data) + 1)))
        # del ---> se usa para eliminar

        if len(head) > len(data):
            # Elimina de la lista head los datos de las posiciones que exceden 
            # a la cantidad de elementos de la lista data
            del head[len(data):]
        return head

    def question(self,text):
        print(f'\n{text}\n')
        option = False
        while True:
            dato = input('Seleccione (si) o (no) >> ').strip() # si -> Si -> SI
            if dato.lower() == 'si':
                option = True
                return option
            elif dato.lower() == 'no':
                option = False
                return option
            else:
                print('Debe elegir una opción...')
        print('\n')
