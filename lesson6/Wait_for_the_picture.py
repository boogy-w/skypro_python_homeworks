from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

try:
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')

    image = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#award"))
    )

    src = driver.find_element(By.CSS_SELECTOR, "#award").get_attribute("src")

    print(src)

finally:
    driver.quit()
