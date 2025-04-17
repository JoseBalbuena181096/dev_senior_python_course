from controllers.curso_controller import CursoController
from mysql.connector import IntegrityError

def menu_cursos(db):
    curso_controller = CursoController(db)

    while True:
        print("\n=== Sistema de Gestión de Cursos ===")
        print("1. Registrar curso")
        print("2. Listar cursos")
        print("3. Obtener curso por ID")
        print("4. Actualizar curso")
        print("5. Eliminar curso")
        print("6. Obtener cursos por profesor")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_curso(curso_controller)
        elif opcion == "2":
            listar_cursos(curso_controller)
        elif opcion == "3":
            obtener_curso_por_id(curso_controller)
        elif opcion == "4":
            actualizar_curso(curso_controller)
        elif opcion == "5":
            eliminar_curso(curso_controller)
        elif opcion == "6":
            obtener_cursos_por_profesor(curso_controller)
        elif opcion == "7":
            print("Gracias por usar el sistema de gestión de cursos")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

def registrar_curso(curso_controller):
    print("\n=== Registrar Curso ===")
    nombre = input("Ingrese el nombre del curso: ")
    descripcion = input("Ingrese la descripción del curso: ")
    duracion_horas = int(input("Ingrese la duración en horas: "))
    profesor_id = int(input("Ingrese el ID del profesor: "))

    try:
        curso_controller.registrar_curso(nombre, descripcion, duracion_horas, profesor_id)
        print("Curso registrado correctamente")
    except IntegrityError as e:
        print(f"Error de integridad: {e.msg}")
    except Exception as e:
        print(f"Error al registrar el curso: {str(e)}")

def listar_cursos(curso_controller):
    print("\n=== Listar Cursos ===")
    try:
        cursos = curso_controller.listar_cursos()
        if cursos:
            print("ID\tNombre\tDescripción\tDuración\tProfesor ID\tProfesor Nombre")
            for c in cursos:
                print(f"{c.id_curso}\t{c.nombre}\t{c.descripcion}\t{c.duracion_horas}\t{c.profesor_id}\t{c.nombre_profesor}")
        else:
            print("No se encontraron cursos registrados.")
    except Exception as e:
        print(f"Error al listar los cursos: {str(e)}")

def obtener_curso_por_id(curso_controller):
    print("\n=== Obtener Curso por ID ===")
    id_curso = int(input("Ingrese el ID del curso: "))
    try:
        curso = curso_controller.obtener_curso_por_id(id_curso)
        if curso:
            print(f"ID: {curso.id_curso}")
            print(f"Nombre: {curso.nombre}")
            print(f"Descripción: {curso.descripcion}")
            print(f"Duración (horas): {curso.duracion_horas}")
            print(f"ID Profesor: {curso.profesor_id}")
            print(f"Profesor Nombre: {curso.nombre_profesor}")
        else:
            print("No se encontró ningún curso con ese ID.")
    except Exception as e:
        print(f"Error al obtener el curso: {str(e)}")

def actualizar_curso(curso_controller):
    print("\n=== Actualizar Curso ===")
    id_curso = int(input("Ingrese el ID del curso: "))
    nombre = input("Ingrese el nombre del curso: ")
    descripcion = input("Ingrese la descripción del curso: ")
    duracion_horas = int(input("Ingrese la duración en horas: "))
    profesor_id = int(input("Ingrese el ID del profesor: "))

    try:
        curso_controller.actualizar_curso(id_curso, nombre, descripcion, duracion_horas, profesor_id)
        print("Curso actualizado correctamente")
    except Exception as e:
        print(f"Error al actualizar el curso: {str(e)}")

def eliminar_curso(curso_controller):
    print("\n=== Eliminar Curso ===")
    id_curso = int(input("Ingrese el ID del curso: "))
    try:
        curso_controller.eliminar_curso(id_curso)
        print("Curso eliminado correctamente")
    except Exception as e:
        print(f"Error al eliminar el curso: {str(e)}")

def obtener_cursos_por_profesor(curso_controller):
    print("\n=== Obtener Cursos por Profesor ===")
    profesor_id = int(input("Ingrese el ID del profesor: "))
    try:
        cursos = curso_controller.obtener_cursos_por_profesor(profesor_id)
        if cursos:
            print(f"\nCursos asignados al profesor ID {profesor_id}:")
            print("ID\tNombre\tDescripción\tDuración")
            for c in cursos:
                print(f"{c.id_curso}\t{c.nombre}\t{c.descripcion}\t{c.duracion_horas}")
        else:
            print(f"No se encontraron cursos asignados al profesor ID {profesor_id}")
    except Exception as e:
        print(f"Error al obtener los cursos del profesor: {str(e)}")
