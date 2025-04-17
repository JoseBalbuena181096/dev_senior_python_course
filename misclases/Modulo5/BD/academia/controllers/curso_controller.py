from models.curso import Curso

class CursoController:
    def __init__(self, db):
        self.db = db

    def registrar_curso(self, nombre, descripcion, duracion_horas, profesor_id):
        """
        Registra un nuevo curso en la base de datos
        :param nombre: str
        :param descripcion: str
        :param duracion_horas: int
        :param profesor_id: int
        """
        sql = """
            INSERT INTO Cursos (nombre, descripcion, duracion_horas, profesor_id)
            VALUES (%s, %s, %s, %s)
        """
        params = (nombre, descripcion, duracion_horas, profesor_id)
        self.db.execute_query(sql, params)

    def listar_cursos(self):
        """
        Obtiene todos los cursos registrados en la base de datos
        :return: lista de objetos Curso
        """
        sql = """
            SELECT c.id_curso, c.nombre, c.descripcion, c.duracion_horas, p.id_profesor,CONCAT(p.nombre,' ',p.apellido) AS  nombre_profesore 
            FROM Cursos c
            JOIN Profesores p ON c.profesor_id = p.id_profesor;
        """
        resultados = self.db.execute_select(sql)
        return [Curso(*resultado) for resultado in resultados]

    def obtener_curso_por_id(self, id_curso):
        """
        Obtiene un curso por su id
        :param id_curso: int
        :return: objeto Curso
        """
        sql = """
            SELECT c.id_curso, c.nombre, c.descripcion, c.duracion_horas, p.id_profesor,CONCAT(p.nombre,' ',p.apellido) AS  nombre_profesore 
            FROM Cursos c
            JOIN Profesores p ON c.profesor_id = p.id_profesor
            WHERE c.id_curso = %s
        """
        resultado = self.db.execute_select(sql, (id_curso,))
        return Curso(*resultado[0]) if resultado else None

    def actualizar_curso(self, id_curso, nombre, descripcion, duracion_horas, profesor_id):
        """
        Actualiza los datos de un curso existente
        :param id_curso: int
        :param nombre: str
        :param descripcion: str
        :param duracion_horas: int
        :param profesor_id: int
        """
        sql = """
            UPDATE Cursos
            SET nombre = %s, descripcion = %s, duracion_horas = %s, profesor_id = %s
            WHERE id_curso = %s
        """
        params = (nombre, descripcion, duracion_horas, profesor_id, id_curso)
        self.db.execute_query(sql, params)

    def eliminar_curso(self, id_curso):
        """
        Elimina un curso por su id
        :param id_curso: int
        """
        sql = "DELETE FROM Cursos WHERE id_curso = %s"
        self.db.execute_query(sql, (id_curso,))

    def obtener_cursos_por_profesor(self, profesor_id):
        """
        Obtiene todos los cursos asignados a un profesor
        :param profesor_id: int
        :return: lista de objetos Curso
        """
        sql = """
            SELECT id_curso, nombre, descripcion, duracion_horas, profesor_id 
            FROM Cursos 
            WHERE profesor_id = %s
        """
        resultados = self.db.execute_select(sql, (profesor_id,))
        return [Curso(*resultado) for resultado in resultados]
