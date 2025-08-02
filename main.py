"""
Punto de entrada principal para la aplicación TTBT2.
Este script se encarga de:
1. Parsear los argumentos de la línea de comandos.
2. Iniciar la aplicación web (Dashboard y API) en un hilo separado.
3. Iniciar la sesión del bot principal en el hilo principal.
"""
import os
import argparse
from threading import Thread
import time

from core.bot import TikTokBot
from dashboard.app import app

def parse_args():
    """Parsea los argumentos de la línea de comandos."""
    parser = argparse.ArgumentParser(description="TTBT2 - TikTok Bot Framework")
    parser.add_argument(
        "--mode",
        choices=["safe", "balanced", "aggressive"],
        default="balanced",
        help="Modo de operación del bot."
    )
    parser.add_argument(
        "--max-views",
        type=int,
        default=5000,
        help="Número máximo de visualizaciones por sesión."
    )
    return parser.parse_args()

def run_bot_session(args):
    """
    Inicializa y ejecuta una sesión completa del bot.
    Maneja la creación y cierre del driver.
    """
    os.environ["MAX_VIEWS_PER_HOUR"] = str(args.max_views)
    bot = None
    try:
        print(f"Iniciando bot en modo '{args.mode}'...")
        bot = TikTokBot()
        if not bot.driver:
            print("Error: No se pudo inicializar el driver de Chrome.")
            return
        bot.run_session()
    except Exception as e:
        print(f"Error crítico en la sesión del bot: {e}")
    finally:
        if bot and bot.driver:
            try:
                bot.driver.quit()
            except Exception as cleanup_error:
                print(f"Error al cerrar el driver: {cleanup_error}")
        print("Sesión del bot finalizada.")

def run_web_app():
    """Inicia la aplicación web Flask."""
    print("Iniciando la aplicación web en http://0.0.0.0:5000...")
    # Usar 'debug=False' para un entorno tipo producción
    app.run(host='0.0.0.0', port=5000, debug=False)

if __name__ == "__main__":
    cli_args = parse_args()

    # Iniciar la aplicación web en un hilo demonio
    web_thread = Thread(target=run_web_app, daemon=True)
    web_thread.start()

    # Pequeña pausa para que el servidor web inicie antes de que el bot
    # potencialmente termine.
    time.sleep(2)

    # Ejecutar la sesión del bot en el hilo principal
    run_bot_session(cli_args)

    print("Proceso principal finalizado.")
