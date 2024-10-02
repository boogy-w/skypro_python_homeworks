from base_page import BasePage
from selenium.webdriver.common.by import By


class CartPage(BasePage):
    def click_checkout(self):
        checkout_button_locator = (By.ID, "checkout")
        self.wait_for_element(checkout_button_locator).click()
