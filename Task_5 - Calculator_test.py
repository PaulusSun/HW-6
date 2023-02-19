from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_assertion():
    driver = webdriver.Chrome()

    driver.implicitly_wait(10)

    driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')

    driver.find_element(By.CSS_SELECTOR,'#delay').clear()

    driver.find_element(By.CSS_SELECTOR,'#delay').send_keys(45)



    driver.find_element(By.XPATH,"//span [contains(text(),'7')]").click() 
    driver.find_element(By.XPATH,"//span [contains(text(),'+')]").click() 
    driver.find_element(By.XPATH,"//span [contains(text(),'8')]").click() 
    driver.find_element(By.XPATH,"//span [contains(text(),'=')]").click() 

    waiter = WebDriverWait(driver, 50)
    waiter.until(EC.text_to_be_present_in_element_attribute((By.CSS_SELECTOR,'.screen') , 'innerHTML', '15'))
       
    assert driver.find_element(By.CSS_SELECTOR,'.screen').get_attribute('innerHTML') == '15'

    driver.quit