from pickletools import OpcodeInfo
from source.Funciones import *
from source.Proporcion import *

def calcular_cafe(proporcion):
    try:
        borrar_pantalla()
        agua = float(input(f'Cantidad de mililitros de agua a usar: '))
        print('\n')
        print(f'RESULTADO'.center(15,'-'))
        return agua/proporcion[1]
    
    except Exception as e:
        print(f'Ocurrio un error: {e}')
    
def calcular_agua(proporcion):
    try:   
        borrar_pantalla()
        cafe = float(input(f'Cantidad de gramos de cafe a usar: '))
        print('\n')
        print(f'RESULTADO'.center(15,'-'))
        return (cafe*proporcion[1]) / proporcion[0]
    
    except Exception as e:
        print(f'Ocurrio un error: {e}')