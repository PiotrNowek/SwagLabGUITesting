"""Test of completing the checkout and order process successfully after login to system with valid data"""
from selenium import webdriver
from selenium.webdriver.common.by import By

from conftest import setup, login, logout


def test_checkout(setup):
    try:
        driver = setup

        """Log in to the website"""
        login(driver)

        """Verify successful login"""
        header_title = driver.find_element(By.CLASS_NAME, "header_label").text
        assert header_title == "Swag Labs", "Login failed or incorrect page loaded"

        """Add the first product to the cart"""
        product_name1 = "Sauce Labs Backpack"
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

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

        """Proceed to checkout"""
        driver.find_element(By.ID, "checkout").click()

        """Fill in the checkout information"""
        driver.find_element(By.ID, "first-name").send_keys("John")
        driver.find_element(By.ID, "last-name").send_keys("Rambo")
        driver.find_element(By.ID, "postal-code").send_keys("12345")
        driver.find_element(By.ID, "continue").click()

        """Verify the checkout overview"""
        summary_items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        summary_product_names = [item.text for item in summary_items]
        assert "Sauce Labs Backpack" in summary_product_names, f"{product_name1} not found in the checkout overview"
        assert "Sauce Labs Bolt T-Shirt" in summary_product_names, f"{product_name2} not found in the checkout overview"

        """Finish the checkout"""
        driver.find_element(By.ID, "finish").click()
    
        """Verify the checkout complete page"""
        complete_header = driver.find_element(By.CLASS_NAME, "complete-header").text
        assert complete_header == "Thank you for your order!", "Verify that the confirmation message after checkout is correct"

        """Go back to main page"""
        driver.find_element(By.ID, "back-to-products").click()

        print("Test passed: Checkout and order process completed successfully.")
    
    finally:
        """Log out and close browser"""
        logout(driver)
        
