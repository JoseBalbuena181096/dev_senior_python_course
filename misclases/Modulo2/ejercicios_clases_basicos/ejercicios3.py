"""
Clase Rectangulo: Crea una clase Rectangulo con: Atributos: largo, ancho. Métodos: area (calcula el área del rectángulo).
Ejemplo:
rect = Rectangulo(5, 4) print(rect.area()) # Salida: 20
"""

class Rectangulo:
    def __init__(self, largo, ancho) -> None:
        self.largo = largo
        self.ancho = ancho
    
    def area(self):
        return self.largo * self.ancho
    

rectangulo = Rectangulo(10, 20)
print(rectangulo.area())