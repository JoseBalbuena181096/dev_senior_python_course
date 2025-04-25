import customtkinter as ctk
from controllers.horario_controller import HorarioController
from controllers.curso_controller import CursoController
from tkinter import messagebox

class RegistrarHorario:
    def __init__(self, ventana_horario):
        self.ventana_principal = ventana_horario["ventana"]
        self.tema = ventana_horario["tema"]
        self.db = ventana_horario["db"]
        self.horario_controller = HorarioController(self.db)
        self.curso_controller = CursoController(self.db)
        
        self.ventana = ctk.CTk()
        self.ventana.title("Registrar Horario")
        
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
        self.titulo = ctk.CTkLabel(self.ventana, text="Registrar Horario", font=("Arial", 16))
        self.titulo.pack(pady=10)
        
        # Crear el frame principal
        self.frame_principal = ctk.CTkFrame(self.ventana)
        self.frame_principal.pack(padx=20, pady=10, fill="both", expand=True)
        
        # Crear los campos de entrada
        self.crear_campos()
        
        # Botón para registrar
        self.boton_registrar = ctk.CTkButton(
            self.ventana,
            text="Registrar",
            command=self.registrar_horario,
            fg_color="green",
            text_color="white"
        )
        self.boton_registrar.pack(pady=10)
        
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
        
        # Cargar los cursos disponibles
        self.cargar_cursos()
    
    def crear_campos(self):
        # Campo para el curso (ComboBox en lugar de Entry)
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
    
    def cargar_cursos(self):
        try:
            # Obtener la lista de cursos
            cursos = self.curso_controller.listar_cursos()
            # Crear un diccionario para mapear nombres de cursos a IDs
            self.cursos_dict = {curso.nombre: curso.id_curso for curso in cursos}
            # Actualizar el ComboBox con los nombres de los cursos
            self.combo_curso.configure(values=list(self.cursos_dict.keys()))
            if self.cursos_dict:
                self.combo_curso.set(list(self.cursos_dict.keys())[0])
        except Exception as e:
            messagebox.showerror("Error", f"Error al cargar los cursos: {str(e)}")
    
    def registrar_horario(self):
        # Obtener los valores de los campos
        nombre_curso = self.combo_curso.get()
        dia = self.entry_dia.get()
        hora_inicio = self.entry_hora_inicio.get()
        hora_fin = self.entry_hora_fin.get()
        
        # Validar que todos los campos estén llenos
        if not all([nombre_curso, dia, hora_inicio, hora_fin]):
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return
        
        # Obtener el ID del curso seleccionado
        curso_id = self.cursos_dict.get(nombre_curso)
        if curso_id is None:
            messagebox.showerror("Error", "Curso no válido")
            return
        
        # Formatear las horas agregando los segundos si no están presentes
        if len(hora_inicio.split(':')) == 2:
            hora_inicio += ':00'
        if len(hora_fin.split(':')) == 2:
            hora_fin += ':00'
        
        # Registrar el horario
        try:
            self.horario_controller.registrar_horario(curso_id, dia, hora_inicio, hora_fin)
            messagebox.showinfo("Éxito", "Horario registrado correctamente")
            self.limpiar_campos()
        except Exception as e:
            messagebox.showerror("Error", f"Error al registrar el horario: {str(e)}")
    
    def limpiar_campos(self):
        if self.cursos_dict:
            self.combo_curso.set(list(self.cursos_dict.keys())[0])
        self.entry_dia.delete(0, "end")
        self.entry_hora_inicio.delete(0, "end")
        self.entry_hora_fin.delete(0, "end")
    
    def cambiar_tema(self):
        if ctk.get_appearance_mode() == "Dark":
            ctk.set_appearance_mode("Light")
        else:
            ctk.set_appearance_mode("Dark")
    
    def cerrar_ventana(self):
        self.ventana.destroy()
        self.ventana_principal.deiconify() 