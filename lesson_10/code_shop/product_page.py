from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import allure


class Product_Page():
    def __init__(self, driver):
        """
        Конструктор класса Product_Page.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    @allure.step("Добавление элементов в корзину")
    def add_to_cart(self):
        """
        Добавляет элементы в корзину.
        """
        self.driver.find_element(
            By.ID, 'add-to-cart-sauce-labs-backpack').click()
        self.driver.find_element(
            By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
        self.driver.find_element(
            By.ID, 'add-to-cart-sauce-labs-onesie').click()

    @allure.step("Переход на страницу корзины")
    def go_to_cart(self):
        """
        Переходит на страницу корзины.
        """
        self.driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').click()
