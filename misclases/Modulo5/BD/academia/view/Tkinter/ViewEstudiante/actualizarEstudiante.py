import customtkinter as ctk
from controllers.estudiante_controller import EstudianteController
from view.Tkinter.ViewEstudiante.listarEstudiantes import ListarEstudiantes

class ActualizarEstudiante:
    def __init__(self, ventana_estudiante):
        self.ventana_principal = ventana_estudiante["ventana"]
        self.tema = ventana_estudiante["tema"]
        self.db = ventana_estudiante["db"]
        self.estudiante_controller = EstudianteController(self.db)
        
        self.ventana = ctk.CTk()
        self.ventana.title("Actualizar Estudiantes")
        
        # Configurar el tamaño de la ventana
        ancho_pantalla = self.ventana.winfo_screenwidth()
        alto_pantalla = self.ventana.winfo_screenheight()
        ancho_ventana = int(ancho_pantalla * 0.8)
        alto_ventana = int(alto_pantalla * 0.6)
        
        # Centrar la ventana
        self.ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{int((ancho_pantalla - ancho_ventana) / 2)}+{int((alto_pantalla - alto_ventana) / 2)}")
        
        # Configurar el tema
        ctk.set_appearance_mode(self.tema)
        self.ventana.resizable(True, True)
        
        # Configurar el cierre de ventana
        self.ventana.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)
        
        # Crear el título
        self.titulo = ctk.CTkLabel(self.ventana, text="Actualizar Estudiantes", font=("Arial", 16))
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
        
        # Frame para los botones inferiores
        self.frame_botones = ctk.CTkFrame(self.ventana)
        self.frame_botones.pack(pady=10)
        
        # Botón para regresar
        self.boton_regresar = ctk.CTkButton(
            self.frame_botones, 
            text="Regresar", 
            command=self.cerrar_ventana,
            fg_color="black",
            text_color="white",
            width=150
        )
        self.boton_regresar.pack(side="left", padx=10)
        
        # Botón para cambiar tema
        self.boton_cambiar_tema = ctk.CTkButton(
            self.frame_botones,
            text="Cambiar Tema",
            command=self.cambiar_tema,
            fg_color="black",
            text_color="white",
            width=150
        )
        self.boton_cambiar_tema.pack(side="left", padx=10)
    
    def crear_tabla(self):
        # Obtener los estudiantes
        estudiantes = self.estudiante_controller.listar_estudiantes()
        
        # Crear encabezados
        encabezados = ["ID", "Nombre", "Apellido", "Correo", "Teléfono", "Actualizar"]
        for i, encabezado in enumerate(encabezados):
            label = ctk.CTkLabel(
                self.frame_tabla,
                text=encabezado,
                font=("Arial", 12, "bold"),
                width=150
            )
            label.grid(row=0, column=i, padx=5, pady=5, sticky="nsew")
        
        # Configurar el grid para que se expanda
        for i in range(6):  # 6 columnas
            self.frame_tabla.grid_columnconfigure(i, weight=1)
        
        # Mostrar los estudiantes
        for i, estudiante in enumerate(estudiantes, start=1):
            # ID
            ctk.CTkLabel(
                self.frame_tabla,
                text=str(estudiante.id_estudiante),
                width=150
            ).grid(row=i, column=0, padx=5, pady=5, sticky="nsew")
            
            # Nombre
            ctk.CTkLabel(
                self.frame_tabla,
                text=estudiante.nombre,
                width=150
            ).grid(row=i, column=1, padx=5, pady=5, sticky="nsew")
            
            # Apellido
            ctk.CTkLabel(
                self.frame_tabla,
                text=estudiante.apellido,
                width=150
            ).grid(row=i, column=2, padx=5, pady=5, sticky="nsew")
            
            # Correo
            ctk.CTkLabel(
                self.frame_tabla,
                text=estudiante.correo,
                width=150
            ).grid(row=i, column=3, padx=5, pady=5, sticky="nsew")
            
            # Teléfono
            ctk.CTkLabel(
                self.frame_tabla,
                text=estudiante.telefono,
                width=150
            ).grid(row=i, column=4, padx=5, pady=5, sticky="nsew")
            
            # Botón de actualizar
            boton_actualizar = ctk.CTkButton(
                self.frame_tabla,
                text="Actualizar",
                command=lambda id=estudiante.id_estudiante: self.abrir_ventana_actualizacion(id),
                fg_color="green",
                width=150
            )
            boton_actualizar.grid(row=i, column=5, padx=5, pady=5, sticky="nsew")
    
    def abrir_ventana_actualizacion(self, id_estudiante):
        # Obtener los datos del estudiante
        estudiante = self.estudiante_controller.obtener_estudiante_por_id(id_estudiante)
        
        # Crear ventana de actualización
        ventana_actualizacion = ctk.CTkToplevel(self.ventana)
        ventana_actualizacion.title("Actualizar Estudiante")
        ventana_actualizacion.geometry("400x300")
        ventana_actualizacion.resizable(False, False)
        
        # Centrar la ventana
        ventana_actualizacion.transient(self.ventana)
        ventana_actualizacion.grab_set()
        
        # Frame para los campos
        frame_campos = ctk.CTkFrame(ventana_actualizacion)
        frame_campos.pack(padx=20, pady=20, fill="both", expand=True)
        
        # Campos de actualización
        campos = [
            ("Nombre:", estudiante.nombre),
            ("Apellido:", estudiante.apellido),
            ("Correo:", estudiante.correo),
            ("Teléfono:", estudiante.telefono)
        ]
        
        self.entradas = {}
        for i, (label_text, valor) in enumerate(campos):
            # Label
            ctk.CTkLabel(
                frame_campos,
                text=label_text,
                font=("Arial", 12)
            ).grid(row=i, column=0, padx=10, pady=5, sticky="w")
            
            # Entry
            entrada = ctk.CTkEntry(frame_campos, width=200)
            entrada.insert(0, valor)
            entrada.grid(row=i, column=1, padx=10, pady=5)
            self.entradas[label_text] = entrada
        
        # Frame para los botones
        frame_botones = ctk.CTkFrame(ventana_actualizacion)
        frame_botones.pack(pady=10)
        
        # Botón de actualizar
        ctk.CTkButton(
            frame_botones,
            text="Actualizar",
            command=lambda: self.confirmar_actualizacion(id_estudiante, ventana_actualizacion),
            fg_color="green"
        ).pack(side="left", padx=10)
        
        # Botón de cancelar
        ctk.CTkButton(
            frame_botones,
            text="Cancelar",
            command=ventana_actualizacion.destroy
        ).pack(side="left", padx=10)
    
    def confirmar_actualizacion(self, id_estudiante, ventana_actualizacion):
        # Crear ventana de confirmación
        ventana_confirmacion = ctk.CTkToplevel(ventana_actualizacion)
        ventana_confirmacion.title("Confirmar Actualización")
        ventana_confirmacion.geometry("300x150")
        ventana_confirmacion.resizable(False, False)
        
        # Centrar la ventana de confirmación
        ventana_confirmacion.transient(ventana_actualizacion)
        ventana_confirmacion.grab_set()
        
        # Mensaje de confirmación
        mensaje = ctk.CTkLabel(
            ventana_confirmacion,
            text="¿Está seguro que desea actualizar este estudiante?",
            font=("Arial", 12)
        )
        mensaje.pack(pady=20)
        
        # Frame para los botones
        frame_botones = ctk.CTkFrame(ventana_confirmacion)
        frame_botones.pack(pady=10)
        
        # Botón de confirmar
        ctk.CTkButton(
            frame_botones,
            text="Sí",
            command=lambda: self.actualizar_estudiante(id_estudiante, ventana_actualizacion, ventana_confirmacion),
            fg_color="green"
        ).pack(side="left", padx=10)
        
        # Botón de cancelar
        ctk.CTkButton(
            frame_botones,
            text="No",
            command=ventana_confirmacion.destroy
        ).pack(side="left", padx=10)
    
    def actualizar_estudiante(self, id_estudiante, ventana_actualizacion, ventana_confirmacion):
        # Obtener los nuevos valores
        nombre = self.entradas["Nombre:"].get()
        apellido = self.entradas["Apellido:"].get()
        correo = self.entradas["Correo:"].get()
        telefono = self.entradas["Teléfono:"].get()
        
        # Actualizar el estudiante
        self.estudiante_controller.actualizar_estudiante(id_estudiante, nombre, apellido, correo, telefono)
        
        # Cerrar las ventanas
        ventana_confirmacion.destroy()
        ventana_actualizacion.destroy()
        
        # Actualizar la tabla
        self.frame_tabla.destroy()
        self.frame_tabla = ctk.CTkFrame(self.scrollable_frame)
        self.frame_tabla.pack(fill="both", expand=True)
        self.crear_tabla()
    
    def cambiar_tema(self):
        if ctk.get_appearance_mode() == "Dark":
            ctk.set_appearance_mode("Light")
        else:
            ctk.set_appearance_mode("Dark")
    
    def cerrar_ventana(self):
        self.ventana.destroy()
        self.ventana_principal.deiconify()
