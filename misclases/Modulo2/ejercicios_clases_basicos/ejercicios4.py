"""
Clase Coche: Crea una clase Coche con los atributos: Marca y Modelo. 
Incluye un método arrancar que imprima: "El coche [Marca] modelo [Modelo] está arrancando."
"""

class Coche:
    def __init__(self, marca, modelo) -> None:
        self.marca = marca
        self.modelo = modelo

    def arrancar(self):
        return f"El coche {self.marca} modelo {self.modelo} está arrancando"

coche = Coche('Nissan', 'March')
print(coche.arrancar())   