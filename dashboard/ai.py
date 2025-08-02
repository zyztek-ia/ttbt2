"""
Blueprint de Flask para la sección de IA Generativa.
Permite a los usuarios interactuar con un futuro modelo de IA.
"""
from flask import Blueprint, render_template, request

bp_ai = Blueprint('ai', __name__, template_folder='templates')

@bp_ai.route("/ai", methods=['GET', 'POST'])
def ai_page():
    """
    Muestra la página de IA y maneja el envío de prompts.
    """
    bot_response = None
    if request.method == 'POST':
        prompt = request.form.get('prompt')
        # Placeholder para la lógica de IA
        # En una implementación real, aquí se llamaría a un modelo LLM.
        bot_response = f"He recibido tu prompt: '{prompt}'. Próximamente, un modelo de IA generará un flujo de bot basado en esto."

    return render_template("ai.html", bot_response=bot_response)
