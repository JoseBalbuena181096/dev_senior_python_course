""""
Datos -> Persistencia de datos
Base de datos MySQL, POSGREST

Precargado de datos
"""

import tkinter as tk
from tkinter import messagebox

productos = {
    1: {
        "nombre" : "manzana",
        "precio" : 1.5,
        "stock" : 100
    },
    2: {
        "nombre" : "pera",
        "precio" : 2,
        "stock" : 100
    },
    3: {
        "nombre" : "sandia",
        "precio" : 3,
        "stock" : 100
    }
}

historial_ventas = []

def obtener_productos(id_productos):
    return productos.get(id_productos, None)

def agregar_producto(id_producto, cantidad, lista_producto):
    
    try:
        id_producto = int()
        if producto:
            if cantidad <= producto['stock']:
                historial_ventas.append({
                    producto
                })
    except:
        print('An exception occurred')


def actualizar_lista():
    lista_productos.delete(0, tk.END)
    for id_producto, dato in productos.items():
        lista_productos.insert(
            tk.END,
            f"{id_producto} : {dato['nombre']} - ${dato['precio']} - Stock: {dato['stock']}"
        )
    

root = tk.Tk()
root.title("Tienda")

frame = tk.Frame(root)
frame.pack(padx=10)

lista_productos = tk.Listbox(frame, width=50)
lista_productos.pack()
actualizar_lista()

frame_inputs = tk.Frame(root)
frame_inputs.pack(padx=10)
tk.Label(frame_inputs, text=('ID productos: ')).grid(row=0, column=0)
entry_id = tk.Entry(frame_inputs)
entry_id.grid(row=0, column=1)


root.mainloop()

    