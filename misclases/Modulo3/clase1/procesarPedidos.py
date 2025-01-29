# App procesar pedidos
# Validar que el código del producto sea alfanumerico
# Validar que la cantidad se a mayor a cero

# Excepciones personalizadas << Último ejercicio >>


class ErrorDePago(Exception):
    """ Gestón de excepciones"""
    pass

class PasarelaDePago():
    """Simulación una estrategia tecnológica de pago"""
    
    @staticmethod
    def procesar_pago(numero_tarjeta, monto):
        
        if not numero_tarjeta.startswith("4"):
            raise ErrorDePago("El número de la tarjeta no es valido")
        if monto <= 0:
            raise ErrorDePago("El monto debe ser mayor a cero")
        
        return f"Pago de ${monto} fue procesado con éxito"

def procesar_pago_cliente(nombre_cliente, numero_tarjeta, monto):
    try:
        print(f"Iniciando el proceso de pago para {nombre_cliente}")
        resultado = PasarelaDePago.procesar_pago(numero_tarjeta, monto)
    except ErrorDePago as e:
        print(f"Error al procesar el pago. {e}")
    except Exception as e:
        print(f"Se produjo un error inesperado. {e}")
    else:
        print(resultado)
    finally:
        print("Registro finalizado")

if __name__ == "__main__":
    #procesar_pago_cliente("Jose", "432156", 99.80)
    #procesar_pago_cliente("Luis", "12345", 100)
    procesar_pago_cliente("Carolina", "456789", 0)
    