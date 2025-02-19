from model.veterinaria import Veterinaria

class ControladorCliente:
    def __init__(self):
        self.veterinaria = Veterinaria

    def registrar_cliente(self, nombre_cliente, telefono):
        return self.veterinaria.registrar_clientes(nombre_cliente, telefono)


    def obter_cliente(self, nombre_cliente):
        return self.veterinaria.clientes[nombre_cliente]
        
