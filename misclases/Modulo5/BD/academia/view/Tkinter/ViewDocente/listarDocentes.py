import customtkinter as ctk
from controllers.docenteController import DocenteController

class ListarDocentes:
    def __init__(self, ventana_docente):
        self.ventana_principal = ventana_docente["ventana"]
        self.tema = ventana_docente["tema"]
        self.db = ventana_docente["db"]
        self.docente_controller = DocenteController(self.db)
        self.docente_seleccionado = None
        
        self.ventana = ctk.CTk()
        self.ventana.title("Lista de Profesores")
        
        # Configurar el tamaño de la ventana
        ancho_pantalla = self.ventana.winfo_screenwidth()
        alto_pantalla = self.ventana.winfo_screenheight()
        ancho_ventana = int(ancho_pantalla * 0.7)  # Un poco más ancho para incluir la especialidad
        alto_ventana = int(alto_pantalla * 0.6)
        
        # Centrar la ventana
        self.ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{int((ancho_pantalla - ancho_ventana) / 2)}+{int((alto_pantalla - alto_ventana) / 2)}")
        
        # Configurar el tema
        ctk.set_appearance_mode(self.tema)
        self.ventana.resizable(True, True)
        
        # Configurar el cierre de ventana
        self.ventana.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)
        
        # Crear el título
        self.titulo = ctk.CTkLabel(self.ventana, text="Lista de Profesores", font=("Arial", 16))
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
        # Obtener los profesores
        docentes = self.docente_controller.listar_docentes()
        
        # Crear encabezados
        encabezados = ["ID", "Nombre", "Apellido", "Correo", "Teléfono", "Especialidad", "Seleccionar"]
        for i, encabezado in enumerate(encabezados):
            label = ctk.CTkLabel(
                self.frame_tabla,
                text=encabezado,
                font=("Arial", 12, "bold"),
                width=150
            )
            label.grid(row=0, column=i, padx=5, pady=5)
        
        # Mostrar los profesores
        for i, docente in enumerate(docentes, start=1):
            # ID
            ctk.CTkLabel(
                self.frame_tabla,
                text=str(docente.id_profesor),
                width=150
            ).grid(row=i, column=0, padx=5, pady=5)
            
            # Nombre
            ctk.CTkLabel(
                self.frame_tabla,
                text=docente.nombre,
                width=150
            ).grid(row=i, column=1, padx=5, pady=5)
            
            # Apellido
            ctk.CTkLabel(
                self.frame_tabla,
                text=docente.apellido,
                width=150
            ).grid(row=i, column=2, padx=5, pady=5)
            
            # Correo
            ctk.CTkLabel(
                self.frame_tabla,
                text=docente.correo_electronico,
                width=150
            ).grid(row=i, column=3, padx=5, pady=5)
            
            # Teléfono
            ctk.CTkLabel(
                self.frame_tabla,
                text=docente.telefono,
                width=150
            ).grid(row=i, column=4, padx=5, pady=5)
            
            # Especialidad
            ctk.CTkLabel(
                self.frame_tabla,
                text=docente.especialidad,
                width=150
            ).grid(row=i, column=5, padx=5, pady=5)
            
            # Botón de selección
            ctk.CTkButton(
                self.frame_tabla,
                text="Seleccionar",
                command=lambda id=docente.id_profesor: self.seleccionar_docente(id),
                width=150
            ).grid(row=i, column=6, padx=5, pady=5)
    
    def seleccionar_docente(self, id_docente):
        self.docente_seleccionado = id_docente
        self.cerrar_ventana()
    
    def cambiar_tema(self):
        if ctk.get_appearance_mode() == "Dark":
            ctk.set_appearance_mode("Light")
        else:
            ctk.set_appearance_mode("Dark")
    
    def cerrar_ventana(self):
        self.ventana.destroy()
        self.ventana_principal.deiconify() 