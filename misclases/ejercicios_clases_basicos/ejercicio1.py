"""
Ejercicios Básicos

Clase Libro: Crea una clase llamada Libro que tenga los atributos: Título y Autor. 
Implementa un método descripcion que devuelva un texto como: "El libro [Título] fue escrito por [Autor]."
"""
class Libro:
    def __init__(self, titulo, autor):
      self.titulo = titulo
      self.autor = autor

    def descripcion(self):
       return f"El libro {self.titulo} fue escrito por {self.autor}"
    

libro = Libro('Atardecer', 'Jose Balbuena')
print(libro.descripcion())