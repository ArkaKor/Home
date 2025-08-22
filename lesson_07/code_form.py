from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class Form_Page():
    def __init__(self, driver):
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

    def open(self):
        self.driver.get(
            'https://bonigarcia.dev/selenium-webdriver-java/data-types.html'
            )

    def fill_form(self):
        for field, value in self.fields.items():
            self.wait.until(
                EC.presence_of_element_located((By.NAME, field))
            ).send_keys(value)

    def submitt(self):
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

    def get_field_class(self, field_id):
        element = self.wait.until(
            EC.presence_of_element_located((By.ID, field_id))
        ).get_attribute('class')
        return element

    def zip_code(self):
        return self.driver.find_element(
            By.CSS_SELECTOR, '#zip-code').value_of_css_property(
                "background-color")

    def success_fields(self):
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
