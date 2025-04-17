from config.database import Database
from models.estudiante import Estudiante

class EstudianteController:
    def __init__(self, db):
        self.db = db

    def registrar_estudiante(self, nombre, apellido, correo, telefono):
        sql = """
            INSERT INTO Estudiantes (nombre, apellido, correo_electronico, telefono)
            VALUES (%s, %s, %s, %s)
        """
        params = (nombre, apellido, correo, telefono)
        self.db.execute_query(sql, params)

    def listar_estudiantes(self):
        sql = "SELECT id_estudiante, nombre, apellido, correo_electronico, telefono FROM estudiantes"
        resultados = self.db.execute_select(sql)
        return [Estudiante(*resultado) for resultado in resultados]
    
    def obtener_estudiante_por_id(self, id_estudiante):
        sql = "SELECT id_estudiante, nombre, apellido, correo_electronico, telefono FROM estudiantes WHERE id_estudiante = %s"
        resultado = self.db.execute_select(sql, (id_estudiante,))
        return Estudiante(*resultado[0]) if resultado else None
    
    def actualizar_estudiante(self, id_estudiante, nombre, apellido, correo, telefono):
        sql = """
            UPDATE estudiantes
            SET nombre = %s, apellido = %s, correo_electronico = %s, telefono = %s
            WHERE id_estudiante = %s
        """
        params = (nombre, apellido, correo, telefono, id_estudiante)
        self.db.execute_query(sql, params)

    def eliminar_estudiante(self, id_estudiante):
        sql = "DELETE FROM estudiantes WHERE id_estudiante = %s"
        self.db.execute_query(sql, (id_estudiante,))        
    
