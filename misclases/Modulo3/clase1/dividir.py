
def division_cero(numero1, numero2):
    """
    División por cero con captura de errores
    """
    try:
        resultado = numero1 / numero2
        print(resultado)
    except ZeroDivisionError as e:
        print("La división entre cero no se puede lograr")
        return None
    
division_cero(2, 0)

