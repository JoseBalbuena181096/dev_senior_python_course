import customtkinter as ctk
from controllers.matricula_controller import MatriculaController
from tkinter import messagebox

class EliminarMatricula:
    def __init__(self, ventana_matricula):
        self.ventana_principal = ventana_matricula["ventana"]
        self.tema = ventana_matricula["tema"]
        self.db = ventana_matricula["db"]
        self.matricula_controller = MatriculaController(self.db)
        self.matricula_seleccionada = None
        
        self.ventana = ctk.CTk()
        self.ventana.title("Eliminar Matrícula")
        
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
        self.titulo = ctk.CTkLabel(self.ventana, text="Eliminar Matrícula", font=("Arial", 16))
        self.titulo.pack(pady=10)
        
        # Crear el frame principal
        self.frame_principal = ctk.CTkFrame(self.ventana)
        self.frame_principal.pack(padx=20, pady=10, fill="both", expand=True)
        
        # Crear los campos
        self.crear_campos()
        
        # Crear el frame para mostrar detalles
        self.frame_detalles = ctk.CTkFrame(self.ventana)
        self.frame_detalles.pack(padx=20, pady=10, fill="both", expand=True)
        
        # Crear los labels para mostrar detalles
        self.crear_labels_detalles()
        
        # Botón para eliminar
        self.boton_eliminar = ctk.CTkButton(
            self.ventana,
            text="Eliminar",
            command=self.eliminar_matricula,
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
        
        # Cargar datos iniciales
        self.cargar_matriculas()
    
    def crear_campos(self):
        # Campo para seleccionar matrícula
        ctk.CTkLabel(
            self.frame_principal,
            text="Seleccionar matrícula:",
            font=("Arial", 12)
        ).pack(pady=5)
        self.combo_matriculas = ctk.CTkComboBox(self.frame_principal, width=300)
        self.combo_matriculas.pack(pady=5)
        
        # Configurar evento de selección
        self.combo_matriculas.configure(command=self.seleccionar_matricula)
    
    def crear_labels_detalles(self):
        # Label para mostrar detalles del estudiante
        ctk.CTkLabel(
            self.frame_detalles,
            text="Estudiante:",
            font=("Arial", 12, "bold")
        ).pack(pady=5)
        self.label_estudiante = ctk.CTkLabel(self.frame_detalles, text="", font=("Arial", 12))
        self.label_estudiante.pack(pady=5)
        
        # Label para mostrar detalles del curso
        ctk.CTkLabel(
            self.frame_detalles,
            text="Curso:",
            font=("Arial", 12, "bold")
        ).pack(pady=5)
        self.label_curso = ctk.CTkLabel(self.frame_detalles, text="", font=("Arial", 12))
        self.label_curso.pack(pady=5)
        
        # Label para mostrar la fecha
        ctk.CTkLabel(
            self.frame_detalles,
            text="Fecha:",
            font=("Arial", 12, "bold")
        ).pack(pady=5)
        self.label_fecha = ctk.CTkLabel(self.frame_detalles, text="", font=("Arial", 12))
        self.label_fecha.pack(pady=5)
        
        # Label para mostrar el estado
        ctk.CTkLabel(
            self.frame_detalles,
            text="Estado:",
            font=("Arial", 12, "bold")
        ).pack(pady=5)
        self.label_estado = ctk.CTkLabel(self.frame_detalles, text="", font=("Arial", 12))
        self.label_estado.pack(pady=5)
    
    def cargar_matriculas(self):
        try:
            matriculas = self.matricula_controller.listar_matriculas()
            if not matriculas:
                messagebox.showinfo("Información", "No hay matrículas disponibles")
                return
            
            # Crear lista de opciones para el combobox
            opciones = [f"{m.nombre_estudiante} - {m.nombre_curso} ({m.fecha_matricula})" for m in matriculas]
            self.combo_matriculas.configure(values=opciones)
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al cargar matrículas: {str(e)}")
    
    def seleccionar_matricula(self, matricula_seleccionada):
        try:
            # Obtener la matrícula seleccionada
            matriculas = self.matricula_controller.listar_matriculas()
            for matricula in matriculas:
                if f"{matricula.nombre_estudiante} - {matricula.nombre_curso} ({matricula.fecha_matricula})" == matricula_seleccionada:
                    self.matricula_seleccionada = matricula
                    # Actualizar los labels con los detalles
                    self.label_estudiante.configure(text=matricula.nombre_estudiante)
                    self.label_curso.configure(text=matricula.nombre_curso)
                    self.label_fecha.configure(text=matricula.fecha_matricula)
                    self.label_estado.configure(text=matricula.estado)
                    break
        except Exception as e:
            messagebox.showerror("Error", f"Error al seleccionar matrícula: {str(e)}")
    
    def eliminar_matricula(self):
        if not self.matricula_seleccionada:
            messagebox.showerror("Error", "Debe seleccionar una matrícula")
            return
        
        # Confirmar eliminación
        confirmacion = messagebox.askyesno(
            "Confirmar eliminación",
            f"¿Está seguro que desea eliminar la matrícula de {self.matricula_seleccionada.nombre_estudiante} en {self.matricula_seleccionada.nombre_curso}?"
        )
        
        if not confirmacion:
            return
        
        try:
            # Eliminar la matrícula
            self.matricula_controller.eliminar_matricula(self.matricula_seleccionada.id_matricula)
            messagebox.showinfo("Éxito", "Matrícula eliminada correctamente")
            self.limpiar_campos()
            self.cargar_matriculas()
        except Exception as e:
            messagebox.showerror("Error", f"Error al eliminar la matrícula: {str(e)}")
    
    def limpiar_campos(self):
        self.combo_matriculas.set("")
        self.label_estudiante.configure(text="")
        self.label_curso.configure(text="")
        self.label_fecha.configure(text="")
        self.label_estado.configure(text="")
        self.matricula_seleccionada = None
    
    def cambiar_tema(self):
        if ctk.get_appearance_mode() == "Dark":
            ctk.set_appearance_mode("Light")
        else:
            ctk.set_appearance_mode("Dark")
    
    def cerrar_ventana(self):
        self.ventana.destroy()
        self.ventana_principal.deiconify() 