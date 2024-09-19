"""Test of attempting to complete the checkout with valid data but experiencing a server error"""
from selenium import webdriver
from selenium.webdriver.common.by import By

from conftest import setup
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_checkout_product_unavailable_simulation(setup):
    try:
        driver = setup

        """Login to system with valid data"""
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        """Verification that login was successful"""
        inventory_page = InventoryPage(driver)
        assert "inventory.html" in driver.current_url, "Login failed or incorrect page loaded"

        """Add a product to the cart"""
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

        """Go to the shopping cart"""
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        """Proceed to checkout"""
        driver.find_element(By.ID, "checkout").click()

        """Fill in the checkout information"""
        driver.find_element(By.ID, "first-name").send_keys("John")
        driver.find_element(By.ID, "last-name").send_keys("Rambo")
        driver.find_element(By.ID, "postal-code").send_keys("12345")
        driver.find_element(By.ID, "continue").click()

        """Simulate product unavailability by removing the product from DOM"""
        driver.execute_script("document.getElementById('item_0_title_link').remove();")

        """Attempt to finalize the order"""
        driver.find_element(By.ID, "finish").click()

        """Verify that an error is displayed"""
        error_message = driver.find_element(By.CLASS_NAME, "error-message-container").text
        assert "Product is unavailable" in error_message, "No error message displayed for unavailable product"

        print("Test passed: Simulated product unavailability during checkout.")

    finally:
        """Log out and close browser"""
        inventory_page.logout()
        
