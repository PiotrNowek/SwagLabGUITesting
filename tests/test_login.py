"""Test login to system with valid data"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

from config.config import driver_path, url


"""FirefoxOptions Settings"""
options = Options()
service = Service(driver_path)

"""Initializing WebDriver with the given path"""
driver = webdriver.Firefox(service=service, options=options)

driver.get(url)
driver.implicitly_wait(5)

username_input = driver.find_element(By.ID, "user-name")
password_input = driver.find_element(By.ID,"password")
login_button = driver.find_element(By.ID,"login-button")

username_input.send_keys("standard_user")
password_input.send_keys("secret_sauce")
login_button.click()

sidebar_button = driver.find_element(By.ID, "react-burger-menu-btn")
logout_button = driver.find_element(By.ID, "logout_sidebar_link")   
sidebar_button.click()
logout_button.click()

"""Close browser"""
driver.quit()
