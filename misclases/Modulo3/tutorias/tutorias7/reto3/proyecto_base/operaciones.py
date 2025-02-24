from productos import obtener_productos

def agregar_producto_historial_venta(id_producto, cantidad, lista_productos):
    producto = obtener_productos(id_producto)
    if producto:
        lista_productos.append({
            "nombre": producto["nombre"],
            "precio": producto["precio"] * cantidad
        })

    else:
        raise ValueError(f'Producto con ID {id_producto} no encontrado')

def calcular_total(lista_productos):
    total = 0
    for producto in lista_productos:
        total += producto['precio']
    return total


