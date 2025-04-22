import customtkinter as ctk
from controllers.matricula_controller import MatriculaController
from controllers.estudiante_controller import EstudianteController
from controllers.curso_controller import CursoController
from tkinter import messagebox

class RegistrarMatricula:
    def __init__(self, ventana_matricula):
        self.ventana_principal = ventana_matricula["ventana"]
        self.tema = ventana_matricula["tema"]
        self.db = ventana_matricula["db"]
        self.matricula_controller = MatriculaController(self.db)
        self.estudiante_controller = EstudianteController(self.db)
        self.curso_controller = CursoController(self.db)
        
        self.ventana = ctk.CTk()
        self.ventana.title("Registrar Matrícula")
        
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
        self.titulo = ctk.CTkLabel(self.ventana, text="Registrar Matrícula", font=("Arial", 16))
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
            command=self.registrar_matricula,
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
        
        # Cargar datos iniciales
        self.cargar_estudiantes()
        self.cargar_cursos()
    
    def crear_campos(self):
        # Campo para seleccionar estudiante
        ctk.CTkLabel(
            self.frame_principal,
            text="Estudiante:",
            font=("Arial", 12)
        ).pack(pady=5)
        self.combo_estudiante = ctk.CTkComboBox(self.frame_principal, width=300)
        self.combo_estudiante.pack(pady=5)
        
        # Campo para seleccionar curso
        ctk.CTkLabel(
            self.frame_principal,
            text="Curso:",
            font=("Arial", 12)
        ).pack(pady=5)
        self.combo_curso = ctk.CTkComboBox(self.frame_principal, width=300)
        self.combo_curso.pack(pady=5)
        
        # Campo para la fecha
        ctk.CTkLabel(
            self.frame_principal,
            text="Fecha (YYYY-MM-DD):",
            font=("Arial", 12)
        ).pack(pady=5)
        self.entry_fecha = ctk.CTkEntry(self.frame_principal, width=300)
        self.entry_fecha.pack(pady=5)
    
    def cargar_estudiantes(self):
        try:
            estudiantes = self.estudiante_controller.listar_estudiantes()
            if not estudiantes:
                messagebox.showinfo("Información", "No hay estudiantes disponibles")
                return
            
            # Crear lista de opciones para el combobox
            opciones = [f"{e.nombre} {e.apellido}" for e in estudiantes]
            self.combo_estudiante.configure(values=opciones)
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al cargar estudiantes: {str(e)}")
    
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
    
    def registrar_matricula(self):
        # Obtener los valores de los campos
        nombre_estudiante = self.combo_estudiante.get()
        nombre_curso = self.combo_curso.get()
        fecha = self.entry_fecha.get()
        
        # Validar que todos los campos estén llenos
        if not all([nombre_estudiante, nombre_curso, fecha]):
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return
        
        try:
            # Obtener el ID del estudiante
            estudiante_id = None
            estudiantes = self.estudiante_controller.listar_estudiantes()
            for estudiante in estudiantes:
                if f"{estudiante.nombre} {estudiante.apellido}" == nombre_estudiante:
                    estudiante_id = estudiante.id_estudiante
                    break
            
            if estudiante_id is None:
                messagebox.showerror("Error", "No se encontró el estudiante seleccionado")
                return
            
            # Obtener el ID del curso
            curso_id = None
            cursos = self.curso_controller.listar_cursos()
            for curso in cursos:
                if curso.nombre == nombre_curso:
                    curso_id = curso.id_curso
                    break
            
            if curso_id is None:
                messagebox.showerror("Error", "No se encontró el curso seleccionado")
                return
            
            # Registrar la matrícula
            self.matricula_controller.registrar_matricula(estudiante_id, curso_id, fecha)
            messagebox.showinfo("Éxito", "Matrícula registrada correctamente")
            self.limpiar_campos()
        except Exception as e:
            messagebox.showerror("Error", f"Error al registrar la matrícula: {str(e)}")
    
    def limpiar_campos(self):
        self.combo_estudiante.set("")
        self.combo_curso.set("")
        self.entry_fecha.delete(0, "end")
    
    def cambiar_tema(self):
        if ctk.get_appearance_mode() == "Dark":
            ctk.set_appearance_mode("Light")
        else:
            ctk.set_appearance_mode("Dark")
    
    def cerrar_ventana(self):
        self.ventana.destroy()
        self.ventana_principal.deiconify() 