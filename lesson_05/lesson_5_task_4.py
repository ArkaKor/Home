from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")
search_name = driver.find_element(By.ID, "username")
search_name.send_keys("tomsmith")
search_pass = driver.find_element(By.ID, "password")
search_pass.send_keys("SuperSecretPassword!")
driver.find_element(By.CLASS_NAME, "fa").click()
green = driver.find_element(By.ID, "flash")
print(green.text)
driver.quit()
