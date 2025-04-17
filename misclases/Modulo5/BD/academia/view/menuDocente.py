from controllers.docenteController import DocenteController
from mysql.connector import IntegrityError

def menu_docente(db):
    docente_controller = DocenteController(db)

    while True:
        print("\n=== Sistema de Gestión de Docentes ===")
        print("1. Registrar docente")
        print("2. Listar docentes")
        print("3. Obtener docente por ID")
        print("4. Actualizar docente")
        print("5. Eliminar docente")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_docente(docente_controller)
        elif opcion == "2":
            listar_docentes(docente_controller)
        elif opcion == "3":
            obtener_docente_por_id(docente_controller)
        elif opcion == "4":
            actualizar_docente(docente_controller)
        elif opcion == "5":
            eliminar_docente(docente_controller)
        elif opcion == "6":
            print("Gracias por usar el sistema de gestión de docentes")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

def registrar_docente(docente_controller):
    print("\n=== Registrar Docente ===")
    nombre = input("Ingrese el nombre del docente: ")
    apellido = input("Ingrese el apellido del docente: ")
    correo = input("Ingrese el correo electrónico del docente: ")
    telefono = input("Ingrese el teléfono del docente: ")
    especialidad = input("Ingrese la especialidad del docente: ")

    try:
        docente_controller.registrar_docente(nombre, apellido, correo, telefono, especialidad)
        print("Docente registrado correctamente")
    except IntegrityError as e:
        print(f"Error de integridad: {e.msg}")
    except Exception as e:
        print(f"Error al registrar el docente: {str(e)}")

def listar_docentes(docente_controller):
    print("\n=== Listar Docentes ===")
    try:
        docentes = docente_controller.listar_docentes()
        if docentes:
            print("ID\tNombre\tApellido\tCorreo\tTeléfono\tEspecialidad")
            for d in docentes:
                print(f"{d.id_profesor}\t{d.nombre}\t{d.apellido}\t{d.correo_electronico}\t{d.telefono}\t{d.especialidad}")
        else:
            print("No se encontraron docentes registrados.")
    except Exception as e:
        print(f"Error al listar los docentes: {str(e)}")

def obtener_docente_por_id(docente_controller):
    print("\n=== Obtener Docente por ID ===")
    id_docente = input("Ingrese el ID del docente: ")
    try:
        docente = docente_controller.obtener_docente_por_id(id_docente)
        if docente:
            print(f"ID: {docente.id_profesor}")
            print(f"Nombre: {docente.nombre}")
            print(f"Apellido: {docente.apellido}")
            print(f"Correo: {docente.correo_electronico}")
            print(f"Teléfono: {docente.telefono}")
            print(f"Especialidad: {docente.especialidad}")
        else:
            print("No se encontró ningún docente con ese ID.")
    except Exception as e:
        print(f"Error al obtener el docente: {str(e)}")

def actualizar_docente(docente_controller):
    print("\n=== Actualizar Docente ===")
    id_docente = input("Ingrese el ID del docente: ")
    nombre = input("Ingrese el nombre del docente: ")
    apellido = input("Ingrese el apellido del docente: ")
    correo = input("Ingrese el correo electrónico del docente: ")
    telefono = input("Ingrese el teléfono del docente: ")
    especialidad = input("Ingrese la especialidad del docente: ")

    try:
        docente_controller.actualizar_docente(id_docente, nombre, apellido, correo, telefono, especialidad)
        print("Docente actualizado correctamente")
    except Exception as e:
        print(f"Error al actualizar el docente: {str(e)}")

def eliminar_docente(docente_controller):
    print("\n=== Eliminar Docente ===")
    id_docente = input("Ingrese el ID del docente: ")
    try:
        docente_controller.eliminar_docente(id_docente)
        print("Docente eliminado correctamente")
    except Exception as e:
        print(f"Error al eliminar el docente: {str(e)}")
