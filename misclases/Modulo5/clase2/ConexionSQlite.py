import sqlite3
import os

# Get the directory where the script is running
current_directory = os.path.dirname(os.path.abspath(__file__))

# Create the database file path in the same directory
db_file_path = os.path.join(current_directory, "academiadevsenior.db")

# Configuration of connection
conexion = sqlite3.connect(db_file_path)

# Ejecutar una consulta sql 
cursor = conexion.cursor()
cursor.execute("SELECT * FROM profesores;")
resultados = cursor.fetchall() #Obtener todos los resultados

for fila in resultados:
    print(fila)

# # Ejecutar sentencias(INSERT) 
# query = "INSERT INTO Profesores(nombre,especialidad,experiencia) VALUES (?, ?, ?);"
# values = ('Jose Palma', "Mecatronico", 5)

# cursor.execute(query, values)
# # Ejecuta las consultas que alteran la base de datos
# conexion.commit()

# print(f"Fila insertada {cursor.rowcount}")

# Actualizar UPDATE
# query = "UPDATE Profesores SET experiencia = ? WHERE id=?;"
# values = (3, 1)
# cursor.execute(query, values)
# conexion.commit()

# print(f"Fila modificada {cursor.rowcount}")

query = "DELETE FROM Profesores WHERE id=?;";
values = (2,)
cursor.execute(query, values)
conexion.commit()

print(f"Fila eliminada {cursor.rowcount}")

# cerramos el cursor
cursor.close()
# Cerrar conexión
conexion.close()