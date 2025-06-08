import os
import argparse
from core.bot import TikTokBot
from threading import Thread
from api.app import app

def parse_args():
    parser = argparse.ArgumentParser(description="TikTok Bot")
    parser.add_argument("--mode", choices=["safe", "balanced", "aggressive"], default="balanced")
    parser.add_argument("--max-views", type=int, default=5000)
    return parser.parse_args()

def run_flask():
    # It's good practice to have a try-except here too for Flask startup
    try:
        print("Flask app thread started.")
        app.run(host='0.0.0.0', port=5000)
    except Exception as e:
        print(f"Flask app failed to start or crashed: {e}")


if __name__ == "__main__":
    args = parse_args()
    os.environ["MAX_VIEWS_PER_HOUR"] = str(args.max_views)

    print("Starting Flask API server...")
    flask_thread = Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()

    bot = None
    try:
        print(f"Iniciando TikTokBot en modo {args.mode}...")
        bot = TikTokBot() # This is where TikTokBot is initialized
        if not bot.driver:
            print("Failed to initialize TikTokBot: Chrome driver not available.")
            # No exit(1) here, allow API to continue running.
        else:
            print("TikTokBot initialized successfully.")
            print("Starting bot session...")
            bot.run_session()
            print("Bot session completed.")
    except Exception as e:
        print(f"Error crítico durante la sesión del bot: {str(e)}")
    finally:
        if bot and bot.driver:
            try:
                print("Cerrando WebDriver...")
                bot.driver.quit()
                print("WebDriver closed.")
            except Exception as cleanup_error:
                print(f"Error cerrando WebDriver: {cleanup_error}")
        print("Proceso principal del bot finalizado. El servidor API puede seguir ejecutándose si no es un hilo daemon o si el programa principal se mantiene vivo.")

    # Main thread will exit here if flask_thread is a daemon and bot session finished.
    # If API should run indefinitely, flask_thread.join() or another mechanism is needed.
    # For now, matching the previous logic of daemonized Flask thread.
    print("Main thread exiting.")