from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class Product_Page():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def add_to_cart(self):
        self.driver.find_element(
            By.ID, 'add-to-cart-sauce-labs-backpack').click()
        self.driver.find_element(
            By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
        self.driver.find_element(
            By.ID, 'add-to-cart-sauce-labs-onesie').click()

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').click()
