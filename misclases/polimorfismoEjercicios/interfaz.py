from abc import ABC, abstractmethod
import math

class FigurasGeometricas(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimetro(self):
        pass

class Circulo(FigurasGeometricas):
    def  __init__(self, radio):
        self.radio = radio 

    def ver_radio(self):
        return self.radio
    
    def area(self):
        return math.pi *  self.radio ** 2
    
    def perimetro(self):
        return math.pi * 2 * self.radio 

circulo = Circulo(10)
print(circulo.ver_radio())
