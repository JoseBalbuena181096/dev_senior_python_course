import tkinter as tk
from tkinter import messagebox, ttk
import datetime

class Vehiculo:
    def __init__(self, placa, hora_entrada):
        self.placa = placa
        self.hora_entrada = hora_entrada

    def calcular_tiempo(self):
        hora_salida = datetime.datetime.now()
        tiempo_total = hora_salida - self.hora_entrada
        return tiempo_total.total_seconds() / 60
    
class ParquederoApp:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Control de Parqueadero")
        self.ventana.geometry("500x400")

        self.vehiculos = {}

        # Entrada de placa
        tk.Label(ventana, text="Placa de vehiculo").pack(pady=5)
        self.entry_placa = tk.Entry(ventana) # Caja de texto
        self.entry_placa.pack(pady=5)

        # Botones
        tk.Button(ventana, text="Registro Entrada", command=self.registro_entrada).pack(pady=5)
        tk.Button(ventana, text="Registro Salida", command=self.registrar_salida).pack(pady=5)

        # Tabla de Vehiculos
        self.tree = ttk.Treeview(ventana, columns=("Placa", "Hora de Entrada"), show="headings")
        self.tree.heading("Placa", text="Placa")
        self.tree.heading("Hora de Entrada", text="Hora de entrada")
        self.tree.pack(pady=20, fill="both", expand=True)
        
    def registro_entrada(self):
        placa = self.entry_placa.get().upper()
        print(placa)
        if placa and placa not in self.vehiculos:
            hora_actual = datetime.datetime.now().strftime('%H:%M:%S')
            self.vehiculos[placa] = Vehiculo(placa, datetime.datetime.now())
            self.tree.insert("","end",iid=placa, values=(placa, hora_actual))
        else:
            messagebox.showerror("Error", "Placa invalida o ya registrada")

    def registrar_salida(self):
        placa = self.entry_placa.get().upper()
        if placa in self.vehiculos:
            vehiculo = self.vehiculos.pop(placa)
            parque_tiempo = vehiculo.calcular_tiempo()
            print(parque_tiempo)
            # eliminar de la tabla 
            self.tree.delete(placa)
            messagebox.showinfo("Salida", f'Vehiculo {placa} salio. \nTiempo: {parque_tiempo:.2f} minutos')
        else:
            messagebox.showerror("Error", "Vehiculo no encontrado")
            
root = tk.Tk()
app = ParquederoApp(root)
root.mainloop()




