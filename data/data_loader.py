# Loader genérico para datos en formato JSON o YAML
# Todos los comentarios están en español.

import json
import yaml

class DataLoader:
    def __init__(self, data_file):
        """
        Inicializa el DataLoader e intenta cargar los datos.
        :param data_file: Ruta al archivo de datos.
        """
        self.data = self.load_data(data_file)

    def load_data(self, data_file):
        """
        Carga los datos del archivo según su extensión.
        :param data_file: Ruta al archivo.
        :return: Diccionario con los datos o {}.
        """
        try:
            with open(data_file, 'r', encoding='utf-8') as f:
                content = f.read()
                if not content.strip():
                    return {}
                if data_file.endswith('.json'):
                    return json.loads(content)
                elif data_file.endswith(('.yml', '.yaml')):
                    data = yaml.safe_load(content)
                    if not isinstance(data, dict):
                        return {}
                    return data
        except (FileNotFoundError, json.JSONDecodeError, yaml.YAMLError):
            return {}
        return {}