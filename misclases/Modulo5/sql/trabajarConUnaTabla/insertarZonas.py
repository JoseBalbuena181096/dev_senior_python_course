import mysql.connector
import csv
import os

# Configuración de la conexión a MySQL
config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'db_practica1'
}

def insertar_datos():
    try:
        # Establecer conexión
        conexion = mysql.connector.connect(**config)
        cursor = conexion.cursor()

        # Crear tabla si no existe
        crear_tabla = """
        CREATE TABLE IF NOT EXISTS zonas (
            ID_zona INT PRIMARY KEY,
            Zona VARCHAR(20)
        )
        """
        cursor.execute(crear_tabla)

        # Ruta del archivo CSV
        ruta_csv = os.path.join(os.path.dirname(__file__), 'trabajarConUnaTabla', 'zona.csv')

        # Leer y insertar datos del CSV
        with open(ruta_csv, 'r') as archivo:
            lector_csv = csv.reader(archivo)
            next(lector_csv)  # Saltar la cabecera
            
            for fila in lector_csv:
                id_zona = int(fila[0])
                zona = fila[1]

                # Consulta de inserción
                insertar = """
                INSERT INTO zonas (ID_zona, Zona)
                VALUES (%s, %s)
                """
                valores = (id_zona, zona)
                cursor.execute(insertar, valores)

        # Confirmar los cambios
        conexion.commit()
        print("Datos de zonas insertados correctamente")

    except mysql.connector.Error as error:
        print(f"Error al insertar datos: {error}")
    
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()
            print("Conexión cerrada")

if __name__ == "__main__":
    insertar_datos() 