# def __init__(self, atributo1, atributo2):
#     self.atributo1 = atributo1
#     self.atributo2 = atributo2

# def comportamientoFuncionDefinicion(self):
#     pass

# Definicion de la clase

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad 
    
    def saludar(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años"
    

