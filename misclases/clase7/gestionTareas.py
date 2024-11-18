from datetime import datetime 
import statistics

class Tarea:

    # método constructor (función de inicializació)    
    def __init__(self, nombre, fechaLimite, categoria, horas) -> None:
        self.nombre = nombre
        self.fechaLimite = fechaLimite
        self.categoria = categoria
        self.horasDedicadas = horas


# Función para agregar una tarea
def agregarTarea(listaTareas):
    nombre = input('Ingrese el nombre de la tarea ')
    fechaLimite_str = input('Ingrese la fecha limite de la tarea (DD/MM/YYYY) ')
    try:
        fechaLimite = datetime.strptime(fechaLimite_str, "%d/%m/%Y")
    except ValueError:
        print('Fecha no valida')
        return 
    categoria  = input('Ingrese la categoria de la tarea(Estudio, Personal, Trabajo, etc.) ')
    horasDedicadas_str = input('Ingrese las horas dedicadas, separadas por comas ej: 3.5, 5.3, 6.0 ')
    try:
        horasDedicadas = list(map(float, horasDedicadas_str.split(',')))
    except ValueError:
        print('Fecha no valida')
        return
    
    # crear un objeto y agregarla a lista de tareas
    tarea = Tarea(nombre, fechaLimite, categoria, horasDedicadas)
    listaTareas.append(tarea)
    print("Tarea agregada con exito ")


def visualizarTareas(listaTareas):
    if not listaTareas:
        print('No tenemos tareas registradas ')
        return
    
    for i,tarea in enumerate(listaTareas, start=1):
        print(f"\nTarea {i}")
        print(f"Nombre: {tarea.nombre}")
        print(f"fecha: {tarea.fechaLimite.strftime('%d/%m/%Y')}")
        print(f"La categoria: {tarea.categoria}")
        print(f"Las horas dedicadas: {tarea.horasDedicadas}")

def analizarHoras(listaTareas):
    if not listaTareas:
        print("No hay tareas registradas")
        return
    for tarea in listaTareas:
        promedio = statistics.mean(tarea.horasDedicadas)
        maximo = max(tarea.horasDedicadas)
        minimo = min(tarea.horasDedicadas)
        print(f"\nAnalisis de {tarea.nombre}")
        print(f"\nPromedio de horas {promedio}")
        print(f"\nMaximo de horas {maximo}")
        print(f"\nMinimo de horas {minimo}")

def generarInforme(listaTareas):
    if not listaTareas:
        print('No hay tareas')
        return
    # Abrir un archivo txt para escribir un informe
    with open('informe_tareas.txt', 'w') as archivo:
        # Escribir los detalles de la tarea en el archivo
        for tarea in listaTareas:
            archivo.write(f'Nombre: {tarea.nombre}\n')
            archivo.write(f'Fecha limite: {tarea.fechaLimite.strftime('%d/%m/%Y')}\n')
            archivo.write(f'Categoria: {tarea.categoria}\n')
            archivo.write(f'Horas dedicadas: {tarea.horasDedicadas}\n')
            archivo.write('\n')
    
    print('El informe generado como "informe_tareas.txt "')

def menu():
    listaTareas = []
    while True:
        print("\n Menu de opciones: ")
        print("\n 1) Agregar tarea: ")
        print("\n 2) Visualizar tareas: ")
        print("\n 3) Analisar horas dedicadas ")
        print("\n 4) Generar informe ")
        print("\n 5) Salir ")

        opcion = int(input('\nSeleccione una opcion '))
        if opcion == 1:
            agregarTarea(listaTareas)
        elif opcion == 2:
            visualizarTareas(listaTareas)
        elif opcion == 3:
            analizarHoras(listaTareas)
        elif opcion == 4:
            generarInforme(listaTareas)
        elif opcion == 5:
            print('Saliendo del programa... ')
            break
        else:
            print('Opcion invalida')

if  __name__ == '__main__':
    menu()
    