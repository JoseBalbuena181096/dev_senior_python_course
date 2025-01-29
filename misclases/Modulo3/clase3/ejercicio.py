"""
Uso del braekpoint simple
"""

class Empleado:
    def __init__(self, nombre, ventas):
        self.nombre = nombre 
        self.ventas = ventas

    def calculo_comision(self):
        if self.ventas > 5000:
            print(f'Empleado: {self.nombre} - Ventas {self.ventas} comisión del 10% ')
            return self.ventas * 0.10
        print(f'Empleado: {self.nombre} - Ventas {self.ventas} comisión del 5% ')
        return self.ventas * 0.05

empleados = [
    Empleado('Ana', 6000),
    Empleado('Luis', 7000)
]

for empleado in empleados:
    print(f'Empleado {empleado.nombre} - comisión {empleado.calculo_comision()}')
    
        