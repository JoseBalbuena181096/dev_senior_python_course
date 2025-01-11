class CuentaBancaria:
    def __init__(self, titular, saldo, clave) -> None:
        self.titular = titular
        self._saldo = saldo
        self.__clave = clave 

    def depositar(self, cantidadDeposito):
        self._saldo += cantidadDeposito
        return f'Deposito exitoso. Saldo actual {self._saldo}'

    def retirar(self, cantidadRetiro):
        if cantidadRetiro > self._saldo:
            return "fondos insuficientes"
        self._saldo -= cantidadRetiro
        return f'Retiro exitoso. El saldo actual es {self._saldo}'

    def modificarClave(self, nuevaClave):
        self.__clave = nuevaClave
        return f'La clave modificada con exito, la nueva clave es {self.__clave}'
    

cuentaBancaria1 = CuentaBancaria("Jose Balbuena", 1000000, 12345)
print(cuentaBancaria1.titular)
print(cuentaBancaria1._saldo)
print(cuentaBancaria1.depositar(5000000))
print(cuentaBancaria1.depositar(5000000))
print(cuentaBancaria1.retirar(2500000))
print(cuentaBancaria1.retirar(7500000))

print(cuentaBancaria1.modificarClave("00000000"))