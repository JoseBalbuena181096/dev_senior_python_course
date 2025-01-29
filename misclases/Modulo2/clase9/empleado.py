class Empleado:
    def __init__(self, nombre, salario) -> None:
        self.nombre = nombre
        self._salario = salario
        self._salarioMinimo = 1300000

    def mostrarInformacion(self):
        return f'Nombre {self.nombre}, Salario: {self._salario} '

    def obtenerSalario(self):
        return self._salario

    def establecerSalario(self, nuevoSalario):
        if nuevoSalario < self._salarioMinimo:
            return "Salario no puede ser menor al salario minimo"
        self._salario = nuevoSalario
        return f"El nuevo salario es: {self._salario}"
    
    def asignacionesSalariales(self):
        pass

    def deduccionesSalariales(self):
        pass

empleado1 = Empleado('carlos', 1500000)


print(empleado1.mostrarInformacion())
print(empleado1.obtenerSalario())
print(empleado1.establecerSalario(1200000))
print(empleado1.establecerSalario(2500000))
