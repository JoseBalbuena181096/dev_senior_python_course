class Vehiculo:
    def __init__(self, marca):
        self.marca = marca
    
    def moverse(self):
        print('Me muevo')

class Motor:
    def __init__(self, tipo):
        self.tipo = tipo

    def encender(self):
        print(f"El motor tipo {self.tipo} se ha encendido")

class Rueda:
    def __init__(self, size):
        self.size = size

    def girar(self):
        print(f'La rueda de tamaño {self.size}')

class Coche(Vehiculo):
    def __init__(self, marca, motor, ruedas):
        super().__init__(marca)
        self.motor = motor
        self.ruedas = ruedas

    def iniciar_viaje(self):
        self.motor.encender()
        for rueda in self.ruedas:
            rueda.girar
        print('El coche se esta moviendo')

moto_deportivo = Motor('V1')
tipo_ruedas = int(input('Ingrese el tipo de ruedas (10-50)'))
ruedas_small = [Rueda(tipo_ruedas),Rueda(tipo_ruedas),Rueda(tipo_ruedas),Rueda(tipo_ruedas)]
coche_deportivo = Coche( "Audi",moto_deportivo, ruedas_small)
coche_deportivo.iniciar_viaje()