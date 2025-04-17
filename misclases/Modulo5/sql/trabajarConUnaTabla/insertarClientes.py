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
        CREATE TABLE IF NOT EXISTS clientes (
            ID_Cliente INT PRIMARY KEY,
            Nombre VARCHAR(100),
            Direccion VARCHAR(200),
            Pais VARCHAR(50),
            Telefono VARCHAR(20),
            Clasificacion_credito VARCHAR(2)
        )
        """
        cursor.execute(crear_tabla)

        # Ruta del archivo CSV
        ruta_csv = os.path.join(os.path.dirname(__file__), 'trabajarConUnaTabla', 'clientes.csv')

        # Leer y insertar datos del CSV
        with open(ruta_csv, 'r') as archivo:
            lector_csv = csv.reader(archivo)
            next(lector_csv)  # Saltar la cabecera
            
            for fila in lector_csv:
                id_cliente = int(fila[0])
                nombre = fila[1]
                direccion = fila[2]
                pais = fila[3]
                telefono = None if fila[4] == '' else fila[4]
                clasificacion_credito = fila[5]

                # Consulta de inserción
                insertar = """
                INSERT INTO clientes (ID_Cliente, Nombre, Direccion, Pais, Telefono, Clasificacion_credito)
                VALUES (%s, %s, %s, %s, %s, %s)
                """
                valores = (id_cliente, nombre, direccion, pais, telefono, clasificacion_credito)
                cursor.execute(insertar, valores)

        # Confirmar los cambios
        conexion.commit()
        print("Datos de clientes insertados correctamente")

    except mysql.connector.Error as error:
        print(f"Error al insertar datos: {error}")
    
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()
            print("Conexión cerrada")

if __name__ == "__main__":
    insertar_datos() 