class Persona:
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self._edad = edad 
        self.__cuentaBancaria = 12345

    def mostrarInformacion(self):
        return f'Nombre: {self.nombre} Edad: {self._edad}'

    # Metodo privado    
    def __mostrarCuenta(self):
        return f"Cuenta Bancaria: {self.__cuentaBancaria}"
    
    def mostrarInformacionCompleta(self):
        return self.__mostrarCuenta()

persona1 = Persona('Luis guillero', 49)
print(persona1.nombre)
print(persona1._edad)
print(persona1.mostrarInformacionCompleta())
