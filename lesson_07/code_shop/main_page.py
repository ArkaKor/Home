from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class Main_Page():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def login(self):
        self.driver.get('https://www.saucedemo.com')
        self.driver.find_element(By.ID, 'user-name').send_keys('standard_user')
        self.driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        self.driver.find_element(By.ID, 'login-button').click()
