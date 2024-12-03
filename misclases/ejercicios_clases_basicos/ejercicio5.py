"""
Clase Calculadora: Diseña una clase Calculadora con un método estático suma que reciba dos números y devuelva la suma de ellos. Ejemplo:
print(Calculadora.suma(3, 4)) # Salida: 7
"""

class Calculadora:
    @staticmethod
    def sumar(numero1, numero2):
        return numero1 + numero2
    
print(Calculadora.sumar(10, 12))