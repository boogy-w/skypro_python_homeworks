from selenium.webdriver.common.by import By
from base_page import BasePage


class CalculatorPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    def load(self):
        self.driver.get(self.url)

    def set_delay(self, delay_value):
        delay_input = self.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(str(delay_value))

    def click_number(self, number):
        self.find_element(By.XPATH, f"//span[text()='{number}']").click()

    def click_operator(self, operator):
        self.find_element(By.XPATH, f"//span[text()='{operator}']").click()

    def get_result_text(self):
        return self.find_element(By.CLASS_NAME, "screen").text

    def wait_for_result(self, expected_result):
        self.wait_for_element_text(By.CLASS_NAME, "screen", expected_result)
