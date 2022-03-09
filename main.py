import os
from time import sleep
from typing import final

agua = None
cafe = None
ratio = None
opcion = None

valor = None

ratio = []

# CALCULOS

def calcular_cafe(agua, ratio):
    return agua/ratio[1]
    
def calcular_agua(cafe, ratio):
    return (cafe*ratio[1]) / ratio[0]

def borrar_pantalla():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
    
def asigancion_ratio():
    borrar_pantalla()
    print('Vamos a determinar el ratio de la receta\n')
    valor = float(input(f'Inserta el valor ratio del cafe (Primer valor): '))
    ratio.append(valor)
    valor = float(input(f'Inserta el valor ratio del agua (Segundo valor: '))
    ratio.append(valor)
    return ratio

def cambiar_ratio():
    ratio.clear()
    print('Vamos a determinar el ratio de la receta\n')
    valor = float(input(f'Inserta el valor ratio del cafe (Primer valor): '))
    ratio.append(valor)
    valor = float(input(f'Inserta el valor ratio del agua (Segundo valor: '))
    ratio.append(valor)
    print(f'\nRatio actual: {int(ratio[0])}/{int(ratio[1])}')
    sleep(1)
    print('\nRegresando al menu en: 3')
    sleep(1)
    print('Regresando al menu en: 2')
    sleep(1)
    print('Regresando al menu en: 1')
    sleep(1)
    return ratio
    
def menu():
    borrar_pantalla()
    print(f'\nRatio de la receta actual: {int(ratio[0])}/{int(ratio[1])}')
    opcion = int(input(f'''\n¿Que dato necesitas saber?: 
                       
            1. Que cantidad de café debo usar
            2. Que cantidad de agua debo usar
            3. Cambiar ratio de la receta
            4. Salir
            
            Opción: '''))
    if opcion == 1:
        borrar_pantalla()

        agua = float(input(f'Cantidad de agua a usar: '))
        print('\n')
        print(f'RESULTADO'.center(15,'-'))
        print(f'Cantidad de cafe a usar: {calcular_cafe(agua, ratio)} gramos.\n')
        print('Regresando al menu en: 3')
        sleep(1)
        print('Regresando al menu en: 2')
        sleep(1)
        print('Regresando al menu en: 1')
        sleep(1)
        menu()
                
    elif opcion == 2:
        borrar_pantalla()
        
        cafe = float(input(f'Cantidad de cafe a usar: '))
        print('\n')
        print(f'RESULTADO'.center(15,'-'))
        print(f'Cantidad de agua a usar: {calcular_agua(cafe, ratio)}mililitros.\n')
        sleep(3)
        print('Regresando al menu en: 3')
        sleep(1)
        print('Regresando al menu en: 2')
        sleep(1)
        print('Regresando al menu en: 1')
        sleep(1)
        menu()
    
    elif opcion == 3:
        borrar_pantalla()
        
        cambiar_ratio()
        menu()
        
    elif opcion == 4:
        borrar_pantalla()
        
        print('Saliendo del programa en: 3')
        sleep(1)
        print('Saliendo del programa en: 2')
        sleep(1)
        print('Saliendo del programa en: 1')
        sleep(1)
        
        exit()
    
try:
    asigancion_ratio()
    
except Exception as e:
        borrar_pantalla()
        print(f'Ocurrio un error: {e}')
        opcion = None 
        print('Regresando al menu en: 3')
        sleep(1)
        print('Regresando al menu en: 2')
        sleep(1)
        print('Regresando al menu en: 1')
        sleep(1)
        asigancion_ratio()

finally:
    try:
        menu()


    except Exception as e:
        borrar_pantalla()
        print(f'Ocurrio un error: {e}')
        opcion = None 
        print('Regresando al menu en: 3')
        sleep(1)
        print('Regresando al menu en: 2')
        sleep(1)
        print('Regresando al menu en: 1')
        sleep(1)
        menu()

    finally:
        exit()


# AGUA.- Dividir cantidad de agu entre ratiod e cafe ejem.- 1/17 , si son 1000gr/ml agua cafe = 58.82 cafe

# CAFE.- cantidad de cafe * el ratio de agua