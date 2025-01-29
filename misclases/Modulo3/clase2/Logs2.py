import logging
from dataclasses import dataclass, field
from pathlib import Path

# App que permite llevar el seguineto de compras/fallos em esta transaccion
# Esta App, registrará ña cantidad de productos comprados, confirmación de compra y error de transacciones

current_dir = Path(__file__).parent
config_path = current_dir / 'registro.log'

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s %(message)s',
    filename= config_path,
    filemode='a'
)

@dataclass
class Producto:
    nombre : str
    precio : int
    cantidad : int

    def comprar(self, cantidad:int):
        if cantidad > self.cantidad:
            logging.error(f'Error no hay suficiente cantidad de producto: {self.nombre} El stock disponible es {self.cantidad}')
            print(f'Error no hay suficiente cantidad de producto: {self.nombre} El stock disponible es {self.cantidad}')
            raise ValueError(f'Error no hay suficiente cantidad de producto: {self.nombre} El stock disponible es {self.cantidad}')
        else:
            self.cantidad -= cantidad
            logging.info(f'La compra fue exitosa. El stock restatnte es {self.cantidad}')
            print(f'La compra fue exitosa. El stock restatnte es {self.cantidad}')
            return self.precio * cantidad
        
@dataclass
class Tienda:
    productos: list[Producto] = field(default_factory=list)

    def agregar_producto(self, producto:Producto):
        self.productos.append(producto)
        logging.debug(f'{producto.nombre} agregado con exito. El precio es de {producto.precio} - cantidad{producto.cantidad} en stock')
        print(f'{producto.nombre} agregado con exito. El precio es de {producto.precio} - cantidad{producto.cantidad} en stock')
    
    def realizar_compra(self, nombre_producto: str, cantidad: int):
        producto = next((p for p in self.productos if p.nombre == nombre_producto), None)
        if producto:
            try:
                total = producto.comprar(cantidad)
                logging.info(f'Comprar realizada {cantidad} unidades de {nombre_producto} por un total de {total}')
                print(f'Comprar realizada {cantidad} unidades de {nombre_producto} por un total de {total}')
                return total
            
            except ValueError as e:
                logging.error(f'Error al efectuar la compra: {e}')
                print(f'Error al efectuar la compra: {e}')
            else:
                logging.warning('El producto fuera de stock')

if __name__ == "__main__":
    tienda = Tienda()
    inventario_portatil = Producto(nombre="Portatil", precio=1000, cantidad=10)
    tienda.agregar_producto(inventario_portatil)
    tienda.realizar_compra('Portatil', 4)

    inventario_teclado = Producto(nombre="teclado", precio=5, cantidad=2)
    tienda.agregar_producto(inventario_teclado)
    tienda.realizar_compra('teclado', 10)

    inventario_pantalla = Producto(nombre="pantalla", precio=4, cantidad=120)
    tienda.agregar_producto(inventario_pantalla)
    tienda.realizar_compra('pantalla', 10)
    
