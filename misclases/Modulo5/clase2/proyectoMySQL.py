import mysql.connector

class ConexionMySQL:
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

        self.conexion = mysql.connector.connect(
            host = self.host,
            port = self.port,
            user = self.user,
            password = self.password,
            database = self.database 
        )
        self.cursor = self.conexion.cursor()
        # Verficamos la conexion
        if self.conexion.is_connected():
            print("Connectado a MySQL")

    def ejecutar_query(self, query, params = ()):
        """  Metodo para ejecutar cuaquier consulta SQL """
        self.cursor.execute(query, params)
        self.conexion.commit()

    def obtener_resultados():
        """ Metodo para obtener los resultados del SELECT """
        return self.cursor.fetchall()

    def cerrar_conexion(self):
        """ Cerrar la conexión """
        self.cursor.close()
        self.conexion.close()
        print("Conexion cerrada")


class GestionarProfesor:
    def __init__(self, mySQLDB):
        self.db = mySQLDB

    def agregarProfesor(self, nombre, especialidad, experiencia):
        query = "INSERT INTO Profesores(nombre,especialidad,experiencia) VALUES (%s, %s, %s);"
        values = (nombre, especialidad, experiencia)
        self.db.ejecutar_query(query, values)
        print(f'Profesor {nombre} agregado con exito')



def main():

    db_mysql = ConexionMySQL(
        host = "127.0.0.1", # "localhost"
        port = 3306,
        user = "root",
        password = "root",
        database = "academiadevsenior"
    )

    gestion = GestionarProfesor(db_mysql)
    gestion.agregarProfesor('Jose Palma', "Medician", 5)


main()


