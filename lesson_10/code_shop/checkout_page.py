from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import allure


class CheckoutPage():
    def __init__(self, driver):
        """
        Конструктор класса Checkout_Page.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    @allure.step("Ввод данных покупателя")
    def insert_value(self):
        """
        Заполняет данные покупателя.
        """
        self.driver.find_element(By.ID, 'first-name').send_keys('Аркадий')
        self.driver.find_element(By.ID, 'last-name').send_keys('Кормилицын')
        self.driver.find_element(By.ID, 'postal-code').send_keys('141300')

    @allure.step("Подтверждение данных")
    def buy(self):
        """
        Подтверждает введенные данные.
        """
        self.driver.find_element(By.ID, 'continue').click()

    @allure.step("Получение результата")
    def get_result(self):
        """
        Возвращает сумму покупки.

        :return: str - сумма покупки"""
        total = self.driver.find_element(
            By.CLASS_NAME, 'summary_total_label').text
        return str(total.split(" ")[1])
