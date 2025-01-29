"""
Clase Persona: Diseña una clase Persona con los atributos: Nombre y Edad. 
Incluye un método es_mayor_de_edad que retorne True si la edad es 18 o mayor, de lo contrario, False.
"""
class Persona:
    def __init__(self, nombre, edad) -> None:
        self.edad = edad
        self.nombre = nombre

    def es_mayor_edad(self):
        return True if self.edad >= 18 else False
    

persona = Persona('Jose', 17)

if(persona.es_mayor_edad()):
    print('eres mayor de edad')
else:
    print('eres menor de edad')