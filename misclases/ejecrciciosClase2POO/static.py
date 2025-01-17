class MiClase:
    @staticmethod
    def sumar(numero1, numero2):
        return numero1 + numero2
    
print(MiClase.sumar(10, 10))

class Conversor:
    @staticmethod 
    def a_fahrenheit(celsius):
        return celsius * 9/5 +32
    

print(Conversor.a_fahrenheit(0))


class Persona:
    total_personas = 0
    total_saldos = 0

    def __init__(self, nombre, saldo):
        self.nombre = nombre
        self.saldo = saldo
        Persona.total_personas += 1
        Persona.total_saldos += self.saldo

    @classmethod
    def cantidad_personas(cls):
        print(f'Cantidad personas {cls.total_personas}')

    @classmethod
    def cantidad_saldos(cls):
        print(f'Los saldos totales son {cls.total_saldos}')

    def total(self):
        return Persona.total_personas 

persona1 = Persona('Jose', 100)
persona2 = Persona('Juan', 200)
persona3 = Persona('Julio', 300)

persona1.cantidad_personas()
print(persona3.total())
persona2.cantidad_saldos()