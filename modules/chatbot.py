"""
Módulo del Chatbot.
Define un chatbot simple basado en reglas para interactuar con los usuarios.
"""

class SimpleRuleBasedChatbot:
    """
    Un chatbot que responde a preguntas predefinidas.
    """
    def __init__(self):
        self.rules = {
            "hola": "¡Hola! ¿Cómo puedo ayudarte hoy?",
            "precio": "Nuestros precios son flexibles. ¿Puedes contarme más sobre tus necesidades?",
            "soporte": "Claro, te estoy transfiriendo a un agente de soporte.",
            "adios": "¡Gracias por contactarnos! Que tengas un buen día."
        }
        self.default_response = "No he entendido tu pregunta. ¿Puedes reformularla?"

    def get_response(self, user_message):
        """
        Obtiene una respuesta del bot basada en el mensaje del usuario.
        :param user_message: El mensaje del usuario en minúsculas.
        :return: La respuesta del bot.
        """
        user_message = user_message.lower()
        for keyword, response in self.rules.items():
            if keyword in user_message:
                return response
        return self.default_response
