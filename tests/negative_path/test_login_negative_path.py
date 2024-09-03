"""The test checks whether the application responds appropriately to an incorrect password or login."""
from selenium import webdriver
import pytest

from conftest import setup
from pages.login_page import LoginPage


@pytest.mark.parametrize("username, password", [
    ("standard_user", "wrong_password"),
    ("locked_out_user", "wrong_password"),
    ("John_Doe", "secret_sauce")
])


def test_unsuccesfull_login(setup, username, password):
    driver = setup

    """Attempt to login with incorrect username or password"""
    login_page = LoginPage(driver)
    login_page.login(username, password)

    """Verification that login was unsuccessful"""
    error_message = login_page.get_error_message()
    assert error_message == "Epic sadface: Username and password do not match any user in this service", \
        "Unexpected error message or no error message displayed"