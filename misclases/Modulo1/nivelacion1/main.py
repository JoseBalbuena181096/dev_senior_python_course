import datetime 

listaDeEquipos = [
    ["Seleccion Colombia", "01/01/1924", "Futbol", [0,1,1,2,3]],
    ["Seleccion Chile", "01/01/1923", "Basquet", [1,2,1,2, 3]]
]


def agregar_equipo():
    try:    
        nombre = input("Ingrese nombre del equipo")
        fecha = input("Ingrese la fecha de creacion del equipo: ")
        tipo = input("Ingrese el tipo de deporte")
        resultados = list(map(int, input("Ingrese resultados de partidos se parados por coma: ").split(',')))
        listaDeEquipos.append([nombre, fecha, tipo, resultados])
    except:
        print("Error al agregar el equipos")

def visualizar_equipos():
    print('Listado de equipos')
    for i, equipo in enumerate(listaDeEquipos):
        print(f"f{i+1} {equipo[0]} {equipo[1]} {equipo[2]} {equipo[3]}")


def calcular_estadisticas():
    visualizar_equipos()
    index = int(input('Ingrese el numero de equipos'))

    if 1 <= index < len(listaDeEquipos):
        resultados = listaDeEquipos[index][3]
        promedio = sum(resultados) / len(resultados)
        maximo = max(resultados)
        minimo = min(resultados)
        print(f'Promedio {promedio}')
        print(f'Maximo {maximo}')
        print(f'Minimo {minimo}')


def comparar_equipos():
    resultados_comparados = []
    visualizar_equipos()
    indices = list(map(int, input("Ingrese los indices a comparar, separados por coma ").split((","))))
    for index in indices:
        if 0 <= index < len(listaDeEquipos):
            promedio = sum(listaDeEquipos[index][3]) / len(listaDeEquipos[index][3])
            resultados_comparados.append(promedio)
        else:
            print(f'indice {index} no valido')
    resultados_comparados.sort(key=lambda x:x[1])
    print("Resultados comparados ")
    for index, promedio in resultados_comparados:
        print(f'{index + 1} . {listaDeEquipos[index][0]} - {promedio}')

def generar_informe():
    pass

def mostrar_menu():
    pass
