from base_page import BasePage
from selenium.webdriver.common.by import By


class InventoryPage(BasePage):
    def add_to_cart_by_product_name(self, product_name):
        product_locator = (
            By.XPATH, f'//div[text()="{product_name}"]/ancestor::div[@class="inventory_item"]//button')
        self.wait_for_element(product_locator).click()

    def go_to_cart(self):
        cart_button_locator = (By.XPATH, '//*[@id="shopping_cart_container"]/a')
        self.wait_for_element(cart_button_locator).click()
