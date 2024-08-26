from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.header_title = driver.find_element(By.CLASS_NAME, "title")

    def get_header_title(self):
        return self.header_title.text

    def logout(self):
        sidebar_button = self.driver.find_element(By.ID, "react-burger-menu-btn")
        logout_button = self.driver.find_element(By.ID, "logout_sidebar_link")
        sidebar_button.click()
        logout_button.click()
        self.driver.quit()