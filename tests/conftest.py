from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.safari.webdriver import WebDriver as SafariDriver
import pytest 

from config.config import chrome_driver_path, firefox_driver_path, edge_driver_path, url


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox", help="Type of browser. E.g. firefox, chrome, edge")

    
@pytest.fixture
def setup(request):
    browser = request.config.getoption("--browser")
    
    if browser == "firefox":
        options = FirefoxOptions()
        service = FirefoxService(firefox_driver_path)
        driver = webdriver.Firefox(service=service, options=options)
    elif browser == "chrome":
        options = ChromeOptions()
        service = ChromeService(chrome_driver_path)
        driver = webdriver.Chrome(service=service, options=options)
    elif browser == "edge":
        options = EdgeOptions()
        service = EdgeService(edge_driver_path)
        driver = webdriver.Edge(service=service, options=options)
    elif browser == "safari":
        driver = SafariDriver()
    else:
        raise ValueError(f"Przeglądarka {browser} nie jest obsługiwana.")
    
    driver.get(url)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
