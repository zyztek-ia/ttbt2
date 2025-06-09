import time
import random

class HumanBehaviorSimulator:
    def __init__(self, driver):
        self.driver = driver
        print(f"HumanBehaviorSimulator initialized with driver.") # Removed driver object from log for brevity

    def random_delay(self, min_seconds, max_seconds):
        delay = random.uniform(min_seconds, max_seconds)
        # print(f"Delaying for {delay:.2f} seconds.") # Keep this commented for less verbose logs during typing
        time.sleep(delay)

    def human_type(self, element, text):
        # Using a more concise log, actual element details can be too verbose.
        element_name = element.get_attribute('name') if element.get_attribute('name') else ""
        print(f"Human typing text (length {len(text)}) into element <{element.tag_name} name='{element_name}'>")
        for char in text:
            element.send_keys(char)
            time.sleep(random.uniform(0.05, 0.2)) # Adjusted upper bound slightly
        print(f"Finished typing.")

    def human_click(self, element):
        element_name = element.get_attribute('name') if element.get_attribute('name') else ""
        print(f"Preparing to human click element <{element.tag_name} name='{element_name}'>")
        self.random_delay(0.4, 1.0) # Adjusted delay slightly
        print(f"Human clicking element.")
        element.click()
        # self.random_delay(0.1, 0.3) # Optional small delay after click

    def watch_video(self):
        print("Attempting to watch a video (simulated)...")
        # Simulate time spent watching the video content
        watch_duration = random.uniform(10, 25)
        print(f"Simulating watching for {watch_duration:.1f} seconds.")
        time.sleep(watch_duration) # Using time.sleep directly as random_delay prints its own message

        # Simulate scrolling to the next video or more content
        print("Scrolling down to simulate finding new content...")
        try:
            self.driver.execute_script("window.scrollBy(0, window.innerHeight * 0.8);") # Scroll 80% of viewport
            self.random_delay(1, 3) # Short delay after scroll
            print("Scrolled successfully.")
        except Exception as e:
            print(f"Error during scrolling: {e}")
        print("Finished watch_video simulation.")

    def like_video(self): # Existing stub
        print("Simulating liking a video...")
        # In a real scenario, this would find and click a like button
        pass

    def random_scroll(self): # Existing stub
        print("Simulating random scroll...")
        # In a real scenario, this would execute scroll JavaScript
        # For now, just a delay to simulate time taken for a scroll
        self.random_delay(1, 3)
