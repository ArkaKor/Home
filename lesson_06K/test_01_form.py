import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestFormValidation(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.ChromiumEdge()
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    def test_form_validation(self):
        self.driver.find_element(By.NAME, 'first-name').send_keys('Иван')
        self.driver.find_element(By.NAME, 'last-name').send_keys('Петров')
        self.driver.find_element(By.NAME, 'address').send_keys('Ленина, 55-3')
        self.driver.find_element(
            By.NAME, 'e-mail').send_keys('test@skypro.com')
        self.driver.find_element(By.NAME, 'phone').send_keys('+7985899998787')
        self.driver.find_element(By.NAME, 'zip-code').send_keys()
        self.driver.find_element(By.NAME, 'city').send_keys('Москва')
        self.driver.find_element(By.NAME, 'country').send_keys('Россия')
        self.driver.find_element(By.NAME, 'job-position').send_keys('QA')
        self.driver.find_element(By.NAME, 'company').send_keys('SkyPro')

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

        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '#zip-code'))
        )
        zip_color = self.driver.find_element(
            By.CSS_SELECTOR, '#zip-code').value_of_css_property(
                "background-color")
        assert zip_color == "rgba(248, 215, 218, 1)", "Zip не красный"
        first_name_color = self.driver.find_element(
            By.CSS_SELECTOR, '#first-name').value_of_css_property(
                "background-color")
        assert first_name_color == "rgba(209, 231, 221, 1)", "Имя не зелёный"
        last_name_color = self.driver.find_element(
            By.CSS_SELECTOR, '#last-name').value_of_css_property(
                "background-color")
        assert last_name_color == "rgba(209, 231, 221, 1)", "Фамилия \
            не зелёный"
        address_color = self.driver.find_element(
            By.CSS_SELECTOR, '#address').value_of_css_property(
                "background-color")
        assert address_color == "rgba(209, 231, 221, 1)", "Адрес не зелёный"
        email_color = self.driver.find_element(
            By.CSS_SELECTOR, '#e-mail').value_of_css_property(
                "background-color")
        assert email_color == "rgba(209, 231, 221, 1)", "Почта не зелёный"
        phone_color = self.driver.find_element(
            By.CSS_SELECTOR, '#phone').value_of_css_property(
                "background-color")
        assert phone_color == "rgba(209, 231, 221, 1)", "Телефон не зелёный"
        city_color = self.driver.find_element(
            By.CSS_SELECTOR, '#city').value_of_css_property("background-color")
        assert city_color == "rgba(209, 231, 221, 1)", "Город не зелёный"
        country_color = self.driver.find_element(
            By.CSS_SELECTOR, '#country').value_of_css_property(
                "background-color")
        assert country_color == "rgba(209, 231, 221, 1)", "Страна не зелёный"
        job_color = self.driver.find_element(
            By.CSS_SELECTOR, '#job-position').value_of_css_property(
                "background-color")
        assert job_color == "rgba(209, 231, 221, 1)", "Должность не зелёный"
        company_color = self.driver.find_element(
            By.CSS_SELECTOR, '#company').value_of_css_property(
                "background-color")
        assert company_color == "rgba(209, 231, 221, 1)", "Компания не зелёный"

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
