from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import pytest 

from config.config import driver_path, url


@pytest.fixture
def setup():
    """Setup for each test case"""
    options = Options()
    service = Service(driver_path)
    driver = webdriver.Firefox(service=service, options=options)
    driver.get(url)
    driver.implicitly_wait(5)  
    yield driver
    driver.quit()


def login(driver):
    """Login to system with valid data"""
    username_input = driver.find_element(By.ID, "user-name")
    password_input = driver.find_element(By.ID,"password")
    login_button = driver.find_element(By.ID,"login-button")

    username_input.send_keys("standard_user")
    password_input.send_keys("secret_sauce")
    login_button.click()
    

def logout(driver):
    """Logout and close browser"""
    sidebar_button = driver.find_element(By.ID, "react-burger-menu-btn")
    logout_button = driver.find_element(By.ID, "logout_sidebar_link")   
    sidebar_button.click()
    logout_button.click()
    driver.quit()
   