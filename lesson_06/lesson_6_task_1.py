from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("http://www.uitestingplayground.com/ajax")
driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()
WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((
        By.CSS_SELECTOR, "#content p.bg-success"))).text

content = driver.find_element(By.CSS_SELECTOR, "#content")
green = content.find_element(By.CSS_SELECTOR, "p.bg-success").text

print(green)

driver.quit()
