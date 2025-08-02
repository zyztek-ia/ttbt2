import time
import random
from selenium.webdriver.common.action_chains import ActionChains

class HumanBehaviorSimulator:
    """
    Simula el comportamiento humano para evadir la detección de bots.
    Incluye escritura, clics y esperas aleatorias.
    """
    def __init__(self, driver):
        """
        Inicializa el simulador con un driver de Selenium.
        """
        self.driver = driver

    def random_delay(self, min_seconds=1, max_seconds=3):
        """Espera un tiempo aleatorio dentro de un rango."""
        time.sleep(random.uniform(min_seconds, max_seconds))

    def human_type(self, element, text):
        """
        Escribe texto en un elemento, letra por letra, con retrasos aleatorios.
        """
        for char in text:
            element.send_keys(char)
            time.sleep(random.uniform(0.05, 0.2))
        self.random_delay()

    def human_click(self, element):
        """
        Mueve el ratón sobre el elemento y hace clic, con retrasos.
        """
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        self.random_delay(0.2, 0.8)
        actions.click()
        actions.perform()
        self.random_delay()

    def random_scroll(self):
        """Realiza un scroll hacia abajo de una cantidad aleatoria."""
        scroll_amount = random.randint(300, 800)
        self.driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
        self.random_delay()

    def watch_video(self):
        """Simula ver un video por un tiempo aleatorio."""
        self.random_delay(5, 15)

    def like_video(self):
        """
        Simula dar un 'like'. Esta es una implementación de placeholder.
        En una implementación real, se buscaría el botón de 'like' y se haría clic.
        """
        print("[Behavior] Simulating a 'like' action.")
        self.random_delay()
