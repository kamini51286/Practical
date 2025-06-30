import os
from datetime import datetime

def take_screenshot(driver, name="screenshot"):
    screenshots_dir = os.path.join(os.getcwd(), "screenshots")
    os.makedirs(screenshots_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_path = os.path.join(screenshots_dir, f"{name}_{timestamp}.png")
    driver.save_screenshot(file_path)
