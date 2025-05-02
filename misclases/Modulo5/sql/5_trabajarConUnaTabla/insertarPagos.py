import mysql.connector
import csv
import os
from datetime import datetime, timedelta

# Configuración de la conexión a MySQL
config = {
    'user': 'root',  # Cambia esto por tu usuario de MySQL
    'password': 'root',  # Cambia esto por tu contraseña de MySQL
    'host': 'localhost',
    'database': 'db_practica1'
}

def excel_date_to_date(excel_date):
    # Convertir fecha de Excel a fecha normal
    base_date = datetime(1899, 12, 30)
    return base_date + timedelta(days=excel_date)

def insertar_datos():
    try:
        # Establecer conexión
        conexion = mysql.connector.connect(**config)
        cursor = conexion.cursor()

        # Crear tabla si no existe
        crear_tabla = """
        CREATE TABLE IF NOT EXISTS pagos (
            ID_Pago INT PRIMARY KEY,
            ID_Venta INT,
            Fecha_pago DATE,
            Monto DECIMAL(10,2),
            FOREIGN KEY (ID_Venta) REFERENCES ventas(id)
        )
        """
        cursor.execute(crear_tabla)

        # Obtener la ruta del directorio actual del script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Ruta del archivo CSV (en el mismo directorio que el script)
        ruta_csv = os.path.join(script_dir, 'pagos.csv')

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
                id_pago = int(fila[0])
                id_venta = int(fila[1])
                fecha_pago = excel_date_to_date(float(fila[2])).strftime('%Y-%m-%d')
                monto = float(fila[3])

                # Consulta de inserción
                insertar = """
                INSERT INTO pagos (ID_Pago, ID_Venta, Fecha_pago, Monto)
                VALUES (%s, %s, %s, %s)
                """
                valores = (id_pago, id_venta, fecha_pago, monto)
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