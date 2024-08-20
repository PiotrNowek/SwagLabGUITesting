"""Test of browsing products after login to system with valid data"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

from config.config import driver_path, url


options = Options()
service = Service(driver_path)

"""Initializing WebDriver with the given path"""
driver = webdriver.Firefox(service=service, options=options)

try:
    """Open the SwagLabs website"""
    driver.get(url)
    driver.implicitly_wait(5)

    """Log in to the website"""
    username_input = driver.find_element(By.ID, "user-name")
    password_input = driver.find_element(By.ID,"password")
    login_button = driver.find_element(By.ID,"login-button")

    username_input.send_keys("standard_user")
    password_input.send_keys("secret_sauce")
    login_button.click()

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
    sidebar_button = driver.find_element(By.ID, "react-burger-menu-btn")
    logout_button = driver.find_element(By.ID, "logout_sidebar_link")   
    sidebar_button.click()
    logout_button.click()
    driver.quit()
