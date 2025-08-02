"""
Blueprint de Flask para la interfaz del Call Center.
Permite iniciar llamadas y ver el estado de las comunicaciones.
"""
from flask import Blueprint, render_template, request, redirect, url_for, flash
from integrations.voip_gateway import VoipGateway, handle_incoming_call, handle_speech_input

bp_call_center = Blueprint('call_center', __name__, template_folder='templates')
gateway = VoipGateway()

@bp_call_center.route("/call-center")
def call_center_page():
    """Muestra la página principal del Call Center."""
    # En una implementación real, aquí se obtendría el historial de llamadas.
    call_history = [
        {"to": "+123456789", "status": "completed", "duration": "32s"},
        {"to": "+987654321", "status": "in-progress", "duration": "12s"}
    ]
    return render_template("call_center.html", history=call_history)

@bp_call_center.route("/call-center/make-call", methods=["POST"])
def make_call():
    """Endpoint para realizar una llamada saliente."""
    to_number = request.form.get("to_number")
    message = request.form.get("message")
    if to_number and message:
        result = gateway.make_outbound_call(to_number, message)
        flash(f"Llamada iniciada a {to_number}. SID: {result['sid']}", "success")
    else:
        flash("Número y mensaje son requeridos.", "error")
    return redirect(url_for("call_center.call_center_page"))

# Registrar los webhooks de Twilio
# Estos endpoints serán llamados por Twilio, no directamente por el usuario.
@bp_call_center.route("/webhook/incoming-call", methods=['POST'])
def webhook_incoming_call():
    return handle_incoming_call()

@bp_call_center.route("/webhook/handle-speech", methods=['POST'])
def webhook_handle_speech():
    return handle_speech_input()
