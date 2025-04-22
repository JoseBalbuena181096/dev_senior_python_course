import customtkinter as ctk
from controllers.horario_controller import HorarioController
from controllers.curso_controller import CursoController
from tkinter import messagebox

class ActualizarHorario:
    def __init__(self, ventana_horario):
        self.ventana_principal = ventana_horario["ventana"]
        self.tema = ventana_horario["tema"]
        self.db = ventana_horario["db"]
        self.horario_controller = HorarioController(self.db)
        self.curso_controller = CursoController(self.db)
        self.horario_seleccionado = None
        
        self.ventana = ctk.CTk()
        self.ventana.title("Actualizar Horario")
        
        # Configurar el tamaño de la ventana
        ancho_pantalla = self.ventana.winfo_screenwidth()
        alto_pantalla = self.ventana.winfo_screenheight()
        ancho_ventana = int(ancho_pantalla * 0.4)
        alto_ventana = int(alto_pantalla * 0.8)
        
        # Centrar la ventana
        self.ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{int((ancho_pantalla - ancho_ventana) / 2)}+{int((alto_pantalla - alto_ventana) / 2)}")
        
        # Configurar el tema
        ctk.set_appearance_mode(self.tema)
        self.ventana.resizable(False, False)
        
        # Configurar el cierre de ventana
        self.ventana.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)
        
        # Crear el título
        self.titulo = ctk.CTkLabel(self.ventana, text="Actualizar Horario", font=("Arial", 16))
        self.titulo.pack(pady=10)
        
        # Crear el frame principal
        self.frame_principal = ctk.CTkFrame(self.ventana)
        self.frame_principal.pack(padx=20, pady=10, fill="both", expand=True)
        
        # Crear los campos de entrada
        self.crear_campos()
        
        # Botón para actualizar
        self.boton_actualizar = ctk.CTkButton(
            self.ventana,
            text="Actualizar",
            command=self.actualizar_horario,
            fg_color="green",
            text_color="white"
        )
        self.boton_actualizar.pack(pady=10)
        
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
        
        # Cargar datos iniciales
        self.cargar_horarios()
        self.cargar_cursos()
    
    def crear_campos(self):
        # Campo para seleccionar horario
        ctk.CTkLabel(
            self.frame_principal,
            text="Seleccionar horario:",
            font=("Arial", 12)
        ).pack(pady=5)
        self.combo_horarios = ctk.CTkComboBox(self.frame_principal, width=300)
        self.combo_horarios.pack(pady=5)
        
        # Campo para el curso
        ctk.CTkLabel(
            self.frame_principal,
            text="Curso:",
            font=("Arial", 12)
        ).pack(pady=5)
        self.combo_curso = ctk.CTkComboBox(self.frame_principal, width=300)
        self.combo_curso.pack(pady=5)
        
        # Campo para el día
        ctk.CTkLabel(
            self.frame_principal,
            text="Día de la semana:",
            font=("Arial", 12)
        ).pack(pady=5)
        self.entry_dia = ctk.CTkEntry(self.frame_principal, width=300)
        self.entry_dia.pack(pady=5)
        
        # Campo para la hora de inicio
        ctk.CTkLabel(
            self.frame_principal,
            text="Hora de inicio (HH:MM):",
            font=("Arial", 12)
        ).pack(pady=5)
        self.entry_hora_inicio = ctk.CTkEntry(self.frame_principal, width=300)
        self.entry_hora_inicio.pack(pady=5)
        
        # Campo para la hora de fin
        ctk.CTkLabel(
            self.frame_principal,
            text="Hora de fin (HH:MM):",
            font=("Arial", 12)
        ).pack(pady=5)
        self.entry_hora_fin = ctk.CTkEntry(self.frame_principal, width=300)
        self.entry_hora_fin.pack(pady=5)
    
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
    
    def cargar_cursos(self):
        try:
            cursos = self.curso_controller.listar_cursos()
            if not cursos:
                messagebox.showinfo("Información", "No hay cursos disponibles")
                return
            
            # Crear lista de opciones para el combobox
            opciones = [c.nombre for c in cursos]
            self.combo_curso.configure(values=opciones)
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al cargar cursos: {str(e)}")
    
    def seleccionar_horario(self, horario_seleccionado):
        try:
            # Obtener el horario seleccionado
            horarios = self.horario_controller.listar_horarios()
            for horario in horarios:
                if f"{horario.nombre_curso} - {horario.dia_semana} ({horario.hora_inicio}-{horario.hora_fin})" == horario_seleccionado:
                    self.horario_seleccionado = horario
                    # Llenar los campos con los datos del horario
                    self.combo_curso.set(horario.nombre_curso)
                    self.entry_dia.delete(0, "end")
                    self.entry_dia.insert(0, horario.dia_semana)
                    self.entry_hora_inicio.delete(0, "end")
                    self.entry_hora_inicio.insert(0, horario.hora_inicio)
                    self.entry_hora_fin.delete(0, "end")
                    self.entry_hora_fin.insert(0, horario.hora_fin)
                    break
        except Exception as e:
            messagebox.showerror("Error", f"Error al seleccionar horario: {str(e)}")
    
    def actualizar_horario(self):
        if not self.horario_seleccionado:
            messagebox.showerror("Error", "Debe seleccionar un horario")
            return
        
        # Obtener los valores de los campos
        nombre_curso = self.combo_curso.get()
        dia = self.entry_dia.get()
        hora_inicio = self.entry_hora_inicio.get()
        hora_fin = self.entry_hora_fin.get()
        
        # Validar que todos los campos estén llenos
        if not all([nombre_curso, dia, hora_inicio, hora_fin]):
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return
        
        try:
            # Obtener el ID del curso
            cursos = self.curso_controller.listar_cursos()
            curso_id = None
            for curso in cursos:
                if curso.nombre == nombre_curso:
                    curso_id = curso.id_curso
                    break
            
            if curso_id is None:
                messagebox.showerror("Error", "El curso seleccionado no existe")
                return
            
            # Actualizar el horario
            self.horario_controller.actualizar_horario(
                self.horario_seleccionado.id_horario,
                curso_id,
                dia,
                hora_inicio,
                hora_fin
            )
            messagebox.showinfo("Éxito", "Horario actualizado correctamente")
            self.limpiar_campos()
            self.cargar_horarios()
        except Exception as e:
            messagebox.showerror("Error", f"Error al actualizar el horario: {str(e)}")
    
    def limpiar_campos(self):
        self.combo_curso.set("")
        self.entry_dia.delete(0, "end")
        self.entry_hora_inicio.delete(0, "end")
        self.entry_hora_fin.delete(0, "end")
        self.horario_seleccionado = None
    
    def cambiar_tema(self):
        if ctk.get_appearance_mode() == "Dark":
            ctk.set_appearance_mode("Light")
        else:
            ctk.set_appearance_mode("Dark")
    
    def cerrar_ventana(self):
        self.ventana.destroy()
        self.ventana_principal.deiconify() 