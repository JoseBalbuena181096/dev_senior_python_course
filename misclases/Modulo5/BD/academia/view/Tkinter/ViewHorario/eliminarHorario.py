import customtkinter as ctk
from controllers.horario_controller import HorarioController
from tkinter import messagebox

class EliminarHorario:
    def __init__(self, ventana_horario):
        self.ventana_principal = ventana_horario["ventana"]
        self.tema = ventana_horario["tema"]
        self.db = ventana_horario["db"]
        self.horario_controller = HorarioController(self.db)
        self.horario_seleccionado = None
        
        self.ventana = ctk.CTk()
        self.ventana.title("Eliminar Horario")
        
        # Configurar el tamaño de la ventana
        ancho_pantalla = self.ventana.winfo_screenwidth()
        alto_pantalla = self.ventana.winfo_screenheight()
        ancho_ventana = int(ancho_pantalla * 0.4)
        alto_ventana = int(alto_pantalla * 0.6)
        
        # Centrar la ventana
        self.ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{int((ancho_pantalla - ancho_ventana) / 2)}+{int((alto_pantalla - alto_ventana) / 2)}")
        
        # Configurar el tema
        ctk.set_appearance_mode(self.tema)
        self.ventana.resizable(False, False)
        
        # Configurar el cierre de ventana
        self.ventana.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)
        
        # Crear el título
        self.titulo = ctk.CTkLabel(self.ventana, text="Eliminar Horario", font=("Arial", 16))
        self.titulo.pack(pady=10)
        
        # Crear el frame principal
        self.frame_principal = ctk.CTkFrame(self.ventana)
        self.frame_principal.pack(padx=20, pady=10, fill="both", expand=True)
        
        # Crear los campos
        self.crear_campos()
        
        # Botón para eliminar
        self.boton_eliminar = ctk.CTkButton(
            self.ventana,
            text="Eliminar",
            command=self.eliminar_horario,
            fg_color="red",
            text_color="white"
        )
        self.boton_eliminar.pack(pady=10)
        
        # Botón para regresar
        self.boton_regresar = ctk.CTkButton(
            self.ventana,
            text="Regresar",
            command=self.cerrar_ventana,
            fg_color="black",
            text_color="white"
        )
        self.boton_regresar.pack(pady=10)
        
        # Botón para cambiar tema
        self.boton_cambiar_tema = ctk.CTkButton(
            self.ventana,
            text="Cambiar Tema",
            command=self.cambiar_tema,
            fg_color="black",
            text_color="white"
        )
        self.boton_cambiar_tema.pack(pady=10)
        
        # Cargar horarios disponibles
        self.cargar_horarios()
    
    def crear_campos(self):
        # Campo para seleccionar horario
        ctk.CTkLabel(
            self.frame_principal,
            text="Seleccionar horario a eliminar:",
            font=("Arial", 12)
        ).pack(pady=5)
        self.combo_horarios = ctk.CTkComboBox(self.frame_principal, width=300)
        self.combo_horarios.pack(pady=5)
        
        # Frame para mostrar detalles del horario seleccionado
        self.frame_detalles = ctk.CTkFrame(self.frame_principal)
        self.frame_detalles.pack(pady=10, fill="x")
        
        # Etiquetas para mostrar detalles
        self.label_curso = ctk.CTkLabel(self.frame_detalles, text="Curso:", font=("Arial", 12))
        self.label_curso.pack(pady=5)
        
        self.label_dia = ctk.CTkLabel(self.frame_detalles, text="Día:", font=("Arial", 12))
        self.label_dia.pack(pady=5)
        
        self.label_hora = ctk.CTkLabel(self.frame_detalles, text="Horario:", font=("Arial", 12))
        self.label_hora.pack(pady=5)
    
    def cargar_horarios(self):
        try:
            horarios = self.horario_controller.listar_horarios()
            if not horarios:
                messagebox.showinfo("Información", "No hay horarios disponibles")
                return
            
            # Crear lista de opciones para el combobox
            opciones = [f"{h.nombre_curso} - {h.dia_semana} ({h.hora_inicio}-{h.hora_fin})" for h in horarios]
            self.combo_horarios.configure(values=opciones)
            
            # Configurar evento de selección
            self.combo_horarios.configure(command=self.seleccionar_horario)
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al cargar horarios: {str(e)}")
    
    def seleccionar_horario(self, horario_seleccionado):
        try:
            # Obtener el horario seleccionado
            horarios = self.horario_controller.listar_horarios()
            for horario in horarios:
                if f"{horario.nombre_curso} - {horario.dia_semana} ({horario.hora_inicio}-{horario.hora_fin})" == horario_seleccionado:
                    self.horario_seleccionado = horario
                    # Actualizar etiquetas con los detalles
                    self.label_curso.configure(text=f"Curso: {horario.nombre_curso}")
                    self.label_dia.configure(text=f"Día: {horario.dia_semana}")
                    self.label_hora.configure(text=f"Horario: {horario.hora_inicio} - {horario.hora_fin}")
                    break
        except Exception as e:
            messagebox.showerror("Error", f"Error al seleccionar horario: {str(e)}")
    
    def eliminar_horario(self):
        if not self.horario_seleccionado:
            messagebox.showerror("Error", "Debe seleccionar un horario")
            return
        
        # Confirmar eliminación
        confirmacion = messagebox.askyesno(
            "Confirmar eliminación",
            f"¿Está seguro que desea eliminar el horario:\n"
            f"Curso: {self.horario_seleccionado.nombre_curso}\n"
            f"Día: {self.horario_seleccionado.dia_semana}\n"
            f"Horario: {self.horario_seleccionado.hora_inicio} - {self.horario_seleccionado.hora_fin}?"
        )
        
        if not confirmacion:
            return
        
        try:
            # Eliminar el horario
            self.horario_controller.eliminar_horario(self.horario_seleccionado.id_horario)
            messagebox.showinfo("Éxito", "Horario eliminado correctamente")
            self.limpiar_campos()
            self.cargar_horarios()
        except Exception as e:
            messagebox.showerror("Error", f"Error al eliminar el horario: {str(e)}")
    
    def limpiar_campos(self):
        self.label_curso.configure(text="Curso:")
        self.label_dia.configure(text="Día:")
        self.label_hora.configure(text="Horario:")
        self.horario_seleccionado = None
    
    def cambiar_tema(self):
        if ctk.get_appearance_mode() == "Dark":
            ctk.set_appearance_mode("Light")
        else:
            ctk.set_appearance_mode("Dark")
    
    def cerrar_ventana(self):
        self.ventana.destroy()
        self.ventana_principal.deiconify() 