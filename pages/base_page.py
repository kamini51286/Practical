from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def type(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def get_text(self, locator):
        return self.driver.find_element(*locator).text
