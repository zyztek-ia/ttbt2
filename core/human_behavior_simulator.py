import time
import random

class HumanBehaviorSimulator:
    def __init__(self, driver):
        self.driver = driver
        print(f"HumanBehaviorSimulator initialized with driver: {driver}")

    def random_delay(self, min_seconds, max_seconds):
        delay = random.uniform(min_seconds, max_seconds)
        # print(f"Delaying for {delay:.2f} seconds.")
        time.sleep(delay)

    def human_type(self, element, text):
        # print(f"Typing '{text}' into element: {element}")
        for char in text:
            element.send_keys(char)
            time.sleep(random.uniform(0.05, 0.15)) # Simulate human typing speed

    def human_click(self, element):
        # print(f"Clicking element: {element}")
        element.click() # Basic click

    def watch_video(self):
        print("Simulating watching a video...")
        self.random_delay(5, 10) # Simulate watching for 5-10 seconds

    def like_video(self):
        print("Simulating liking a video...")
        # In a real scenario, this would find and click a like button
        pass

    def random_scroll(self):
        print("Simulating random scroll...")
        # In a real scenario, this would execute scroll JavaScript
        # For now, just a delay to simulate time taken for a scroll
        self.random_delay(1, 3)
