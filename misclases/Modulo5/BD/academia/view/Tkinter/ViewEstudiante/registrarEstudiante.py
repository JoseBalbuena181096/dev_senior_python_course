import customtkinter as ctk
from controllers.estudiante_controller import EstudianteController
from view.Tkinter.ViewEstudiante.listarEstudiantes import ListarEstudiantes

class RegistrarEstudiante:
    def __init__(self, ventana_estudiante):
        self.ventana_principal = ventana_estudiante["ventana"]
        self.tema = ventana_estudiante["tema"]
        self.db = ventana_estudiante["db"]
        self.estudiante_controller = EstudianteController(self.db)
        
        self.ventana = ctk.CTk()
        self.ventana.title("Registrar Estudiante")
        
        # Configurar el tamaño de la ventana
        ancho_pantalla = self.ventana.winfo_screenwidth()
        alto_pantalla = self.ventana.winfo_screenheight()
        ancho_ventana = int(ancho_pantalla * 0.4)
        alto_ventana = int(alto_pantalla * 0.5)
        
        # Centrar la ventana
        self.ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{int((ancho_pantalla - ancho_ventana) / 2)}+{int((alto_pantalla - alto_ventana) / 2)}")
        
        # Configurar el tema
        ctk.set_appearance_mode(self.tema)
        self.ventana.resizable(False, False)
        
        # Configurar el cierre de ventana
        self.ventana.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)
        
        # Crear el título
        self.titulo = ctk.CTkLabel(self.ventana, text="Registrar Nuevo Estudiante", font=("Arial", 16))
        self.titulo.pack(pady=10)
        
        # Crear el frame para los campos
        self.frame_campos = ctk.CTkFrame(self.ventana)
        self.frame_campos.pack(padx=20, pady=10, fill="both", expand=True)
        
        # Crear los campos de entrada
        self.crear_campos()
        
        # Crear el frame para los botones
        self.frame_botones = ctk.CTkFrame(self.ventana)
        self.frame_botones.pack(padx=20, pady=10, fill="x")
        
        # Botón para registrar
        self.boton_registrar = ctk.CTkButton(
            self.frame_botones,
            text="Registrar",
            command=self.confirmar_registro,
            fg_color="green"
        )
        self.boton_registrar.pack(side="left", padx=5, pady=5)
        
        # Botón para regresar
        self.boton_regresar = ctk.CTkButton(
            self.frame_botones,
            text="Regresar",
            command=self.cerrar_ventana,
            fg_color="black",
            text_color="white"
        )
        self.boton_regresar.pack(side="right", padx=5, pady=5)
        
        # Botón para cambiar tema
        self.boton_cambiar_tema = ctk.CTkButton(
            self.ventana,
            text="Cambiar Tema",
            command=self.cambiar_tema,
            fg_color="black",
            text_color="white"
        )
        self.boton_cambiar_tema.pack(pady=10)
    
    def crear_campos(self):
        # Campos de entrada
        campos = [
            ("Nombre", "nombre"),
            ("Apellido", "apellido"),
            ("Correo", "correo"),
            ("Teléfono", "telefono")
        ]
        
        self.entradas = {}
        
        for i, (label_text, nombre_campo) in enumerate(campos):
            # Label
            ctk.CTkLabel(
                self.frame_campos,
                text=label_text,
                font=("Arial", 12)
            ).grid(row=i, column=0, padx=10, pady=5, sticky="w")
            
            # Campo de entrada
            entrada = ctk.CTkEntry(
                self.frame_campos,
                width=200
            )
            entrada.grid(row=i, column=1, padx=10, pady=5)
            self.entradas[nombre_campo] = entrada
    
    def confirmar_registro(self):
        try:
            # Obtener los valores de los campos
            nombre = self.entradas["nombre"].get()
            apellido = self.entradas["apellido"].get()
            correo = self.entradas["correo"].get()
            telefono = self.entradas["telefono"].get()
            
            # Validar que todos los campos estén llenos
            if not all([nombre, apellido, correo, telefono]):
                raise ValueError("Todos los campos son obligatorios")
            
            # Crear ventana de confirmación
            ventana_confirmacion = ctk.CTkToplevel(self.ventana)
            ventana_confirmacion.title("Confirmar Registro")
            ventana_confirmacion.geometry("300x150")
            ventana_confirmacion.resizable(False, False)
            
            # Centrar la ventana de confirmación
            ventana_confirmacion.transient(self.ventana)
            ventana_confirmacion.grab_set()
            
            # Mensaje de confirmación
            mensaje = ctk.CTkLabel(
                ventana_confirmacion,
                text="¿Está seguro que desea registrar este estudiante?",
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
                command=lambda: self.registrar_estudiante(nombre, apellido, correo, telefono, ventana_confirmacion),
                fg_color="green"
            ).pack(side="left", padx=10)
            
            # Botón de cancelar
            ctk.CTkButton(
                frame_botones,
                text="No",
                command=ventana_confirmacion.destroy
            ).pack(side="left", padx=10)
                
        except Exception as e:
            # Mostrar mensaje de error
            ctk.CTkLabel(
                self.ventana,
                text=f"Error: {str(e)}",
                text_color="red"
            ).pack(pady=5)
    
    def registrar_estudiante(self, nombre, apellido, correo, telefono, ventana_confirmacion):
        try:
            # Registrar el estudiante
            self.estudiante_controller.registrar_estudiante(nombre, apellido, correo, telefono)
            
            # Cerrar la ventana de confirmación
            ventana_confirmacion.destroy()
            
            # Cerrar la ventana actual
            self.ventana.destroy()
            
            # Abrir la ventana de listar estudiantes
            ventana_listar = {
                "ventana": self.ventana_principal,
                "tema": self.tema,
                "db": self.db
            }
            listar_estudiantes = ListarEstudiantes(ventana_listar)
            listar_estudiantes.ventana.mainloop()
            
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
