from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Calc:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(
            'https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html' # noqa
            )
        self.driver.implicitly_wait(4)

    def time_delay(self, time):
        field = self.driver.find_element(By.ID, 'delay')
        field.clear()
        field.send_keys(time)

    def select_summ(self):
        self.driver.find_element(By.XPATH, "//span[text()='7']").click()
        self.driver.find_element(By.XPATH, "//span[text()='+']").click()
        self.driver.find_element(By.XPATH, "//span[text()='8']").click()
        self.driver.find_element(By.XPATH, "//span[text()='=']").click()
        WebDriverWait(self.driver, 50).until(
            EC.text_to_be_present_in_element((
                By.CSS_SELECTOR, '.screen'), "15"))

    def find_res(self):
        calc_res = self.driver.find_element(By.CSS_SELECTOR, '.screen').text
        return (calc_res)

    def quit(self):
        self.driver.quit()
