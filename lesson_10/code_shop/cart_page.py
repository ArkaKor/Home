from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CartPage():
    def __init__(self, driver):
        """
        Конструктор класса Cart_Page.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    @allure.step("Оформление заказа")
    def confirm(self):
        """
        Переходит на страницу оформления заказа.
        """
        self.wait.until(
            EC.element_to_be_clickable((By.ID, 'checkout'))).click()
