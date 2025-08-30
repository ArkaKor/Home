from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Cart_Page():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def confirm(self):
        self.wait.until(
            EC.element_to_be_clickable((By.ID, 'checkout'))).click()
