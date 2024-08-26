"""Test login to system with valid data"""
from selenium import webdriver

from conftest import setup
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_succesfull_login(setup):
    driver = setup

    """Login to system with valid data"""
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    """Verification that login was successful"""
    inventory_page = InventoryPage(driver)
    assert "inventory.html" in driver.current_url, "Login failed or incorrect page loaded"
    assert inventory_page.get_header_title() == "Products", "Login successful but incorrect page title"

    """Logout and close browser"""
    inventory_page.logout()