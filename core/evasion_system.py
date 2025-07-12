# core/evasion_system.py
from .evasion import Evasion

class EvasionSystem:
    """
    Sistema de evasión que aplica fingerprints y proxies a los bots.
    """
    def __init__(self, fingerprints, proxies):
        self.evasion = Evasion(fingerprints, proxies)

    def apply_evasion(self, bot):
        """
        Aplica un fingerprint y un proxy a un bot.
        """
        bot.fingerprint = self.evasion.rotate_fingerprint()
        bot.proxy = self.evasion.rotate_proxy()