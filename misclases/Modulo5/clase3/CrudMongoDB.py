from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId

uri = "mongodb+srv://admin:181096@cluster0.exci0ju.mongodb.net/?appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection

# Elegir una base de datos
db = client["mi_base"]
coleccion = db["usuarios"]

# Crear un usuario
def crear_usuario(nombre, edad, direccion):
    coleccion.insert_one({
            "nombre": nombre,
            "edad": edad,
            "direccion": direccion
        })
    print("Usuario creado")


def mostrar_usuarios():
    usuarios = coleccion.find()
    for usuario in usuarios:
        print(usuario)

def actualizar_usuario(id_str, nombre, edad, direccion):
    nuevos_datos = {}
    if nombre: nuevos_datos["nombre"] = nombre
    if edad: nuevos_datos["edad"] = edad    
    if direccion: nuevos_datos["direccion"] = direccion

    if not nuevos_datos:
        print("No se proporcionaron datos para actualizar")
        return

    
    query = {"_id": ObjectId(id_str)}  # Find user by username
    reultado = coleccion.update_one(
        query,
        {"$set": nuevos_datos}  # Update user with new data
    )

    if reultado.modified_count > 0:
        print("Usuario actualizado")

def eliminar_ir_id(id_str):
    coleccion.delete_one({"_id": ObjectId(id_str)})
    print("Usuario eliminado")

def buscar_por_direccion(direccion):
    resultado = coleccion.find({"direccion": direccion})
    for usuario in resultado:
        print(usuario)

def buscar_por_direccion_edad(direccion, edad):
    resultado = coleccion.find({
        "$and": [
            {"direccion": direccion},
            {"edad": edad}
        ]
    })
    for usuario in resultado:
        print(usuario)

def buscar_edad_entre_rango(edad_min, edad_max):
    resultado = coleccion.find({
        "$and": [
            {"edad": {"$gte": edad_min}},
            {"edad": {"$lte": edad_max}}
        ]
    })
    for usuario in resultado:
        print(usuario)

def buscar_direccion_(ciudad1, ciudad2):
    resultado = coleccion.find({
        '$or': [
            {'direccion': ciudad1},
            {'direccion': ciudad2}
        ]
    })
    for usuario in resultado:
        print(usuario)

def contar_mexico():
    resultado = coleccion.count_documents({'direccion': 'Mexico'})
    print(f"Total de usuarios en Mexico: {resultado}")

# buscar_edad_entre_rango(10,30)
crear_usuario("Pedro Lopez", 30, "Mexico")
contar_mexico()

# crear_usuario("Pedro Lopez", 30, "Calle 1234")
# actualizar_usuario('67ef45b21f6d1df718048922', 'Juan Dominguez', 24, 'Calle 1222')

# eliminar_ir_id('67ef45b21f6d1df718048922')
# mostrar_usuarios()


# { "nombre": "Juan Pérez", "edad": 25, "direccion": "Avenida Reforma 567" }
# { "nombre": "María González", "edad": 32, "direccion": "Calle Juárez 890" }
# { "nombre": "Luis Ramírez", "edad": 40, "direccion": "Boulevard Insurgentes 123" }
# { "nombre": "Ana Torres", "edad": 28, "direccion": "Calle Morelos 456" }
# { "nombre": "Carlos Mendoza", "edad": 35, "direccion": "Avenida Universidad 789" }
# { "nombre": "Sofía Herrera", "edad": 22, "direccion": "Calle Independencia 321" }
# { "nombre": "Jorge Castillo", "edad": 29, "direccion": "Carrera 7 #45-23" }
# { "nombre": "Elena Rojas", "edad": 31, "direccion": "Paseo de la Reforma 101" }
# { "nombre": "Fernando López", "edad": 37, "direccion": "Avenida Central 505" }
# { "nombre": "Gabriela Sánchez", "edad": 27, "direccion": "Calle Hidalgo 678" }
# { "nombre": "Ricardo Núñez", "edad": 45, "direccion": "Plaza Mayor 900" }
# { "nombre": "Patricia Vargas", "edad": 33, "direccion": "Calle 5 de Mayo 234" }
# { "nombre": "Miguel Ángel Domínguez", "edad": 38, "direccion": "Carretera Nacional 567" }
# { "nombre": "Verónica Fernández", "edad": 30, "direccion": "Callejón del Beso 12" }
# { "nombre": "Eduardo Salinas", "edad": 26, "direccion": "Calle 20 de Noviembre 111" }
# { "nombre": "Alejandra Paredes", "edad": 34, "direccion": "Avenida del Sol 77" }
# { "nombre": "Francisco Ortega", "edad": 42, "direccion": "Calle Primavera 456" }
# { "nombre": "Lorena Díaz", "edad": 29, "direccion": "Avenida Libertad 654" }
# { "nombre": "Raúl Gutiérrez", "edad": 36, "direccion": "Callejón San Pedro 88" }
# { "nombre": "Isabel Romero", "edad": 39, "direccion": "Boulevard del Mar 999" }
