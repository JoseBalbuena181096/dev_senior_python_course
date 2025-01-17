"""
# Ejercicios Básicos

1. Definir una clase básica con encapsulamiento

 - Ejercicio: Crea una clase `CuentaBancaria` con un atributo privado `_saldo`. Agrega métodos para depositar y retirar dinero, asegurándote de que no se permita un saldo negativo.  


 3. Método protegido en una clase

 - Ejercicio: Agrega un método protegido `_calcular_interes` en la clase `CuentaBancaria` que calcule un 5% de interés sobre el saldo actual. 

 5. Propiedades con decoradores

 - Ejercicio: Modifica la clase `CuentaBancaria` para usar decoradores `@property` y `@setter` en el atributo `_saldo`.  

 """

class CuentaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo
    
    def agregar(self, monto):
        if monto >= 0:
            self.__saldo += monto 
            print(f'Su saldo es de {self.__saldo}')
            return
        print('El monto debe ser positivo')

    def retirar(self, monto):
        previo_monto = self.__saldo - monto
        if previo_monto < 0:
            print(f'No puede retirar ese monto {monto} su saldo no puede ser negativo')
            return
        self.__saldo -= monto
        print(f'Su nuevo saldo es {self.__saldo}')

    def _calcular_interes(self):
        return  self.saldo * 0.05


    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, saldo):
        if saldo < 0:
            print("Saldo invalido negativo")
            return    
        self.__saldo = saldo

    
cuenta = CuentaBancaria(1000)
cuenta.agregar(100)
cuenta.saldo = 1200
print(f"El saldo es {cuenta.saldo}")
cuenta.agregar(-100)
cuenta.retirar(200)
cuenta.retirar(1500)
print(cuenta._calcular_interes())