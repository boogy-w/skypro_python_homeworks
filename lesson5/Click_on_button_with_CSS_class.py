from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time


def main():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    try:
        driver.get("http://uitestingplayground.com/classattr")
        time.sleep(5)

        blue_button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
        blue_button.click()
        time.sleep(2)

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
