"""
Desarrollar una aplicación de escritorio que permita:
Seleccionar productos desde una lista.
Especificar la cantidad a comprar.
Verificar la disponibilidad del producto antes de añadirlo a la
compra.
Calcular el total de la compra en tiempo real.
Registrar el historial de ventas y mostrarlo en pantalla.
Gestionar correctamente la actualización del stock de productos.
"""

import tkinter as tk
from tkinter import messagebox, ttk
from  operaciones import agregar_producto_historial_venta, calcular_total
from excepciones import manejo_errores
from productos import historial_ventas, productos

# Configurar la interfaz
ventana = tk.Tk()
ventana.title("Caja registradora - Tienda fruber")

# Marco principal
marco_principal = tk.Frame(ventana, padx=30, pady=30, bg='#fff1f8')
marco_principal.pack(fill='both', expand=True)

# Titulo
titulo = tk.Label(marco_principal, text="Bienvenido a la tienda Fruber", font=('Arial', 15), bg='#fff1f8', fg="green")  
titulo.grid(row=0, column=0, padx=10, pady=10)


# Frame para lista de productos
frame_productos = tk.Frame(marco_principal, bg='#f4f4f9')
frame_productos.grid(row=1, column=0, padx=10, pady=10)

#TreeView
etiqueta = tk.Label(frame_productos, text="Seleccionar un producto", font=('Arial', 12), bg='#f4f4f9')  
etiqueta.pack(pady=10)

treeview_productos = ttk.Treeview(frame_productos, columns=("Producto", "Precio", "Cantidad Disponible"), show="headings", height=10)
treeview_productos.heading('Producto', text="Producto")
treeview_productos.heading('Precio', text="Precio")
treeview_productos.heading('Cantidad Disponible', text="Cantidad Disponible")

treeview_productos.column("Producto")
treeview_productos.column("Precio")
treeview_productos.column("Cantidad Disponible")

# Insertar productos en el TreeView
for key, producto in productos.items():
    cantidad_disponible = producto['stock']
    treeview_productos.insert("", "end", iid=str(key), values=(producto['nombre'], f"${producto['precio']}", cantidad_disponible))

treeview_productos.pack(pady=10)

# Frame para la cantidad y el boton 
frame_cantidad = tk.Frame(marco_principal, bg="#f4f4f9")
frame_cantidad.grid(row=1, column=1, padx=10, pady=10)

#campo para la cantidad
etiqueta_cantidad = tk.Label(frame_cantidad, text="Cantidad", font=("Arial", 14), bg="#f4f4f9")
etiqueta_cantidad.pack(pady=10)


ventana.mainloop()