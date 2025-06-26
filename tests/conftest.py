import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

@pytest.fixture
def browser():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
    driver.maximize_window()
    driver.get("https://practicetestautomation.com/practice-test-login/")  # Change URL as needed
    yield driver
    driver.quit()