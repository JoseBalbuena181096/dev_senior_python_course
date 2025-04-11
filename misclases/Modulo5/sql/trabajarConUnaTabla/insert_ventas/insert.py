import csv
import mysql.connector
import os

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
        
        # Preparar la consulta SQL para insertar datos
        insert_query = """
        INSERT INTO Ventas (Fecha, ID_local, clave_producto, venta, venta_empleado) 
        VALUES (%s, %s, %s, %s, %s)
        """
        
        # Leer el archivo CSV y procesar cada fila
        with open(csv_path, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)  # Saltar la cabecera
            
            for row in csv_reader:
                # Convertir la fecha del formato español dd-mmm-yy a formato MySQL yyyy-mm-dd
                fecha_str = row[0]
                try:
                    # Mapeo de nombres de meses en español a números
                    meses = {
                        'ene': '01', 'feb': '02', 'mar': '03', 'abr': '04',
                        'may': '05', 'jun': '06', 'jul': '07', 'ago': '08',
                        'sep': '09', 'oct': '10', 'nov': '11', 'dic': '12'
                    }
                    
                    # Separar día, mes y año
                    dia, mes_abr, anio = fecha_str.split('-')
                    mes = meses[mes_abr.lower()]
                    
                    # Añadir el '20' al inicio del año si tiene dos dígitos
                    if len(anio) == 2:
                        anio = '20' + anio
                        
                    # Formatear la fecha para MySQL (yyyy-mm-dd)
                    fecha_mysql = f"{anio}-{mes}-{dia.zfill(2)}"
                except Exception as e:
                    print(f"Error al procesar la fecha '{fecha_str}': {e}")
                    continue
                
                # Preparar los datos para inserción
                data = (
                    fecha_mysql,
                    int(row[1]),  # ID_local
                    row[2],       # clave_producto
                    int(row[3]),  # venta
                    int(row[4])   # venta_empleado
                )
                
                try:
                    cursor.execute(insert_query, data)
                except mysql.connector.Error as err:
                    print(f"Error al insertar fila {row}: {err}")
                    # Continuar con la siguiente fila en caso de error
        
        # Confirmar los cambios y cerrar la conexión
        conn.commit()
        print(f"Datos insertados correctamente en la tabla Ventas")
        
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
    'database': 'Index'
}

# Ejecutar la función
if __name__ == "__main__":
    # Obtener la ruta absoluta del script actual
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construir la ruta absoluta al archivo CSV
    csv_path = os.path.join(script_dir, 'ventas_idx.csv')
    
    print(f"Buscando archivo en: {csv_path}")
    insert_ventas_data(csv_path, db_config)