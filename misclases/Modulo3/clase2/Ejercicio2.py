# Implementar sistema para facturación c/manejo de excepciones por consola y .log file

import logging
from dataclasses import dataclass

from pathlib import Path

current_dir = Path(__file__).parent
config_path = current_dir / 'ejercicio.log'

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s %(message)s',
    filename= config_path,
    filemode='a'
)

# Crear un nuevo handler para gestionar mensaje de audotiroria por .log y por consola
console_handler = logging.StreamHandler() # Crea instancia, es decir un nuevo manejador
console_handler.setLevel(logging.DEBUG) # Configurar el nivel del loogin, en este caso, el nivel mas level
console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s %(message)s',)) # dando formato de salida al loogin
logging.getLogger().addHandler(console_handler) # Agregando la instancia al manejador principal

@dataclass
class Factura:
    cliente: str
    cantidad: int
    precio_unitario: float

    def procesar(self):
        try:
            logging.info(f'Iniciando el proceso de facturacion para el cliente {self.cliente}')

            if self.cantidad <= 0:
                raise ValueError(f'La cantidad del producto debe ser mayor a cero')
            if self.precio_unitario <= 0:
                raise ValueError(f'El precio debe ser mayor a cero')
            
            total = self.cantidad * self.precio_unitario
            logging.info(f'Factura fue procesada con exito Taotal de la compra ')

        except ValueError as e:
            logging.error(f'Error de la lalidacion de cliente {self.cliente} {e}')
        
        except Exception as e:
            logging.critical(f'Erroor inesperado al crear la factura {self.cliente} {e}')
        
        finally:
            logging.info(f'El proceso de facturacion para {self.cliente} finalizo')

if __name__ == "__main__":
    factura1 =  Factura("Jose", 10, 1500.25)
    factura1.procesar()

    factura2 = Factura('Pedro', 150, 1233)
    factura2.procesar()