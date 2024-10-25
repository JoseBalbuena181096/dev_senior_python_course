var1 = 100
var2 = 200

var = var1 + var2

ancho = 1203
alto = 8760
area = ancho * alto

a = 30
b = 30
c = a ** b

d = 30.0

f = "3.0"

g = "30"

x = a == b

# y = True  and  False (&& || !)
y = x and a == c
z = not y

y = (a == b and d < a) or (f == g) 

z = a*b == b*d and a*d < b*a

# print((a == b and d < a) )
# print(y)

altura = 80
peso = "80"

# str = "80"
pesoNumEnt = int(peso)
# str = "80.0"
pesoNumFloat = float(peso) + 0.1
# str = "80.1"

# str value of 80
peso2 = str(pesoNumFloat)

# "80" == "80.0"
# print(peso == peso2)

# 80 == 80.0
# print(pesoNumEnt == pesoNumFloat)

xy = (a == b and d < a)
y = xy or (f == g) 


# Ejercicio 1

# print(F"El text es numero: {isNumeric or isDecimal}")

#(a == b, a != b, a > b, a < b, a >= b, a <= b)
# booleanValue = true1
# if logic booleanValue

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

inputUsuario = input("Ingresa el primer número: ")

isFloat = is_float(inputUsuario)

# if logic operation:
#    action
if not isFloat:
    inputUsuario = input("El numero no es valido, Ingresa el primer número nuevamente: ")

numero1 = float(inputUsuario)

numero2 = float(input("Ingresa el segundo número: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

# Suma: {suma}
# Suma: 100.0
# print("Suma: ", suma)
# print("Suma: " + str(suma))
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")
