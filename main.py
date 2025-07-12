from core.bot_engine import BotEngine
from core.account_manager import AccountManager
from proxies.proxy_manager import ProxyManager
from fingerprints.fingerprint_manager import FingerprintManager
from core.logger import get_logger

# Configuración de rutas
ACCOUNTS_FILE = 'accounts.json'
PROXIES_FILE = 'proxies/proxies.json'
FINGERPRINTS_FILE = 'fingerprints/fingerprints.json'

logger = get_logger(__name__)

def main():
    logger.info("Iniciando el framework TTBT1.")

    # Cargar componentes
    account_manager = AccountManager(ACCOUNTS_FILE)
    proxy_manager = ProxyManager(PROXIES_FILE)
    fingerprint_manager = FingerprintManager(FINGERPRINTS_FILE)

    accounts = account_manager.get_all_accounts()
    if not accounts:
        logger.error("No se encontraron cuentas. Saliendo.")
        return

    # Inicializar y ejecutar el motor de bots
    engine = BotEngine(accounts, proxy_manager, fingerprint_manager)
    engine.initialize_bots()
    engine.run_all()

    logger.info("Framework TTBT1 finalizado.")

if __name__ == '__main__':
    main()