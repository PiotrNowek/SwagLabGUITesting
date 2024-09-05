"""Test for attempting to access a non-existent product"""
import pytest
from selenium.webdriver.common.by import By

from conftest import setup
from pages.login_page import LoginPage
from pages.product_page import ProductPage


@pytest.mark.parametrize("product_id", [
    "non_existing_product_1",
    "invalid_id_12345",
    "999999999",  
])
def test_access_non_existing_product(setup, product_id):
    driver = setup
    
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    product_page = ProductPage(driver)
    product_page.go_to_non_existing_product(product_id)

    element = driver.find_element(By.XPATH, '//div[@class="inventory_details_name large_size"]')
    assert element.text == "ITEM NOT FOUND"

    
    




