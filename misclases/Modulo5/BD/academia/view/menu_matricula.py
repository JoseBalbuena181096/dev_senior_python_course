from controllers.matricula_controller import MatriculaController
from mysql.connector import IntegrityError

def menu_matricula(db):
    matricula_controller = MatriculaController(db)

    while True:
        print("\n=== Sistema de Gestión de Matrículas ===")
        print("1. Registrar matrícula")
        print("2. Listar matrículas")
        print("3. Obtener matrícula por ID")
        print("4. Actualizar matrícula")
        print("5. Eliminar matrícula")
        print("6. Obtener matrículas por estudiante")
        print("7. Obtener matrículas por curso")
        print("8. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_matricula(matricula_controller)
        elif opcion == "2":
            listar_matriculas(matricula_controller)
        elif opcion == "3":
            obtener_matricula_por_id(matricula_controller)
        elif opcion == "4":
            actualizar_matricula(matricula_controller)
        elif opcion == "5":
            eliminar_matricula(matricula_controller)
        elif opcion == "6":
            obtener_matriculas_por_estudiante(matricula_controller)
        elif opcion == "7":
            obtener_matriculas_por_curso(matricula_controller)
        elif opcion == "8":
            print("Gracias por usar el sistema de gestión de matrículas")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

def registrar_matricula(matricula_controller):
    print("\n=== Registrar Matrícula ===")
    estudiante_id = int(input("Ingrese el ID del estudiante: "))
    curso_id = int(input("Ingrese el ID del curso: "))
    fecha_matricula = input("Ingrese la fecha de matrícula (YYYY-MM-DD): ")

    try:
        matricula_controller.registrar_matricula(estudiante_id, curso_id, fecha_matricula)
        print("Matrícula registrada correctamente")
    except ValueError as e:
        print(f"Error: {str(e)}")
        print("Por favor, verifique que el ID del curso sea correcto.")
    except IntegrityError as e:
        print(f"Error de integridad: {e.msg}")
        print("Por favor, verifique que los IDs del estudiante y curso sean correctos.")
    except Exception as e:
        print(f"Error al registrar la matrícula: {str(e)}")

def listar_matriculas(matricula_controller):
    print("\n=== Listar Matrículas ===")
    try:
        matriculas = matricula_controller.listar_matriculas()
        if matriculas:
            print("ID\tEstudiante ID\tCurso ID\tFecha\tNombre Estudiante\tNombre Curso")
            for m in matriculas:
                print(f"{m.id_matricula}\t{m.estudiante_id}\t{m.curso_id}\t{m.fecha_matricula}\t{m.nombre_estudiante}\t{m.nombre_curso}")
        else:
            print("No se encontraron matrículas registradas.")
    except Exception as e:
        print(f"Error al listar las matrículas: {str(e)}")

def obtener_matricula_por_id(matricula_controller):
    print("\n=== Obtener Matrícula por ID ===")
    id_matricula = int(input("Ingrese el ID de la matrícula: "))
    try:
        matricula = matricula_controller.obtener_matricula_por_id(id_matricula)
        if matricula:
            print(f"ID: {matricula.id_matricula}")
            print(f"ID Estudiante: {matricula.estudiante_id}")
            print(f"ID Curso: {matricula.curso_id}")
            print(f"Fecha: {matricula.fecha_matricula}")
            print(f"Nombre Estudiante: {matricula.nombre_estudiante}")
            print(f"Nombre Curso: {matricula.nombre_curso}")
        else:
            print("No se encontró ninguna matrícula con ese ID.")
    except Exception as e:
        print(f"Error al obtener la matrícula: {str(e)}")

def actualizar_matricula(matricula_controller):
    print("\n=== Actualizar Matrícula ===")
    id_matricula = int(input("Ingrese el ID de la matrícula: "))
    estudiante_id = int(input("Ingrese el ID del estudiante: "))
    curso_id = int(input("Ingrese el ID del curso: "))
    fecha_matricula = input("Ingrese la fecha de matrícula (YYYY-MM-DD): ")

    try:
        matricula_controller.actualizar_matricula(id_matricula, estudiante_id, curso_id, fecha_matricula)
        print("Matrícula actualizada correctamente")
    except Exception as e:
        print(f"Error al actualizar la matrícula: {str(e)}")

def eliminar_matricula(matricula_controller):
    print("\n=== Eliminar Matrícula ===")
    id_matricula = int(input("Ingrese el ID de la matrícula: "))
    try:
        matricula_controller.eliminar_matricula(id_matricula)
        print("Matrícula eliminada correctamente")
    except Exception as e:
        print(f"Error al eliminar la matrícula: {str(e)}")

def obtener_matriculas_por_estudiante(matricula_controller):
    print("\n=== Obtener Matrículas por Estudiante ===")
    estudiante_id = int(input("Ingrese el ID del estudiante: "))
    try:
        matriculas = matricula_controller.obtener_matriculas_por_estudiante(estudiante_id)
        if matriculas:
            print(f"\nMatrículas del estudiante ID {estudiante_id}:")
            print("ID\tCurso ID\tFecha\tNombre Curso")
            for m in matriculas:
                print(f"{m.id_matricula}\t{m.curso_id}\t{m.fecha_matricula}\t{m.nombre_curso}")
        else:
            print(f"No se encontraron matrículas para el estudiante ID {estudiante_id}")
    except Exception as e:
        print(f"Error al obtener las matrículas del estudiante: {str(e)}")

def obtener_matriculas_por_curso(matricula_controller):
    print("\n=== Obtener Matrículas por Curso ===")
    curso_id = int(input("Ingrese el ID del curso: "))
    try:
        matriculas = matricula_controller.obtener_matriculas_por_curso(curso_id)
        if matriculas:
            print(f"\nMatrículas del curso ID {curso_id}:")
            print("ID\tEstudiante ID\tFecha\tNombre Estudiante")
            for m in matriculas:
                print(f"{m.id_matricula}\t{m.estudiante_id}\t{m.fecha_matricula}\t{m.nombre_estudiante}")
        else:
            print(f"No se encontraron matrículas para el curso ID {curso_id}")
    except Exception as e:
        print(f"Error al obtener las matrículas del curso: {str(e)}")
