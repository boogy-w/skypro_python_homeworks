from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Firefox()

try:
    driver.get("http://the-internet.herokuapp.com/entry_ad")

    time.sleep(2)

    close_button = driver.find_element(By.CSS_SELECTOR, "div.modal-footer > p")
    close_button.click()

    time.sleep(2)

finally:
    driver.quit()
