from core.bot import Bot
from core.logger import get_logger

logger = get_logger(__name__)

class BotEngine:
    def __init__(self, accounts, proxy_manager, fingerprint_manager):
        self.accounts = accounts
        self.proxy_manager = proxy_manager
        self.fingerprint_manager = fingerprint_manager
        self.bots = []

    def initialize_bots(self):
        for username, credentials in self.accounts.items():
            bot = Bot(username, credentials)
            proxy = self.proxy_manager.get_random_active_proxy()
            fingerprint = self.fingerprint_manager.get_fingerprint()
            bot.assign_proxy(proxy)
            bot.assign_fingerprint(fingerprint)
            self.bots.append(bot)
        logger.info(f"Se inicializaron {len(self.bots)} bots.")

    def run_all(self):
        # Aquí se podría implementar multithreading o multiprocessing
        for bot in self.bots:
            bot.run()