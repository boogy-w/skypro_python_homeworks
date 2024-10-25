from base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    """Страница входа."""

    username_locator = (By.ID, "user-name")
    password_locator = (By.ID, "password")
    login_button_locator = (By.ID, "login-button")

    def enter_username(self, username: str):
        """
        Ввести имя пользователя.

        :param username: str, имя пользователя.
        """
        self.find_element(*self.username_locator).send_keys(username)

    def enter_password(self, password: str):
        """
        Ввести пароль.

        :param password: str, пароль.
        """
        self.find_element(*self.password_locator).send_keys(password)

    def click_login(self):
        """Нажать кнопку входа."""
        self.find_element(*self.login_button_locator).click()
