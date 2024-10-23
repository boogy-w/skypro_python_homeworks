from base_page import BasePage
from selenium.webdriver.common.by import By


class InventoryPage(BasePage):
    """Страница товарных запасов."""

    def add_to_cart_by_product_name(self, product_name: str):
        """
        Добавить продукт в корзину по имени.

        :param product_name: str, имя продукта.
        """
        product_locator = (
            By.XPATH, f'//div[text()="{product_name}"]/ancestor::div[@class="inventory_item"]//button')
        self.wait_for_element(product_locator).click()

    def go_to_cart(self):
        """Перейти в корзину."""
        cart_button_locator = (By.XPATH, '//*[@id="shopping_cart_container"]/a')
        self.wait_for_element(cart_button_locator).click()
