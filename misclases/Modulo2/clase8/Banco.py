class Banco:
    tasaInteres = 0.03

    def __init__(self, nombre) -> None:
        self.nombre = nombre

    @classmethod
    def cambiarTasa(cls, nuevaTasa):
        cls.tasaInteres = nuevaTasa

    @staticmethod
    def convertirDolaresEuros(dolares):
        return dolares * 0.85
    

    

banco = Banco('BBVA')
print(f"El banco es {banco.nombre}")

# cambiar tasa de interes
Banco.cambiarTasa(0.16)
print(f'La nueva tasa es de {Banco.tasaInteres}')

# Convertir 10 dolares a euros
euros = Banco.convertirDolaresEuros(10)
print(euros)