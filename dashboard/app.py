"""
Módulo principal de la aplicación web unificada (Dashboard y API).
Utiliza Flask para servir la interfaz de usuario y los endpoints de la API.
"""
from flask import Flask, render_template, jsonify
import os
from dashboard.api_config import bp_api_config
from dashboard.call_center import bp_call_center
from dashboard.gamification import bp_gamification

app = Flask(__name__, template_folder="templates")

# Registrar Blueprints
app.register_blueprint(bp_api_config)
app.register_blueprint(bp_call_center)
app.register_blueprint(bp_gamification)

from dashboard.ai import bp_ai
app.register_blueprint(bp_ai)

from dashboard.ethics import bp_ethics
app.register_blueprint(bp_ethics)

# Es necesario configurar una SECRET_KEY para que los mensajes flash funcionen.
app.config['SECRET_KEY'] = os.urandom(24)

# --- Rutas del Dashboard (Interfaz de Usuario) ---

@app.route("/")
def index():
    """Sirve la página principal del dashboard."""
    return render_template("index.html")

# --- Rutas de la API ---

@app.route("/api/status")
def status():
    """
    Endpoint de la API que devuelve el estado actual de los bots.
    (Actualmente con datos simulados).
    """
    # TODO: Integrar un sistema real para comprobar el estado de los bots.
    return jsonify({
        "bots_running": 3,
        "active_users": [],
        "status": "ok"
    })

# --- Ejecución ---

if __name__ == "__main__":
    # La aplicación se ejecuta desde main.py, no directamente.
    # Esta sección es para desarrollo y pruebas locales.
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
