from selenium import webdriver
from selenium.webdriver.common.by import By

def test_assertion():
    driver = webdriver.Chrome()

    driver.implicitly_wait(10)

    driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

    driver.find_element(By.CSS_SELECTOR,'[name="first-name"]').send_keys('Иван')
    driver.find_element(By.CSS_SELECTOR,'[name="last-name"]').send_keys('Петров')
    driver.find_element(By.CSS_SELECTOR,'[name="address"]').send_keys('Ленина, 55-3')
    driver.find_element(By.CSS_SELECTOR,'[name="city"]').send_keys('Москва')
    driver.find_element(By.CSS_SELECTOR,'[name="country"]').send_keys('Россия')
    driver.find_element(By.CSS_SELECTOR,'[name="job-position"]').send_keys('QA')
    driver.find_element(By.CSS_SELECTOR,'[name="company"]').send_keys('SkyPro')

    driver.find_element(By.CSS_SELECTOR, '[class*="btn-outline-primary"]').click()


    assert driver.find_element(By.CSS_SELECTOR,'#first-name').value_of_css_property("background-color") == 'rgba(209, 231, 221, 1)'
    assert driver.find_element(By.CSS_SELECTOR,'#last-name').value_of_css_property("background-color") == 'rgba(209, 231, 221, 1)'
    assert driver.find_element(By.CSS_SELECTOR,'#address').value_of_css_property("background-color") == 'rgba(209, 231, 221, 1)'
    assert driver.find_element(By.CSS_SELECTOR,'#zip-code').value_of_css_property("background-color") == 'rgba(248, 215, 218, 1)'
    assert driver.find_element(By.CSS_SELECTOR,'#city').value_of_css_property("background-color") == 'rgba(209, 231, 221, 1)'
    assert driver.find_element(By.CSS_SELECTOR,'#country').value_of_css_property("background-color") == 'rgba(209, 231, 221, 1)'
    assert driver.find_element(By.CSS_SELECTOR,'#job-position').value_of_css_property("background-color") == 'rgba(209, 231, 221, 1)'
    assert driver.find_element(By.CSS_SELECTOR,'#company').value_of_css_property("background-color") == 'rgba(209, 231, 221, 1)'


    driver.quit