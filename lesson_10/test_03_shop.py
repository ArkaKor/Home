import pytest
from selenium import webdriver
from code_shop.main_page import Main_Page
from code_shop.product_page import Product_Page
from code_shop.cart_page import Cart_Page
from code_shop.checkout_page import Checkout_Page
import allure


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера.
    """
    browser = webdriver.Firefox()
    browser.implicitly_wait(5)
    browser.maximize_window()
    yield browser
    browser.quit()


@allure.title("Тестирование покупки")
@allure.description("Тест проверяет алгоритм поккупки")
@allure.feature("Магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop(driver):
    with allure.step("Авторизация на сайте"):
        Main_Page(driver).login()
    with allure.step("Продукты"):
        product = Product_Page(driver)
        with allure.step("Наполнение корзины"):
            product.add_to_cart()
        with allure.step("Переход в корзину"):
            product.go_to_cart()
    with allure.step("Подтверждение выбора и переход к оформлению"):
        Cart_Page(driver).confirm()
    with allure.step("Касса"):
        checkout = Checkout_Page(driver)
        with allure.step("Заполнение данных покупателя"):
            checkout.insert_value()
        with allure.step("Подтверждеие данных и переход к оплате"):
            checkout.buy()
    with allure.step("Получение и проверка результата"):
        price = checkout.get_result()
        assert price == '$58.29', "Неверная сумма"
