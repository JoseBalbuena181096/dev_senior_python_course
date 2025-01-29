from abc import ABC, abstractmethod

class Vehiculo(ABC):
    @abstractmethod
    def create(self):
        pass
class Carro(Vehiculo):
    def create(self):
        return "Se creo un carro"
    
class Moto(Vehiculo):
    def create(self):
        return "Se creo una moto"
    
class FactoryVehiculo:
    @staticmethod
    def get_vehiculo(vehiculo_tipo):
        if vehiculo_tipo == "Carro":
            return Carro()
        elif vehiculo_tipo == "Moto":
            return Moto()
        else:
            return ValueError("Tipo de vehiculo desconocido")
        
try:
    factory = FactoryVehiculo()
    car = factory.get_vehiculo('Carro')
    print(car.create())
    moto = factory.get_vehiculo('Moto')
    print(moto.create())
    tren = factory.get_vehiculo('Tren')
except ValueError as e:
    print(e)
