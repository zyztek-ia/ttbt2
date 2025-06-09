import os
import argparse
from core.bot import TikTokBot
from threading import Thread
from api.app import app

def parse_args():
    parser = argparse.ArgumentParser(description="TikTok Bot")
    parser.add_argument("--mode", choices=["safe", "balanced", "aggressive"], default="balanced")
    parser.add_argument("--max-views", type=int, default=5000)
    parser.add_argument("--tiktok-username", type=str, default=None, help="TikTok username for login.")
    parser.add_argument("--tiktok-password", type=str, default=None, help="TikTok password for login.")
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
        # Pass CLI credentials to TikTokBot constructor
        bot = TikTokBot(tiktok_username=args.tiktok_username, tiktok_password=args.tiktok_password)
        if not bot.driver:
            print("Failed to initialize TikTokBot: Chrome driver not available.")
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
        print("Proceso principal del bot finalizado.")

    print("Flask API server is running. Main thread will wait for Flask to exit (Ctrl+C to stop API).")
    flask_thread.join() # Keep main thread alive for Flask
    print("Main thread exiting.")