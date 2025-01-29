# Manejo de excepciones específicad "Exception" << No es recomendable SIMPRE puede esconder errores >>


def abrir_archivo():
    try:
        with open("datos.txt", "r") as archivo:
            contenido = archivo.read()
            numero  = int(contenido.strip())
            print(numero)
    except Exception as e:
        print(f'Se produjo un error {e}')

abrir_archivo()