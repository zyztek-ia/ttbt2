import os
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from .account_manager import CoreAccountManager # Corrected import
from .human_behavior_simulator import HumanBehaviorSimulator # Corrected import

class TikTokBot:
    def __init__(self, tiktok_username=None, tiktok_password=None):
        self.driver = self._init_driver()
        self.account_manager = CoreAccountManager() # Always initialize
        self.tiktok_username = tiktok_username
        self.tiktok_password = tiktok_password
        self.behavior = HumanBehaviorSimulator(self.driver)

    def _init_driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("user-agent=Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36")
        return webdriver.Chrome(options=options)

    def _authenticate(self):
        account_to_use = None
        if self.tiktok_username and self.tiktok_password:
            print("Using command-line credentials for authentication.")
            account_to_use = {"email": self.tiktok_username, "password": self.tiktok_password, "source": "cli"}
        else:
            print("No command-line credentials provided, trying AccountManager.")
            account_to_use = self.account_manager.get_next_account()

        if not account_to_use or not account_to_use.get("email") or not account_to_use.get("password"):
            print("No se encontró ninguna cuenta válida (CLI o AccountManager).")
            return False

        try:
            self.driver.get("https://www.tiktok.com/login")
            self.behavior.random_delay(3, 5)
            print(f"Attempting to log in with username: {account_to_use['email']}")

            email_field = self.driver.find_element(By.NAME, "username")
            print("Found username field.")
            self.behavior.human_type(email_field, account_to_use['email'])

            pass_field = self.driver.find_element(By.NAME, "password")
            print("Found password field.")
            self.behavior.human_type(pass_field, account_to_use['password'])

            submit_btn = self.driver.find_element(By.XPATH, '//button[@type="submit"]')
            print("Found submit button.")
            self.behavior.human_click(submit_btn)
            print("Login form submitted.")

            # Basic check for login success (highly simplified)
            self.behavior.random_delay(5, 7) # Wait for page to potentially change
            if "login" in self.driver.current_url.lower() or "error" in self.driver.current_url.lower():
                 print("Login may have failed or redirected to an error page.")
                 # self.driver.save_screenshot("login_failed_page.png") # Save screenshot if possible
                 return False
            print("Login appears successful (no longer on login/error page).")
            return True

        except Exception as e:
            print(f"Error de autenticación: {str(e)}")
            # self.driver.save_screenshot('auth_error.png')
            return False

    def run_session(self):
        if self._authenticate():
            self._perform_organic_actions()

    def _perform_organic_actions(self):
        max_views = int(os.getenv("MAX_VIEWS_PER_HOUR", "50"))
        for _ in range(max_views):
            self.behavior.watch_video()
            # 65% de probabilidad de like
            if random.random() < 0.65:
                self.behavior.like_video()
            self.behavior.random_scroll()
            time.sleep(random.uniform(8, 15))