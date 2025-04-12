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
        CREATE TABLE IF NOT EXISTS vendedores (
            ID_Vendedor INT PRIMARY KEY,
            Nombre VARCHAR(50),
            Apellido VARCHAR(50),
            Telefono VARCHAR(20),
            Estado_Civil VARCHAR(20),
            Edad INT,
            Salario DECIMAL(10,2),
            ID_supervisor INT
        )
        """
        cursor.execute(crear_tabla)

        # Ruta del archivo CSV
        ruta_csv = os.path.join(os.path.dirname(__file__), 'trabajarConUnaTabla', 'vendedor.csv')

        # Leer y insertar datos del CSV
        with open(ruta_csv, 'r') as archivo:
            lector_csv = csv.reader(archivo)
            next(lector_csv)  # Saltar la cabecera
            
            for fila in lector_csv:
                id_vendedor = int(fila[0])
                nombre = fila[1]
                apellido = fila[2]
                telefono = fila[3]
                estado_civil = fila[4]
                edad = int(fila[5])
                salario = float(fila[6])
                id_supervisor = None if fila[7] == '' else int(fila[7])

                # Consulta de inserción
                insertar = """
                INSERT INTO vendedores (ID_Vendedor, Nombre, Apellido, Telefono, Estado_Civil, Edad, Salario, ID_supervisor)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """
                valores = (id_vendedor, nombre, apellido, telefono, estado_civil, edad, salario, id_supervisor)
                cursor.execute(insertar, valores)

        # Confirmar los cambios
        conexion.commit()
        print("Datos de vendedores insertados correctamente")

    except mysql.connector.Error as error:
        print(f"Error al insertar datos: {error}")
    
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()
            print("Conexión cerrada")

if __name__ == "__main__":
    insertar_datos() 