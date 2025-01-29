# Polimorfismo con herencia y methodos sobreescritos

# class Animal:
#     def sonido(self):
#         return "Sonido generico"
    

# class Perro(Animal):
#     def sonido(self):
#         return "Gua Gua"
    
# class Gato(Animal):
#     def sonido(self):
#         return "Miau Miau"
    
# mi_gato = Gato()
# mi_perro = Perro()

# print(mi_gato.sonido())
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sonido(self):
        return "Sonido generico"
    

class Perro(Animal):
    def sonido(self):
        return "Gua Gua"
    
class Gato(Animal):
    def sonido(self):
        return "Miau Miau"
    
mi_gato = Gato()
mi_perro = Perro()

print(mi_gato.sonido())