"""
Clase Banco: Implementa una clase Banco con: Atributo de clase tasa_interes. Método de clase actualizar_tasa(nueva_tasa).
 Método calcular_interes(monto) que calcule el interés sobre un monto basado en la tasa actual.
"""
class Banco:
    tasa_interes = 0.1

    @classmethod
    def actualizar_taza(cls, nueva_tasa):
        cls.tasa_interes = nueva_tasa

    @classmethod
    def calcular_interes(cls, monto):
         return (monto * cls.tasa_interes) / 100
    

Banco.actualizar_taza(0.3)
print(Banco.tasa_interes)
print(Banco.calcular_interes(1000))