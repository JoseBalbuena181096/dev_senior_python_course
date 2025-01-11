# Interfaces en python
from abc import ABC, abstractmethod

class ProcesoPago(ABC):
    @abstractmethod
    def procesoPago(self, cantidad:float) -> None:
        pass

    @abstractmethod
    def reembolsoPago(self, trasaccionId:str) -> None:
        pass

class Paypal(ProcesoPago):
    def procesoPago(self, cantidad: float) -> None:
        print(f'Procesando pago por ${cantidad} por paypal')

    def reembolsoPago(self, trasaccionId: str) -> None:
        print(f'Reembolsando Id transaccion número {trasaccionId} por paypal')

class Stripe(ProcesoPago):
    def procesoPago(self, cantidad: float) -> None:
        print(f'Procesando pago por ${cantidad} por stripe')

    def reembolsoPago(self, trasaccionId: str) -> None:
        print(f'Reembolsando Id transaccion número {trasaccionId} por stripe')
        

    
if __name__ == "__main__":
    procesoPaypal = Paypal()
    procesoStripe = Stripe()
    procesoPaypal.procesoPago(500.0)
    procesoPaypal.reembolsoPago("EXFPMLJSKLAXXLL")
    procesoStripe.procesoPago(400.0)
    procesoStripe.reembolsoPago("EXFPMLJSKLAXXLL")
    
        