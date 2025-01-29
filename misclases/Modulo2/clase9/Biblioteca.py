class Libro:
    def __init__(self, titulo, autor) -> None:
        self.titulo = titulo
        self.autor = autor

    def descripcion(self):
        return f"Libro: {self.titulo} Autor: {self.autor}"

    def __str__(self) -> str:
        return f"Libro: {self.titulo} Autor: {self.autor}"



class libroDigital(Libro):
    def __init__(self, titulo, autor, formato) -> None:
        super().__init__(titulo, autor)
        self.formato = formato 

    def descripcion(self):
        return f"Libro: {self.titulo} Autor: {self.autor} Formato {self.formato}"
    
    def __str__(self) -> str:
        return f"Libro: {self.titulo} Autor: {self.autor} Formato {self.formato}"
    
libro1 = Libro("La peste", "Alberto Campo")
libroDigital1 = libroDigital("El conde de Montecristo", "Alejandro Dumas", "PDF")

print(libro1)
print(libroDigital1)