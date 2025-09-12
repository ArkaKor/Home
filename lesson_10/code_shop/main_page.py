from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import allure


class Main_Page():
    def __init__(self, driver):
        """
        Конструктор класса Form_Page.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    @allure.step("Авторизация на сайте магазина")
    def login(self):
        """
        Открывает страницу магазина.
        Проводит авторизацию.
        """
        self.driver.get('https://www.saucedemo.com')
        self.driver.find_element(By.ID, 'user-name').send_keys('standard_user')
        self.driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        self.driver.find_element(By.ID, 'login-button').click()
