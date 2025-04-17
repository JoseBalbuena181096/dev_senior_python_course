from controllers.horario_controller import HorarioController
from mysql.connector import IntegrityError

def menu_horario(db):
    horario_controller = HorarioController(db)

    while True:
        print("\n=== Sistema de Gestión de Horarios ===")
        print("1. Registrar horario")
        print("2. Listar horarios")
        print("3. Obtener horario por ID")
        print("4. Actualizar horario")
        print("5. Eliminar horario")
        print("6. Obtener horarios por curso")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_horario(horario_controller)
        elif opcion == "2":
            listar_horarios(horario_controller)
        elif opcion == "3":
            obtener_horario_por_id(horario_controller)
        elif opcion == "4":
            actualizar_horario(horario_controller)
        elif opcion == "5":
            eliminar_horario(horario_controller)
        elif opcion == "6":
            obtener_horarios_por_curso(horario_controller)
        elif opcion == "7":
            print("Gracias por usar el sistema de gestión de horarios")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

def registrar_horario(horario_controller):
    print("\n=== Registrar Horario ===")
    curso_id = int(input("Ingrese el ID del curso: "))
    dia_semana = input("Ingrese el día de la semana: ")
    hora_inicio = input("Ingrese la hora de inicio (HH:MM:SS): ")
    hora_fin = input("Ingrese la hora de fin (HH:MM:SS): ")

    try:
        horario_controller.registrar_horario(curso_id, dia_semana, hora_inicio, hora_fin)
        print("Horario registrado correctamente")
    except IntegrityError as e:
        print(f"Error de integridad: {e.msg}")
    except Exception as e:
        print(f"Error al registrar el horario: {str(e)}")

def listar_horarios(horario_controller):
    print("\n=== Listar Horarios ===")
    try:
        horarios = horario_controller.listar_horarios()
        if horarios:
            print("ID\tCurso ID\tDía\tHora Inicio\tHora Fin\tNombre Curso")
            for h in horarios:
                print(f"{h.id_horario}\t{h.curso_id}\t{h.dia_semana}\t{h.hora_inicio}\t{h.hora_fin}\t{h.nombre_curso}")
        else:
            print("No se encontraron horarios registrados.")
    except Exception as e:
        print(f"Error al listar los horarios: {str(e)}")

def obtener_horario_por_id(horario_controller):
    print("\n=== Obtener Horario por ID ===")
    id_horario = int(input("Ingrese el ID del horario: "))
    try:
        horario = horario_controller.obtener_horario_por_id(id_horario)
        if horario:
            print(f"ID: {horario.id_horario}")
            print(f"ID Curso: {horario.curso_id}")
            print(f"Día: {horario.dia_semana}")
            print(f"Hora Inicio: {horario.hora_inicio}")
            print(f"Hora Fin: {horario.hora_fin}")
            print(f"Nombre Curso: {horario.nombre_curso}")
        else:
            print("No se encontró ningún horario con ese ID.")
    except Exception as e:
        print(f"Error al obtener el horario: {str(e)}")

def actualizar_horario(horario_controller):
    print("\n=== Actualizar Horario ===")
    id_horario = int(input("Ingrese el ID del horario: "))
    curso_id = int(input("Ingrese el ID del curso: "))
    dia_semana = input("Ingrese el día de la semana: ")
    hora_inicio = input("Ingrese la hora de inicio (HH:MM:SS): ")
    hora_fin = input("Ingrese la hora de fin (HH:MM:SS): ")

    try:
        horario_controller.actualizar_horario(id_horario, curso_id, dia_semana, hora_inicio, hora_fin)
        print("Horario actualizado correctamente")
    except Exception as e:
        print(f"Error al actualizar el horario: {str(e)}")

def eliminar_horario(horario_controller):
    print("\n=== Eliminar Horario ===")
    id_horario = int(input("Ingrese el ID del horario: "))
    try:
        horario_controller.eliminar_horario(id_horario)
        print("Horario eliminado correctamente")
    except Exception as e:
        print(f"Error al eliminar el horario: {str(e)}")

def obtener_horarios_por_curso(horario_controller):
    print("\n=== Obtener Horarios por Curso ===")
    curso_id = int(input("Ingrese el ID del curso: "))
    try:
        horarios = horario_controller.obtener_horarios_por_curso(curso_id)
        if horarios:
            print(f"\nHorarios del curso ID {curso_id}:")
            print("ID\tDía\tHora Inicio\tHora Fin\tNombre Curso")
            for h in horarios:
                print(f"{h.id_horario}\t{h.dia_semana}\t{h.hora_inicio}\t{h.hora_fin}\t{h.nombre_curso}")
        else:
            print(f"No se encontraron horarios para el curso ID {curso_id}")
    except Exception as e:
        print(f"Error al obtener los horarios del curso: {str(e)}")
