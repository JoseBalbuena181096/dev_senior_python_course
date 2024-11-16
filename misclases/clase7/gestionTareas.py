from datetime import datetime 
import statistics

class Tarea:

    # método constructor (función de inicializació)    
    def __init__(self, nombre, fechaLimite, categorias, horas) -> None:
        self.nombre = nombre
        self.fechaLimite = fechaLimite
        self.categorias = categorias
        self.horas = horas


# Función para agregar una tarea
def agregarTarea(listaTareas):
    nombre = input('Ingrese el nombre de la tarea')
    fechaLimite_str = input('Ingrese la fecha limite de la tarea (DD/MM/YYYY)')
    try:
        fechaLimite = datetime.strftime(fechaLimite_str, "%d/%m/%Y")
    except ValueError:
        print('Fecha no valida')
        return 
    categoria  = input('Ingrese la categoria de la tarea(Estudio, Personal, Trabajo, etc.)')
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
        print(f"fecha: {tarea.fechaLimite}")



    