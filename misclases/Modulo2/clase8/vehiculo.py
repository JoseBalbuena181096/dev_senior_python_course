class Vehiculo:
    def __init__(self, tipo) -> None:
        self.tipo = tipo

    def descripcion(self):
        return f'Este vehiculo es tipo {self.tipo}'
    
class Moto(Vehiculo):
    def __init__(self, tipo, marca) -> None:
        super().__init__(tipo)
        self.marca = marca
    

moto1 = Moto("Motocicleta", "Ducatti")
print(moto1.descripcion())