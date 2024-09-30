from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

driver.find_element(By.NAME, 'first-name').send_keys('Иван')
driver.find_element(By.NAME, 'last-name').send_keys('Петров')
driver.find_element(By.NAME, 'address').send_keys('Ленина, 55-3')
driver.find_element(By.NAME, 'e-mail').send_keys('test@skypro.com')
driver.find_element(By.NAME, 'phone').send_keys('+7985899998787')
driver.find_element(By.NAME, 'city').send_keys('Москва')
driver.find_element(By.NAME, 'country').send_keys('Россия')
driver.find_element(By.NAME, 'job-position').send_keys('QA')
driver.find_element(By.NAME, 'company').send_keys('SkyPro')

driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

zip_code_field = driver.find_element(By.ID, "zip-code")
assert 'alert-danger' in zip_code_field.get_attribute("class")

field = driver.find_element(By.ID, "first-name")
assert 'alert-success' in field.get_attribute("class")

field = driver.find_element(By.ID, "last-name")
assert 'alert-success' in field.get_attribute("class")

field = driver.find_element(By.ID, "address")
assert 'alert-success' in field.get_attribute("class")

field = driver.find_element(By.ID, "e-mail")
assert 'alert-success' in field.get_attribute("class")

field = driver.find_element(By.ID, "phone")
assert 'alert-success' in field.get_attribute("class")

field = driver.find_element(By.ID, "city")
assert 'alert-success' in field.get_attribute("class")

field = driver.find_element(By.ID, "country")
assert 'alert-success' in field.get_attribute("class")

field = driver.find_element(By.ID, "job-position")
assert 'alert-success' in field.get_attribute("class")

field = driver.find_element(By.ID, "company")
assert 'alert-success' in field.get_attribute("class")

print("Все проверки успешно пройдены.")

driver.quit()
