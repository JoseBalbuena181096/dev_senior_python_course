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
        CREATE TABLE IF NOT EXISTS pagos (
            ID_pago INT PRIMARY KEY,
            ID_venta INT,
            Fecha_pago INT,
            Pago DECIMAL(10,2),
            FOREIGN KEY (ID_venta) REFERENCES ventas(ID_Venta)
        )
        """
        cursor.execute(crear_tabla)

        # Ruta del archivo CSV
        ruta_csv = os.path.join(os.path.dirname(__file__), 'pagos.csv')

        # Leer y insertar datos del CSV
        with open(ruta_csv, 'r') as archivo:
            lector_csv = csv.reader(archivo)
            next(lector_csv)  # Saltar la cabecera
            
            for fila in lector_csv:
                # Convertir los valores a los tipos correctos
                id_pago = int(fila[0])
                id_venta = int(fila[1])
                fecha_pago = int(fila[2])
                pago = float(fila[3])

                # Consulta de inserción
                insertar = """
                INSERT INTO pagos (ID_pago, ID_venta, Fecha_pago, Pago)
                VALUES (%s, %s, %s, %s)
                """
                valores = (id_pago, id_venta, fecha_pago, pago)
                cursor.execute(insertar, valores)

        # Confirmar los cambios
        conexion.commit()
        print("Datos de pagos insertados correctamente")

    except mysql.connector.Error as error:
        print(f"Error al insertar datos: {error}")
    
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()
            print("Conexión cerrada")

if __name__ == "__main__":
    insertar_datos() 