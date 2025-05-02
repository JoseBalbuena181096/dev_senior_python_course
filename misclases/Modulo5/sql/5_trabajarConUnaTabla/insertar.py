import mysql.connector
import csv
import os

# Configuración de la conexión a MySQL
config = {
    'user': 'root',  # Cambia esto por tu usuario de MySQL
    'password': 'root',  # Cambia esto por tu contraseña de MySQL
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
        CREATE TABLE IF NOT EXISTS ventas (
            ID_Venta INT PRIMARY KEY,
            Fecha_venta INT,
            ID_producto INT,
            ID_Zona INT,
            Venta DECIMAL(10,2),
            ID_Vendedor INT,
            ID_Cliente INT
        )
        """
        cursor.execute(crear_tabla)

        # Ruta del archivo CSV
        ruta_csv = os.path.join(os.path.dirname(__file__), 'ventas.csv')

        # Leer y insertar datos del CSV
        with open(ruta_csv, 'r') as archivo:
            lector_csv = csv.reader(archivo)
            next(lector_csv)  # Saltar la cabecera
            
            for fila in lector_csv:
                # Convertir los valores a los tipos correctos
                id_venta = int(fila[0])
                fecha_venta = int(fila[1])
                id_producto = int(fila[2])
                id_zona = int(fila[3])
                venta = float(fila[4])
                id_vendedor = int(fila[5])
                id_cliente = int(fila[6])

                # Consulta de inserción
                insertar = """
                INSERT INTO ventas (ID_Venta, Fecha_venta, ID_producto, ID_Zona, Venta, ID_Vendedor, ID_Cliente)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
                valores = (id_venta, fecha_venta, id_producto, id_zona, venta, id_vendedor, id_cliente)
                cursor.execute(insertar, valores)

        # Confirmar los cambios
        conexion.commit()
        print("Datos insertados correctamente")

    except mysql.connector.Error as error:
        print(f"Error al insertar datos: {error}")
    
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()
            print("Conexión cerrada")

if __name__ == "__main__":
    insertar_datos()
