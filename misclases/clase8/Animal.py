class Animal:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age =  age

    def saludar(self):
        return f"Mi animalito se llama {self.name} y tiene {self.age} años"
    

animal1 = Animal('Ginebra', 12)
print(animal1.saludar())

    