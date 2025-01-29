# uso del else y finally, ejercicio de division por cero

def division_completa():
    try:
        numero = int(input("Ingrese un número"))
        resultado =  10 / numero
        print(f'El resultado de la división es {resultado}')

    except ValueError as e:
        print(f'Error: {e}')
    
    except ZeroDivisionError as e:
        print(f'Error: {e}')
    else:
        print(f'El resultado es {resultado}')
    finally:
        print('Se termino la operacion')

division_completa()
     