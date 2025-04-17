import customtkinter as ctk
from view.Tkinter.ViewEstudiante.listarEstudiantes import ListarEstudiantes
from view.Tkinter.ViewEstudiante.registrarEstudiante import RegistrarEstudiante
from view.Tkinter.ViewEstudiante.buscarEstudiante import BuscarEstudiante


class MenuEstudiante:
    def __init__(self, db, ventana_estudiante ):
        self.db = db
        self.ventana_principal = ventana_estudiante["ventana"]
        self.tema = ventana_estudiante["tema"]
        self.ventana = ctk.CTk()
        self.ventana.title("Menu Estudiantes")

        # configurar el cierre de ventana
        self.ventana.protocol("WM_DELETE_WINDOW", self.regresar_a_menu_principal)

        # obtener el tamaño de la pantalla
        ancho_pantalla = self.ventana.winfo_screenwidth()
        alto_pantalla = self.ventana.winfo_screenheight()

        # calcular el tamaño de la ventana
        ancho_ventana = int(ancho_pantalla * 0.3)
        alto_ventana = int(alto_pantalla * 0.60)

        # centrar la ventana en la pantalla
        self.ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{int((ancho_pantalla - ancho_ventana) / 2)}+{int((alto_pantalla - alto_ventana) / 2)}")
        
        # Configurar el tema de la ventana
        ctk.set_appearance_mode(self.tema)
        self.ventana.resizable(False, False)

        # Configurar el tema de la ventana
        self.titulo = ctk.CTkLabel(self.ventana, text="Menu Estudiantes", font=("Arial", 16))
        self.titulo.pack(pady=10)

        # Crear botones para las operaciones CRUD
        botones = [
            ("Registrar Estudiante", self.registrar_estudiante),
            ("Listar Estudiantes", self.listar_estudiantes),
            ("Buscar Estudiante", self.buscar_estudiante),
            ("Actualizar Estudiante", self.actualizar_estudiante),
            ("Eliminar Estudiante", self.eliminar_estudiante)
        ]

        for i, (texto, comando) in enumerate(botones):
            ctk.CTkButton(self.ventana, text=texto, command=comando).pack(pady=10)

        
        # Boton para regresar a la ventana principal con un color de fondo y un color de texto
        self.boton_regresar = ctk.CTkButton(self.ventana, text="Regresar", command=self.regresar_a_menu_principal, fg_color="black", text_color="white")
        self.boton_regresar.pack(pady=10)

        # Boton para cambiar el tema de la ventana y enviar el tema a la ventana principal
        self.boton_cambiar_tema = ctk.CTkButton(self.ventana, text="Cambiar Tema", command=self.cambiar_tema, fg_color="black", text_color="white")
        self.boton_cambiar_tema.pack(pady=10)

    def cambiar_tema(self):
        if ctk.get_appearance_mode() == "Dark":
            ctk.set_appearance_mode("Light")
        else:
            ctk.set_appearance_mode("Dark")

    def regresar_a_menu_principal(self):
        self.ventana.destroy()
        if self.ventana_principal:
            self.ventana_principal.deiconify()

    def registrar_estudiante(self):
        # Crear una ventana para registrar un estudiante
        ventana_registrar_estudiante = {
            "ventana": self.ventana,
            "tema": self.tema,
            "db": self.db
        }
        self.ventana_registrar_estudiante = RegistrarEstudiante(ventana_registrar_estudiante)
        self.ventana_registrar_estudiante.ventana.mainloop()
        
    def listar_estudiantes(self):
        # Crear una ventana para listar los estudiantes  llama a la ventana de listar estudiantes y le pasa el tema del estudiante y mandar la base de datos
        ventana_listar_estudiantes = {
            "ventana": self.ventana,
            "tema": self.tema,
            "db": self.db
        }
        self.ventana_listar_estudiantes = ListarEstudiantes(ventana_listar_estudiantes)
        self.ventana_listar_estudiantes.ventana.mainloop()
        

    def buscar_estudiante(self):
        # Crear una ventana para buscar un estudiante
        ventana_buscar_estudiante = {
            "ventana": self.ventana,
            "tema": self.tema,
            "db": self.db
        }
        self.ventana_buscar_estudiante = BuscarEstudiante(ventana_buscar_estudiante)
        self.ventana_buscar_estudiante.ventana.mainloop()

    def actualizar_estudiante(self):
        pass

    def eliminar_estudiante(self):
        pass

