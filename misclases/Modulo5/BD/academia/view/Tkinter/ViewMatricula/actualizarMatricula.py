import customtkinter as ctk
from controllers.matricula_controller import MatriculaController
from controllers.estudiante_controller import EstudianteController
from controllers.curso_controller import CursoController
from tkinter import messagebox

class ActualizarMatricula:
    def __init__(self, ventana_matricula):
        self.ventana_principal = ventana_matricula["ventana"]
        self.tema = ventana_matricula["tema"]
        self.db = ventana_matricula["db"]
        self.matricula_controller = MatriculaController(self.db)
        self.estudiante_controller = EstudianteController(self.db)
        self.curso_controller = CursoController(self.db)
        self.matricula_seleccionada = None
        
        self.ventana = ctk.CTk()
        self.ventana.title("Actualizar Matrícula")
        
        # Configurar el tamaño de la ventana
        ancho_pantalla = self.ventana.winfo_screenwidth()
        alto_pantalla = self.ventana.winfo_screenheight()
        ancho_ventana = int(ancho_pantalla * 0.4)
        alto_ventana = int(alto_pantalla)
        
        # Centrar la ventana
        self.ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{int((ancho_pantalla - ancho_ventana) / 2)}+{int((alto_pantalla - alto_ventana) / 2)}")
        
        # Configurar el tema
        ctk.set_appearance_mode(self.tema)
        self.ventana.resizable(False, False)
        
        # Configurar el cierre de ventana
        self.ventana.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)
        
        # Crear el título
        self.titulo = ctk.CTkLabel(self.ventana, text="Actualizar Matrícula", font=("Arial", 16))
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
            command=self.actualizar_matricula,
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
        self.cargar_matriculas()
        self.cargar_estudiantes()
        self.cargar_cursos()
    
    def crear_campos(self):
        # Campo para seleccionar matrícula
        ctk.CTkLabel(
            self.frame_principal,
            text="Seleccionar matrícula:",
            font=("Arial", 12)
        ).pack(pady=5)
        self.combo_matriculas = ctk.CTkComboBox(self.frame_principal, width=300)
        self.combo_matriculas.pack(pady=5)
        
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
    
    def cargar_matriculas(self):
        try:
            matriculas = self.matricula_controller.listar_matriculas()
            if not matriculas:
                messagebox.showinfo("Información", "No hay matrículas disponibles")
                return
            
            # Crear lista de opciones para el combobox
            opciones = [f"{m.nombre_estudiante} - {m.nombre_curso} ({m.fecha_matricula})" for m in matriculas]
            self.combo_matriculas.configure(values=opciones)
            
            # Configurar evento de selección
            self.combo_matriculas.configure(command=self.seleccionar_matricula)
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al cargar matrículas: {str(e)}")
    
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
    
    def seleccionar_matricula(self, matricula_seleccionada):
        try:
            # Obtener la matrícula seleccionada
            matriculas = self.matricula_controller.listar_matriculas()
            for matricula in matriculas:
                if f"{matricula.nombre_estudiante} - {matricula.nombre_curso} ({matricula.fecha_matricula})" == matricula_seleccionada:
                    self.matricula_seleccionada = matricula
                    # Llenar los campos con los datos de la matrícula
                    self.combo_estudiante.set(matricula.nombre_estudiante)
                    self.combo_curso.set(matricula.nombre_curso)
                    self.entry_fecha.delete(0, "end")
                    self.entry_fecha.insert(0, matricula.fecha_matricula)
                    break
        except Exception as e:
            messagebox.showerror("Error", f"Error al seleccionar matrícula: {str(e)}")
    
    def actualizar_matricula(self):
        if not self.matricula_seleccionada:
            messagebox.showerror("Error", "Debe seleccionar una matrícula")
            return
        
        # Obtener los valores de los campos
        nombre_estudiante = self.combo_estudiante.get()
        nombre_curso = self.combo_curso.get()
        fecha = self.entry_fecha.get()
        
        # Validar que todos los campos estén llenos
        if not all([nombre_estudiante, nombre_curso, fecha]):
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        try:
            # Obtener los IDs correspondientes
            estudiante_id = None
            curso_id = None
            
            # Buscar el ID del estudiante
            estudiantes = self.estudiante_controller.listar_estudiantes()
            for estudiante in estudiantes:
                if f"{estudiante.nombre} {estudiante.apellido}" == nombre_estudiante:
                    estudiante_id = estudiante.id_estudiante
                    break
            
            # Buscar el ID del curso
            cursos = self.curso_controller.listar_cursos()
            for curso in cursos:
                if curso.nombre == nombre_curso:
                    curso_id = curso.id_curso
                    break
            
            if estudiante_id is None or curso_id is None:
                messagebox.showerror("Error", "No se encontró el estudiante o curso seleccionado")
                return
            
            # Actualizar la matrícula
            self.matricula_controller.actualizar_matricula(
                self.matricula_seleccionada.id_matricula,
                estudiante_id,
                curso_id,
                fecha
            )
            
            messagebox.showinfo("Éxito", "Matrícula actualizada correctamente")
            self.limpiar_campos()
            self.cargar_matriculas()
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al actualizar matrícula: {str(e)}")
    
    def limpiar_campos(self):
        self.combo_matriculas.set("")
        self.combo_estudiante.set("")
        self.combo_curso.set("")
        self.entry_fecha.delete(0, "end")
        self.matricula_seleccionada = None
    
    def cambiar_tema(self):
        if ctk.get_appearance_mode() == "Dark":
            ctk.set_appearance_mode("Light")
        else:
            ctk.set_appearance_mode("Dark")
    
    def cerrar_ventana(self):
        self.ventana.destroy()
        self.ventana_principal.deiconify() 