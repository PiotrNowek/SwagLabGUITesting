from selenium.webdriver.common.by import By


class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    """Locators for items on the product page"""
    product_title_locator = (By.CLASS_NAME, "inventory_details_name")
    product_description_locator = (By.CLASS_NAME, "inventory_details_desc")
    product_price_locator = (By.CLASS_NAME, "inventory_details_price")
    add_to_cart_button_locator = (By.CLASS_NAME, "btn_inventory")

    """Locator for error message or 404 page"""
    error_message_locator = (By.CLASS_NAME, "error-message-container")
    not_found_message_locator = (By.TAG_NAME, "h1")

    def get_product_title(self):
        return self.driver.find_element(*self.product_title_locator).text

    def get_product_description(self):
        return self.driver.find_element(*self.product_description_locator).text

    def get_product_price(self):
        return self.driver.find_element(*self.product_price_locator).text

    def add_product_to_cart(self):
        self.driver.find_element(*self.add_to_cart_button_locator).click()

    def get_error_message(self):
        return self.driver.find_element(*self.error_message_locator).text

    def get_not_found_message(self):
        return self.driver.find_element(*self.not_found_message_locator).text

    def go_to_non_existing_product(self, product_id):
        self.driver.get(f"https://www.saucedemo.com/inventory-item.html?id={product_id}")

