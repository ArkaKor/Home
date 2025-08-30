import pytest
from selenium import webdriver
from code_shop.main_page import Main_Page
from code_shop.product_page import Product_Page
from code_shop.cart_page import Cart_Page
from code_shop.checkout_page import Checkout_Page


@pytest.fixture
def driver():
    browser = webdriver.Firefox()
    browser.implicitly_wait(5)
    browser.maximize_window()
    yield browser
    browser.quit()


def test_shop(driver):
    Main_Page(driver).login()
    product = Product_Page(driver)
    product.add_to_cart()
    product.go_to_cart()
    Cart_Page(driver).confirm()
    checkout = Checkout_Page(driver)
    checkout.insert_value()
    checkout.buy()
    price = checkout.get_result()
    assert price == '$58.29', "Неверная сумма"
