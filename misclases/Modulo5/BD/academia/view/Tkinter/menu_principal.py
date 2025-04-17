import customtkinter as ctk
from view.Tkinter.ViewEstudiante.menuEstudiante import MenuEstudiante

# Crear clase de la ventana principal la cual se encarga de redireccionar 
# al usuario a la ventana que el usuario seleccione

class MenuPrincipal:
    def __init__(self, db):
        self.db = db
        self.ventana = ctk.CTk()
        self.ventana.title("Menu Principal")
        # obtener el tamaño de la pantalla
        ancho_pantalla = self.ventana.winfo_screenwidth()
        alto_pantalla = self.ventana.winfo_screenheight()

        # calcular el tamaño de la ventana
        ancho_ventana = int(ancho_pantalla * 0.3)
        alto_ventana = int(alto_pantalla * 0.50)

        self.ventana.geometry(f"{ancho_ventana}x{alto_ventana}")
        ctk.set_appearance_mode("Dark")  # "System" (sistema), "Light", "Dark"
        ctk.set_default_color_theme("blue")

        # Centrar la ventana en la pantalla
        self.ventana.geometry(f"+{int((ancho_pantalla - ancho_ventana) / 2)}+{int((alto_pantalla - alto_ventana) / 2)}")

        # Configuracion de restricciones de la ventana
        self.ventana.resizable(False, False)

        # Crear el tirulo de la ventana
        self.titulo = ctk.CTkLabel(self.ventana, text="Menu Principal", font=("Arial", 16))
        self.titulo.pack(pady=10)

        botones = [
            ("Estudiantes", self.abrir_menu_estudiantes),   
            ("Profesores", self.abrir_menu_profesores),
            ("Cursos", self.abrir_menu_cursos),
            ("Horarios", self.abrir_menu_horarios),
            ("Matriculas", self.abrir_menu_matriculas)
        ]
        
        for i, (texto, comando) in enumerate(botones):
            ctk.CTkButton(self.ventana, text=texto, command=comando).pack(pady=10)

        # Boton cambiar tema el boton de otro color 
        self.boton_cambiar_tema = ctk.CTkButton(self.ventana, text="Cambiar Tema", command=self.cambiar_tema, fg_color="black", text_color="white")
        self.boton_cambiar_tema.pack(pady=10)

    def cambiar_tema(self):
        if ctk.get_appearance_mode() == "Dark":
            ctk.set_appearance_mode("Light")
        else:
            ctk.set_appearance_mode("Dark")

    def abrir_menu_estudiantes(self):
        # Envia a la ventana de estudiante el tamaño de la ventana principal y el tema de la ventana principal como un dict
        ventana_estudiante = {
            "ventana": self.ventana,
            "tema": ctk.get_appearance_mode()
        }   
        self.ventana.withdraw()  # Ocultar la ventana principal
        self.ventana_estudiantes = MenuEstudiante(self.db, ventana_estudiante)
        self.ventana_estudiantes.ventana.mainloop()

    def abrir_menu_profesores(self):
        pass

    def abrir_menu_cursos(self):
        pass

    def abrir_menu_horarios(self):
        pass

    def abrir_menu_matriculas(self):
        pass

    def cerrar_ventana_estudiantes(self):
        self.ventana_estudiantes.ventana.destroy()
        self.ventana.deiconify()  # Mostrar la ventana principal nuevamente

    def cerrar_ventana_secundaria(self, ventana_secundaria):
        ventana_secundaria.destroy()
        self.ventana.deiconify()  # Mostrar la ventana principal nuevamente
            
