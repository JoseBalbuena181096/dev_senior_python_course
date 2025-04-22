import customtkinter as ctk
from view.Tkinter.ViewHorario.listarHorarios import ListarHorarios
from view.Tkinter.ViewHorario.registrarHorario import RegistrarHorario
from view.Tkinter.ViewHorario.buscarHorario import BuscarHorario
from view.Tkinter.ViewHorario.actualizarHorario import ActualizarHorario
from view.Tkinter.ViewHorario.eliminarHorario import EliminarHorario

class MenuHorario:
    def __init__(self, db, ventana_horario):
        self.db = db
        self.ventana_principal = ventana_horario["ventana"]
        self.tema = ventana_horario["tema"]
        self.ventana = ctk.CTk()
        self.ventana.title("Menú Horarios")

        # Configurar el cierre de ventana
        self.ventana.protocol("WM_DELETE_WINDOW", self.regresar_a_menu_principal)

        # Obtener el tamaño de la pantalla
        ancho_pantalla = self.ventana.winfo_screenwidth()
        alto_pantalla = self.ventana.winfo_screenheight()

        # Calcular el tamaño de la ventana
        ancho_ventana = int(ancho_pantalla * 0.3)
        alto_ventana = int(alto_pantalla * 0.60)

        # Centrar la ventana en la pantalla
        self.ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{int((ancho_pantalla - ancho_ventana) / 2)}+{int((alto_pantalla - alto_ventana) / 2)}")
        
        # Configurar el tema de la ventana
        ctk.set_appearance_mode(self.tema)
        self.ventana.resizable(False, False)

        # Título de la ventana
        self.titulo = ctk.CTkLabel(self.ventana, text="Menú Horarios", font=("Arial", 16))
        self.titulo.pack(pady=10)

        # Crear botones para las operaciones CRUD
        botones = [
            ("Registrar Horario", self.registrar_horario),
            ("Listar Horarios", self.listar_horarios),
            ("Buscar Horario", self.buscar_horario),
            ("Actualizar Horario", self.actualizar_horario),
            ("Eliminar Horario", self.eliminar_horario)
        ]

        for texto, comando in botones:
            ctk.CTkButton(self.ventana, text=texto, command=comando).pack(pady=10)

        # Botón para regresar a la ventana principal
        self.boton_regresar = ctk.CTkButton(self.ventana, text="Regresar", command=self.regresar_a_menu_principal, fg_color="black", text_color="white")
        self.boton_regresar.pack(pady=10)

        # Botón para cambiar el tema
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

    def registrar_horario(self):
        ventana_registrar = {
            "ventana": self.ventana,
            "tema": self.tema,
            "db": self.db
        }
        self.ventana_registrar = RegistrarHorario(ventana_registrar)
        self.ventana_registrar.ventana.mainloop()

    def listar_horarios(self):
        ventana_listar = {
            "ventana": self.ventana,
            "tema": self.tema,
            "db": self.db
        }
        self.ventana_listar = ListarHorarios(ventana_listar)
        self.ventana_listar.ventana.mainloop()

    def buscar_horario(self):
        ventana_buscar = {
            "ventana": self.ventana,
            "tema": self.tema,
            "db": self.db
        }
        self.ventana_buscar = BuscarHorario(ventana_buscar)
        self.ventana_buscar.ventana.mainloop()

    def actualizar_horario(self):
        ventana_actualizar = {
            "ventana": self.ventana,
            "tema": self.tema,
            "db": self.db
        }
        self.ventana_actualizar = ActualizarHorario(ventana_actualizar)
        self.ventana_actualizar.ventana.mainloop()

    def eliminar_horario(self):
        ventana_eliminar = {
            "ventana": self.ventana,
            "tema": self.tema,
            "db": self.db
        }
        self.ventana_eliminar = EliminarHorario(ventana_eliminar)
        self.ventana_eliminar.ventana.mainloop()
