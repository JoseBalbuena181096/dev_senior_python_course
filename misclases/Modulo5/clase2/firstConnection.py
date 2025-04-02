import mysql.connector

# Configuracion de conexion
conexion = mysql.connector.connect(
    host = "127.0.0.1", # "localhost"
    port = 3306,
    user = "root",
    password = "root",
    database = "academiadevsenior"
)

# Verficamos la conexion
if conexion.is_connected():
    print("Connectado a MySQL")

# Ejecutar una consulta sql 
cursor = conexion.cursor()
cursor.execute("SELECT * FROM profesores;")
resultados = cursor.fetchall() #Obtener todos los resultados

for fila in resultados:
    print(fila)

# Ejecutar sentencias(INSERT) 
# query = "INSERT INTO Profesores(nombre,especialidad,experiencia) VALUES (%s, %s, %s);"
# values = ('Jose Palma', "Mecatronico", 5)

# cursor.execute(query, values)
# # Ejecuta las consultas que alteran la base de datos
# conexion.commit()

# print(f"Fila insertada {cursor.rowcount}")

# Actualizar UPDATE
# query = "UPDATE Profesores SET experiencia = %s WHERE id=%s"
# values = (10, 12)
# cursor.execute(query, values)
# conexion.commit()

# print(f"Fila modificada {cursor.rowcount}")

query = "DELETE FROM Profesores WHERE id=%s;";
values = (12,)
cursor.execute(query, values)
conexion.commit()

print(f"Fila eliminada {cursor.rowcount}")

# cerramos el cursor
cursor.close()
# Cerrar conexión
conexion.close()



