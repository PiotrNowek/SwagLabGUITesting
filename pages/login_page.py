from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        username_input = self.driver.find_element(By.ID, "user-name")
        password_input = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.ID, "login-button")
        
        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button.click()
