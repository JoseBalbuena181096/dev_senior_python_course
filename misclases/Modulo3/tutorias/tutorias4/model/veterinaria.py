from .cliente import Cliente
from .mascota import Mascota
from .citas import Cita


class Veterinaria:
    def __init__(self):
        self.clientes = {}

    def registrar_clientes(self, nombre_cliente, telefono):
        if nombre_cliente not in self.clientes:
            self.clientes[nombre_cliente] = Cliente(nombre_cliente, telefono)
            return True
        return False

    # mascota y citas 


