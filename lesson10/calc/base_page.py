from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        """
        Инициализация базовой страницы.

        :param driver: веб-драйвер для управления браузером.
        """
        self.driver = driver

    def find_element(self, by: str, value: str):
        """
        Находит элемент на странице.

        :param by: метод поиска элемента (например, By.ID).
        :param value: значение метода поиска (например, "element_id").
        :return: найденный веб-элемент.
        """
        return self.driver.find_element(by, value)

    def wait_for_element_text(self, by: str, value: str, text: str, timeout: int = 46) -> bool:
        """
        Ожидание появления текста в элементе.

        :param by: метод поиска элемента.
        :param value: значение метода поиска.
        :param text: текст, который ожидается в элементе.
        :param timeout: максимальное время ожидания (в секундах).
        :return: True, если текст появился в элементе.
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element((by, value), text)
        )
