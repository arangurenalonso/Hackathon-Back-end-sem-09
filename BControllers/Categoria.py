from AModels.Categoria import Categoria
from DHelpers.validacion import validacion
from DHelpers.menu import Menu

class ControllerCategoria:
    def __init__(self):
        self.categorias = Categoria()
        self.salir = False
        self.validar = validacion()
    
    def menu(self): 
        try:
            while True:
                print('''
                ==================
                  Menu Categoria
                ==================
                ''')
                lista_menu = ["Crear Categoria", "Mostrar Categoria","Buscar Categoria", "Salir"]
                respuesta = Menu(lista_menu).show()

                if respuesta == 1:
                    self.insert_categorias()
                elif respuesta == 2:
                    self.show_categoria()
                elif respuesta == 3:
                    self.search_categoria()
                else:
                    self.salir = True
                    break
        except Exception as e:
            print(f'{str(e)}')

    def insert_categorias(self):
        print('''
            ====================
                CREAR CATEGORIA
            ====================
            ''')
        Nombre_categoria = self.validar.valiar_ingreso_texto("Ingrese el nombre de la categoria")
        data = {
            'nombres_categoria': Nombre_categoria
        }
        
        self.categorias.insert_categorias(data)
        
        print('''
        =========================
            Categoria Creada
        =========================
        ''')
        categoria_creada=self.validar.validar_existencia_campo_valor_categoria('nombres_categoria',Nombre_categoria)
        print(self.validar.print_table(categoria_creada, ['ID', 'Nombre Categoria']))
        input('Presiona una tecla para continuar...')

    def show_categoria(self):
        try:
            print('''
                =====================
                   MOSTRAR CATEGORIA
                =====================
                ''')
            condicion = {}
            seleccion = {
                '_id' : 1,
                'nombres_categoria': 1

            }    
            cates = self.categorias.get_categorias(condicion, seleccion)
            
            
            print('''
            =========================
                    Categorias
            =========================
            ''')
            print(self.validar.print_table(cates, ['ID', 'Nombre Categoria']))
            input('Presiona una tecla para continuar...')

        except Exception as e:
            print(f'{str(e)}')
    
    def search_categoria(self):
        try:
            print('''
                =====================
                    BUSCAR CATEGORIA
                =====================
                ''')
            Nombre_categoria = self.validar.valiar_ingreso_texto("Ingrese el nombre de la categoria a buscar")
            categoria_buscada=self.validar.validar_existencia_campo_valor_categoria('nombres_categoria',Nombre_categoria)

            if categoria_buscada:
                print('''
            =========================
               Categoria Encontrada
            =========================
            ''')
                print(self.validar.print_table(categoria_buscada, ['ID', 'Nombre Categoria']))
                if self.validar.question('¿Deseas dar mantenimiento a la categorias?'):
                    opciones = ['Editar', 'Eliminar', 'Salir']
                    respuesta = Menu(opciones).show()
                    print(respuesta)
                    if respuesta == 1:
                        self.update_categoria(categoria_buscada["_id"])
                    elif respuesta == 2:
                        print(categoria_buscada)
                        self.delete_categoria(categoria_buscada["_id"])
            else:
                print("No existe ninguna categoria ingresada con ese nombre")
            
        except Exception as e:
            print(f'{str(e)}')
        input('Presiona una tecla para continuar...')
    
    def delete_categoria(self,id_categoria):
        
        data = {
            '_id': id_categoria
        }
        self.categorias.delete_categoria(data)
        print('''
                =========================
                    Categoria Eliminada
                =========================
                ''')
    def update_categoria(self, id_categoria):   
    
        print('''
            =========================
                ACTUALIZAR CATEGORIA
            =========================
            ''')
        Nombre_categoria = self.validar.valiar_ingreso_texto("Ingrese el nuevo nombre de la categoria")

        condicion = {
            '_id': id_categoria
        }
        cambio = {
            'nombres_categoria': Nombre_categoria
        }
        self.categorias.update_categoria(condicion,cambio)
        


        print('''
        =========================
          Categoria Actualizada
        =========================
        ''')
