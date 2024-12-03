"""
Sistema de Inventario Simple: Diseña una clase Producto con: Nombre y Precio. 
Luego, implementa una clase Inventario que administre una lista de productos. Incluye métodos para:
Agregar un producto.
Mostrar la lista de productos.
Calcular el valor total del inventario.
"""

class Producto:
    def __init__(self, nombre, precio) -> None:
        self.nombre = nombre
        self.precio = precio

    
class Inventario:
    def __init__(self) -> None:
        self.productos = []

    def addProducto(self, producto):
        self.productos.append(producto)
        print(f'El producto {producto.nombre} se agrego correctamente')

    def mostrarProductos(self):
        if not self.productos:
            print('No tenemos productos en el inventario')
        for producto in self.productos:
            print(f'El producto {producto.nombre} cuesta {producto.precio}')

    def totalInventario(self):
        return sum([producto.precio for producto in self.productos])
    

inventario = Inventario()

producto1 = Producto('comida1', 1)
inventario.addProducto(producto1)
producto2 = Producto('comida2', 2)
inventario.addProducto(producto2)
producto3 = Producto('comida3', 3)
inventario.addProducto(producto3)
producto4 = Producto('comida4', 4)
inventario.addProducto(producto4)
producto5 = Producto('comida5', 5)
inventario.addProducto(producto5)

inventario.mostrarProductos()

print(inventario.totalInventario())