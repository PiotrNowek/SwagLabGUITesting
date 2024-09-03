from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = driver.find_element(By.ID, "user-name")
        self.password_input = driver.find_element(By.ID, "password")
        self.login_button = driver.find_element(By.ID, "login-button")

    def login(self, username, password):
        self.username_input.send_keys(username)
        self.password_input.send_keys(password)
        self.login_button.click()

    def get_error_message(self):
        """Finds the element that contains the error message"""
        error_message_element = self.driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
        return error_message_element.text