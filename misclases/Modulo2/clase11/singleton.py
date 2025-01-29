# Patron de diseño singleton

class SingletonCreacionInstancia:
    _instancia = None
    
    def __new__(cls, *args, **kwargs):
        if not cls._instancia:
            cls._instancia = super(SingletonCreacionInstancia, cls).__new__(cls)
        return cls._instancia

