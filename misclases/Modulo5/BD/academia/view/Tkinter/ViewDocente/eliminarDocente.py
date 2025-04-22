import customtkinter as ctk
from controllers.docenteController import DocenteController
from view.Tkinter.ViewDocente.listarDocentes import ListarDocentes

class EliminarDocente:
    def __init__(self, ventana_docente):
        self.ventana_principal = ventana_docente["ventana"]
        self.tema = ventana_docente["tema"]
        self.db = ventana_docente["db"]
        self.docente_controller = DocenteController(self.db)
        
        self.ventana = ctk.CTk()
        self.ventana.title("Eliminar Profesores")
        
        # Configurar el tamaño de la ventana
        ancho_pantalla = self.ventana.winfo_screenwidth()
        alto_pantalla = self.ventana.winfo_screenheight()
        ancho_ventana = int(ancho_pantalla * 0.8)  # Aumentado el ancho
        alto_ventana = int(alto_pantalla * 0.6)
        
        # Centrar la ventana
        self.ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{int((ancho_pantalla - ancho_ventana) / 2)}+{int((alto_pantalla - alto_ventana) / 2)}")
        
        # Configurar el tema
        ctk.set_appearance_mode(self.tema)
        self.ventana.resizable(True, True)
        
        # Configurar el cierre de ventana
        self.ventana.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)
        
        # Crear el título
        self.titulo = ctk.CTkLabel(self.ventana, text="Eliminar Profesores", font=("Arial", 16))
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
        # Obtener los profesores
        docentes = self.docente_controller.listar_docentes()
        
        # Crear encabezados
        encabezados = ["ID", "Nombre", "Apellido", "Correo", "Teléfono", "Especialidad", "Eliminar"]
        for i, encabezado in enumerate(encabezados):
            label = ctk.CTkLabel(
                self.frame_tabla,
                text=encabezado,
                font=("Arial", 12, "bold"),
                width=150
            )
            label.grid(row=0, column=i, padx=5, pady=5, sticky="nsew")
        
        # Configurar el grid para que se expanda
        for i in range(7):  # 7 columnas (incluyendo especialidad)
            self.frame_tabla.grid_columnconfigure(i, weight=1)
        
        # Mostrar los profesores
        for i, docente in enumerate(docentes, start=1):
            # ID
            ctk.CTkLabel(
                self.frame_tabla,
                text=str(docente.id_profesor),
                width=150
            ).grid(row=i, column=0, padx=5, pady=5, sticky="nsew")
            
            # Nombre
            ctk.CTkLabel(
                self.frame_tabla,
                text=docente.nombre,
                width=150
            ).grid(row=i, column=1, padx=5, pady=5, sticky="nsew")
            
            # Apellido
            ctk.CTkLabel(
                self.frame_tabla,
                text=docente.apellido,
                width=150
            ).grid(row=i, column=2, padx=5, pady=5, sticky="nsew")
            
            # Correo
            ctk.CTkLabel(
                self.frame_tabla,
                text=docente.correo_electronico,
                width=150
            ).grid(row=i, column=3, padx=5, pady=5, sticky="nsew")
            
            # Teléfono
            ctk.CTkLabel(
                self.frame_tabla,
                text=docente.telefono,
                width=150
            ).grid(row=i, column=4, padx=5, pady=5, sticky="nsew")
            
            # Especialidad
            ctk.CTkLabel(
                self.frame_tabla,
                text=docente.especialidad,
                width=150
            ).grid(row=i, column=5, padx=5, pady=5, sticky="nsew")
            
            # Botón de eliminar
            boton_eliminar = ctk.CTkButton(
                self.frame_tabla,
                text="Eliminar",
                command=lambda id=docente.id_profesor: self.confirmar_eliminacion(id),
                fg_color="red",
                width=150
            )
            boton_eliminar.grid(row=i, column=6, padx=5, pady=5, sticky="nsew")
    
    def confirmar_eliminacion(self, id_docente):
        # Crear ventana de confirmación
        ventana_confirmacion = ctk.CTkToplevel(self.ventana)
        ventana_confirmacion.title("Confirmar Eliminación")
        ventana_confirmacion.geometry("300x150")
        ventana_confirmacion.resizable(False, False)
        
        # Centrar la ventana de confirmación
        ventana_confirmacion.transient(self.ventana)
        ventana_confirmacion.grab_set()
        
        # Mensaje de confirmación
        mensaje = ctk.CTkLabel(
            ventana_confirmacion,
            text="¿Está seguro que desea eliminar este profesor?",
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
            command=lambda: self.eliminar_docente(id_docente, ventana_confirmacion),
            fg_color="red"
        ).pack(side="left", padx=10)
        
        # Botón de cancelar
        ctk.CTkButton(
            frame_botones,
            text="No",
            command=ventana_confirmacion.destroy
        ).pack(side="left", padx=10)
    
    def eliminar_docente(self, id_docente, ventana_confirmacion):
        try:
            # Eliminar el profesor
            self.docente_controller.eliminar_docente(id_docente)
            
            # Cerrar la ventana de confirmación
            ventana_confirmacion.destroy()
            
            # Actualizar la tabla
            self.frame_tabla.destroy()
            self.frame_tabla = ctk.CTkFrame(self.scrollable_frame)
            self.frame_tabla.pack(fill="both", expand=True)
            self.crear_tabla()
            
        except Exception as e:
            # Mostrar mensaje de error
            ctk.CTkLabel(
                self.ventana,
                text=f"Error: {str(e)}",
                text_color="red"
            ).pack(pady=5)
    
    def cambiar_tema(self):
        if ctk.get_appearance_mode() == "Dark":
            ctk.set_appearance_mode("Light")
        else:
            ctk.set_appearance_mode("Dark")
    
    def cerrar_ventana(self):
        self.ventana.destroy()
        self.ventana_principal.deiconify() 