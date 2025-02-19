"""
Tipos de eventos
# DEBUG: 
    - Informa detalladamente el diagnostico o el problema
# INFO:
    - Confirma que las cosas funcionan como esperaban
# WARNIG:
    - Indica que algo inesperadamente ocurrio o va a ocurrir (se rompio se va a romper)
# ERROR:
    - Un problema serio que afecta la funcionalidad(una funcion se cayo o se rompio)
# CRITTICAL 
    - Un error grave el programa ya no funcione
"""

import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logging.debug("Mensaje de depuración")
logging.warning("Mensaje de depuración")


