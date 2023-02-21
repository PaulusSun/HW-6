from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_Total_price():   
    driver = webdriver.Chrome()
    driver.get('https://www.saucedemo.com/')


    driver.find_element(By.CSS_SELECTOR,'#user-name').send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR,'#password').send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR,'#login-button').click()


    driver.find_element(By.CSS_SELECTOR,'#add-to-cart-sauce-labs-backpack').click()
    driver.find_element(By.CSS_SELECTOR,'#add-to-cart-sauce-labs-bolt-t-shirt').click()
    driver.find_element(By.CSS_SELECTOR,'#add-to-cart-sauce-labs-onesie').click()
    driver.find_element(By.CSS_SELECTOR,'#shopping_cart_container > a').click()
    driver.find_element(By.CSS_SELECTOR,'#checkout').click()

    driver.find_element(By.CSS_SELECTOR,'#first-name').send_keys("Pavel")
    driver.find_element(By.CSS_SELECTOR,'#last-name').send_keys("Brovkin")
    driver.find_element(By.CSS_SELECTOR,'#postal-code').send_keys("140203")
    driver.find_element(By.CSS_SELECTOR,'#continue').click()

    total = driver.find_element(By.CSS_SELECTOR,'#checkout_summary_container > div > div.summary_info > div.summary_total_label').text

    driver.quit

    assert total == 'Total: $58.29'
