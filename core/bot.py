from core.logger import get_logger

class Bot:
    def __init__(self, username, credentials):
        self.username = username
        self.credentials = credentials
        self.proxy = None
        self.fingerprint = None
        self.logger = get_logger(self.username)
        self.plugin_manager = None

    def assign_proxy(self, proxy):
        self.proxy = proxy
        self.logger.info(f"Proxy asignado: {proxy}")

    def assign_fingerprint(self, fingerprint):
        self.fingerprint = fingerprint
        self.logger.info(f"Fingerprint asignado: {fingerprint}")

    def set_plugin_manager(self, manager):
        self.plugin_manager = manager

    def run(self):
        self.logger.info("Iniciando bot...")
        # Lógica de login
        self.logger.info("Login exitoso.")
        if self.plugin_manager:
            self.plugin_manager.execute_hook("after_login", self)

        # Lógica principal del bot
        self.logger.info("Ejecutando tareas...")
        if self.plugin_manager:
            self.plugin_manager.execute_hook("before_logout", self)
        self.logger.info("Bot finalizado.")