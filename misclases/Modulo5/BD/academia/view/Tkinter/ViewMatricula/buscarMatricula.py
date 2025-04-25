import customtkinter as ctk
from controllers.matricula_controller import MatriculaController
from controllers.estudiante_controller import EstudianteController
from controllers.curso_controller import CursoController
from tkinter import messagebox

class BuscarMatricula:
    def __init__(self, ventana_matricula):
        self.ventana_principal = ventana_matricula["ventana"]
        self.tema = ventana_matricula["tema"]
        self.db = ventana_matricula["db"]
        self.matricula_controller = MatriculaController(self.db)
        self.estudiante_controller = EstudianteController(self.db)
        self.curso_controller = CursoController(self.db)
        
        self.ventana = ctk.CTk()
        self.ventana.title("Buscar Matrícula")
        
        # Configurar el tamaño de la ventana
        ancho_pantalla = self.ventana.winfo_screenwidth()
        alto_pantalla = self.ventana.winfo_screenheight()
        ancho_ventana = int(ancho_pantalla * 0.7)
        alto_ventana = int(alto_pantalla * 0.9)
        
        # Centrar la ventana
        self.ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{int((ancho_pantalla - ancho_ventana) / 2)}+{int((alto_pantalla - alto_ventana) / 2)}")
        
        # Configurar el tema
        ctk.set_appearance_mode(self.tema)
        self.ventana.resizable(True, True)
        
        # Configurar el cierre de ventana
        self.ventana.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)
        
        # Crear el título
        self.titulo = ctk.CTkLabel(self.ventana, text="Buscar Matrícula", font=("Arial", 16))
        self.titulo.pack(pady=10)
        
        # Crear el frame principal para los campos de búsqueda
        self.frame_busqueda = ctk.CTkFrame(self.ventana)
        self.frame_busqueda.pack(padx=20, pady=10, fill="x")
        
        # Crear los campos de búsqueda
        self.crear_campos_busqueda()
        
        # Crear el frame principal para la tabla
        self.frame_principal = ctk.CTkFrame(self.ventana)
        self.frame_principal.pack(padx=20, pady=10, fill="both", expand=True)
        
        # Crear el scrollable frame
        self.scrollable_frame = ctk.CTkScrollableFrame(
            self.frame_principal,
            width=ancho_ventana - 100,
            height=alto_ventana - 200
        )
        self.scrollable_frame.pack(fill="both", expand=True)
        
        # Crear el frame para la tabla
        self.frame_tabla = ctk.CTkFrame(self.scrollable_frame)
        self.frame_tabla.pack(fill="both", expand=True)
        
        # Crear la tabla
        self.crear_tabla()
        
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
    
    def crear_campos_busqueda(self):
        # Campo para buscar por estudiante
        ctk.CTkLabel(
            self.frame_busqueda,
            text="Buscar por estudiante:",
            font=("Arial", 12)
        ).pack(side="left", padx=5)
        self.entry_estudiante = ctk.CTkEntry(self.frame_busqueda, width=200)
        self.entry_estudiante.pack(side="left", padx=5)
        
        # Campo para buscar por curso
        ctk.CTkLabel(
            self.frame_busqueda,
            text="Buscar por curso:",
            font=("Arial", 12)
        ).pack(side="left", padx=5)
        self.entry_curso = ctk.CTkEntry(self.frame_busqueda, width=200)
        self.entry_curso.pack(side="left", padx=5)
        
        # Campo para buscar por estado
        ctk.CTkLabel(
            self.frame_busqueda,
            text="Buscar por estado:",
            font=("Arial", 12)
        ).pack(side="left", padx=5)
        self.combo_estado = ctk.CTkComboBox(
            self.frame_busqueda,
            width=150,
            values=["", "Activa", "Inactiva", "Completada"]
        )
        self.combo_estado.pack(side="left", padx=5)
        
        # Botón para buscar
        self.boton_buscar = ctk.CTkButton(
            self.frame_busqueda,
            text="Buscar",
            command=self.buscar_matriculas,
            fg_color="green",
            text_color="white"
        )
        self.boton_buscar.pack(side="left", padx=5)
    
    def crear_tabla(self):
        # Crear encabezados
        encabezados = ["ID", "Estudiante", "Curso", "Fecha", "Estado"]
        for i, encabezado in enumerate(encabezados):
            label = ctk.CTkLabel(
                self.frame_tabla,
                text=encabezado,
                font=("Arial", 12, "bold"),
                width=150
            )
            label.grid(row=0, column=i, padx=5, pady=5)
    
    def buscar_matriculas(self):
        # Obtener los criterios de búsqueda
        estudiante = self.entry_estudiante.get().strip()
        curso = self.entry_curso.get().strip()
        estado = self.combo_estado.get().strip()
        
        try:
            # Buscar matrículas
            matriculas = self.matricula_controller.buscar_matriculas(estudiante, curso, estado)
            
            # Limpiar la tabla
            for widget in self.frame_tabla.winfo_children():
                if isinstance(widget, ctk.CTkLabel) and widget.grid_info()["row"] > 0:
                    widget.destroy()
            
            # Mostrar los resultados
            if not matriculas:
                messagebox.showinfo("Información", "No se encontraron matrículas con los criterios especificados")
                return
            
            # Mostrar las matrículas
            for i, matricula in enumerate(matriculas, start=1):
                # ID
                ctk.CTkLabel(
                    self.frame_tabla,
                    text=str(matricula.id_matricula),
                    width=150
                ).grid(row=i, column=0, padx=5, pady=5)
                
                # Estudiante
                ctk.CTkLabel(
                    self.frame_tabla,
                    text=matricula.nombre_estudiante,
                    width=150
                ).grid(row=i, column=1, padx=5, pady=5)
                
                # Curso
                ctk.CTkLabel(
                    self.frame_tabla,
                    text=matricula.nombre_curso,
                    width=150
                ).grid(row=i, column=2, padx=5, pady=5)
                
                # Fecha
                ctk.CTkLabel(
                    self.frame_tabla,
                    text=matricula.fecha_matricula,
                    width=150
                ).grid(row=i, column=3, padx=5, pady=5)
                
                # Estado
                ctk.CTkLabel(
                    self.frame_tabla,
                    text=matricula.estado,
                    width=150
                ).grid(row=i, column=4, padx=5, pady=5)
                
        except Exception as e:
            messagebox.showerror("Error", f"Error al buscar matrículas: {str(e)}")
    
    def cambiar_tema(self):
        if ctk.get_appearance_mode() == "Dark":
            ctk.set_appearance_mode("Light")
        else:
            ctk.set_appearance_mode("Dark")
    
    def cerrar_ventana(self):
        self.ventana.destroy()
        self.ventana_principal.deiconify() 