"""Test of adding products to cart after login to system with valid data"""
from selenium import webdriver
from selenium.webdriver.common.by import By

from conftest import setup
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_add_item_to_cart(setup):
    try:
        driver = setup

        """Login to system with valid data"""
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        """Verification that login was successful"""
        inventory_page = InventoryPage(driver)
        assert "inventory.html" in driver.current_url, "Login failed or incorrect page loaded"
        assert inventory_page.get_header_title() == "Products", "Login successful but incorrect page title"

        """Add the first product to the cart"""
        product_name1 = "Sauce Labs Bike Light"
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()

        """Add the second product to the cart"""
        product_name2 = "Sauce Labs Bolt T-Shirt"
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()

        """Go to the shopping cart"""
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        """Verify both products are in the cart"""
        cart_items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        cart_products_names = [item.text for item in cart_items]

        assert product_name1 in cart_products_names, f"{product_name1} not found in the cart"
        assert product_name2 in cart_products_names, f"{product_name2} not found in the cart"

        print("Test passed: Both products were successfully added to the cart.")


    finally:
        """Clean cart, log out and close browser"""
        driver.find_element(By.ID, "remove-sauce-labs-bike-light").click()
        driver.find_element(By.ID, "remove-sauce-labs-bolt-t-shirt").click()
        inventory_page.logout()