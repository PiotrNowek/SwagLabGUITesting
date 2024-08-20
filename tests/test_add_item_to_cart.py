"""Test of adding products to cart after login to system with valid data"""
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
    sidebar_button = driver.find_element(By.ID, "react-burger-menu-btn")
    logout_button = driver.find_element(By.ID, "logout_sidebar_link")   
    sidebar_button.click()
    logout_button.click()
    driver.quit()