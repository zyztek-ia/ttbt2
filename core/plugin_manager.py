import importlib.util
import sys
import os

"""
Módulo para la gestión de plugins.
Permite cargar y ejecutar dinámicamente plugins externos.
"""
class PluginManager:
    """Gestiona la carga y ejecución de plugins dinámicos."""
    def __init__(self):
        """Inicializa el gestor de plugins."""
        self.hooks = {}

    def load_plugin(self, plugin_path):
        """
        Carga un plugin desde una ruta de archivo.
        :param plugin_path: La ruta al archivo .py del plugin.
        """
        if not os.path.isfile(plugin_path):
            return
        spec = importlib.util.spec_from_file_location("plugin", plugin_path)
        plugin = importlib.util.module_from_spec(spec)
        sys.modules["plugin"] = plugin
        spec.loader.exec_module(plugin)
        for attr in dir(plugin):
            if not attr.startswith("_"):
                self.hooks[attr] = getattr(plugin, attr)

    def execute_hook(self, hook_name, *args, **kwargs):
        """
        Ejecuta un 'hook' (función) si ha sido cargado.
        :param hook_name: El nombre de la función a ejecutar.
        :param args: Argumentos posicionales a pasar al hook.
        :param kwargs: Argumentos de palabra clave a pasar al hook.
        """
        if hook_name in self.hooks:
            return self.hooks[hook_name](*args, **kwargs)