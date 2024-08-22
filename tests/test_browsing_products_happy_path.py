"""Test of browsing products after login to system with valid data"""
from selenium import webdriver
from selenium.webdriver.common.by import By

from conftest import setup, login, logout


def test_browsing_product(setup):
    try:
        driver = setup

        """Log in to the website"""
        login(driver)

        """Verify successful login"""
        header_title = driver.find_element(By.CLASS_NAME, "header_label").text
        assert header_title == "Swag Labs", "Login failed or incorrect page loaded"

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
        logout(driver)