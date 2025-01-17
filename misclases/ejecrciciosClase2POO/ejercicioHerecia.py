"""
Ejercicio: Crea una clase 'Vehiculo' con atributos 'marca' y 'modelo'. Luego, crear una clase 'Coche' 
que herede de 'Vehiculo' y agregar un atributo 'puertas

4. Herencia con método personalizado

 - Ejercicio: Agrega un método `mostrar_info` a `Coche` para mostrar los detalles del vehículo. 
"""

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas

    def mostrar_info(self):
        print(f'El vehiculo es marca: {self.marca}, modelo: {self.modelo} y con puertas {self.puertas}')


coche = Coche('Ford', 'Fiesta', 4)
coche.mostrar_info()