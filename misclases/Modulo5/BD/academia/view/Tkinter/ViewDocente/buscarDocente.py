import customtkinter as ctk
from controllers.docenteController import DocenteController

class BuscarDocente:
    def __init__(self, ventana_docente):
        self.ventana_principal = ventana_docente["ventana"]
        self.tema = ventana_docente["tema"]
        self.db = ventana_docente["db"]
        self.docente_controller = DocenteController(self.db)
        self.docente_encontrado = None
        
        self.ventana = ctk.CTk()
        self.ventana.title("Buscar Profesor")
        
        # Configurar el tamaño de la ventana
        ancho_pantalla = self.ventana.winfo_screenwidth()
        alto_pantalla = self.ventana.winfo_screenheight()
        ancho_ventana = int(ancho_pantalla * 0.6)  # Un poco más ancho para incluir especialidad
        alto_ventana = int(alto_pantalla * 0.6)
        
        # Centrar la ventana
        self.ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{int((ancho_pantalla - ancho_ventana) / 2)}+{int((alto_pantalla - alto_ventana) / 2)}")
        
        # Configurar el tema
        ctk.set_appearance_mode(self.tema)
        self.ventana.resizable(True, True)
        
        # Configurar el cierre de ventana
        self.ventana.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)
        
        # Crear frame para título y botón regresar
        self.frame_superior = ctk.CTkFrame(self.ventana)
        self.frame_superior.pack(pady=10, fill="x")
        
        # Crear el título
        self.titulo = ctk.CTkLabel(self.frame_superior, text="Buscar Profesor", font=("Arial", 16))
        self.titulo.pack(pady=10, side="left", padx=20)
        
        # Botón para regresar al lado del título
        self.boton_regresar = ctk.CTkButton(
            self.frame_superior,
            text="Regresar",
            command=self.cerrar_ventana,
            fg_color="black",
            text_color="white",
            width=100
        )
        self.boton_regresar.pack(side="right", padx=20, pady=10)
        
        # Crear el frame para la búsqueda
        self.frame_busqueda = ctk.CTkFrame(self.ventana)
        self.frame_busqueda.pack(padx=20, pady=10, fill="x")
        
        # Crear los campos de búsqueda
        self.crear_campos_busqueda()
        
        # Crear el frame para la tabla con scroll
        self.frame_tabla_principal = ctk.CTkFrame(self.ventana)
        self.frame_tabla_principal.pack(padx=20, pady=10, fill="both", expand=True)
        
        # Crear el scrollable frame
        self.scrollable_frame = ctk.CTkScrollableFrame(
            self.frame_tabla_principal,
            width=ancho_ventana - 100,
            height=alto_ventana - 200
        )
        self.scrollable_frame.pack(fill="both", expand=True)
        
        # Crear el frame para la tabla
        self.frame_tabla = ctk.CTkFrame(self.scrollable_frame)
        self.frame_tabla.pack(fill="both", expand=True)
        
        # Crear la tabla
        self.crear_tabla()
        
        # Crear el frame para los botones
        self.frame_botones = ctk.CTkFrame(self.ventana)
        self.frame_botones.pack(padx=20, pady=10, fill="x", side="bottom")
        
        # Frame para alinear los botones
        self.frame_botones_interno = ctk.CTkFrame(self.frame_botones)
        self.frame_botones_interno.pack(fill="x", expand=True)
        
        # Botón para buscar
        self.boton_buscar = ctk.CTkButton(
            self.frame_botones_interno,
            text="Buscar",
            command=self.buscar,
            fg_color="green",
            width=100
        )
        self.boton_buscar.pack(side="left", padx=5, pady=5)
        
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
        # Frame para los campos de búsqueda
        self.frame_campos = ctk.CTkFrame(self.frame_busqueda)
        self.frame_campos.pack(padx=10, pady=10, fill="x")
        
        # Radio buttons para tipo de búsqueda
        self.tipo_busqueda = ctk.StringVar(value="nombre")
        
        ctk.CTkRadioButton(
            self.frame_campos,
            text="Buscar por Nombre",
            variable=self.tipo_busqueda,
            value="nombre"
        ).pack(side="left", padx=10)
        
        ctk.CTkRadioButton(
            self.frame_campos,
            text="Buscar por ID",
            variable=self.tipo_busqueda,
            value="id"
        ).pack(side="left", padx=10)
        
        # Campo de entrada
        self.entrada_busqueda = ctk.CTkEntry(
            self.frame_busqueda,
            width=300,
            placeholder_text="Ingrese el término de búsqueda"
        )
        self.entrada_busqueda.pack(padx=10, pady=10)
        
        # Botón de búsqueda
        self.boton_buscar = ctk.CTkButton(
            self.frame_busqueda,
            text="Buscar",
            command=self.buscar,
            fg_color="green"
        )
        self.boton_buscar.pack(padx=10, pady=10)

    def crear_tabla(self):
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
    
    def buscar(self):
        try:
            # Limpiar la tabla
            for widget in self.frame_tabla.winfo_children():
                if isinstance(widget, ctk.CTkLabel) and widget.grid_info()["row"] > 0:
                    widget.destroy()
            
            # Obtener el término de búsqueda
            termino = self.entrada_busqueda.get().strip()
            
            if not termino:
                raise ValueError("Ingrese un término de búsqueda")
            
            # Realizar la búsqueda según el tipo seleccionado
            if self.tipo_busqueda.get() == "id":
                try:
                    id_docente = int(termino)
                    docente = self.docente_controller.obtener_docente_por_id(id_docente)
                    if docente:
                        self.mostrar_docente(docente)
                    else:
                        raise ValueError(f"No se encontró profesor con ID {id_docente}")
                except ValueError:
                    raise ValueError("El ID debe ser un número entero")
            else:
                # Buscar por nombre
                docentes = self.docente_controller.listar_docentes()
                resultados = [
                    d for d in docentes 
                    if termino.lower() in d.nombre.lower() or 
                       termino.lower() in d.apellido.lower()
                ]
                
                if not resultados:
                    raise ValueError(f"No se encontraron profesores con el término '{termino}'")
                
                for i, docente in enumerate(resultados, start=1):
                    self.mostrar_docente(docente, i)
                    
        except Exception as e:
            # Mostrar mensaje de error
            ctk.CTkLabel(
                self.ventana,
                text=f"Error: {str(e)}",
                text_color="red"
            ).pack(pady=5)
    
    def mostrar_docente(self, docente, fila=1):
        # ID
        ctk.CTkLabel(
            self.frame_tabla,
            text=str(docente.id_profesor),
            width=150
        ).grid(row=fila, column=0, padx=5, pady=5)
        
        # Nombre
        ctk.CTkLabel(
            self.frame_tabla,
            text=docente.nombre,
            width=150
        ).grid(row=fila, column=1, padx=5, pady=5)
        
        # Apellido
        ctk.CTkLabel(
            self.frame_tabla,
            text=docente.apellido,
            width=150
        ).grid(row=fila, column=2, padx=5, pady=5)
        
        # Correo
        ctk.CTkLabel(
            self.frame_tabla,
            text=docente.correo_electronico,
            width=150
        ).grid(row=fila, column=3, padx=5, pady=5)
        
        # Teléfono
        ctk.CTkLabel(
            self.frame_tabla,
            text=docente.telefono,
            width=150
        ).grid(row=fila, column=4, padx=5, pady=5)
        
        # Especialidad
        ctk.CTkLabel(
            self.frame_tabla,
            text=docente.especialidad,
            width=150
        ).grid(row=fila, column=5, padx=5, pady=5)
        
        # Botón de selección
        ctk.CTkButton(
            self.frame_tabla,
            text="Seleccionar",
            command=lambda id=docente.id_profesor: self.seleccionar_docente(id),
            width=150
        ).grid(row=fila, column=6, padx=5, pady=5)
    
    def seleccionar_docente(self, id_docente):
        self.docente_encontrado = id_docente
        self.cerrar_ventana()
    
    def cambiar_tema(self):
        if ctk.get_appearance_mode() == "Dark":
            ctk.set_appearance_mode("Light")
        else:
            ctk.set_appearance_mode("Dark")
    
    def cerrar_ventana(self):
        self.ventana.destroy()
        self.ventana_principal.deiconify() 