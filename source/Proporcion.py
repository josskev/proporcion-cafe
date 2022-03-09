from time import sleep
from source.Funciones import borrar_pantalla
from source.Funciones import borrar_pantalla

proporcion = []
valor = None

def asignar_proporcion(proporcion):
    try:
        borrar_pantalla()
        print('Vamos a determinar el proporcion de la receta\n')
        valor = float(input(f'Inserta la proporcion del cafe (Primer valor): '))
        proporcion.append(valor)
        valor = float(input(f'Inserta la proporcion del agua (Segundo valor: '))
        proporcion.append(valor)
        borrar_pantalla()
        return proporcion
    
    except Exception as e:
        print(f'Ocurrio un error: {e}')
        asignar_proporcion(proporcion)


def cambiar_proporcion(proporcion):
    try:
        borrar_pantalla()
        print('Vamos a determinar el proporcion de la receta\n')
        valor = float(input(f'Inserta la proporcion del cafe (Primer valor): '))
        proporcion[0] = valor
        valor = float(input(f'Inserta la proporcion del agua (Segundo valor: '))
        proporcion[1] = valor
        print(f'\nProporcion actual: {int(proporcion[0])}/{int(proporcion[1])}')
        return proporcion
    
    except Exception as e:
        print(f'Ocurrio un error: {e}')
        