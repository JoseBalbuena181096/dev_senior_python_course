from config.conexion import DatabaseConnection
from controllers.estudiantes_controller import EstudiantesController
from view.menu import Menu

def main():
    # Crear la conexión a la base de datos
    db = DatabaseConnection()
    
    # Crear el controlador con la conexión
    controller = EstudiantesController(db)
    
    # Crear y ejecutar el menú
    menu = Menu(controller)
    menu.ejecutar()

if __name__ == "__main__":
    main()
