from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.implicitly_wait(5)

driver.get('http://uitestingplayground.com/textinput')

enter_New_Name = driver.find_element(By.CSS_SELECTOR, '#newButtonName').send_keys("SkyPro")

driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()

print("Новое имя:", driver.find_element(By.CSS_SELECTOR, "#updatingButton").text)

driver.quit