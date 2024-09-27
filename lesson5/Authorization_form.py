from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Firefox()

try:
    driver.get("http://the-internet.herokuapp.com/login")

    username_input = driver.find_element(By.ID, "username")
    username_input.send_keys("tomsmith")

    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("SuperSecretPassword!")

    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()

    time.sleep(3)

finally:
    driver.quit()
