from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class DataTypesPage:
    def __init__(self, driver: WebDriver):
        """
        Инициализирует страницу с формой ввода данных.

        :param driver: WebDriver экземпляр для управления браузером
        """
        self.driver = driver
        self.first_name_field = (By.NAME, 'first-name')
        self.last_name_field = (By.NAME, 'last-name')
        self.address_field = (By.NAME, 'address')
        self.email_field = (By.NAME, 'e-mail')
        self.phone_field = (By.NAME, 'phone')
        self.city_field = (By.NAME, 'city')
        self.country_field = (By.NAME, 'country')
        self.job_position_field = (By.NAME, 'job-position')
        self.company_field = (By.NAME, 'company')
        self.submit_button = (By.CSS_SELECTOR, 'button[type="submit"]')
        self.zip_code_field = (By.ID, 'zip-code')

    def open(self, url: str) -> None:
        """
        Открывает страницу по указанному URL.

        :param url: str - адрес страницы
        """
        self.driver.get(url)

    def fill_form(self, first_name: str, last_name: str, address: str, email: str, phone: str, city: str, country: str, job_position: str, company: str) -> None:
        """
        Заполняет форму данными пользователя.

        :param first_name: str - имя пользователя
        :param last_name: str - фамилия пользователя
        :param address: str - адрес пользователя
        :param email: str - электронная почта пользователя
        :param phone: str - телефон пользователя
        :param city: str - город проживание пользователя
        :param country: str - страна проживания
        :param job_position: str - должность пользователя
        :param company: str - название компании пользователя
        """
        self.driver.find_element(*self.first_name_field).send_keys(first_name)
        self.driver.find_element(*self.last_name_field).send_keys(last_name)
        self.driver.find_element(*self.address_field).send_keys(address)
        self.driver.find_element(*self.email_field).send_keys(email)
        self.driver.find_element(*self.phone_field).send_keys(phone)
        self.driver.find_element(*self.city_field).send_keys(city)
        self.driver.find_element(*self.country_field).send_keys(country)
        self.driver.find_element(*self.job_position_field).send_keys(job_position)
        self.driver.find_element(*self.company_field).send_keys(company)

    def submit(self) -> None:
        """
        Нажимает кнопку отправки формы.
        """
        self.driver.find_element(*self.submit_button).click()

    def get_alert_class(self, element_id: str) -> str:
        """
        Возвращает класс элемента с указанным ID.

        :param element_id: str - идентификатор элемента
        :return: str - значение атрибута класса элемента
        """
        element = self.driver.find_element(By.ID, element_id)
        return element.get_attribute('class')
