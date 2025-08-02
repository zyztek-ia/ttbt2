"""
Módulo principal del Bot.
Define la clase TikTokBot que encapsula la lógica de interacción con la plataforma.
"""
import os
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from core.account_manager import CoreAccountManager
from core.behavior import HumanBehaviorSimulator

class TikTokBot:
    """
    Representa un bot principal que interactúa con TikTok.
    Gestiona el driver de Selenium, la autenticación y las acciones orgánicas.
    """
    def __init__(self):
        """
        Inicializa el bot, el driver de Selenium y los gestores de comportamiento.
        """
        self.driver = self._init_driver()
        self.account_manager = CoreAccountManager()
        self.behavior = HumanBehaviorSimulator(self.driver)

    def _init_driver(self):
        """
        Configura e inicializa el driver de Selenium (Chrome) con opciones de evasión.
        """
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("user-agent=Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36")
        return webdriver.Chrome(options=options)

    def _authenticate(self):
        """
        Realiza el proceso de login en TikTok usando una cuenta del gestor.
        :return: True si la autenticación es exitosa, False en caso contrario.
        """
        account = self.account_manager.get_next_account()
        if not account or not account.get("email") or not account.get("password"):
            print("No se encontró ninguna cuenta válida en la base de datos.")
            return False
        try:
            self.driver.get("https://www.tiktok.com/login")
            self.behavior.random_delay(3, 5)

            # Llenar campos de login
            email_field = self.driver.find_element(By.NAME, "username")
            self.behavior.human_type(email_field, account['email'])

            pass_field = self.driver.find_element(By.NAME, "password")
            self.behavior.human_type(pass_field, account['password'])

            # Enviar formulario
            submit_btn = self.driver.find_element(By.XPATH, '//button[@type="submit"]')
            self.behavior.human_click(submit_btn)

            return True
        except Exception as e:
            print(f"Error de autenticación: {str(e)}")
            return False

    def run_session(self):
        """
        Inicia y ejecuta una sesión completa del bot.
        Intenta autenticarse y luego realiza acciones orgánicas.
        """
        if self._authenticate():
            self._perform_organic_actions()

    def _perform_organic_actions(self):
        """
        Bucle principal de acciones del bot, como ver videos, dar likes y hacer scroll.
        """
        max_views = int(os.getenv("MAX_VIEWS_PER_HOUR", "50"))
        for _ in range(max_views):
            self.behavior.watch_video()
            # 65% de probabilidad de like
            if random.random() < 0.65:
                self.behavior.like_video()
            self.behavior.random_scroll()
            time.sleep(random.uniform(8, 15))