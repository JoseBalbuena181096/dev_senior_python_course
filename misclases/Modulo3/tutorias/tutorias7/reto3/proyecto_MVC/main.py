from models.Modelo import Tienda
from controllers.Controlador import ControladorTienda
from views.Vista import VistaTienda

modelo = Tienda()
modelo.agregar_productos(1, "Manzana", 1, 1000)
modelo.agregar_productos(2, "Platano", 3, 1000)
modelo.agregar_productos(3, "Pera", 2, 1000)

controlador = ControladorTienda(modelo, None)
vista = VistaTienda(controlador)

