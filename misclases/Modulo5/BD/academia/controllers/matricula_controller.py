from models.matricula import Matricula
from controllers.curso_controller import CursoController

class MatriculaController:
    def __init__(self, db):
        self.db = db
        self.curso_controller = CursoController(db)

    def verificar_curso_existe(self, curso_id):
        """
        Verifica si un curso existe en la base de datos
        :param curso_id: int
        :return: bool
        """
        curso = self.curso_controller.obtener_curso_por_id(curso_id)
        return curso is not None

    def registrar_matricula(self, estudiante_id, curso_id, fecha_matricula):
        """
        Registra una nueva matrícula en la base de datos
        :param estudiante_id: int
        :param curso_id: int
        :param fecha_matricula: str (formato YYYY-MM-DD)
        """
        # Verificar si el curso existe
        if not self.verificar_curso_existe(curso_id):
            raise ValueError(f"No existe un curso con el ID {curso_id}")

        sql = """
            INSERT INTO Matriculas (estudiante_id, curso_id, fecha_matricula)
            VALUES (%s, %s, %s)
        """
        params = (estudiante_id, curso_id, fecha_matricula)
        self.db.execute_query(sql, params)

    def listar_matriculas(self):
        """
        Obtiene todas las matrículas registradas en la base de datos
        :return: lista de objetos Matricula
        """
        sql = """
            SELECT m.id_matricula, m.estudiante_id, m.curso_id, m.fecha_matricula,
                   CONCAT(e.nombre, ' ', e.apellido) as nombre_estudiante,
                   c.nombre as nombre_curso
            FROM Matriculas m
            JOIN Estudiantes e ON m.estudiante_id = e.id_estudiante
            JOIN Cursos c ON m.curso_id = c.id_curso
        """
        resultados = self.db.execute_select(sql)
        return [Matricula(*resultado) for resultado in resultados]

    def obtener_matricula_por_id(self, id_matricula):
        """
        Obtiene una matrícula por su id
        :param id_matricula: int
        :return: objeto Matricula
        """
        sql = """
            SELECT m.id_matricula, m.estudiante_id, m.curso_id, m.fecha_matricula,
                   CONCAT(e.nombre, ' ', e.apellido) as nombre_estudiante,
                   c.nombre as nombre_curso
            FROM Matriculas m
            JOIN Estudiantes e ON m.estudiante_id = e.id_estudiante
            JOIN Cursos c ON m.curso_id = c.id_curso
            WHERE m.id_matricula = %s
        """
        resultado = self.db.execute_select(sql, (id_matricula,))
        return Matricula(*resultado[0]) if resultado else None

    def actualizar_matricula(self, id_matricula, estudiante_id, curso_id, fecha_matricula):
        """
        Actualiza los datos de una matrícula existente
        :param id_matricula: int
        :param estudiante_id: int
        :param curso_id: int
        :param fecha_matricula: str (formato YYYY-MM-DD)
        """
        sql = """
            UPDATE Matriculas
            SET estudiante_id = %s, curso_id = %s, fecha_matricula = %s
            WHERE id_matricula = %s
        """
        params = (estudiante_id, curso_id, fecha_matricula, id_matricula)
        self.db.execute_query(sql, params)

    def eliminar_matricula(self, id_matricula):
        """
        Elimina una matrícula por su id
        :param id_matricula: int
        """
        sql = "DELETE FROM Matriculas WHERE id_matricula = %s"
        self.db.execute_query(sql, (id_matricula,))

    def obtener_matriculas_por_estudiante(self, estudiante_id):
        """
        Obtiene todas las matrículas de un estudiante
        :param estudiante_id: int
        :return: lista de objetos Matricula
        """
        sql = """
            SELECT m.id_matricula, m.estudiante_id, m.curso_id, m.fecha_matricula,
                   CONCAT(e.nombre, ' ', e.apellido) as nombre_estudiante,
                   c.nombre as nombre_curso
            FROM Matriculas m
            JOIN Estudiantes e ON m.estudiante_id = e.id_estudiante
            JOIN Cursos c ON m.curso_id = c.id_curso
            WHERE m.estudiante_id = %s
        """
        resultados = self.db.execute_select(sql, (estudiante_id,))
        return [Matricula(*resultado) for resultado in resultados]

    def obtener_matriculas_por_curso(self, curso_id):
        """
        Obtiene todas las matrículas de un curso
        :param curso_id: int
        :return: lista de objetos Matricula
        """
        sql = """
            SELECT m.id_matricula, m.estudiante_id, m.curso_id, m.fecha_matricula,
                   CONCAT(e.nombre, ' ', e.apellido) as nombre_estudiante,
                   c.nombre as nombre_curso
            FROM Matriculas m
            JOIN Estudiantes e ON m.estudiante_id = e.id_estudiante
            JOIN Cursos c ON m.curso_id = c.id_curso
            WHERE m.curso_id = %s
        """
        resultados = self.db.execute_select(sql, (curso_id,))
        return [Matricula(*resultado) for resultado in resultados]
