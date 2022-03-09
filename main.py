# Importando funciones propias
from source.Proporcion import *
from source.Menu import menu
from source.Funciones import borrar_pantalla
from source.Calculos import *

# Importando librerias
from time import sleep

opcion = None
proporcion = []


asignar_proporcion(proporcion)

while opcion != 4:
    opcion = menu(opcion, proporcion)
    if opcion == 1:
        print(f'Cantidad de gramos de cáfe a usar: {calcular_cafe(proporcion)}')
    elif opcion == 2:
        print(f'Cantidad de mililitros de agua que debes usar: {calcular_agua(proporcion)}')
    elif opcion == 3:
        cambiar_proporcion(proporcion)
    elif opcion == 4:
        exit()