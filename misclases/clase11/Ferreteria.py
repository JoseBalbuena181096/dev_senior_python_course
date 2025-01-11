#import threading
from abc import ABC, abstractmethod

# Patrón Singleton

class SistemaFacturacion:
    _instancia = None
    #_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        # with cls._lock:
        #     if cls._instacia is None:
        #         cls._instacia = super(SistemaFacturacion, cls).__new__(cls)
        #         cls._instacia._inicializacionHistorico()
        #     return cls._instacia
        if not cls._instancia:
            cls._instancia = super(SistemaFacturacion, cls).__new__(cls)
            cls._instancia._inicializacionHistorico()
        return cls._instancia
    
    def _inicializacionHistorico(self):
        self.historial = []
        print('Sistema de facturación inicializado')

    def registarOperacion(self, operacion):
        self.historial.append(operacion)
        print(f'La operación es registrada {operacion}')

# Clase abstracta = Superclase
class ProcesoNegocio(ABC):

    @abstractmethod
    def ejecutar(self):
        pass

class ProcesarPedido(ProcesoNegocio):
    def ejecutar(self):
        print("Procesar pedido ...")
        return "Pedido procesado"

class ProcesarFactura(ProcesoNegocio):
    def ejecutar(self):
        print("Procesar factura ...")
        return "Factura procesada"
    
# Crear la fabrica (patron factory)
class FabricaProcesoNegocio:
    @staticmethod
    def crearProceso(tipoProceso):
        if tipoProceso == 'pedido':
            return ProcesarPedido()
        elif tipoProceso == 'factura':
            return ProcesarFactura()
        else:
            raise ValueError(f'El proceso {tipoProceso} no existe')
        
if __name__ == '__main__':
    sistema_facturacion = SistemaFacturacion()
    proceso1 = FabricaProcesoNegocio.crearProceso('pedido')
    proceso2 = FabricaProcesoNegocio.crearProceso('factura')

    resultadoPedido1 = proceso1.ejecutar()
    sistema_facturacion.registarOperacion(resultadoPedido1)

    resultadoPedido2 = proceso2.ejecutar()
    sistema_facturacion.registarOperacion(resultadoPedido2)

    print('Sistema de facturacion historial')
    for operacion in sistema_facturacion.historial:
        print(f'Transaccion {operacion}')