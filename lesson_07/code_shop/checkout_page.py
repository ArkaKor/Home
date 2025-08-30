from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class Checkout_Page():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def insert_value(self):
        self.driver.find_element(By.ID, 'first-name').send_keys('Аркадий')
        self.driver.find_element(By.ID, 'last-name').send_keys('Кормилицын')
        self.driver.find_element(By.ID, 'postal-code').send_keys('141300')

    def buy(self):
        self.driver.find_element(By.ID, 'continue').click()

    def get_result(self):
        total = self.driver.find_element(
            By.CLASS_NAME, 'summary_total_label').text
        return str(total.split(" ")[1])
