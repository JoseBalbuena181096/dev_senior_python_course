from models.estudiante import Estudiante    

class EstudiantesController:
    def __init__(self, db):
        self.db = db

    def registrar_estudiante(self, nombre, apellido, correo, telefono):
        query = "INSERT INTO estudiantes (nombre, apellido, correo_electronico, telefono) VALUES (%s, %s, %s, %s)"
        params = (nombre, apellido, correo, telefono)
        if self.db.execute_query(query, params):
            print("Estudiante registrado exitosamente")
            return True
        return False
                
    def listar_estudiantes(self):
        query = "SELECT * FROM estudiantes"
        estudiantes = self.db.execute_query_with_results(query)
        if estudiantes:
            print("\nLista de estudiantes:")
            for estudiante in estudiantes:
                print(f"ID: {estudiante[0]}, Nombre: {estudiante[1]}, Apellido: {estudiante[2]}, Correo: {estudiante[3]}, Teléfono: {estudiante[4]}")
        else:
            print("No hay estudiantes registrados")
        return estudiantes


