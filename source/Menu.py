# Importando funciones propias
from source.Funciones import borrar_pantalla

# Importando utilidades
from time import sleep
from source.Proporcion import *

def menu(opcion, proporcion):
    try:
        print(f'\nRatio de la receta actual: {int(proporcion[0])}/{int(proporcion[1])}')
        opcion = int(input(f'''\n¿Que dato necesitas saber?: 

                1. ¿Que cantidad de café debo usar?
                2. ¿Que cantidad de agua debo usar?
                3. Cambiar proporcion de la receta
                4. Salir

                Opción: '''))
        return opcion
    
    except Exception as e:
        borrar_pantalla()
        print(f'Ocurrio un error: {e}')
        opcion = None