"""
First test will fail because item exist, third test pass only in case of application error.I added these tests to show my skills.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

from conftest import setup
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


"""Test of adding unavailable products to cart after login to system with valid data"""
def test_add_unavailable_item_to_cart(setup):
    try:
        driver = setup

        """Login to system with valid data"""
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        """Verification that login was successful"""
        inventory_page = InventoryPage(driver)
        assert "inventory.html" in driver.current_url, "Login failed or incorrect page loaded"
        assert inventory_page.get_header_title() == "Products", "Login successful but incorrect page title"

        """Try to add an unavailable product to the cart"""
        product_name = "Sauce Labs Fleece Jacket"  """Assuming this product is out of stock""" 

        try:
            add_to_cart_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket")
            if add_to_cart_button.is_enabled():
                add_to_cart_button.click()  
                assert False, "The product is unavailable but was added to the cart"
        except Exception as e:
            print(f"Expected behavior: Unable to add {product_name} to the cart. Exception: {str(e)}")

        """Verify that the unavailable product is NOT in the cart"""
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        cart_items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        cart_products_names = [item.text for item in cart_items]

        assert product_name not in cart_products_names, f"{product_name} found in the cart, but it shouldn't be available."

        print("Test passed: Unavailable product was not added to the cart.")

    finally:
        """Clean up and close browser"""
        inventory_page.logout()


"""Test of adding a non-existent product to the cart after login to system with valid data"""
def test_add_non_existent_item_to_cart(setup):
    try:
        driver = setup

        """Login to system with valid data"""
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        """Verification that login was successful"""
        inventory_page = InventoryPage(driver)
        assert "inventory.html" in driver.current_url, "Login failed or incorrect page loaded"
        assert inventory_page.get_header_title() == "Products", "Login successful but incorrect page title"

        """Attempt to add a non-existent product to the cart"""
        non_existent_product_id = "add-to-cart-sauce-lab-hat"  """Non-existent product ID"""
        product_name = "Sauce Lab Hat"

        try:
            add_to_cart_button = driver.find_element(By.ID, non_existent_product_id)
            add_to_cart_button.click()  #This should not be possible
            assert False, f"Non-existent product {product_name} was unexpectedly added to the cart"
        except Exception as e:
            print(f"Expected behavior: Unable to add non-existent product {product_name} to the cart. Exception: {str(e)}")

        """Verify that the non-existent product is NOT in the cart"""
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        cart_items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        cart_products_names = [item.text for item in cart_items]

        assert product_name not in cart_products_names, f"{product_name} found in the cart, but it shouldn't exist."

        print("Test passed: Non-existent product was not added to the cart.")

    finally:
        """Clean up and close browser"""
        inventory_page.logout()


"""Test of attempting to add a product to the cart that fails due to an application error"""
def test_add_item_to_cart_with_application_error(setup):
    try:
        driver = setup

        """Login to system with valid data"""
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        """Verification that login was successful"""
        inventory_page = InventoryPage(driver)
        assert "inventory.html" in driver.current_url, "Login failed or incorrect page loaded"
        assert inventory_page.get_header_title() == "Products", "Login successful but incorrect page title"

        """Attempt to add a product that should be available"""
        product_id = "add-to-cart-sauce-labs-bike-light"  
        product_name = "Sauce Labs Bike Light"

        try:
            add_to_cart_button = driver.find_element(By.ID, product_id)
            add_to_cart_button.click()  # This click might fail due to an application error

            """Verify that the product was not added due to the error"""
            cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
            assert cart_badge.text == "0", f"{product_name} was added to the cart, but it should have failed due to an application error."

        except Exception as e:
            print(f"Expected behavior: Failed to add product {product_name} to the cart due to application error. Exception: {str(e)}")

        """Verify that the product is NOT in the cart"""
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        cart_items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        cart_products_names = [item.text for item in cart_items]

        assert product_name not in cart_products_names, f"{product_name} found in the cart, but it should not be there due to an application error."

        print("Test passed: Product was not added to the cart due to the application error.")

    finally:
        """Clean up and close browser"""
        inventory_page.logout()