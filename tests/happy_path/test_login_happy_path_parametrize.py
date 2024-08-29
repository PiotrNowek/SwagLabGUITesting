"""Test login to system with valid data"""
from selenium import webdriver
import pytest

from conftest import setup
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


"""Test login with different usernames"""
@pytest.mark.parametrize("username", ["standard_user", "problem_user", "performance_glitch_user", "error_user", "visual_user"])
def test_succesfull_login(setup, username):
    driver = setup

    """Login to system with valid data"""
    login_page = LoginPage(driver)
    login_page.login(username, "secret_sauce")

    """Verification that login was successful"""
    inventory_page = InventoryPage(driver)
    assert "inventory.html" in driver.current_url, "Login failed or incorrect page loaded"
    assert inventory_page.get_header_title() == "Products", "Login successful but incorrect page title"

    """Logout and close browser"""
    inventory_page.logout()