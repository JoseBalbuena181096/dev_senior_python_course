
class Animal:
    def __init__(self, nombre):
      self.nombre = nombre 

    def hablar(self):
       return "Todo animal habla de alguna forma"

    def __str__(self) -> str:
       return f"El animal es {self.nombre}"

class Perro(Animal):
    def __init__(self, nombre, raza):
       super().__init__(nombre)
       self.raza = raza

    def hablar(self):
       return "Guaa Guau"

    def __str__(self) -> str:
       return f"El nombre del perro es {self.nombre} y su raza {self.raza}"
    
animal1 = Animal("Perrito")
perrito = Perro('Tequila', 'Chihuahua')
print(animal1)

print(perrito.hablar())
print(perrito.__str__())

