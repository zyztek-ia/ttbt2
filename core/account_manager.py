import json
from core.logger import get_logger

logger = get_logger(__name__)

class AccountManager:
    def __init__(self, accounts_file):
        self.accounts_file = accounts_file
        self.accounts = self.load_accounts()

    def load_accounts(self):
        try:
            with open(self.accounts_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.error(f"El archivo de cuentas no se encontró en: {self.accounts_file}")
            return {}
        except json.JSONDecodeError:
            logger.error(f"Error al decodificar el JSON en: {self.accounts_file}")
            return {}

    def get_account(self, username):
        return self.accounts.get(username)

    def get_all_accounts(self):
        return self.accounts