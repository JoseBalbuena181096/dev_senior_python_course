# Clases abstractas en python
from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def area(self):
        pass


class Circulo(Forma):
    def __init__(self, radio) -> None:
        self.radio = radio

    def area(self):
        return f"El area es {3.14 * self.radio ** 2}"
    
    def perimetro(self):
        return f'El perimetro de un ciculo {2 * 3.14 * self.radio }'
    
class Rectangulo(Forma):
    def __init__(self, base, altura) -> None:
        self.base = base
        self.altura = altura
    
    def area(self):
        return f"El area de un rectangulo es {self.base * self.altura}"
    
    def perimetro(self):
        return f"El perimetro de un rectagulo es {2* self.base + 2 * self.altura}"
    
class Cuadrado(Forma):
    def __init__(self, lado) -> None:
        self.lado = lado 
    
    def area(self):
        return f'El area de un cuadrado es {self.lado **2}'
    
formas = [
    Circulo(5),
    Rectangulo(2, 10),
    Cuadrado(8),
    Rectangulo(10, 20),
    Circulo(22)
]

print("Areas formas")
for forma in formas:
    print(forma.area())

circulo1 = Circulo(5)
print(circulo1.perimetro())

rectangulo1 = Rectangulo(10, 12)
print(rectangulo1.perimetro())
# print("Perimetro formas")
# for forma in formas:
#     print(forma.perimetro())
