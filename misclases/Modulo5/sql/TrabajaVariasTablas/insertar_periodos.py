import mysql.connector
import csv
import os
from datetime import datetime

# Configuración de la conexión a MySQL
config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'db_practica1'
}

# Diccionario de meses en español a inglés
meses_es_en = {
    'ene': 'jan', 'feb': 'feb', 'mar': 'mar', 'abr': 'apr',
    'may': 'may', 'jun': 'jun', 'jul': 'jul', 'ago': 'aug',
    'sep': 'sep', 'oct': 'oct', 'nov': 'nov', 'dic': 'dec'
}

def convertir_fecha_espanol_a_ingles(fecha_str):
    # Dividir la fecha en día, mes y año
    dia, mes, anio = fecha_str.split('-')
    # Convertir el mes al formato en inglés
    mes_en = meses_es_en[mes.lower()]
    # Reconstruir la fecha en formato inglés
    return f"{dia}-{mes_en}-{anio}"

def crear_schema_periodos():
    try:
        conexion = mysql.connector.connect(**config)
        cursor = conexion.cursor()
        
        # Crear schema periodos si no existe
        cursor.execute("CREATE SCHEMA IF NOT EXISTS periodos")
        
        # Crear tabla periodo1
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS periodos.periodo1 (
            Fecha DATE,
            ID_Empleado INT,
            Local VARCHAR(1),
            Turno_completo VARCHAR(2)
        )
        """)
        
        # Crear tabla periodo2
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS periodos.periodo2 (
            Fecha DATE,
            ID_Empleado INT,
            Local VARCHAR(1),
            Turno_completo VARCHAR(2)
        )
        """)
        
        conexion.commit()
        print("Schema y tablas creados correctamente")
        
    except mysql.connector.Error as error:
        print(f"Error al crear schema y tablas: {error}")
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()

def insertar_datos_periodo(archivo_csv, nombre_tabla):
    try:
        conexion = mysql.connector.connect(**config)
        cursor = conexion.cursor()
        
        # Ruta del archivo CSV
        ruta_csv = os.path.join(os.path.dirname(__file__), archivo_csv)
        
        # Leer y insertar datos del CSV
        with open(ruta_csv, 'r', encoding='utf-8') as archivo:
            lector_csv = csv.reader(archivo)
            next(lector_csv)  # Saltar la cabecera
            
            for fila in lector_csv:
                # Convertir la fecha al formato correcto
                fecha_ingles = convertir_fecha_espanol_a_ingles(fila[0])
                fecha = datetime.strptime(fecha_ingles, '%d-%b-%y').strftime('%Y-%m-%d')
                id_empleado = int(fila[1])
                local = fila[2]
                turno_completo = fila[3]
                
                # Consulta de inserción
                insertar = f"""
                INSERT INTO periodos.{nombre_tabla} (Fecha, ID_Empleado, Local, Turno_completo)
                VALUES (%s, %s, %s, %s)
                """
                valores = (fecha, id_empleado, local, turno_completo)
                cursor.execute(insertar, valores)
        
        conexion.commit()
        print(f"Datos insertados correctamente en la tabla {nombre_tabla}")
        
    except mysql.connector.Error as error:
        print(f"Error al insertar datos en {nombre_tabla}: {error}")
    except Exception as e:
        print(f"Error al procesar el archivo {archivo_csv}: {str(e)}")
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()

if __name__ == "__main__":
    # Crear schema y tablas
    crear_schema_periodos()
    
    # Insertar datos de periodo1
    insertar_datos_periodo('periodo1.csv', 'periodo1')
    
    # Insertar datos de periodo2
    insertar_datos_periodo('periodo2.csv', 'periodo2') 