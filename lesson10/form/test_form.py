import unittest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages import DataTypesPage


@allure.feature('Форма ввода данных')
class TestForm(unittest.TestCase):

    def setUp(self) -> None:
        """
        Устанавливает тестовую среду. Запускает браузер и инициализирует страницу данных.
        """
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.page = DataTypesPage(self.driver)

    def tearDown(self) -> None:
        """
        Завершает тесты и закрывает браузер.
        """
        self.driver.quit()

    @allure.title('Тест отправки формы с некорректными данными')
    @allure.description('Проверка отображения ошибок при отправке формы с некорректными данными')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_form_submission(self) -> None:
        """
        Тестирует отправку формы и проверяет правильность отображения классов ошибок.
        """
        with allure.step("Открытие страницы формы"):
            self.page.open('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

        with allure.step("Заполнение формы данными"):
            self.page.fill_form('Иван', 'Петров', 'Ленина, 55-3', 'test@skypro.com', '+7985899998787', 'Москва', 'Россия', 'QA', 'SkyPro')

        with allure.step("Отправка формы"):
            self.page.submit()

        with allure.step("Проверка класса ошибки zip-code"):
            self.assertIn('alert-danger', self.page.get_alert_class("zip-code"))

        fields = ["first-name", "last-name", "address", "e-mail", "phone", "city", "country", "job-position", "company"]
        with allure.step("Проверка успешного заполнения других полей"):
            for field in fields:
                self.assertIn('alert-success', self.page.get_alert_class(field))
