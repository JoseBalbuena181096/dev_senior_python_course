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
        CREATE TABLE IF NOT EXISTS dias (
            ID_Dia INT PRIMARY KEY,
            Dia_semana VARCHAR(20)
        )
        """
        cursor.execute(crear_tabla)

        # Obtener la ruta del directorio actual del script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Ruta del archivo CSV (en el mismo directorio que el script)
        ruta_csv = os.path.join(script_dir, 'dias.csv')

        # Verificar si el archivo existe
        if not os.path.isfile(ruta_csv):
            print(f"Error: No se encontró el archivo {ruta_csv}")
            print(f"Directorio actual: {script_dir}")
            print(f"Contenido del directorio: {os.listdir(script_dir)}")
            return

        # Leer y insertar datos del CSV
        with open(ruta_csv, 'r', encoding='utf-8') as archivo:
            lector_csv = csv.reader(archivo)
            next(lector_csv)  # Saltar la cabecera
            
            for fila in lector_csv:
                id_dia = int(fila[0])
                dia_semana = fila[1]

                # Consulta de inserción
                insertar = """
                INSERT INTO dias (ID_Dia, Dia_semana)
                VALUES (%s, %s)
                """
                valores = (id_dia, dia_semana)
                cursor.execute(insertar, valores)

        # Confirmar los cambios
        conexion.commit()
        print("Datos de días insertados correctamente")

    except mysql.connector.Error as error:
        print(f"Error al insertar datos: {error}")
    
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()
            print("Conexión cerrada")

if __name__ == "__main__":
    insertar_datos() 