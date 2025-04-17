from view.menu import menu_principal
from view.menuDocente import menu_docente
from view.menuCursos import menu_cursos
from view.menu_horario import menu_horario
from view.menu_matricula import menu_matricula
from view.Tkinter.menu_principal import MenuPrincipal
from config.database import Database

if __name__ == "__main__":
    db = Database()
    try:
        #menu_principal(db)
        #menu_docente(db)
        #menu_cursos(db)
        #menu_horario(db)
        #menu_matricula(db)
        menu_principal = MenuPrincipal(db)
        menu_principal.ventana.mainloop()
    finally: 
        db.close()