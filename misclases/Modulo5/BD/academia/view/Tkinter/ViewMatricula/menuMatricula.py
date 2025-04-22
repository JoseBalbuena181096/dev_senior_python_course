import customtkinter as ctk
from view.Tkinter.ViewMatricula.listarMatriculas import ListarMatriculas
from view.Tkinter.ViewMatricula.registrarMatricula import RegistrarMatricula
from view.Tkinter.ViewMatricula.buscarMatricula import BuscarMatricula
from view.Tkinter.ViewMatricula.actualizarMatricula import ActualizarMatricula
from view.Tkinter.ViewMatricula.eliminarMatricula import EliminarMatricula

class MenuMatricula:
    def __init__(self, db, ventana_matricula):
        self.db = db
        self.ventana_principal = ventana_matricula["ventana"]
        self.tema = ventana_matricula["tema"]
        self.ventana = ctk.CTk()
        self.ventana.title("Menú Matrículas")

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
        self.titulo = ctk.CTkLabel(self.ventana, text="Menú Matrículas", font=("Arial", 16))
        self.titulo.pack(pady=10)

        # Crear botones para las operaciones CRUD
        botones = [
            ("Registrar Matrícula", self.registrar_matricula),
            ("Listar Matrículas", self.listar_matriculas),
            ("Buscar Matrícula", self.buscar_matricula),
            ("Actualizar Matrícula", self.actualizar_matricula),
            ("Eliminar Matrícula", self.eliminar_matricula)
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

    def registrar_matricula(self):
        ventana_registrar = {
            "ventana": self.ventana,
            "tema": self.tema,
            "db": self.db
        }
        self.ventana_registrar = RegistrarMatricula(ventana_registrar)
        self.ventana_registrar.ventana.mainloop()

    def listar_matriculas(self):
        ventana_listar = {
            "ventana": self.ventana,
            "tema": self.tema,
            "db": self.db
        }
        self.ventana_listar = ListarMatriculas(ventana_listar)
        self.ventana_listar.ventana.mainloop()

    def buscar_matricula(self):
        ventana_buscar = {
            "ventana": self.ventana,
            "tema": self.tema,
            "db": self.db
        }
        self.ventana_buscar = BuscarMatricula(ventana_buscar)
        self.ventana_buscar.ventana.mainloop()

    def actualizar_matricula(self):
        ventana_actualizar = {
            "ventana": self.ventana,
            "tema": self.tema,
            "db": self.db
        }
        self.ventana_actualizar = ActualizarMatricula(ventana_actualizar)
        self.ventana_actualizar.ventana.mainloop()

    def eliminar_matricula(self):
        ventana_eliminar = {
            "ventana": self.ventana,
            "tema": self.tema,
            "db": self.db
        }
        self.ventana_eliminar = EliminarMatricula(ventana_eliminar)
        self.ventana_eliminar.ventana.mainloop()
