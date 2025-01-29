from abc import ABC, abstractmethod

class EstrategiaTarifa(ABC):
    @abstractmethod
    def calcularTarifa(self, distancia, tiempo):
        raise NotImplemented("Se debe implementar este método")
    

class TarifaFija(EstrategiaTarifa):
    def calcularTarifa(self, distancia, tiempo):
        return 300
     

class TarifaHora(EstrategiaTarifa):
    def calcularTarifa(self, distancia=None, tiempo=None):
        return tiempo * 25
    
class TarifaKilometro(EstrategiaTarifa):
    def calcularTarifa(self, distancia, tiempo):
        return distancia * 2
    

class CalcularTarifa:
    def __init__(self, estrategia):
        self.estrategia  = estrategia

    def cambiarEstrategia(self, estrategia):
        self.estrategia = estrategia

    def calcular(self, distacia, tiempo):
        return self.estrategia.calcularTarifa(distacia, tiempo)
    
arriendo1 = TarifaFija()
calculadora = CalcularTarifa(arriendo1)
print(f'La tarifa fija: {calculadora.calcular(10, 5)}')
    
calculadora.cambiarEstrategia(TarifaHora())
print(f"Tarifa por hora: calculadora {calculadora.calcular(10, 2)}")

calculadora.cambiarEstrategia(TarifaKilometro())
print(f"Tarifa por kilometro: calculadora {calculadora.calcular(20, 2)}")