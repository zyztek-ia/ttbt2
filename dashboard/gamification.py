"""
Blueprint de Flask para la sección de Gamificación.
Muestra el leaderboard de usuarios.
"""
from flask import Blueprint, render_template
from modules.gamification_manager import GamificationManager

bp_gamification = Blueprint('gamification', __name__, template_folder='templates')
manager = GamificationManager()

@bp_gamification.route("/gamification")
def leaderboard_page():
    """Muestra la página con el leaderboard de gamificación."""
    leaderboard_data = manager.get_leaderboard()
    return render_template("gamification.html", leaderboard=leaderboard_data)
