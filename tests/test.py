import pytest
from config.config import driver_path, url
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options


"""FirefoxOptions Settings"""
options = Options()
service = Service(driver_path)

"""Initializing WebDriver with the given path"""
driver = webdriver.Firefox(service=service, options=options)

driver.get(url)

"""Write the title of the page"""
print(driver.title)

"""Close browser"""
driver.quit()
