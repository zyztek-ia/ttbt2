"""
Módulo para la gestión de cuentas de usuario.
Permite añadir y recuperar cuentas para ser usadas por los bots.
"""
class CoreAccountManager:
    """Gestiona una lista de cuentas de usuario en memoria."""
    def __init__(self):
        """Inicializa el gestor de cuentas con una lista vacía."""
        self.accounts = []

    def add_account(self, email, password):
        """
        Añade una nueva cuenta a la lista.
        :param email: El email o nombre de usuario.
        :param password: La contraseña de la cuenta.
        """
        self.accounts.append({"email": email, "password": password})

    def get_next_account(self):
        """
        Obtiene la siguiente cuenta disponible.
        Actualmente, siempre devuelve la primera cuenta de la lista.
        :return: Un diccionario con los datos de la cuenta, o None si no hay cuentas.
        """
        if not self.accounts:
            return None
        return self.accounts[0]