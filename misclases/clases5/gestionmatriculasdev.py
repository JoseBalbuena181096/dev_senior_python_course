estudiantes = []
cursos = ['Java', 'Python']
docentes = []
horarios = []

# función para matricular un estudiante
def matricularEstudiante():
    nombre = input('Ingrese el nombre del estudiante:\n')

    print("Seleccione el curso a matricular")
    for i, curso in enumerate(cursos):
        print(f'{i+1} : {curso}')
    
    cursoSeleccionado = int(input("Ingrese el numero del curso: \n"))
    if cursoSeleccionado > 0 and cursoSeleccionado <= len(cursos):
        curso = cursos[cursoSeleccionado - 1]
        estudiante = {'nombre': nombre, 'curso': curso}
        estudiantes.append(estudiante)
        print(f'Estudiante : {nombre} , matriculado en el curso {curso}')

    else:
        print(f'Opcion de curso invalida, solo tenemos {len(cursos)} cursos')

# funcion para asignar un docente a curso

def asignarDocente():
    print('Seleccione el curso al que se desea asignar un curso: ')
    for i, curso in enumerate(cursos):
        print(f'{i+1} : {curso}')

    cursoSeleccionado = int(input("Ingrese el numero del curso: "))
    if cursoSeleccionado > 0 and cursoSeleccionado <= len(cursos):
        curso = cursos[cursoSeleccionado - 1]
        nombreDocente = input('Ingrese nombre del docente: ')
        docente = {'nombre': nombreDocente, 'curso': curso}
        docentes.append(docente)
        print(f"Docente {nombreDocente}, asignado al curso {curso}")
    else:
        print(f'Opcion de curso invalida, solo tenemos {len(cursos)} cursos')
    

#funcion para asignar un horario a un curso
def asignarHorario():
    print('Seleccione el curso al que se desea asignar un horario: ')
    for i, curso in enumerate(cursos):
        print(f'{i+1} : {curso}')
    cursoSeleccionado = int(input("Ingrese el numero del curso: "))
    if cursoSeleccionado > 0 and cursoSeleccionado <= len(cursos):
        curso = cursos[cursoSeleccionado - 1]
        dias = input("Ingrese los dias de clase (ej: martes y jueves): ")
        hora = input("Ingrese la hora de la clase (ej: 6pm): ")
        horario = {'curso': curso, 'dias': dias, 'hora':hora}
        horarios.append(horario)
        print(f'Horario asignado al curso: {curso},  {dias} a las horas {hora}')
    else:
        print(f'Opcion de curso invalida, solo tenemos {len(cursos)} cursos')

def mostrarEstudiantes():
    if estudiantes:
        print('lista de estudiantes matriculados: ')
        for estudiante in estudiantes:
            print(f'Estudiante: {estudiante['nombre']}, curso {estudiante['curso']}')
    else:
        print('No tenemos estudiantes matriculados')

def mostrarDocentes():
    if docentes:
        print('lista de docentes asignados: ')
        for docente in docentes:
            print(f'Docente: {docente['nombre']}, curso {docente['curso']}')
    else:
        print('No tenemos docentes asignados')


def mostrarHorarios():
    if horarios:
        print('\nHorarios del los cursos: ')
        for horario in horarios:
            print(f'Curso: {horario['curso']}, Dias: {horario['dia']}, hora: {horario['hora']}')
    else:
        print('No tenemos horarios asignados')


while True:
    print('\nSistema de matricula de Dev senior ')
    print('\n1. Matricular estudiante ')
    print('\n2. Asignar docente a un curso ')
    print('\n3. Asignar horario a un curso ')
    print('\n4. Mostrar la lista de estudiantes matriculados ')
    print('\n5. Mostrar la lista de docentes asignados ')
    print('\n6. Mostrar horarios asignados ')
    print('\n7. Salir')

    opcion = int(input('digite la opcion: '))
    if opcion == 1:
        matricularEstudiante()
    elif opcion == 2:
        asignarDocente()
    elif opcion == 3:
        asignarHorario()
    elif opcion == 4:
        mostrarEstudiantes()
    elif opcion == 5:
        mostrarDocentes()
    elif opcion == 6:
        mostrarHorarios()
    elif opcion == 7:
        print('Fin del programa hasta pronto')
        break
    else:
        print('Seleccione una opcion correcta')
    


    
    


    

    
    


        
