"""
App para registro de empleados
"""
from typing import Tuple

def obtener_info_empleado(empleado: Tuple[int, str, str]) -> Tuple:
    id_empleado, nombre_empleado, cargo_empleado = empleado
    print(f"Id: {id_empleado}, Nombre: {nombre_empleado}, Cargo{cargo_empleado}")

def analizar_salarios(salarios: Tuple[int, ...]) -> None:
    print(f"Salarios tabulados: {salarios}")
    print(f"Cantidad de salarios registrados {len(salarios)}")
    print(f"Suma de salarios registrados {sum(salarios)}")
    print(f'El salario mas alto registrado es {max(salarios)}')
    print(f'El salario mas bajo registrado es {min(salarios)}')
    print(f"Los salarios de forma ordenada: {sorted(salarios)}")

    salarios_a_buscar = 500
    print(f'El salario con un valor de  {salarios_a_buscar}\
         se encuentra {salarios.count(salarios_a_buscar)} veces')

    if salarios_a_buscar in salarios:
        print(f"El salario a con un valor {salarios_a_buscar}\
            se encuentra en la posición {salarios.index(salarios_a_buscar)}")

def main():
    empleado = (111111, "Cristian Rubio", "Director de desarrollo")
    obtener_info_empleado(empleado)    

    salarios_empleados = (500, 500, 100, 200, 300, 400, 500, 600)
    analizar_salarios(salarios_empleados)

if __name__ == "__main__":
    main()