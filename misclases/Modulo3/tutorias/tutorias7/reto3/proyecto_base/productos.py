
productos = {
    1: {
        "nombre" : "Manzana",
        "precio" : 500,
        "stock" : 100
    },
    2: {
        "nombre" : "Mango",
        "precio" : 200,
        "stock" : 100
    },
    3: {
        "nombre" : "Piña",
        "precio" : 600,
        "stock" : 100
    },
    4: {
        "nombre" : "Limon",
        "precio" : 700,
        "stock" : 100
    }
    ,
    5: {
        "nombre" : "Kiwi",
        "precio" : 1500,
        "stock" : 100
    }
}

historial_ventas = []


def obtener_productos(id_producto):
    return productos.get(id_producto, None)





