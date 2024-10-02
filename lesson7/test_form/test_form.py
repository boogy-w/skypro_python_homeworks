from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages import DataTypesPage

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

page = DataTypesPage(driver)
page.open('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

page.fill_form('Иван', 'Петров', 'Ленина, 55-3', 'test@skypro.com', '+7985899998787', 'Москва', 'Россия', 'QA', 'SkyPro')

page.submit()

assert 'alert-danger' in page.get_alert_class("zip-code")

fields = ["first-name", "last-name", "address", "e-mail", "phone", "city", "country", "job-position", "company"]
for field in fields:
    assert 'alert-success' in page.get_alert_class(field)

print("Все проверки успешно пройдены.")

driver.quit()
