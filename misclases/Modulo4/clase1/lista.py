# App: Gestión de pedidos de una tienda
def agregar_pedido(pedidos: list[str], nuevo_pedido: str)->list[str]:
    pedidos.append(nuevo_pedido)
    return pedidos

def eliminar_pedido(pedidos: list[str], pedido_a_eliminar: str) -> list[str]:
    if pedido_a_eliminar in pedidos:
        pedidos.remove(pedido_a_eliminar)
    else:
        print('El pedido no se encuantra en la lista')
    return pedidos

def buscar_pedido(pedidos: list[str], pedido_a_buscar: str) ->int:
    if pedido_a_buscar in pedidos:
        return pedidos.index(pedido_a_buscar)
    
    else:
        print('El pedido no se encuentra en la lista')
        return -1

def main():
    # Lista inicial de pedidos
    pedido_tienda = ["Pedido 1", "Pedido3"]

    # Agregar un nuevo pedido
    pedido_tienda = agregar_pedido(pedido_tienda, "Pedido 2")

    # sort modifica la lista original 

    pedido_tienda.sort()
    # Mostrar los elementos de la lista
    print("lista actualizado de pedidos ordenadas", pedido_tienda)

    pedido_a_buscar = "Pedido3"
    indice = buscar_pedido(pedido_tienda, pedido_a_buscar)
    if indice !=  -1:
        print(f'El pedido {pedido_tienda[indice]} se encuantra en la posición {indice}')

    # Eliminar un pedido de la lista
    pedido_a_eliminar = "Pedido 1"
    pedido_tienda = eliminar_pedido(pedido_tienda, pedido_a_eliminar)
    print(f'La lista resultante a pedido es {pedido_tienda} des pues de eliminar {pedido_a_eliminar}')

if __name__ == "__main__":
    main()
