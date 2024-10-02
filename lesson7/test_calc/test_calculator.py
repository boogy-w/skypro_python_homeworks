import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from calculator_page import CalculatorPage


class CalculatorTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.calculator_page = CalculatorPage(self.driver)

    def test_addition(self):
        self.calculator_page.load()
        self.calculator_page.set_delay(45)

        self.calculator_page.click_number(7)
        self.calculator_page.click_operator('+')
        self.calculator_page.click_number(8)
        self.calculator_page.click_operator('=')

        self.calculator_page.wait_for_result("15")
        result_text = self.calculator_page.get_result_text()

        self.assertEqual(result_text, "15", f"Ожидалось 15, но получено {result_text}")
        print("Тест пройден успешно. Количество 15")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
