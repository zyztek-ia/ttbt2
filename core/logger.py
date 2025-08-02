"""
Módulo de configuración del logger para el proyecto.
Utiliza Loguru para un logging potente y configurable.
"""
from loguru import logger
import os

LOG_PATH = os.getenv("LOG_PATH", "logs/ttbt1.log")
os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)

# Logger estándar para la consola y el archivo de bot
logger.add(LOG_PATH, rotation="1 MB", retention="7 days", level="INFO", enqueue=True)
logger.add(lambda msg: print(msg, end=""), level="INFO")  # Console

# Logger de auditoría con formato JSON
AUDIT_LOG_PATH = "logs/audit.log"
logger.add(AUDIT_LOG_PATH, level="INFO", rotation="10 MB", compression="zip", serialize=True,
           filter=lambda record: "AUDIT" in record["extra"])

def get_logger(name=None):
    """
    Retorna la instancia del logger, opcionalmente ligada a un nombre.
    Para crear un log de auditoría, usar: logger.bind(AUDIT=True).info(...)
    """
    return logger.bind(name=name)