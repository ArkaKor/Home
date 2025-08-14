from selenium.webdriver.common.by import By
from selenium import webdriver


def test_shop():
    driver = webdriver.Firefox()
    driver.get('https://www.saucedemo.com')
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-onesie').click()
    driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').click()
    driver.find_element(By.ID, 'checkout').click()
    driver.find_element(By.ID, 'first-name').send_keys('Арка')
    driver.find_element(By.ID, 'last-name').send_keys('Карма')
    driver.find_element(By.ID, 'postal-code').send_keys('141300')
    driver.find_element(By.ID, 'continue').click()
    total = driver.find_element(By.CLASS_NAME, 'summary_total_label').text
    price = str(total.split(" ")[1])
    driver.quit()
    assert price == '$58.29', "Неверная сумма"
