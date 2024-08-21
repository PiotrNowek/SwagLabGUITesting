"""Test login to system with valid data"""
from selenium import webdriver
from selenium.webdriver.common.by import By

from conftest import setup


def test_succesfull_login(setup):

    driver = setup
    username_input = driver.find_element(By.ID, "user-name")
    password_input = driver.find_element(By.ID,"password")
    login_button = driver.find_element(By.ID,"login-button")

    username_input.send_keys("standard_user")
    password_input.send_keys("secret_sauce")
    login_button.click()

    assert "inventory.html" in driver.current_url, "Login failed or incorrect page loaded"
    header_title = driver.find_element(By.CLASS_NAME, "title").text
    assert header_title == "Products", "Login successful but incorrect page title"

    """Close browser"""
    sidebar_button = driver.find_element(By.ID, "react-burger-menu-btn")
    logout_button = driver.find_element(By.ID, "logout_sidebar_link")   
    sidebar_button.click()
    logout_button.click()
    driver.quit()
