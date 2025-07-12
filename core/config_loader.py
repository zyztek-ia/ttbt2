import json
import yaml
from core.logger import get_logger

logger = get_logger(__name__)

def load_config(file_path):
    try:
        with open(file_path, 'r') as f:
            if file_path.endswith('.json'):
                return json.load(f)
            elif file_path.endswith(('.yml', '.yaml')):
                return yaml.safe_load(f)
            else:
                logger.warning(f"Formato de archivo no soportado para: {file_path}")
                return None
    except FileNotFoundError:
        logger.error(f"Archivo de configuración no encontrado: {file_path}")
        return None
    except Exception as e:
        logger.error(f"Error al cargar la configuración desde {file_path}: {e}")
        return None