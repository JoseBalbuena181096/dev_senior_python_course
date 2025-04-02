import sqlite3
import os
import mysql.connector

# Get the directory where the script is running
current_directory = os.path.dirname(os.path.abspath(__file__))

# Create the database file path in the same directory
db_file_path = os.path.join(current_directory, "academiadevsenior.db")

# Conexion 
class ConexionSQLite:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conexion = sqlite3.connect(db_path)
        self.cursor = self.conexion.cursor()
        print('Conexión establecida SQLite3')

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
    def __init__(self, db_path):
        self.db = ConexionSQLite(db_path)

    def agregarProfesor(self, nombre, especialidad, experiencia):
        query = "INSERT INTO Profesores(nombre,especialidad,experiencia) VALUES (?, ?, ?);"
        values = (nombre, especialidad, experiencia)
        self.db.ejecutar_query(query, values)
        print(f'Profesor {nombre} agregado con exitp')

def main():
    gestion = GestionarProfesor(db_file_path)
    gestion.agregarProfesor('Jose Palma', "Medician", 5)

main()