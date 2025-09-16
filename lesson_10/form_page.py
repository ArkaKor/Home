from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import allure


class FormPage():
    def __init__(self, driver):
        """
        Конструктор класса Form_Page.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        self.fields = {
            'first-name': 'Иван',
            'last-name': 'Петров',
            'address': 'Ленина, 55-3',
            'e-mail': 'test@skypro.com',
            'phone': '+7985899998787',
            'zip-code': '',
            'city': 'Москва',
            'country': 'Россия',
            'job-position': 'QA',
            'company': 'SkyPro'
        }

    @allure.step("Открытие страницы заполнения формы")
    def open(self):
        """
        Открывает страницу заполнения формы.
        """
        self.driver.get(
            'https://bonigarcia.dev/selenium-webdriver-java/data-types.html'
            )

    @allure.step("Заполнение формы")
    def fill_form(self):
        """
        Заполняет форму из таблицы класса.
        """
        for field, value in self.fields.items():
            self.wait.until(
                EC.presence_of_element_located((By.NAME, field))
            ).send_keys(value)

    @allure.step("Нажатие кнопки 'submitt'")
    def submitt(self):
        """
        Нажимает кнопку 'submitt'
        """
        self.wait.until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR, 'button[type="submit"]'))
        ).send_keys(Keys.END)
        button = self.driver.find_element(
            By.CSS_SELECTOR, 'button[type="submit"]')
        button.send_keys(Keys.END)
        button.send_keys(Keys.PAGE_DOWN)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR, 'button[type="submit"]'))
        )
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, 'button[type="submit"]'))
        )
        button.click()

    @allure.step("Получение атрибута по id {field_id}")
    def get_field_class(self, field_id):
        """
        Возвращает атрибут класса элемента.

        :param field_id: str — id искомого элемента.
        :return: str - значение атрибута искомого элемента.
        """
        return self.wait.until(
            EC.presence_of_element_located((By.ID, field_id))
        ).get_attribute('class')

    @allure.step("Получение атрибута элемента zip-code")
    def zip_code(self):
        """
        Возвращает значение атрибута элемента zip-code.

        :return: str - значение атрибута элемента.
        """
        return self.driver.find_element(
            By.CSS_SELECTOR, '#zip-code').value_of_css_property(
                "background-color")

    @allure.step("Проверка заполненных полей")
    def success_fields(self):
        """
        Возвращает результат проверки полей согласно списка.

        :return: bool - результат проверки.
        """
        fields = [
            'first-name',
            'last-name',
            'address',
            'e-mail',
            'phone',
            'city',
            'country',
            'job-position',
            'company'
        ]
        for field in fields:
            if 'success' not in self.get_field_class(field):
                return False
            return True
