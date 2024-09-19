from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.header_title = driver.find_element(By.CLASS_NAME, "title")

    def get_header_title(self):
        return self.header_title.text

    def logout(self):
        wait = WebDriverWait(self.driver, 5)
        sidebar_button = wait.until(EC.element_to_be_clickable((By.ID, "react-burger-menu-btn")))
        sidebar_button.click()
        logout_button = wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link")))
        logout_button.click()
        self.driver.quit()

        