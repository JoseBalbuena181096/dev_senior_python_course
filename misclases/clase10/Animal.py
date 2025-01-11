class Animal:
    def __init__(self) -> None:
        pass

    def hablar(self):
        pass

class Perro(Animal):
    def __init__(self) -> None:
        super().__init__()

    def hablar(self):
        return f"El perro hace gua gua"

class Gato(Animal):
    def __init__(self) -> None:
        super().__init__()

    def hablar(self):
        return f"El gato hace miuw"
    
animales = [Perro(), Gato(), Perro(), Gato()]
for animal in animales:
    print(animal.hablar())