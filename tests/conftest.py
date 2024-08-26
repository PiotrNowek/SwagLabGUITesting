from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import pytest 

from config.config import firefox_driver_path, url


@pytest.fixture
def setup():
    """Setup for each test case"""
    options = Options()
    service = Service(firefox_driver_path)
    driver = webdriver.Firefox(service=service, options=options)
    driver.get(url)
    driver.implicitly_wait(5)  
    yield driver
    driver.quit()  