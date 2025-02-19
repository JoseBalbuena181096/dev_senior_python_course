import tkinter as tk
from tkinter import messagebox
from app.controlador_cliente import ControladorCliente

class Vista:
    def __init__(self):
        self.controlador_cliente = ControladorCliente()
        self.root = tk.Tk()
        self.root.title("Veterinaria")
        
        self.label_cliente = tk.Label(self.root, text="Nombre Cliente: ")
        self.label_cliente.grid(row=0, column=0)

        self.entry_cliente = tk.Entry(self.root)
        self.entry_cliente.grid(row=0, column=1)

        self.label_telefono = tk.Label(self.root, text="Telefono: ")
        self.label_telefono.grid(row=1, column=0)
        self.entry_telefono = tk.Entry(self.root)
        self.entry_telefono.grid(row=1, column=1)

        self.registrar_clientes_btn = tk.Button(
            self.root, 
            text="Registrar",
            command=self.registrar_cliente)

        self.registrar_clientes_btn.grid(row=2, column=0)

        self.root.mainloop()

    def registrar_cliente(self):
        nombre_cliente = self.entry_cliente.get()
        telefono = self.entry_telefono.get()

        if not self.controlador_cliente.registrar_cliente(nombre_cliente, telefono):
            messagebox.showerror("El cliente ya existe")
        else:
            messagebox.showinfo('Exito el cliente se registro correctamente')

