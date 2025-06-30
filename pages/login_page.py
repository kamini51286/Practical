from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    SUBMIT = (By.ID, "submit")
    ERROR = (By.ID, "error")
    logout_button=(By.LINK_TEXT, "Log out")

    def login(self, username, password):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.SUBMIT)

    def get_error_message(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            error_element = wait.until(EC.visibility_of_element_located(self.ERROR))
            return error_element.text
        except Exception as e:
            print(f"❌ Failed to get error message: {e}")
            return ""
        # return self.get_text(self.ERROR)
    
    def logout(self, username, password):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.SUBMIT)
        self.click(self.logout_button)
