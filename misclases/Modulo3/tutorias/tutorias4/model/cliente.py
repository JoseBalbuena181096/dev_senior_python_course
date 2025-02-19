class Cliente:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono
        self.mascotas = {}
        self.citas =  {}

    def agregar_mascotas(self, mascota):
        self.mascotas[mascota.nombre] = mascota

    def agregar_cita(self, mascota, cita):
        if mascota.nombre not in self.citas:
            self.citas[mascota.nombre] = []
        self.citas[mascota.nombre].append(cita)


