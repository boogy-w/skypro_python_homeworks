import unittest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from calculator_page import CalculatorPage


@allure.feature('Калькулятор')
class CalculatorTests(unittest.TestCase):

    def setUp(self):
        """
        Настройка тестового окружения.
        """
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.calculator_page = CalculatorPage(self.driver)

    @allure.title('Тест сложения чисел')
    @allure.description('Проверка корректности выполнения операции сложения в калькуляторе.')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_addition(self):
        """Тест на сложение чисел."""
        with allure.step("Загрузка страницы калькулятора"):
            self.calculator_page.load()

        with allure.step("Установка задержки"):
            self.calculator_page.set_delay(45)

        with allure.step("Ввод чисел и операции"):
            self.calculator_page.click_number(7)
            self.calculator_page.click_operator('+')
            self.calculator_page.click_number(8)
            self.calculator_page.click_operator('=')

        with allure.step("Ожидание результата"):
            self.calculator_page.wait_for_result("15")

        with allure.step("Проверка результата"):
            result_text = self.calculator_page.get_result_text()
            self.assertEqual(result_text, "15", f"Ожидалось 15, но получено {result_text}")
            print("Тест пройден успешно. Количество 15")

    def tearDown(self):
        """Закрытие браузера после тестов."""
        self.driver.quit()
