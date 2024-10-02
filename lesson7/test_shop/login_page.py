from base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    username_locator = (By.ID, "user-name")
    password_locator = (By.ID, "password")
    login_button_locator = (By.ID, "login-button")

    def enter_username(self, username):
        self.find_element(*self.username_locator).send_keys(username)

    def enter_password(self, password):
        self.find_element(*self.password_locator).send_keys(password)

    def click_login(self):
        self.find_element(*self.login_button_locator).click()
