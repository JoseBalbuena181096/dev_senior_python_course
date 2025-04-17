from models.horario import Horario

class HorarioController:
    def __init__(self, db):
        self.db = db

    def registrar_horario(self, curso_id, dia_semana, hora_inicio, hora_fin):
        """
        Registra un nuevo horario en la base de datos
        :param curso_id: int
        :param dia_semana: str
        :param hora_inicio: str (formato HH:MM:SS)
        :param hora_fin: str (formato HH:MM:SS)
        """
        sql = """
            INSERT INTO Horarios (curso_id, dia_semana, hora_inicio, hora_fin)
            VALUES (%s, %s, %s, %s)
        """
        params = (curso_id, dia_semana, hora_inicio, hora_fin)
        self.db.execute_query(sql, params)

    def listar_horarios(self):
        """
        Obtiene todos los horarios registrados en la base de datos
        :return: lista de objetos Horario
        """
        sql = """
            SELECT h.id_horario, h.curso_id, h.dia_semana, h.hora_inicio, h.hora_fin,
                   c.nombre as nombre_curso
            FROM Horarios h
            JOIN Cursos c ON h.curso_id = c.id_curso
        """
        resultados = self.db.execute_select(sql)
        return [Horario(*resultado) for resultado in resultados]

    def obtener_horario_por_id(self, id_horario):
        """
        Obtiene un horario por su id
        :param id_horario: int
        :return: objeto Horario
        """
        sql = """
            SELECT h.id_horario, h.curso_id, h.dia_semana, h.hora_inicio, h.hora_fin,
                   c.nombre as nombre_curso
            FROM Horarios h
            JOIN Cursos c ON h.curso_id = c.id_curso
            WHERE h.id_horario = %s
        """
        resultado = self.db.execute_select(sql, (id_horario,))
        return Horario(*resultado[0]) if resultado else None

    def actualizar_horario(self, id_horario, curso_id, dia_semana, hora_inicio, hora_fin):
        """
        Actualiza los datos de un horario existente
        :param id_horario: int
        :param curso_id: int
        :param dia_semana: str
        :param hora_inicio: str (formato HH:MM:SS)
        :param hora_fin: str (formato HH:MM:SS)
        """
        sql = """
            UPDATE Horarios
            SET curso_id = %s, dia_semana = %s, hora_inicio = %s, hora_fin = %s
            WHERE id_horario = %s
        """
        params = (curso_id, dia_semana, hora_inicio, hora_fin, id_horario)
        self.db.execute_query(sql, params)

    def eliminar_horario(self, id_horario):
        """
        Elimina un horario por su id
        :param id_horario: int
        """
        sql = "DELETE FROM Horarios WHERE id_horario = %s"
        self.db.execute_query(sql, (id_horario,))

    def obtener_horarios_por_curso(self, curso_id):
        """
        Obtiene todos los horarios asignados a un curso
        :param curso_id: int
        :return: lista de objetos Horario
        """
        sql = """
            SELECT h.id_horario, h.curso_id, h.dia_semana, h.hora_inicio, h.hora_fin,
                   c.nombre as nombre_curso
            FROM Horarios h
            JOIN Cursos c ON h.curso_id = c.id_curso
            WHERE h.curso_id = %s
        """
        resultados = self.db.execute_select(sql, (curso_id,))
        return [Horario(*resultado) for resultado in resultados]
