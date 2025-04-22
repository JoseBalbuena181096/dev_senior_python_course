import customtkinter as ctk
from controllers.matricula_controller import MatriculaController

class ListarMatriculas:
    def __init__(self, ventana_matricula):
        self.ventana_principal = ventana_matricula["ventana"]
        self.tema = ventana_matricula["tema"]
        self.db = ventana_matricula["db"]
        self.matricula_controller = MatriculaController(self.db)
        self.matricula_seleccionada = None
        
        self.ventana = ctk.CTk()
        self.ventana.title("Lista de Matrículas")
        
        # Configurar el tamaño de la ventana
        ancho_pantalla = self.ventana.winfo_screenwidth()
        alto_pantalla = self.ventana.winfo_screenheight()
        ancho_ventana = int(ancho_pantalla * 0.7)
        alto_ventana = int(alto_pantalla * 0.6)
        
        # Centrar la ventana
        self.ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{int((ancho_pantalla - ancho_ventana) / 2)}+{int((alto_pantalla - alto_ventana) / 2)}")
        
        # Configurar el tema
        ctk.set_appearance_mode(self.tema)
        self.ventana.resizable(True, True)
        
        # Configurar el cierre de ventana
        self.ventana.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)
        
        # Crear el título
        self.titulo = ctk.CTkLabel(self.ventana, text="Lista de Matrículas", font=("Arial", 16))
        self.titulo.pack(pady=10)
        
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
    
    def crear_tabla(self):
        # Obtener las matrículas
        matriculas = self.matricula_controller.listar_matriculas()
        
        # Crear encabezados
        encabezados = ["ID", "Estudiante", "Curso", "Fecha", "Seleccionar"]
        for i, encabezado in enumerate(encabezados):
            label = ctk.CTkLabel(
                self.frame_tabla,
                text=encabezado,
                font=("Arial", 12, "bold"),
                width=150
            )
            label.grid(row=0, column=i, padx=5, pady=5)
        
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
            
            # Botón de selección
            ctk.CTkButton(
                self.frame_tabla,
                text="Seleccionar",
                command=lambda id=matricula.id_matricula: self.seleccionar_matricula(id),
                width=150
            ).grid(row=i, column=4, padx=5, pady=5)
    
    def seleccionar_matricula(self, id_matricula):
        self.matricula_seleccionada = id_matricula
        self.cerrar_ventana()
    
    def cambiar_tema(self):
        if ctk.get_appearance_mode() == "Dark":
            ctk.set_appearance_mode("Light")
        else:
            ctk.set_appearance_mode("Dark")
    
    def cerrar_ventana(self):
        self.ventana.destroy()
        self.ventana_principal.deiconify() 