from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


chrome_options = Options()
chrome_options.add_argument("--headless")
driver_service = Service(ChromeDriverManager().install())


driver = webdriver.Chrome(service=driver_service, options=chrome_options)

try:
    driver.get("http://uitestingplayground.com/dynamicid")

    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn-primary')]"))
    )

    button.click()

    print("Кнопка успешно нажата")
finally:

    driver.quit()
