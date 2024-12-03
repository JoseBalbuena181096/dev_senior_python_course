"""
Clase CuentaBancaria: Implementa una clase CuentaBancaria con: Atributos: saldo.
 Métodos: depositar(cantidad) y retirar(cantidad) con validaciones. Si intentas retirar más del saldo disponible, debe imprimir: "Fondos insuficientes."

"""
class CuentaBancaria:
    def __init__(self, saldo = 0) -> None:
        self.saldo = saldo 

    def depositar(self, cantidad):
        if cantidad > 0: 
            self.saldo += cantidad
    
    def retirar(self, cantidad):
        if self.saldo < cantidad:
            print(f'Saldo insuficiente usted tiene solo {self.saldo} le faltan {cantidad-self.saldo}')
            return
        self.saldo -= cantidad

    
cuenta = CuentaBancaria(1000)
cuenta.depositar(1500)
print(cuenta.saldo)
cuenta.retirar(3000)
