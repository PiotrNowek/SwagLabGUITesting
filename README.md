# SwagLabs Test Crusaders - Mastering Web UI Testing with Selenium

## About the Project

Welcome to the ultimate challenge in the world of web UI testing! Our mission: to explore and test the SwagLabs e-commerce galaxy using the powerful Selenium framework. Join us on this journey where we leave no bug unchallenged and ensure the SwagLabs experience is flawless!

## Goal

When the precision of Selenium meets the vast expanse of SwagLabs, we ensure every click, every product, and every transaction is tested to perfection. Our goal is to create robust tests that make the SwagLabs interface run smoother than a droid in peak condition!

## Features

- **Selenium WebDriver**: Our hyperdrive for navigating through the SwagLabs website, ensuring we interact with every element as intended.
- **Pytest**: The lightsaber of our testing arsenal, making sure our tests are sharp, efficient, and ready to slice through any bugs.

## How to Run

1. **Clone the Repository**: Download the code and prepare your test environment.
2. **Install Dependencies**: Make sure your test environment is powered up with all the necessary libraries.
3. **Launch Selenium Tests**: Engage the engines and watch as our tests cruise through SwagLabs, validating every interaction!

## Test Structure

Our tests are meticulously organized to ensure clarity, maintainability, and ease of use. Here's the breakdown:

- **`tests/`**: The battleground where our Web UI test cases are executed. May your tests be as accurate as a sharpshooter's aim!

- **`drivers/`**: The hangar where we keep our browser drivers, such as `geckodriver` for Firefox. These drivers are essential for steering the Selenium WebDriver through the SwagLabs interface.

- **`reports/`**: The archive where we store detailed test reports. Here, you can find logs, screenshots, and summaries of each test run, helping us track the performance and outcomes of our test suite. 

- **`tests/config/`**: The command center where we store all the necessary configurations, including browser drivers and URLs. This is the hub that guides our tests through the SwagLabs interface with precision.

- **`tests/conftest.py`**: The strategic base where shared fixtures and configurations reside, ensuring our tests are streamlined and efficient.

## Example Tests

```python
"""Test of completing the checkout and order process successfully after login to system with valid data"""
from selenium import webdriver
from selenium.webdriver.common.by import By

from conftest import setup
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_checkout(setup):
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
        inventory_page.logout()
```

## How to Contribute

1. **Fork the Repository**: Join the SwagLabs Test Crusaders by forking the repo and adding your unique testing strategies.
2. **Create Pull Requests**: Strengthen our forces by submitting your improvements and helping us maintain the integrity of SwagLabs!

## About the Author

I'm an aspiring tester with a passion for creating bulletproof web UI tests. My journey through the SwagLabs universe is just beginning, but with each test, I'm honing my skills and mastering the art of Selenium testing. Let's work together to conquer the SwagLabs galaxy, one test at a time.

## License

This project is open-source, like the endless possibilities in the universe. Feel free to use, modify, and share the code to help others improve their web testing practices!

Enjoy your adventure through the SwagLabs universe! 🚀
