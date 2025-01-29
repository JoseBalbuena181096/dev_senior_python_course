# Build a simple calculator

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

inputUsuario = input("Ingrese el primero número ")
isNumber =  is_float(inputUsuario) 
if not isNumber:
    inputUsuario = input("ingrese un valor numerico porfavor ")

numero1 = float(inputUsuario)
numero2 = float(float(input("Ingrese el segundo número por favor")))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

print("Suma ", suma)
# Extrapolación de un string
print("Resta: {0}".format(resta))
print(f"Multiplicacio: {multiplicacion}")
print(f"Divicion: {division}")



