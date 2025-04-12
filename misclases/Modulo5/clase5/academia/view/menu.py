from controllers.estudiantes_controller import EstudiantesController

class Menu:
    def __init__(self, controller):
        self.controller = controller

    def mostrar_menu(self):
        print("\n=== Sistema de Gestión Académica ===")
        print("1. Registrar estudiante")
        print("2. Listar estudiantes")
        print("3. Salir")
        return input("\nSeleccione una opción: ")

    def registrar_estudiante(self):
        print("\n=== Registro de Estudiante ===")
        nombre = input("Ingrese el nombre del estudiante: ")
        apellido = input("Ingrese el apellido del estudiante: ")
        correo = input("Ingrese el correo del estudiante: ")
        telefono = input("Ingrese el teléfono del estudiante: ")
        self.controller.registrar_estudiante(nombre, apellido, correo, telefono)

    def ejecutar(self):
        while True:
            opcion = self.mostrar_menu()
            
            if opcion == "1":
                self.registrar_estudiante()
            elif opcion == "2":
                self.controller.listar_estudiantes()
            elif opcion == "3":
                print("\nSaliendo del programa...")
                break
            else:
                print("\nOpción inválida. Por favor, seleccione una opción válida.")
