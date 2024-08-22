"""Test login to system with valid data"""
from selenium import webdriver
from selenium.webdriver.common.by import By

from conftest import setup, login, logout


def test_succesfull_login(setup):

    driver = setup

    """Log in to the website"""
    login(driver)

    assert "inventory.html" in driver.current_url, "Login failed or incorrect page loaded"
    header_title = driver.find_element(By.CLASS_NAME, "title").text
    assert header_title == "Products", "Login successful but incorrect page title"

    logout(driver)
