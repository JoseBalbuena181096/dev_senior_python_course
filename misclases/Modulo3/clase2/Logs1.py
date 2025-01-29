import logging


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s %(message)s'
)

logging.debug("Este es mensaje del DEBUG")
logging.info("Este es mensaje del info")
logging.warning("Este es mensaje del warning")
logging.error("Este es mensaje del error")
logging.critical("Este es mensaje del critico")