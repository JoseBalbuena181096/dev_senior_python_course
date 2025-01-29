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
    
    def __str__(self):
        return f'Circulo area: {self.area():.2f} perimetro: {self.perimetro():.2f} '

class Cuadrado(FigurasGeometricas):
    def __init__(self, lado):
        self.lado =  lado

    def ver_lado(self):
        return self.lado

    def area(self):
        return self.lado * self.lado
    
    def perimetro(self):
        return 4 * self.lado
    
    def __str__(self):
        return f'Cuadrado area: {self.area():.2f} perimetro: {self.perimetro():.2f} '


def main():
    figuras = [
        Circulo(10), 
        Cuadrado(3), 
        Circulo(12), 
        Cuadrado(14)
    ]
    for figura in figuras:
        print(figura)

if __name__ == '__main__':
    main()
