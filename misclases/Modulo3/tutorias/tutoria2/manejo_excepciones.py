"""
Una excepción es un evento ocurre cuando, la ejecuación de codigo es interrumpida
en su flujo normal de ejecuacion un crash
"""

# envuelve el codigo que puede generar excepciones. Si ocurre una excepcion, ejecuta el bloque except
try:
    num = int(input("Ingrese eun numero: "))
    print(f"El doble es : {num * 2}")
except ValueError:
    print('No ingreso un número')
# El bloque else se ejecuta si no ocurre ninguna exceion en el boque try
else:
    print(f"Todo ok, el número ingresado es {num}" )


import os

# Opción 2: Usando os.path para construir la ruta (más portable)
ruta_base = os.path.dirname(__file__)  # Obtiene el directorio del script actual
ruta_archivo = os.path.join(ruta_base, "archivo.txt")

archivo = None
try:
    archivo = open(ruta_archivo, 'r')
    contenido = archivo.read()
    print(contenido)
except FileNotFoundError:
    print('Error: el archivp no existe')
# este simpre se ejecuta siempre, independientemente si ocurre o no ocurre una exception, 
# es util para liberar recursos, cerrar archivos, conexiones a base de datos, etc.
finally:
    try:
        archivo.close()
        if archivo is not None:
            archivo.close()
        print("me ejecute")
    except NameError:
        print("El archivo no se abrio, no hay que cerrar")


# Manejo de extenciones 
# Puedes manejar diferentes tipos de exepciones en el bloque separados por except o agruparlos en una
# tupla

# try:
#     num = int(input("Ingresa un número: "))
#     resultado = 10 / num
# except ValueError:
#     print("Error: no ingresaste un número valido")
# except ZeroDivisionError:
#     print("Error: no se puede dividir por 0")


        
# try:
#     num = int(input("Ingresa un número: "))
#     resultado = 10 / num
# except (ValueError, ZeroDivisionError) as e:
#     print(f"Error: {e}")

# try:
#     num = int(input("Ingresa un número: "))
#     resultado = 10 / num
# except  Exception as e:
#     print(f"Error: {e}")

# Creación de excepciones personalizadas
class MisExcepciones(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)

try:
    edad = int(input('Ingrese su edad: '))
    if edad < 0:
        raise MisExcepciones("La edad no puede ser negativa")
    print(f'Tu edad es {edad}')
except MisExcepciones as e:
    print(f'Una excepcion ocurrio {e}')
    
# Recomendaciones
# Use de excepciones solo para situaciones excepcionales, no como lógica de control
# Simpre usara finally para liberar recursos
# Se especifica al capturar error (para saber que error ocurrio con mayor frecuencia)
# Se especifia al capturar error
#

