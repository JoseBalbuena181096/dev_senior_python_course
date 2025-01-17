# Polimorfismo a travez de metodos comunes en diferentes clases

class Gato:
    def sonido(self):
        return "Miau miu"
    
class Carro:
    def sonido(self):
        return "Pii pii"
    

def hacer_sonido(objeto):
    print(objeto.sonido())


#Instanciar
hacer_sonido(Gato())
hacer_sonido(Carro())