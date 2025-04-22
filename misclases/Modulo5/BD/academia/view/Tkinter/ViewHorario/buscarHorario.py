import customtkinter as ctk
from controllers.horario_controller import HorarioController
from tkinter import messagebox

class BuscarHorario:
    def __init__(self, ventana_horario):
        self.ventana_principal = ventana_horario["ventana"]
        self.tema = ventana_horario["tema"]
        self.db = ventana_horario["db"]
        self.horario_controller = HorarioController(self.db)
        
        self.ventana = ctk.CTk()
        self.ventana.title("Buscar Horario")
        
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
        self.titulo = ctk.CTkLabel(self.ventana, text="Buscar Horario", font=("Arial", 16))
        self.titulo.pack(pady=10)
        
        # Crear el frame principal
        self.frame_principal = ctk.CTkFrame(self.ventana)
        self.frame_principal.pack(padx=20, pady=10, fill="both", expand=True)
        
        # Crear los campos de búsqueda
        self.crear_campos_busqueda()
        
        # Frame para mostrar resultados
        self.frame_resultados = ctk.CTkFrame(self.ventana)
        self.frame_resultados.pack(padx=20, pady=10, fill="both", expand=True)
        
        # Botón para buscar
        self.boton_buscar = ctk.CTkButton(
            self.ventana,
            text="Buscar",
            command=self.buscar_horario,
            fg_color="blue",
            text_color="white"
        )
        self.boton_buscar.pack(pady=10)
        
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
        # Campo para buscar por curso
        ctk.CTkLabel(
            self.frame_principal,
            text="Buscar por curso:",
            font=("Arial", 12)
        ).pack(pady=5)
        self.entry_curso = ctk.CTkEntry(self.frame_principal, width=300)
        self.entry_curso.pack(pady=5)
        
        # Campo para buscar por día
        ctk.CTkLabel(
            self.frame_principal,
            text="Buscar por día:",
            font=("Arial", 12)
        ).pack(pady=5)
        self.entry_dia = ctk.CTkEntry(self.frame_principal, width=300)
        self.entry_dia.pack(pady=5)
    
    def buscar_horario(self):
        # Obtener los criterios de búsqueda
        curso = self.entry_curso.get()
        dia = self.entry_dia.get()
        
        # Validar que al menos un criterio esté presente
        if not curso and not dia:
            messagebox.showerror("Error", "Debe ingresar al menos un criterio de búsqueda")
            return
        
        try:
            # Buscar horarios
            resultados = self.horario_controller.buscar_horarios(curso, dia)
            
            # Limpiar resultados anteriores
            for widget in self.frame_resultados.winfo_children():
                widget.destroy()
            
            if not resultados:
                ctk.CTkLabel(
                    self.frame_resultados,
                    text="No se encontraron horarios",
                    font=("Arial", 12)
                ).pack(pady=10)
                return
            
            # Mostrar resultados
            for horario in resultados:
                frame_horario = ctk.CTkFrame(self.frame_resultados)
                frame_horario.pack(pady=5, padx=10, fill="x")
                
                info = f"Curso: {horario.nombre_curso} | Día: {horario.dia_semana} | Hora: {horario.hora_inicio} - {horario.hora_fin}"
                ctk.CTkLabel(
                    frame_horario,
                    text=info,
                    font=("Arial", 12)
                ).pack(pady=5)
        
        except Exception as e:
            messagebox.showerror("Error", f"Error al buscar horarios: {str(e)}")
    
    def cambiar_tema(self):
        if ctk.get_appearance_mode() == "Dark":
            ctk.set_appearance_mode("Light")
        else:
            ctk.set_appearance_mode("Dark")
    
    def cerrar_ventana(self):
        self.ventana.destroy()
        self.ventana_principal.deiconify() 