# Metodos de clase

# El metodo constructor se ejecuta de forma automatica al instanciar la clase

class Animall:
    cantidadAnimales = 0
    def __init__(self, name) -> None:
        self.name = name
        Animall.cantidadAnimales += 1
    
    @classmethod
    def totalAnimales(cls):
        return f"Tengo {cls.cantidadAnimales} animales"
    
animalito1 = Animall("Ron")
animalito2 = Animall("Rayo")
animalito3 = Animall("Tobi")

print(animalito2.name)
print(Animall.totalAnimales())