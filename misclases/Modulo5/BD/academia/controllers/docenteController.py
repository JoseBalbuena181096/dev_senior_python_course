from models.docente import Docente
from config.database import Database

class DocenteController:
    def __init__(self, db):
        self.db = db

    def registrar_docente(self, nombre, apellido, correo, telefono, especialidad):
        """
        Registra un nuevo docente en la base de datos
        :param nombre: str
        :param apellido: str
        :param correo: str
        :param telefono: str
        :param especialidad: str
        """
        sql = """
            INSERT INTO Profesores (nombre, apellido, correo_electronico, telefono, especialidad)
            VALUES (%s, %s, %s, %s, %s)
        """
        params = (nombre, apellido, correo, telefono, especialidad)
        self.db.execute_query(sql, params)

    def listar_docentes(self):
        """
        Obtiene todos los docentes registrados en la base de datos
        :return: lista de objetos Docente
        """
        sql = "SELECT id_profesor, nombre, apellido, correo_electronico, telefono, especialidad FROM Profesores"
        resultados = self.db.execute_select(sql)
        return [Docente(*resultado) for resultado in resultados]
    
    def obtener_docente_por_id(self, id_docente):
        """
        Obtiene un docente por su id
        :param id_docente: int
        :return: objeto Docente
        """
        sql = "SELECT id_profesor, nombre, apellido, correo_electronico, telefono, especialidad FROM Profesores WHERE id_profesor = %s"
        resultado = self.db.execute_select(sql, (id_docente,))
        return Docente(*resultado[0]) if resultado else None
    
    def actualizar_docente(self, id_docente, nombre, apellido, correo, telefono, especialidad):
        """
        Actualiza los datos de un docente existente
        :param id_docente: int
        :param nombre: str
        :param apellido: str
        :param correo: str
        :param telefono: str
        :param especialidad: str    
        """
        sql = """
            UPDATE Profesores
            SET nombre = %s, apellido = %s, correo_electronico = %s, telefono = %s, especialidad = %s
            WHERE id_profesor = %s
        """ 
        params = (nombre, apellido, correo, telefono, especialidad, id_docente)
        self.db.execute_query(sql, params)

    def eliminar_docente(self, id_docente):
        """
        Elimina un docente por su id
        :param id_docente: int
        """
        sql = "DELETE FROM Profesores WHERE id_profesor = %s"
        self.db.execute_query(sql, (id_docente,))           
