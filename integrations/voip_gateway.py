"""
Gateway para la integración con servicios de VOIP como Twilio.
Permite realizar y recibir llamadas, conectando al chatbot de voz.
"""
from flask import request
from twilio.twiml.voice_response import VoiceResponse
from modules.chatbot import SimpleRuleBasedChatbot

# Esta clase es un placeholder. En una implementación real, se usaría el cliente de Twilio.
class VoipGateway:
    """Gestiona la lógica para interactuar con un proveedor de VOIP."""
    def __init__(self):
        self.chatbot = SimpleRuleBasedChatbot()
        # En una implementación real, se inicializaría el cliente de Twilio aquí.
        # from twilio.rest import Client
        # self.client = Client(ACCOUNT_SID, AUTH_TOKEN)

    def make_outbound_call(self, to_number, message):
        """
        Realiza una llamada saliente (placeholder).
        :param to_number: El número de teléfono de destino.
        :param message: El mensaje inicial que el bot dirá.
        """
        print(f"Llamando a {to_number} con el mensaje: '{message}'")
        # Aquí iría la lógica para iniciar la llamada con Twilio:
        # self.client.calls.create(to=to_number, from_=TWILIO_NUMBER, twiml=f'<Response><Say>{message}</Say></Response>')
        return {"status": "success", "sid": "simulated_call_sid"}

# --- Endpoints de Webhook para Twilio ---

def handle_incoming_call():
    """
    Maneja una llamada entrante recibida a través de un webhook de Twilio.
    """
    response = VoiceResponse()
    response.say("Hola, bienvenido a TTBT2. ¿En qué puedo ayudarte?", voice='alice', language='es-ES')
    response.gather(input='speech', action='/handle-speech', speechTimeout='auto')
    return str(response)

def handle_speech_input():
    """
    Procesa la entrada de voz del usuario y devuelve una respuesta del chatbot.
    """
    speech_text = request.values.get('SpeechResult', '').lower()
    chatbot = SimpleRuleBasedChatbot()
    bot_response_text = chatbot.get_response(speech_text)

    response = VoiceResponse()
    response.say(bot_response_text, voice='alice', language='es-ES')

    # Si la conversación debe continuar, se puede volver a usar gather
    if "transferir" not in bot_response_text and "adios" not in bot_response_text:
        response.gather(input='speech', action='/handle-speech', speechTimeout='auto')
    else:
        response.hangup()

    return str(response)
