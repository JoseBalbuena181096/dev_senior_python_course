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
        CREATE TABLE IF NOT EXISTS productos (
            ID_Producto INT PRIMARY KEY,
            Producto VARCHAR(50)
        )
        """
        cursor.execute(crear_tabla)

        # Obtener la ruta del directorio actual del script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Ruta del archivo CSV (en el mismo directorio que el script)
        ruta_csv = os.path.join(script_dir, 'producto.csv')

        # Verificar si el archivo existe
        if not os.path.isfile(ruta_csv):
            print(f"Error: No se encontró el archivo {ruta_csv}")
            print(f"Directorio actual: {script_dir}")
            print(f"Contenido del directorio: {os.listdir(script_dir)}")
            return

        # Leer y insertar datos del CSV
        with open(ruta_csv, 'r', encoding='utf-8') as archivo:
            lector_csv = csv.reader(archivo)
            cabecera = next(lector_csv)  # Saltar la cabecera
            print(f"Columnas en el CSV: {cabecera}")
            
            for i, fila in enumerate(lector_csv, 1):
                try:
                    print(f"Procesando fila {i}: {fila}")
                    id_producto = int(fila[0])
                    producto = fila[1]

                    # Consulta de inserción
                    insertar = """
                    INSERT INTO productos (ID_Producto, Producto)
                    VALUES (%s, %s)
                    """
                    valores = (id_producto, producto)
                    cursor.execute(insertar, valores)
                except IndexError as e:
                    print(f"Error en la fila {i}: {fila}")
                    print(f"Error: {str(e)}")
                    continue
                except Exception as e:
                    print(f"Error en la fila {i}: {fila}")
                    print(f"Error: {str(e)}")
                    continue

        # Confirmar los cambios
        conexion.commit()
        print("Datos de productos insertados correctamente")

    except mysql.connector.Error as error:
        print(f"Error al insertar datos: {error}")
    
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()
            print("Conexión cerrada")

if __name__ == "__main__":
    insertar_datos() 