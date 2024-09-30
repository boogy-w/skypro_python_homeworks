from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 10)

driver.get("https://www.saucedemo.com/")

username_field = driver.find_element(By.ID, "user-name")
password_field = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

username_field.send_keys("standard_user")
password_field.send_keys("secret_sauce")
login_button.click()


def add_to_cart_by_product_name(product_name):
    product = wait.until(EC.element_to_be_clickable((
        By.XPATH, f'//div[text()="{product_name}"]/ancestor::div[@class="inventory_item"]//button')))
    product.click()


add_to_cart_by_product_name("Sauce Labs Backpack")
add_to_cart_by_product_name("Sauce Labs Bolt T-Shirt")
add_to_cart_by_product_name("Sauce Labs Onesie")

cart_button = wait.until(EC.element_to_be_clickable((
    By.XPATH, '//*[@id="shopping_cart_container"]/a')))
cart_button.click()

checkout_button = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
checkout_button.click()

first_name_field = wait.until(EC.visibility_of_element_located((
    By.ID, "first-name")))
last_name_field = driver.find_element(By.ID, "last-name")
postal_code_field = driver.find_element(By.ID, "postal-code")

first_name_field.send_keys("YourFirstName")
last_name_field.send_keys("YourLastName")
postal_code_field.send_keys("12345")

continue_button = driver.find_element(By.ID, "continue")
continue_button.click()

total_element = wait.until(EC.visibility_of_element_located((
    By.CLASS_NAME, "summary_total_label")))
total_text = total_element.text
total_amount = float(total_text.replace("Total: $", ""))

assert total_amount == 58.29, f"Ожидалось $58.29, но получено ${total_amount:.2f}"

print("Тест пройден успешно. Общая сумма $58.29")

driver.quit()
