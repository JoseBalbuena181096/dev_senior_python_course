# Patron de diseño factory
from abc import ABC, abstractmethod

#clase abstracta
class Clases(ABC):
    @abstractmethod
    def operacion(self):
        pass

class claseA(Clases):
    def operacion(self):
        return "Esta es la clase A"
    

class claseB(Clases):
    def operacion(self):
        return "Esta es la clase B"
    
    def impresion(self):
        pass
    
    def retiro(self):
        pass

# Clase Factory Factoria, Fabrica
class FabricaClases:
    @staticmethod
    def creacionObjetos(tipoObjeto):
        if tipoObjeto == 'A':
            return claseA()
        elif tipoObjeto == 'B':
            return claseB()
        else:
            raise ValueError(f'La clase {tipoObjeto} no existe')
        
object1 = FabricaClases.creacionObjetos('A')
object2 = FabricaClases.creacionObjetos('B') 
print(object1.operacion())
print(object2.operacion())