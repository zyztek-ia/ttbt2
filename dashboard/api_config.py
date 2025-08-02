"""
Blueprint de Flask para la página de configuración de APIs.
Permite a los usuarios ver, añadir y conectar APIs externas.
"""
from flask import Blueprint, render_template, request, redirect, url_for
from plugins.api_discovery_manager import ApiDiscoveryManager

bp_api_config = Blueprint('api_config', __name__, template_folder='templates')
manager = ApiDiscoveryManager()

@bp_api_config.route("/api-config")
def config_page():
    """Muestra la página principal de configuración de APIs."""
    available_apis = manager.discover_public_apis()
    connected_apis = manager.get_all_configs()

    # Unir información de APIs disponibles y conectadas
    for name, details in available_apis.items():
        if name in connected_apis:
            details["status"] = connected_apis[name].get("status", "connected")
            details["config"] = connected_apis[name]

    return render_template("api_config.html", apis=available_apis)

@bp_api_config.route("/api-config/add", methods=["POST"])
def add_manual_api():
    """Endpoint para añadir una API manualmente a través de un formulario."""
    name = request.form.get("name")
    endpoint = request.form.get("endpoint")
    api_key = request.form.get("api_key")
    if name and endpoint and api_key:
        manager.add_api_manual(name, endpoint, api_key)
    return redirect(url_for("api_config.config_page"))

@bp_api_config.route("/api-config/connect/<service_name>")
def connect_oauth_api(service_name):
    """Endpoint para iniciar el flujo de conexión OAuth."""
    manager.start_oauth_flow(service_name)
    return redirect(url_for("api_config.config_page"))
