import json
import os
import yaml

class ConfigLoader:
    """
    Clase de utilidad para cargar configuraciones desde archivos JSON o YAML.
    """
    @staticmethod
    def load(path):
        """
        Carga un archivo de configuración desde una ruta dada.
        Soporta los formatos .json, .yml y .yaml.

        :param path: La ruta al archivo de configuración.
        :return: Un diccionario con la configuración, o un diccionario vacío si hay un error.
        """
        try:
            if path.endswith(".json"):
                with open(path, "r", encoding="utf-8") as f:
                    return json.load(f)
            elif path.endswith((".yml", ".yaml")):
                with open(path, "r", encoding="utf-8") as f:
                    return yaml.safe_load(f)
        except (IOError, json.JSONDecodeError, yaml.YAMLError):
            return {}
        return {}