from selenium.webdriver.common.by import By
from base_page import BasePage


class CalculatorPage(BasePage):
    def __init__(self, driver):
        """
        Инициализация страницы калькулятора.

        :param driver: веб-драйвер для управления браузером.
        """
        super().__init__(driver)
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    def load(self):
        """Загружает страницу калькулятора."""
        self.driver.get(self.url)

    def set_delay(self, delay_value: int):
        """
        Устанавливает задержку калькулятора.

        :param delay_value: значение задержки.
        """
        delay_input = self.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(str(delay_value))

    def click_number(self, number: int):
        """
        Нажимает на кнопку с числом на калькуляторе.

        :param number: число, которое нужно нажать.
        """
        self.find_element(By.XPATH, f"//span[text()='{number}']").click()

    def click_operator(self, operator: str):
        """
        Нажимает на кнопку с оператором на калькуляторе.

        :param operator: оператор, который нужно нажать.
        """
        self.find_element(By.XPATH, f"//span[text()='{operator}']").click()

    def get_result_text(self) -> str:
        """
        Получает текст результата с экрана калькулятора.

        :return: текстовое значение результата.
        """
        return self.find_element(By.CLASS_NAME, "screen").text

    def wait_for_result(self, expected_result: str):
        """
        Ожидание результата на экране калькулятора.

        :param expected_result: ожидаемый текст результата.
        """
        self.wait_for_element_text(By.CLASS_NAME, "screen", expected_result)
