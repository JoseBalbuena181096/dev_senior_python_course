from controllers.docenteController import DocenteController
from mysql.connector import IntegrityError

def menu_docente(db):
    docente_controller = DocenteController(db)

    while True:
        print("\n=== Menú de Gestión de Profesores ===")
        print("1. Registrar profesor")
        print("2. Listar profesores")
        print("3. Obtener profesor por ID")
        print("4. Actualizar profesor")
        print("5. Eliminar profesor")
        print("6. Volver al menú principal")
        
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
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

def registrar_docente(docente_controller):
    print("\n============ Registrar Profesor =============")
    nombre = input("Ingrese el nombre del profesor: ")
    apellido = input("Ingrese el apellido del profesor: ")
    correo = input("Ingrese el correo electrónico del profesor: ")
    telefono = input("Ingrese el teléfono del profesor: ")
    especialidad = input("Ingrese la especialidad del profesor: ")

    try:
        docente_controller.registrar_docente(nombre, apellido, correo, telefono, especialidad)
        print("Profesor registrado correctamente")
    except IntegrityError as e:
        print(f"Error de integridad: {e.msg}")
    except Exception as e:
        print(f"Error al registrar el profesor: {str(e)}")

def listar_docentes(docente_controller):
    print("\n============ Listar Profesores =============")
    try:
        docentes = docente_controller.listar_docentes()
        if docentes:
            print("ID\tNombre\tApellido\tCorreo\tTeléfono\tEspecialidad")
            for d in docentes:
                print(f"{d.id_profesor}\t{d.nombre}\t{d.apellido}\t{d.correo_electronico}\t{d.telefono}\t{d.especialidad}")
        else:
            print("No se encontraron profesores registrados.")
    except Exception as e:
        print(f"Error al listar los profesores: {str(e)}")

def obtener_docente_por_id(docente_controller):
    print("\n============ Obtener Profesor por ID =============")
    id_docente = input("Ingrese el ID del profesor: ")
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
            print("No se encontró ningún profesor con ese ID.")
    except Exception as e:
        print(f"Error al obtener el profesor: {str(e)}")

def actualizar_docente(docente_controller):
    print("\n============ Actualizar Profesor =============")
    id_docente = input("Ingrese el ID del profesor: ")
    nombre = input("Ingrese el nombre del profesor: ")
    apellido = input("Ingrese el apellido del profesor: ")
    correo = input("Ingrese el correo electrónico del profesor: ")
    telefono = input("Ingrese el teléfono del profesor: ")
    especialidad = input("Ingrese la especialidad del profesor: ")

    try:
        docente_controller.actualizar_docente(id_docente, nombre, apellido, correo, telefono, especialidad)
        print("Profesor actualizado correctamente")
    except Exception as e:
        print(f"Error al actualizar el profesor: {str(e)}")

def eliminar_docente(docente_controller):
    print("\n============ Eliminar Profesor =============")
    id_docente = input("Ingrese el ID del profesor: ")
    try:
        docente_controller.eliminar_docente(id_docente)
        print("Profesor eliminado correctamente")
    except Exception as e:
        print(f"Error al eliminar el profesor: {str(e)}")
