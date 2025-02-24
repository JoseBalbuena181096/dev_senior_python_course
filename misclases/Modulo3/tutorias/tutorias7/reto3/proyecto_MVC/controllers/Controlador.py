from tkinter  import messagebox

class ControladorTienda:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
        self.carrito = []

    