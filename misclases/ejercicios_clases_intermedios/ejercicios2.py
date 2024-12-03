"""
Herencia: Clase Vehiculo y Moto: Crea una clase base Vehiculo con los atributos: Tipo y Marca. 
Crea una subclase Moto que herede de Vehiculo y tenga un método hacer_wheelie que imprima: "¡La moto [Marca] está haciendo un wheelie!"
"""

class Vehiculo:
    def __init__(self, tipo, marca) -> None:
        self.marca = marca
        self.tipo = tipo


class Moto(Vehiculo):
    def __init__(self, tipo, marca) -> None:
        super().__init__(tipo, marca)

    def hacer_wheelie(self):
        return  f"¡La moto {self.marca} está haciendo un wheelie!"
    

motito = Moto('moto', 'ducatii')
print(motito.hacer_wheelie())