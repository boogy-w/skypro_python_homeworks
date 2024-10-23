from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Базовый класс для всех страниц. Содержит основные методы для работы с элементами страницы."""

    def __init__(self, driver):
        """
        Конструктор класса BasePage.

        :param driver: WebDriver, используемый для взаимодействия с браузером.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_for_element(self, locator):
        """
        Ожидание, пока элемент не станет кликабельным.

        :param locator: tuple, локатор элемента.
        :return: WebElement, кликабельный элемент.
        """
        return self.wait.until(EC.element_to_be_clickable(locator))

    def find_element(self, *locator):
        """
        Найти элемент на странице.

        :param locator: tuple, локатор элемента.
        :return: WebElement, найденный элемент.
        """
        return self.driver.find_element(*locator)

    def wait_for_visibility(self, locator):
        """
        Ожидание видимости элемента на странице.

        :param locator: tuple, локатор элемента.
        :return: WebElement, видимый элемент.
        """
        return self.wait.until(EC.visibility_of_element_located(locator))
