class NuevoCanal:
    def __init__(self):
        self._suscriptor = []
        self._later_news = None

    def suscribir(self, suscribirse):
        self._suscriptor.append(suscribirse)

    def desuscribir(self, suscribirse):
        self._suscriptor.remove(suscribirse)

    def notificacion(self):
        for sus in self._suscriptor:
            sus.update(self._later_news)

    def publicacion(self, news):
        self._later_news = news
        print(f'Notificacion publicada: {news}')
        self.notificacion()

class Suscriptores:
    def __init__(self, name):
        self.name = name 

    def update(self, news):
        print(f'{self.name} ha recibido la notificacion {news}')

canalDevSeniorCode = NuevoCanal()
sus1 = Suscriptores("Jose")
sus2 = Suscriptores('Juan')
sus3 = Suscriptores("Marcos")

canalDevSeniorCode.suscribir(sus1)
canalDevSeniorCode.suscribir(sus3)

canalDevSeniorCode.publicacion("Tenemos tutoria")