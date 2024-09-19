"""Test of failing the checkout process due to missing required information after login to system with valid data"""
from selenium import webdriver
from selenium.webdriver.common.by import By

from conftest import setup
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_checkout_failure(setup):
    try:
        driver = setup

        """Login to system with valid data"""
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        """Verification that login was successful"""
        inventory_page = InventoryPage(driver)
        assert "inventory.html" in driver.current_url, "Login failed or incorrect page loaded"
        assert inventory_page.get_header_title() == "Products", "Login successful but incorrect page title"

        """Add a product to the cart"""
        product_name = "Sauce Labs Backpack"
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

        """Go to the shopping cart"""
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        """Verify the product is in the cart"""
        cart_items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        cart_products_names = [item.text for item in cart_items]
        assert product_name in cart_products_names, f"{product_name} not found in the cart"

        """Proceed to checkout"""
        driver.find_element(By.ID, "checkout").click()

        """Leave checkout information blank and try to continue"""
        driver.find_element(By.ID, "first-name").send_keys("")
        driver.find_element(By.ID, "last-name").send_keys("")
        driver.find_element(By.ID, "postal-code").send_keys("")
        driver.find_element(By.ID, "continue").click()

        """Verify the error message is displayed"""
        error_message = driver.find_element(By.CLASS_NAME, "error-message-container").text
        assert "Error: First Name is required" in error_message, "Error message for missing first name not displayed"

        print("Test passed: Checkout failed due to missing required information.")
    
    finally:
        """Log out and close browser"""
        inventory_page.logout()