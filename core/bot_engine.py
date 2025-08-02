"""
Módulo del motor de bots.
Define la clase BotEngine, responsable de ejecutar y gestionar un bot.
"""
class BotEngine:
    """Orquesta la ejecución de una instancia de un bot."""
    def __init__(self, bot):
        """
        Inicializa el motor con una instancia de bot.
        :param bot: La instancia del bot a ejecutar.
        """
        self.bot = bot

    def run(self):
        """Inicia la ejecución de la sesión del bot."""
        self.bot.run_session()