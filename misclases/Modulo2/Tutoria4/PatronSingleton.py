import json
from pathlib import Path

class SistemaGuardado:
    
    __intance = None
    
    @staticmethod
    def get_instance():
        if SistemaGuardado.__intance is None:
            SistemaGuardado.__intance = SistemaGuardado()
        return SistemaGuardado.__intance
    
    def __init__(self):
        current_dir = Path(__file__).parent
        config_path = current_dir / "guardado.bat"
        self.archivo_gurdado = config_path
        
    def guardar_juego(self, dato_a_guardar):
        with open(self.archivo_gurdado, "w") as f:
            json.dump(dato_a_guardar,f, indent=2)
            
    def cargar_juego(self):
        with open(self.archivo_gurdado, "r") as f:
            return json.load(f)
        

class Jugador():
    
    def __init__(self, nombre, nivel):
        self.nombre = nombre
        self.nivel = nivel
    
    def serializar(self):
        return {
            "nombre": self.nombre,
            "nivel": self.nivel
        }
        
    @classmethod   
    def deserializar(self, data):
        return self(data["nombre"], data["nivel"])
        
def cargar_partida():
    guardo = SistemaGuardado.get_instance()
    datos_guardados = guardo.cargar_juego()
    jugador = Jugador.deserializar(datos_guardados)



# jugado1 = Jugador('jose balbuena', 28)
# guardado = SistemaGuardado.get_instance()
# guardado.guardar_juego(jugado1.serializar())

guardado = SistemaGuardado.get_instance()
datos_cargados = guardado.cargar_juego()
jugador_cargado = Jugador.deserializar(datos_cargados)
print(jugador_cargado.nombre)
