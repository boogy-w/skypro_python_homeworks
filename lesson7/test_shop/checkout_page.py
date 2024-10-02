from base_page import BasePage
from selenium.webdriver.common.by import By


class CheckoutPage(BasePage):
    first_name_locator = (By.ID, "first-name")
    last_name_locator = (By.ID, "last-name")
    postal_code_locator = (By.ID, "postal-code")
    continue_button_locator = (By.ID, "continue")
    total_label_locator = (By.CLASS_NAME, "summary_total_label")

    def fill_checkout_info(self, first_name, last_name, postal_code):
        self.wait_for_visibility(self.first_name_locator).send_keys(first_name)
        self.find_element(*self.last_name_locator).send_keys(last_name)
        self.find_element(*self.postal_code_locator).send_keys(postal_code)

    def click_continue(self):
        self.find_element(*self.continue_button_locator).click()

    def get_total_amount(self):
        total_text = self.wait_for_visibility(self.total_label_locator).text
        return float(total_text.replace("Total: $", ""))
