import csv
import mysql.connector
import os

def create_table(cursor):
    """
    Crea la tabla ventas si no existe
    """
    create_table_query = """
    CREATE TABLE IF NOT EXISTS ventas (
        id INT AUTO_INCREMENT PRIMARY KEY,
        fecha_venta DATE NOT NULL,
        id_producto INT NOT NULL,
        id_zona INT NOT NULL,
        venta DECIMAL(10,2) NOT NULL,
        id_vendedor INT NOT NULL,
        id_cliente INT NOT NULL
    );
    """
    cursor.execute(create_table_query)
    print("Tabla 'ventas' creada o ya existente")

def insert_ventas_data(csv_path, db_config):
    """
    Inserta datos desde un archivo CSV a la tabla Ventas en MySQL
    
    Args:
        csv_path: Ruta al archivo CSV de ventas
        db_config: Diccionario con la configuración de la base de datos
    """
    try:
        # Verificar si el archivo existe
        if not os.path.isfile(csv_path):
            print(f"El archivo {csv_path} no existe en la ruta especificada.")
            print(f"Directorio actual: {os.getcwd()}")
            print(f"Contenido del directorio: {os.listdir('.')}")
            return
            
        # Conectar a la base de datos
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        # Crear la tabla si no existe
        create_table(cursor)
        
        # Preparar la consulta SQL para insertar datos
        insert_query = """
        INSERT INTO ventas (fecha_venta, id_producto, id_zona, venta, id_vendedor, id_cliente)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        
        # Leer el archivo CSV y procesar cada fila
        with open(csv_path, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)  # Saltar la cabecera
            
            rows_inserted = 0
            rows_failed = 0
            
            for i, row in enumerate(csv_reader):
                try:
                    # Verificar que la fila tenga suficientes columnas
                    if len(row) < 7:
                        print(f"Advertencia: Fila {i+2} incompleta, saltando. Contenido: {row}")
                        rows_failed += 1
                        continue

                    # La fecha ya está en formato YYYY-MM-DD (índice 1)
                    fecha_mysql = row[1]
                    
                    # Preparar los datos para inserción (ajustar índices y tipos)
                    data = (
                        fecha_mysql,       # fecha_venta (índice 1)
                        int(row[2]),       # id_producto (índice 2)
                        int(row[3]),       # id_zona (índice 3)
                        float(row[4]),     # venta (índice 4)
                        int(row[5]),       # id_vendedor (índice 5)
                        int(row[6])        # id_cliente (índice 6)
                    )
                    
                    cursor.execute(insert_query, data)
                    rows_inserted += 1
                except ValueError as ve:
                    print(f"Error de conversión de tipo en fila {i+2}: {ve}. Fila: {row}")
                    rows_failed += 1
                    continue # Saltar a la siguiente fila
                except mysql.connector.Error as err:
                    print(f"Error de MySQL al insertar fila {i+2}: {err}. Fila: {row}")
                    rows_failed += 1
                    # Considerar si detenerse o continuar
                except Exception as e:
                    print(f"Error inesperado procesando fila {i+2}: {e}. Fila: {row}")
                    rows_failed += 1
                    continue # Saltar a la siguiente fila
        
        # Confirmar los cambios si hubo inserciones exitosas
        if rows_inserted > 0:
            conn.commit()
            print(f"Proceso completado.")
            print(f"Filas insertadas correctamente: {rows_inserted}")
            print(f"Filas con errores: {rows_failed}")
        else:
            print("No se insertaron filas. Verifique los errores anteriores o el archivo CSV.")
            if rows_failed > 0:
                 print(f"Total de filas con errores: {rows_failed}")
            conn.rollback() # Revertir si no hubo inserciones o solo errores
        
    except mysql.connector.Error as err:
        print(f"Error de conexión a MySQL: {err}")
    except FileNotFoundError:
        print(f"Error: El archivo {csv_path} no fue encontrado.")
    except Exception as e:
        print(f"Error general: {e}")
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()
            print("Conexión a MySQL cerrada")

# Configuración de la base de datos
db_config = {
    'host': 'localhost',
    'user': 'root',     # Cambia esto por tu usuario de MySQL
    'password': 'root', # Cambia esto por tu contraseña de MySQL
    'database': 'db_practica1' # Asegúrate que esta es la base de datos correcta
}

# Ejecutar la función
if __name__ == "__main__":
    # Obtener la ruta absoluta del script actual
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construir la ruta absoluta al archivo CSV
    csv_path = os.path.join(script_dir, 'ventas_idx.csv') 
    
    print(f"Buscando archivo CSV en: {csv_path}")
    insert_ventas_data(csv_path, db_config)