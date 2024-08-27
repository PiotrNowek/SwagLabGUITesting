"""Test of browsing products after login to system with valid data"""
from selenium import webdriver
from selenium.webdriver.common.by import By

from conftest import setup
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_browsing_product(setup):
    try:
        driver = setup

        """Login to system with valid data"""
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        """Verification that login was successful"""
        inventory_page = InventoryPage(driver)
        assert "inventory.html" in driver.current_url, "Login failed or incorrect page loaded"
        assert inventory_page.get_header_title() == "Products", "Login successful but incorrect page title"

        """Click on a product"""
        product_name = "Sauce Labs Backpack"
        driver.find_element(By.XPATH, f"//div[text()='{product_name}']").click()

        """Verify product details page"""
        product_detail_name = driver.find_element(By.CLASS_NAME, "inventory_details_name").text
        assert product_detail_name == product_name, "Incorrect product page"

        """Get the product price"""
        product_price = driver.find_element(By.CLASS_NAME, "inventory_details_price").text
        print(f"Product: {product_detail_name}, Price: {product_price}")

        """Go back to the product inventory"""
        driver.find_element(By.ID, "back-to-products").click()

        """Click on a second product"""
        product_name2 = "Sauce Labs Onesie"
        driver.find_element(By.XPATH, f"//div[text()='{product_name2}']").click()

        """Verify product details page"""
        product_detail_name2 = driver.find_element(By.CLASS_NAME, "inventory_details_name").text
        assert product_detail_name2 == product_name2, "Incorrect product page"

        """Get the second product price"""
        product_price2 = driver.find_element(By.CLASS_NAME, "inventory_details_price").text
        print(f"Product: {product_detail_name2}, Price: {product_price2}")

        """Go back to the product inventory"""
        driver.find_element(By.ID, "back-to-products").click()

        """Click on a third product"""
        product_name3 = "Sauce Labs Fleece Jacket"
        driver.find_element(By.XPATH, f"//div[text()='{product_name3}']").click()

        """Verify product details page"""
        product_detail_name3 = driver.find_element(By.CLASS_NAME, "inventory_details_name").text
        assert product_detail_name3 == product_name3, "Incorrect product page"

        """Get the second product price"""
        product_price3 = driver.find_element(By.CLASS_NAME, "inventory_details_price").text
        print(f"Product: {product_detail_name3}, Price: {product_price3}")


        print("Test passed: Product browsing is working as expected.")
    

    finally:
        """Log out and close browser"""
        inventory_page.logout()