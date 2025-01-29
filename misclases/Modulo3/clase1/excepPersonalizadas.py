# Excepciones personalizadas

class ErrorProductoNoDisponible(Exception):
    def __init__(self, message = "El producto no esta en stock"):
        self.message = message
        