import sqlite3

class DatabaseConnection:
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if not cls._instances:
            cls._instances = super(DatabaseConnection, cls).__new__(cls, *args, **kwargs)
            cls._instances.connection = None
        return cls._instances
    
    def connect(self, database_name):
        if self.connection is None:
            self.connection = sqlite3.Connection(database_name)
            print('Conectado a la base de datos')
        else:
            print('Ya existe una conexión activa')
        return self.connection
    
    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("La conexión cerrada")
            self.connection = None

db1 = DatabaseConnection()
db2 = DatabaseConnection()
connection1 = db1.connect('mi_base_de_datos.db')
connection2 = db2.connect('mi_base_de_datos2.db')
print(db2 is db1)

db1.close_connection()
db2.close_connection()