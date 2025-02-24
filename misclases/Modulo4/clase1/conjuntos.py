#  Conjunto (set) en Python

# App de gestion de clientes (únicos) de una empresa

from typing import Set

def obtener_clientes_unicos(clientes: Set[str], nuevos_clientes: Set[str]) -> Set[str]:
    return clientes.union(nuevos_clientes)

def gestionar_clientes(clientes: Set[str]) -> None:
    # Agregar un cliente
    clientes.add("Pedro")
    print("Clientes despues de agregar a pedro: ", clientes)

    # agregar un cliente duplicado 
    clientes.add("Carlos")
    print("Clinete despúes de intentar agregar a carlos: ",clientes)

    # uso de la función remove para eliminar un cliente (si exite el cliente y sino error)
    cliente = "Ana"
    clientes.remove(cliente)
    print("Clientes despues de eliminar a Ana con el metodo remove", clientes)

    #uso de la funcion discard para eliminar un elemento
    cliente2 = "Luis"
    clientes.discard(cliente2)
    print("Clientes despues de eleminar a Luis con el metodo discard", clientes)

    # uso del metodo pop para mostrar un elemento del set y posterior lo borra automaticamente
    cliente_removido = clientes.pop()
    print(f"Cliente removido aleatoriamente: {cliente_removido}")
    print(f"Clintes restantes: ", clientes)

    # blanquear o borrar los elemtos de un set
    clientes.clear()
    print('Clientes despues del método clear: ',clientes)

def main():
    clientes_antiguos = {
        "Carlos",
        "Ana",
        "Luis"
    }
    clientes_nuevos = {
        "Luis",
        "Maria",
        "Jorge"
    }

    clientes_finales = obtener_clientes_unicos(clientes_antiguos, clientes_nuevos)
    print("La lista actualizada de clientes es ", clientes_finales)

    gestionar_clientes(clientes_finales)

if __name__ == "__main__":
    main()