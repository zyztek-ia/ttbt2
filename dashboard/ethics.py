"""
Blueprint de Flask para la sección de Auditoría y Ética.
Muestra los logs de auditoría estructurados.
"""
import json
import os
from flask import Blueprint, render_template

bp_ethics = Blueprint('ethics', __name__, template_folder='templates')
AUDIT_LOG_FILE = "logs/audit.log"

@bp_ethics.route("/ethics")
def ethics_page():
    """Muestra la página con el log de auditoría."""
    audit_logs = []
    if os.path.exists(AUDIT_LOG_FILE):
        with open(AUDIT_LOG_FILE, "r", encoding="utf-8") as f:
            for line in f:
                try:
                    # Cada línea es un objeto JSON
                    log_entry = json.loads(line)
                    audit_logs.append(log_entry)
                except json.JSONDecodeError:
                    continue # Ignorar líneas malformadas

    # Invertir para mostrar los más recientes primero
    audit_logs.reverse()

    return render_template("ethics.html", logs=audit_logs)
