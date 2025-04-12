import mysql.connector
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

# Configuración de la conexión a la base de datos
class DatabaseConnection:
    def __init__(self):
        self.host = os.getenv("DB_HOST", "localhost")
        self.user = os.getenv("DB_USER", "root")
        self.password = os.getenv("DB_PASSWORD", "root")
        self.port = int(os.getenv("DB_PORT", "3306"))
        self.database = os.getenv("DB_NAME", "academia")

    def conectar(self):
        try:
            conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                port=self.port,
                database=self.database
            )
            if conn.is_connected():
                print("Conexión exitosa a la base de datos")
                return conn
            return None
        except mysql.connector.Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            return None
        except Exception as e:
            print(f"Error inesperado: {e}")
            return None

    def execute_query(self, query, params=None):
        conn = self.conectar()
        cursor = None
        if not conn:
            return False
        try:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            return True
        except mysql.connector.Error as e:
            print(f"Error al ejecutar la consulta: {e}")
            return False
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def execute_query_with_results(self, query, params=None):
        conn = self.conectar()
        cursor = None
        if not conn:
            return []
        try:
            cursor = conn.cursor()
            cursor.execute(query, params)
            resultados = cursor.fetchall()
            return resultados
        except mysql.connector.Error as e:
            print(f"Error al ejecutar la consulta: {e}")
            return []
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

# Función de conveniencia para mantener compatibilidad con código existente
def connection():
    db = DatabaseConnection()
    return db.conectar()

# Probar la conexión al importar el módulo
if __name__ == "__main__":
    conn = connection()
    if conn:
        conn.close()










