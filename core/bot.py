import os
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

            wait = WebDriverWait(self.driver, 10) # Initialize WebDriverWait

            # Attempt to find username/email field
            print("Attempting to find username/email field...")
            try:
                email_field_selectors = [
                    (By.XPATH, "//input[@type='text' and (contains(@name, 'username') or contains(@placeholder, 'mail') or contains(@aria-label, 'mail') or contains(@name, 'email'))]"),
                    (By.NAME, "username"), # Original
                    (By.NAME, "email"),
                    (By.XPATH, "//input[@type='email']"),
                    (By.CSS_SELECTOR, "input[type='text'][name='username']"),
                    (By.CSS_SELECTOR, "input[type='email']")
                ]
                email_field = None
                for by, selector_value in email_field_selectors:
                    print(f"Trying selector: {by} = {selector_value}")
                    try:
                        email_field = wait.until(EC.presence_of_element_located((by, selector_value)))
                        if email_field.is_displayed() and email_field.is_enabled():
                            print(f"Found username/email field with: {by} = {selector_value}")
                            break
                        else:
                            email_field = None # Element not interactable
                    except:
                        print(f"Selector failed: {by} = {selector_value}")
                        continue
                if not email_field:
                    print("Could not find an interactable username/email field with tried selectors.")
                    # self.driver.save_screenshot('username_field_not_found.png')
                    return False
            except Exception as e_user:
                print(f"Error finding username/email field: {e_user}")
                # self.driver.save_screenshot('username_field_error.png')
                return False

            print("Found username field. Attempting to type.")
            self.behavior.human_type(email_field, account_to_use['email'])

            # Attempt to find password field
            print("Attempting to find password field...")
            try:
                pass_field_selectors = [
                    (By.XPATH, "//input[@type='password']"),
                    (By.NAME, "password") # Original
                ]
                pass_field = None
                for by, selector_value in pass_field_selectors:
                    print(f"Trying selector: {by} = {selector_value}")
                    try:
                        pass_field = wait.until(EC.presence_of_element_located((by, selector_value)))
                        if pass_field.is_displayed() and pass_field.is_enabled():
                            print(f"Found password field with: {by} = {selector_value}")
                            break
                        else:
                            pass_field = None
                    except:
                        print(f"Selector failed: {by} = {selector_value}")
                        continue
                if not pass_field:
                    print("Could not find an interactable password field with tried selectors.")
                    # self.driver.save_screenshot('password_field_not_found.png')
                    return False
            except Exception as e_pass:
                print(f"Error finding password field: {e_pass}")
                # self.driver.save_screenshot('password_field_error.png')
                return False

            print("Found password field. Attempting to type.")
            self.behavior.human_type(pass_field, account_to_use['password'])

            # Attempt to find submit button
            print("Attempting to find submit button...")
            try:
                submit_button_selectors = [
                    (By.XPATH, "//button[@type='submit']"), # Original
                    (By.CSS_SELECTOR, "button[type='submit']"),
                    (By.XPATH, "//button[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'log in')]"),
                    (By.XPATH, "//button[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'sign in')]")
                ]
                submit_btn = None
                for by, selector_value in submit_button_selectors:
                    print(f"Trying selector: {by} = {selector_value}")
                    try:
                        submit_btn = wait.until(EC.element_to_be_clickable((by, selector_value)))
                        print(f"Found submit button with: {by} = {selector_value}")
                        break
                    except:
                        print(f"Selector failed: {by} = {selector_value}")
                        continue
                if not submit_btn:
                    print("Could not find a clickable submit button with tried selectors.")
                    # self.driver.save_screenshot('submit_button_not_found.png')
                    return False
            except Exception as e_submit:
                print(f"Error finding submit button: {e_submit}")
                # self.driver.save_screenshot('submit_button_error.png')
                return False

            print("Found submit button. Attempting to click.")
            self.behavior.human_click(submit_btn)
            print("Login form submitted.")

            # Basic check for login success (highly simplified)
            self.behavior.random_delay(5, 7) # Wait for page to potentially change
            if "login" in self.driver.current_url.lower() or "error" in self.driver.current_url.lower():
                 print("Login may have failed or redirected to an error page.")
                 # self.driver.save_screenshot("login_failed_page.png")
                 return False
            print("Login appears successful (no longer on login/error page).")
            return True

        except Exception as e:
            print(f"Error de autenticación global: {str(e)}") # Clarified this is a global auth error
            # self.driver.save_screenshot('auth_error_global.png')
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