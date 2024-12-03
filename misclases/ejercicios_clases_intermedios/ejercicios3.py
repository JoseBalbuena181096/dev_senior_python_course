"""
Clase Empleado: Diseña una clase Empleado con atributos: Nombre y Salario. 
Incluye un método aumentar_salario que aumente el salario en un porcentaje dado como argumento. Ejemplo:
emp = Empleado("Luis", 2000) emp.aumentar_salario(10) # Incrementa el salario un 10% print(emp.salario) # Salida: 2200
"""

class Empleado:
    def __init__(self, nombre, salario) -> None:
        self.nombre = nombre 
        self.salario = salario

    def aumentar_salario(self, incremento):
     self.salario += (incremento*self.salario/100)
    
empleado = Empleado('Jose', 2000)
empleado.aumentar_salario(10)
print(empleado.salario)