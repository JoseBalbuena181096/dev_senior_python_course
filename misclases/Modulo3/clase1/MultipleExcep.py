# Mismo ejercicio explicando las excepciones multiples

def division_segura(numero1, numero2):
    try:
        numerador = int(input("Ingrese porfavor el numerador\n"))
        denominador = int(input("Ingrese poravor el denominador\n"))
        resultado = numerador / denominador 
        print(f"El resultado de la división de {numerador} entre el {denominador} es igual a {resultado}")
    except (ZeroDivisionError, ValueError) as e:
        print(f'El error es {e}') 

division_segura(10, 'a')