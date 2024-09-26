from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

    add_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")
    for _ in range(5):
        add_button.click()
        time.sleep(2)

    delete_buttons = driver.find_elements(By.XPATH, "//button[text()='Delete']")

    print(f"Количество кнопок 'Delete': {len(delete_buttons)}")

finally:
    driver.quit()
