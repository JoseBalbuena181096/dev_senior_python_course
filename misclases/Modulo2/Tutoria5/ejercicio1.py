from abc import ABC, abstractmethod

# Clase abstracta
class Empleado(ABC):
    def __init__(self, name, id, salary_base):
        self._name = name
        self._id = id
        self._salary_base = salary_base

    @property
    def nombre(self):
        return self._name
    
    @property
    def id(self):
        return self._id

    @property
    def salary_base(self):
        return self._salary_base
    
    @salary_base.setter
    def salary_base(self, new_salary):
        if new_salary > 0:
            self._salary_base = new_salary
        else:
            raise ValueError('el salario debe ser mayor a 0')

    @abstractmethod
    def calculate_bone(self):
        pass

    def __str__(self):
        return f'Empleado {self._name}, id {self._id}, salario base: {self._salary_base}'

class Desarrollador(Empleado):
    def calculate_bone(self):
        return self._salary_base * 0.10

class Designer(Empleado):
    def calculate_bone(self):
        return self.salary_base * 0.05

class Manager(Empleado):
    def calculate_bone(self):
        return 500.0

if __name__ == "__main__":
    dev = Desarrollador('Jose', 101, 5000)
    designer = Designer('Jorge', 102, 4000)
    manager = Manager('Julian', 104, 8000)
    empleados = [dev, designer, manager]
    for empleado in empleados:
        print(empleado)
        print(empleado.calculate_bone())
  